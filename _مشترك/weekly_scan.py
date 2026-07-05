#!/usr/bin/env python3
"""
Weekly EGX batch scanner — 5 timeframes per symbol → ranked score.

Usage:
  python weekly_scan.py --input ../فحص-2026-07-10 --output ../فحص-2026-07-10/نتيجة.csv
  python weekly_scan.py --input ../فحص-2026-07-10 --md ../فحص-2026-07-10/نتيجة.md

Expected layout:
  INPUT/
    symbols.txt          # one ticker per line
    data/COMI_W.csv      # or COMI/W.csv or charts only (CSV required for this script)
    data/COMI_D.csv
    ...

CSV columns: time, open, high, low, close, volume (TradingView export)
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

TIMEFRAMES = ("M", "W", "D", "4H", "1H")
WEIGHT_W = "W"
WEIGHT_D = "D"
WEIGHT_M = "M"


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    cols = {c.lower().strip(): c for c in df.columns}
    mapping = {}
    for want in ("time", "open", "high", "low", "close", "volume"):
        for k, orig in cols.items():
            if want in k or k == want:
                mapping[orig] = want
                break
    df = df.rename(columns=mapping)
    needed = {"open", "high", "low", "close"}
    if not needed.issubset(df.columns):
        raise ValueError(f"Missing OHLC in {path}: {df.columns.tolist()}")
    for c in ("open", "high", "low", "close"):
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if "volume" in df.columns:
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce").fillna(0)
    else:
        df["volume"] = 0.0
    df = df.dropna(subset=["close"]).reset_index(drop=True)
    return df


def find_csv(data_dir: Path, symbol: str, tf: str) -> Optional[Path]:
    patterns = [
        data_dir / f"{symbol}_{tf}.csv",
        data_dir / symbol / f"{tf}.csv",
        data_dir / f"{symbol}-{tf}.csv",
        data_dir / f"{symbol}{tf}.csv",
    ]
    for p in patterns:
        if p.exists():
            return p
    # glob fallback
    for p in data_dir.glob(f"{symbol}*{tf}*.csv"):
        return p
    return None


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=max(1, n // 2)).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0)
    down = -d.clip(upper=0)
    ru = up.ewm(alpha=1 / n, adjust=False).mean()
    rd = down.ewm(alpha=1 / n, adjust=False).mean()
    rs = ru / rd.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def adx(df: pd.DataFrame, n: int = 14) -> tuple[float, float, float]:
    if len(df) < n + 2:
        return 0.0, 0.0, 0.0
    h, l, c = df["high"], df["low"], df["close"]
    tr = pd.concat(
        [h - l, (h - c.shift()).abs(), (l - c.shift()).abs()], axis=1
    ).max(axis=1)
    up = h.diff()
    down = -l.diff()
    plus_dm = np.where((up > down) & (up > 0), up, 0.0)
    minus_dm = np.where((down > up) & (down > 0), down, 0.0)
    atr = tr.ewm(alpha=1 / n, adjust=False).mean()
    plus_di = 100 * pd.Series(plus_dm).ewm(alpha=1 / n, adjust=False).mean() / atr
    minus_di = 100 * pd.Series(minus_dm).ewm(alpha=1 / n, adjust=False).mean() / atr
    dx = (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan) * 100
    adx_v = dx.ewm(alpha=1 / n, adjust=False).mean().iloc[-1]
    return float(adx_v), float(plus_di.iloc[-1]), float(minus_di.iloc[-1])


def macd_hist(close: pd.Series) -> float:
    m = ema(close, 12) - ema(close, 26)
    sig = ema(m, 9)
    return float((m - sig).iloc[-1])


def bb_width(close: pd.Series, n: int = 20) -> float:
    mid = sma(close, n)
    std = close.rolling(n).std()
    upper = mid + 2 * std
    lower = mid - 2 * std
    bw = (upper - lower) / mid.replace(0, np.nan)
    return float(bw.iloc[-1]) if len(bw.dropna()) else 0.0


def ttm_squeeze_on(close: pd.Series, n: int = 20) -> bool:
    mid = sma(close, n)
    std = close.rolling(n).std()
    bb_u, bb_l = mid + 2 * std, mid - 2 * std
    atr = (close.diff().abs()).rolling(n).mean()
    kc_u, kc_l = mid + 1.5 * atr, mid - 1.5 * atr
    return bool((bb_u.iloc[-1] < kc_u.iloc[-1]) and (bb_l.iloc[-1] > kc_l.iloc[-1]))


def bos_bullish(df: pd.DataFrame, lookback: int = 20) -> bool:
    if len(df) < lookback + 2:
        return False
    prev_high = df["high"].iloc[-lookback - 1 : -1].max()
    return bool(df["close"].iloc[-1] > prev_high)


def higher_highs_lows(df: pd.DataFrame, n: int = 10) -> bool:
    if len(df) < n * 2:
        return False
    h1 = df["high"].iloc[-n:].max()
    h0 = df["high"].iloc[-n * 2 : -n].max()
    l1 = df["low"].iloc[-n:].min()
    l0 = df["low"].iloc[-n * 2 : -n].min()
    return h1 > h0 and l1 > l0


def obv_slope(close: pd.Series, vol: pd.Series, n: int = 8) -> bool:
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * vol).cumsum()
    if len(obv) < n:
        return False
    y = obv.iloc[-n:].values
    x = np.arange(n)
    slope = np.polyfit(x, y, 1)[0]
    return slope > 0


@dataclass
class ScanResult:
    symbol: str
    score: float = 0.0
    tier: str = "OUT"
    setup: str = ""
    trigger: str = ""
    stop_hint: str = ""
    flags: list[str] = field(default_factory=list)
    rejected: bool = False
    reject_reason: str = ""


def score_symbol(symbol: str, frames: dict[str, pd.DataFrame]) -> ScanResult:
    r = ScanResult(symbol=symbol)
    w = frames.get("W")
    d = frames.get("D")
    m = frames.get("M")

    if w is None or d is None:
        r.rejected = True
        r.reject_reason = "missing W or D CSV"
        return r

    score = 0.0
    c_w, c_d = w["close"].iloc[-1], d["close"].iloc[-1]
    ma20_w = sma(w["close"], 20).iloc[-1]
    ma50_w = sma(w["close"], 50).iloc[-1] if len(w) >= 50 else ma20_w
    ma200_w = sma(w["close"], 200).iloc[-1] if len(w) >= 50 else ma20_w

    # --- auto reject ---
    if c_w < ma200_w and len(w) >= 30:
        r.rejected = True
        r.reject_reason = "below MA200W"
        return r

    ext = (c_w - ma20_w) / ma20_w * 100 if ma20_w else 0
    if ext > 25:
        r.rejected = True
        r.reject_reason = "extended >25% above MA20W"
        return r

    adx_v, pdi, mdi = adx(w)
    if adx_v < 15 and bb_width(w["close"]) < np.percentile(
        bb_width(w["close"]).dropna(), 20
    ) if len(w) > 20 else True:
        r.rejected = True
        r.reject_reason = "dead money (low ADX + squeeze)"
        return r

    avg_vol_d = d["volume"].tail(20).mean() if d["volume"].sum() > 0 else 0
    if 0 < avg_vol_d < 500_000:
        r.rejected = True
        r.reject_reason = "low liquidity (<500K EGP/day avg vol proxy)"
        return r

    # --- A trend 25 ---
    if c_w > ma20_w:
        score += 5
    if ma20_w > ma50_w:
        score += 5
    if adx_v > 25 and pdi > mdi:
        score += 5
    if m is not None and len(m) >= 30:
        ma30_m = sma(m["close"], 30).iloc[-1]
        if m["close"].iloc[-1] > ma30_m and ma30_m > sma(m["close"], 30).iloc[-5]:
            score += 5
    else:
        if c_w > ma50_w:
            score += 3
    if higher_highs_lows(w):
        score += 5

    # --- B momentum 20 ---
    rsi_d = rsi(d["close"]).iloc[-1]
    if 50 <= rsi_d <= 70:
        score += 5
    elif 40 <= rsi_d < 50:
        score += 2
    if macd_hist(d["close"]) > 0:
        score += 5
    ma200_d = sma(d["close"], 200).iloc[-1] if len(d) >= 50 else sma(d["close"], 20).iloc[-1]
    rsi2 = rsi(d["close"], 2).iloc[-1]
    if rsi2 < 10 and c_d > ma200_d:
        score += 5
        r.setup = "Connors RSI-2 bounce"

    # --- C structure 20 ---
    if bos_bullish(w):
        score += 7
        r.setup = r.setup or "Weekly BOS"
    if bos_bullish(d, 15):
        score += 3
    h4 = frames.get("4H")
    if h4 is not None and bos_bullish(h4, 15):
        score += 5

    # --- D volatility 15 ---
    if ttm_squeeze_on(d["close"]):
        score += 4
        r.setup = r.setup or "TTM Squeeze coiled"
    # squeeze fire: was on, now expanding
    if len(d) > 25:
        bw = bb_width(d["close"])
        if bw > bb_width(d["close"].iloc[:-1]).iloc[-1]:
            score += 4

    # --- E volume 10 ---
    if len(w) >= 10 and w["volume"].iloc[-1] > w["volume"].tail(10).mean():
        score += 5
    if obv_slope(d["close"], d["volume"]):
        score += 5

    # --- trigger / stop hints ---
    trigger_level = w["high"].iloc[-5:-1].max() if len(w) > 5 else c_w * 1.02
    stop_level = w["low"].iloc[-5:].min() if len(w) > 5 else c_w * 0.93
    r.trigger = f"close > {trigger_level:.2f} (W BOS confirm)"
    r.stop_hint = f"below {stop_level:.2f} (~7-8%)"

    r.score = min(100.0, score)
    if r.score >= 75:
        r.tier = "A"
    elif r.score >= 60:
        r.tier = "B"
    elif r.score >= 45:
        r.tier = "C"
    else:
        r.tier = "OUT"
    return r


def load_symbols(input_dir: Path) -> list[str]:
    sym_file = input_dir / "symbols.txt"
    if sym_file.exists():
        lines = sym_file.read_text(encoding="utf-8").splitlines()
        return [ln.strip().upper() for ln in lines if ln.strip() and not ln.startswith("#")]
    # infer from data/
    data_dir = input_dir / "data"
    if not data_dir.exists():
        data_dir = input_dir
    syms = set()
    for p in data_dir.glob("*.csv"):
        m = re.match(r"^([A-Z0-9]+)[_\-]?(M|W|D|4H|1H)", p.stem.upper())
        if m:
            syms.add(m.group(1))
    return sorted(syms)


def run_scan(input_dir: Path) -> list[ScanResult]:
    data_dir = input_dir / "data" if (input_dir / "data").exists() else input_dir
    symbols = load_symbols(input_dir)
    results: list[ScanResult] = []

    for sym in symbols:
        frames = {}
        for tf in TIMEFRAMES:
            p = find_csv(data_dir, sym, tf)
            if p:
                try:
                    frames[tf] = load_csv(p)
                except Exception as e:
                    frames[tf] = None  # type: ignore
        results.append(score_symbol(sym, frames))  # type: ignore

    results.sort(key=lambda x: (-x.score if not x.rejected else -1, x.symbol))
    return results


def write_csv(results: list[ScanResult], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            ["rank", "symbol", "score", "tier", "setup", "trigger", "stop", "rejected", "reject_reason"]
        )
        rank = 0
        for r in results:
            if r.rejected:
                continue
            rank += 1
            w.writerow([rank, r.symbol, f"{r.score:.1f}", r.tier, r.setup, r.trigger, r.stop_hint, "", ""])
        w.writerow([])
        w.writerow(["--- REJECTED ---"])
        for r in results:
            if r.rejected:
                w.writerow(["", r.symbol, "", "OUT", "", "", "", "yes", r.reject_reason])


def write_md(results: list[ScanResult], out: Path, scan_date: str) -> None:
    passed = [r for r in results if not r.rejected and r.tier in ("A", "B", "C")]
    top = [r for r in passed if r.tier in ("A", "B")][:15]
    lines = [
        f"# 📅 نتيجة الفحص الأسبوعي — {scan_date}",
        "",
        "> ⚠️ تحليل تعليمي · محاكاة من CSV · ليس نصيحة استثمارية",
        "",
        f"**إجمالي:** {len(results)} · **Passed:** {len(passed)} · **Rejected:** {sum(1 for r in results if r.rejected)}",
        "",
        "## 🏆 Top 15",
        "",
        "| Rank | الكود | Score | Tier | Setup | Trigger | Stop |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(top, 1):
        lines.append(
            f"| {i} | **{r.symbol}** | {r.score:.0f} | {r.tier} | {r.setup or '—'} | {r.trigger} | {r.stop_hint} |"
        )
    lines.extend(["", "## 🚫 Rejected (sample)", ""])
    rej = [r for r in results if r.rejected][:20]
    for r in rej:
        lines.append(f"- **{r.symbol}:** {r.reject_reason}")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Weekly EGX batch scanner")
    ap.add_argument("--input", "-i", type=Path, required=True, help="Scan folder (symbols.txt + data/)")
    ap.add_argument("--output", "-o", type=Path, help="Output CSV path")
    ap.add_argument("--md", type=Path, help="Output markdown summary")
    args = ap.parse_args()

    results = run_scan(args.input)
    scan_date = args.input.name.replace("فحص-", "") or "scan"

    out_csv = args.output or args.input / f"نتيجة-{scan_date}.csv"
    write_csv(results, out_csv)
    print(f"Wrote {out_csv}")

    out_md = args.md or args.input / f"نتيجة-الفحص-الأسبوعي-{scan_date}.md"
    write_md(results, out_md, scan_date)
    print(f"Wrote {out_md}")

    top3 = [r for r in results if not r.rejected and r.tier == "A"][:3]
    if top3:
        print("\nTop 3 Tier A:")
        for r in top3:
            print(f"  {r.symbol}: {r.score:.0f} — {r.trigger}")


if __name__ == "__main__":
    main()

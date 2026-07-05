"""EGX analysis indicators — shared by weekly_scan and analyze CLI."""

from __future__ import annotations

import numpy as np
import pandas as pd


def load_ohlcv_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    cols = {c.lower().strip(): c for c in df.columns}
    mapping = {}
    for want in ("time", "open", "high", "low", "close", "volume"):
        for k, orig in cols.items():
            if want in k or k == want:
                mapping[orig] = want
                break
    df = df.rename(columns=mapping)
    for c in ("open", "high", "low", "close"):
        if c not in df.columns:
            raise ValueError(f"Missing {c} in {path}")
        df[c] = pd.to_numeric(df[c], errors="coerce")
    if "volume" in df.columns:
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce").fillna(0)
    else:
        df["volume"] = 0.0
    return df.dropna(subset=["close"]).reset_index(drop=True)


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=max(1, n // 2)).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> float:
    d = close.diff()
    up = d.clip(lower=0)
    down = -d.clip(upper=0)
    ru = up.ewm(alpha=1 / n, adjust=False).mean()
    rd = down.ewm(alpha=1 / n, adjust=False).mean()
    rs = ru / rd.replace(0, np.nan)
    val = 100 - (100 / (1 + rs))
    return float(val.iloc[-1]) if len(val.dropna()) else 50.0


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
    atr = close.diff().abs().rolling(n).mean()
    kc_u, kc_l = mid + 1.5 * atr, mid - 1.5 * atr
    if len(close) < n + 1:
        return False
    return bool((bb_u.iloc[-1] < kc_u.iloc[-1]) and (bb_l.iloc[-1] > kc_l.iloc[-1]))


def signal_color(bull: bool, bear: bool) -> str:
    if bull and not bear:
        return "🟢"
    if bear and not bull:
        return "🔴"
    return "🟡"


def compute_snapshot(df: pd.DataFrame) -> dict:
    c = df["close"]
    close = float(c.iloc[-1])
    ma20 = float(sma(c, 20).iloc[-1])
    ma50 = float(sma(c, 50).iloc[-1]) if len(c) >= 50 else ma20
    rsival = rsi(c)
    macd = macd_hist(c)
    bw = bb_width(c)
    sq = ttm_squeeze_on(c)
    vol = df["volume"]
    avg_vol = float(vol.tail(20).mean()) if vol.sum() > 0 else 0.0
    adv_egp = avg_vol * close

    trend_bull = close > ma20 > ma50
    trend_bear = close < ma20 < ma50

    return {
        "close": close,
        "ma20": ma20,
        "ma50": ma50,
        "rsi14": round(rsival, 2),
        "rsi2": round(rsi(c, 2), 2),
        "macd_hist": round(macd, 4),
        "bb_width": round(bw, 4),
        "ttm_squeeze": sq,
        "avg_vol": int(avg_vol),
        "adv_egp": round(adv_egp, 0),
        "trend": signal_color(trend_bull, trend_bear),
        "momentum": signal_color(50 <= rsival <= 70 and macd > 0, rsival > 75 or macd < -0.01),
    }


def format_snapshot_md(snap: dict, label: str = "") -> str:
    title = f"### {label}\n\n" if label else ""
    return (
        f"{title}"
        f"| Metric | Value |\n|---|---|\n"
        f"| Close | {snap['close']} |\n"
        f"| MA20 | {snap['ma20']:.4f} |\n"
        f"| MA50 | {snap['ma50']:.4f} |\n"
        f"| RSI(14) | {snap['rsi14']} {snap['momentum']} |\n"
        f"| RSI(2) | {snap['rsi2']} |\n"
        f"| MACD hist | {snap['macd_hist']} |\n"
        f"| BB width | {snap['bb_width']} |\n"
        f"| TTM Squeeze | {'ON' if snap['ttm_squeeze'] else 'off'} |\n"
        f"| Avg vol (20) | {snap['avg_vol']:,} |\n"
        f"| ADV (EGP est) | {snap['adv_egp']:,.0f} |\n"
        f"| Trend | {snap['trend']} |\n"
    )

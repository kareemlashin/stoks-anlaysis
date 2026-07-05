"""Wyckoff 9 buying/selling tests — heuristic scoring from OHLCV."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from indicators import load_ohlcv_csv, sma


@dataclass
class WyckoffResult:
    phase: str
    buy_score: int
    sell_score: int
    buy_tests: list[tuple[int, str, bool, str]]
    sell_tests: list[tuple[int, str, bool, str]]
    target: float
    stop: float
    rr_ratio: float
    verdict: str


def _recent_range(df: pd.DataFrame, n: int = 60) -> tuple[float, float]:
    tail = df.tail(n)
    return float(tail["low"].min()), float(tail["high"].max())


def _spring_detected(df: pd.DataFrame, support: float, lookback: int = 20) -> tuple[bool, str]:
    tail = df.tail(lookback)
    for _, row in tail.iterrows():
        if row["low"] < support * 0.995 and row["close"] > support:
            return True, f"sweep L={row['low']:.2f} close>{support:.2f}"
    return False, "no spring in window"


def _volume_pattern(df: pd.DataFrame, n: int = 30) -> tuple[bool, str]:
    if df["volume"].sum() <= 0:
        return False, "no volume data"
    tail = df.tail(n).copy()
    tail["ret"] = tail["close"].pct_change()
    up = tail[tail["ret"] > 0]
    down = tail[tail["ret"] < 0]
    if len(up) < 3 or len(down) < 3:
        return False, "insufficient bars"
    up_vol = up["volume"].mean()
    down_vol = down["volume"].mean()
    ok = up_vol > down_vol * 1.05
    return ok, f"rally vol {up_vol:.0f} vs reaction {down_vol:.0f}"


def _higher_lows(df: pd.DataFrame, n: int = 20) -> tuple[bool, str]:
    tail = df.tail(n)
    lows = tail["low"].values
    if len(lows) < 10:
        return False, "short history"
    mid = len(lows) // 2
    first = float(np.min(lows[:mid]))
    second = float(np.min(lows[mid:]))
    ok = second > first
    return ok, f"low1={first:.2f} low2={second:.2f}"


def _higher_highs(df: pd.DataFrame, n: int = 20) -> tuple[bool, str]:
    tail = df.tail(n)
    highs = tail["high"].values
    if len(highs) < 10:
        return False, "short history"
    mid = len(highs) // 2
    first = float(np.max(highs[:mid]))
    second = float(np.max(highs[mid:]))
    ok = second > first
    return ok, f"high1={first:.2f} high2={second:.2f}"


def _lower_highs(df: pd.DataFrame, n: int = 20) -> tuple[bool, str]:
    ok, ev = _higher_highs(df, n)
    return not ok, ev


def _lower_lows(df: pd.DataFrame, n: int = 20) -> tuple[bool, str]:
    ok, ev = _higher_lows(df, n)
    return not ok, ev


def _base_forming(df: pd.DataFrame, n: int = 40) -> tuple[bool, str]:
    tail = df.tail(n)
    rng = float(tail["high"].max() - tail["low"].min())
    mid = float(tail["close"].mean())
    if mid <= 0:
        return False, "invalid"
    pct = rng / mid * 100
    ok = pct < 25
    return ok, f"range {pct:.1f}% of price"


def _stride_broken_bull(df: pd.DataFrame, n: int = 30) -> tuple[bool, str]:
    tail = df.tail(n)
    c = tail["close"]
    ma = sma(c, 10)
    ok = float(c.iloc[-1]) > float(ma.iloc[-1]) and float(c.iloc[-5]) > float(c.iloc[-15])
    return ok, f"close {float(c.iloc[-1]):.2f} vs MA10 {float(ma.iloc[-1]):.2f}"


def _stride_broken_bear(df: pd.DataFrame, n: int = 30) -> tuple[bool, str]:
    tail = df.tail(n)
    c = tail["close"]
    ma = sma(c, 10)
    ok = float(c.iloc[-1]) < float(ma.iloc[-1]) and float(c.iloc[-5]) < float(c.iloc[-15])
    return ok, f"close {float(c.iloc[-1]):.2f} vs MA10 {float(ma.iloc[-1]):.2f}"


def _sc_st_pattern(df: pd.DataFrame, n: int = 60) -> tuple[bool, str]:
    if df["volume"].sum() <= 0:
        return False, "no volume"
    tail = df.tail(n)
    avg_vol = tail["volume"].mean()
    climax = tail[tail["volume"] > avg_vol * 2.0]
    if climax.empty:
        return False, "no climax bar"
    idx = climax.index[-1]
    after = df.loc[idx:].tail(15)
    if len(after) < 3:
        return False, "no secondary test window"
    st_vol = after["volume"].iloc[1:].min()
    ok = st_vol < climax["volume"].iloc[-1] * 0.7
    return ok, f"climax vol {climax['volume'].iloc[-1]:.0f} ST {st_vol:.0f}"


def _rs_improving(df: pd.DataFrame, bench: pd.DataFrame | None) -> tuple[bool, str]:
    if bench is None or len(bench) < 20:
        return False, "no benchmark CSV"
    n = min(26, len(df), len(bench))
    s = df["close"].tail(n).pct_change().fillna(0).add(1).prod() - 1
    b = bench["close"].tail(n).pct_change().fillna(0).add(1).prod() - 1
    ok = s > b
    return ok, f"stock {s*100:.1f}% vs bench {b*100:.1f}%"


def infer_phase(buy: int, sell: int) -> str:
    if buy >= 5 and sell < 5:
        return "Accumulation → Markup"
    if sell >= 5 and buy < 5:
        return "Distribution → Markdown"
    if buy >= 5 and sell >= 5:
        return "Transition (conflicted)"
    return "Unclear / Range"


def run_wyckoff_tests(
    df: pd.DataFrame,
    *,
    stop: float | None = None,
    target: float | None = None,
    support: float | None = None,
    bench: pd.DataFrame | None = None,
) -> WyckoffResult:
    close = float(df["close"].iloc[-1])
    lo, hi = _recent_range(df)
    support = support or lo
    stop = stop or support * 0.98
    target = target or hi

    risk = max(close - stop, 0.01)
    reward = max(target - close, 0)
    rr = round(reward / risk, 2) if risk else 0.0

    buy_tests: list[tuple[int, str, bool, str]] = []
    sell_tests: list[tuple[int, str, bool, str]] = []

    t1, e1 = close <= support * 1.08, f"near support {support:.2f}"
    buy_tests.append((1, "Downside objective near support", t1, e1))

    t2, e2 = _sc_st_pattern(df)
    buy_tests.append((2, "SC + Secondary Test pattern", t2, e2))

    t3, e3 = _volume_pattern(df)
    buy_tests.append((3, "Bullish vol: up rallies > down reactions", t3, e3))

    t4, e4 = _stride_broken_bull(df)
    buy_tests.append((4, "Downward stride broken", t4, e4))

    t5, e5 = _higher_lows(df)
    buy_tests.append((5, "Higher lows forming", t5, e5))

    t6, e6 = _higher_highs(df)
    buy_tests.append((6, "Higher highs forming", t6, e6))

    t7, e7 = _spring_detected(df, support)
    buy_tests.append((7, "Spring or shakeout", t7, e7))

    t8, e8 = _rs_improving(df, bench)
    buy_tests.append((8, "Stronger than benchmark (RS)", t8, e8))

    t9, e9 = _base_forming(df)
    buy_tests.append((9, "Base / horizontal range", t9, e9))

    t10, e10 = rr >= 3.0, f"upside {reward:.2f} / risk {risk:.2f} = {rr}:1"
    buy_tests.append((10, "Upside ≥ 3× stop risk", t10, e10))

    s1, se1 = close >= hi * 0.92, f"near highs {hi:.2f}"
    sell_tests.append((1, "Upside objective accomplished", s1, se1))

    st_ok, st_ev = _sc_st_pattern(df)
    s2 = st_ok and close > hi * 0.85
    se2 = f"{st_ev}; near highs={close > hi * 0.85}"
    sell_tests.append((2, "PS + BC + Secondary Test", s2, se2))

    vol_ok, vol_ev = _volume_pattern(df)
    s3 = (not vol_ok) and df["volume"].sum() > 0
    se3 = f"inverse of bull vol: {vol_ev}"
    sell_tests.append((3, "Bearish vol pattern", s3, se3))

    s4, se4 = _stride_broken_bear(df)
    sell_tests.append((4, "Upward stride broken", s4, se4))

    s5, se5 = _lower_highs(df)
    sell_tests.append((5, "Lower highs forming", s5, se5))

    s6, se6 = _lower_lows(df)
    sell_tests.append((6, "Lower lows forming", s6, se6))

    last_h = float(df["high"].iloc[-1])
    s7 = last_h > hi * 0.98 and close < hi * 0.95
    se7 = f"last H={last_h:.2f} vs range hi={hi:.2f}"
    sell_tests.append((7, "Upthrust / UTAD", s7, se7))

    s8, se8 = not _rs_improving(df, bench)[0] if bench is not None else (False, "no benchmark")
    sell_tests.append((8, "Weaker than benchmark", s8, se8))

    bf_ok, bf_ev = _base_forming(df)
    s9 = bf_ok and close > hi * 0.85
    se9 = f"{bf_ev}; at top={close > hi * 0.85}"
    sell_tests.append((9, "Crown at top (lateral near highs)", s9, se9))

    down_risk = max(stop - close, 0.01) if close < stop else max(close - lo, 0.01)
    s10 = (close - target) / down_risk >= 3 if target < close else False
    se10 = f"downside vs stop (target={target:.2f})"
    sell_tests.append((10, "Downside ≥ 3× stop risk", s10, se10))

    buy_score = sum(1 for _, _, ok, _ in buy_tests if ok)
    sell_score = sum(1 for _, _, ok, _ in sell_tests if ok)
    phase = infer_phase(buy_score, sell_score)

    if buy_score >= 5 and sell_score < 5:
        verdict = f"🟢 LONG bias — {buy_score}/10 buying tests pass (min 5)"
    elif sell_score >= 5:
        verdict = f"🔴 EXIT/SHORT bias — {sell_score}/10 selling tests pass"
    else:
        verdict = f"🟡 NEUTRAL — buy {buy_score}/10 · sell {sell_score}/10"

    return WyckoffResult(
        phase=phase,
        buy_score=buy_score,
        sell_score=sell_score,
        buy_tests=buy_tests,
        sell_tests=sell_tests,
        target=target,
        stop=stop,
        rr_ratio=rr,
        verdict=verdict,
    )


def format_wyckoff_md(res: WyckoffResult, label: str = "") -> str:
    title = f"## Wyckoff 9 Tests — {label}\n\n" if label else ""
    lines = [
        title,
        f"**Phase:** {res.phase} · **R:R** {res.rr_ratio}:1 "
        f"(target {res.target:.2f} / stop {res.stop:.2f})\n",
        f"**{res.verdict}**\n",
        "### Buying Tests\n",
        "| # | Test | Pass | Evidence |",
        "|---|------|------|----------|",
    ]
    for num, name, ok, ev in res.buy_tests:
        lines.append(f"| {num} | {name} | {'✅' if ok else '❌'} | {ev} |")
    lines += [
        f"\n**Buy score:** {res.buy_score}/10 (need ≥5 for long)\n",
        "### Selling Tests\n",
        "| # | Test | Pass | Evidence |",
        "|---|------|------|----------|",
    ]
    for num, name, ok, ev in res.sell_tests:
        lines.append(f"| {num} | {name} | {'✅' if ok else '❌'} | {ev} |")
    lines.append(f"\n**Sell score:** {res.sell_score}/10\n")
    return "\n".join(lines)


def wyckoff_from_csv(
    path: str,
    *,
    stop: float | None = None,
    target: float | None = None,
    support: float | None = None,
    bench_path: str | None = None,
) -> WyckoffResult:
    df = load_ohlcv_csv(path)
    bench = load_ohlcv_csv(bench_path) if bench_path else None
    return run_wyckoff_tests(df, stop=stop, target=target, support=support, bench=bench)

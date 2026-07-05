"""Simple signal backtests on OHLCV CSV — MA cross, RSI bounce, trend follow."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from indicators import ema, load_ohlcv_csv, rsi, sma


@dataclass
class BacktestResult:
    strategy: str
    trades: int
    win_rate: float
    avg_return_pct: float
    total_return_pct: float
    max_drawdown_pct: float
    sharpe_approx: float


def _max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    dd = (equity - peak) / peak.replace(0, np.nan)
    return float(abs(dd.min()) * 100) if len(dd) else 0.0


def _run_trades(signals: pd.Series, df: pd.DataFrame, hold_bars: int = 5) -> BacktestResult:
    """Enter on signal=1, exit after hold_bars or signal=-1."""
    close = df["close"].values
    n = len(df)
    returns: list[float] = []
    i = 0
    while i < n - hold_bars:
        if signals.iloc[i] == 1:
            entry = close[i]
            exit_i = min(i + hold_bars, n - 1)
            for j in range(i + 1, exit_i + 1):
                if signals.iloc[j] == -1:
                    exit_i = j
                    break
            ret = (close[exit_i] - entry) / entry * 100
            returns.append(ret)
            i = exit_i + 1
        else:
            i += 1

    if not returns:
        return BacktestResult("unknown", 0, 0.0, 0.0, 0.0, 0.0, 0.0)

    arr = np.array(returns)
    wins = (arr > 0).sum()
    equity = (1 + arr / 100).cumprod()
    eq_s = pd.Series(equity)
    sharpe = float(arr.mean() / arr.std()) if arr.std() > 0 else 0.0

    return BacktestResult(
        strategy="",
        trades=len(returns),
        win_rate=round(wins / len(returns) * 100, 1),
        avg_return_pct=round(float(arr.mean()), 2),
        total_return_pct=round(float((eq_s.iloc[-1] - 1) * 100), 2),
        max_drawdown_pct=round(_max_drawdown(eq_s), 2),
        sharpe_approx=round(sharpe, 2),
    )


def strategy_ma_cross(df: pd.DataFrame, fast: int = 20, slow: int = 50) -> pd.Series:
    c = df["close"]
    f, s = sma(c, fast), sma(c, slow)
    sig = pd.Series(0, index=df.index)
    cross_up = (f > s) & (f.shift(1) <= s.shift(1))
    cross_dn = (f < s) & (f.shift(1) >= s.shift(1))
    sig[cross_up] = 1
    sig[cross_dn] = -1
    return sig


def strategy_rsi_bounce(df: pd.DataFrame, oversold: float = 30, overbought: float = 70) -> pd.Series:
    c = df["close"]
    sig = pd.Series(0, index=df.index)
    for i in range(15, len(df)):
        window = c.iloc[: i + 1]
        r = rsi(window, 14)
        prev_r = rsi(c.iloc[:i], 14) if i > 14 else 50
        if prev_r < oversold and r > oversold:
            sig.iloc[i] = 1
        elif r > overbought:
            sig.iloc[i] = -1
    return sig


def strategy_trend_follow(df: pd.DataFrame, ma_n: int = 20) -> pd.Series:
    c = df["close"]
    m = sma(c, ma_n)
    sig = pd.Series(0, index=df.index)
    sig[(c > m) & (c.shift(1) <= m.shift(1))] = 1
    sig[(c < m) & (c.shift(1) >= m.shift(1))] = -1
    return sig


def strategy_macd_cross(df: pd.DataFrame) -> pd.Series:
    c = df["close"]
    m = ema(c, 12) - ema(c, 26)
    sig_line = ema(m, 9)
    hist = m - sig_line
    signals = pd.Series(0, index=df.index)
    cross_up = (hist > 0) & (hist.shift(1) <= 0)
    cross_dn = (hist < 0) & (hist.shift(1) >= 0)
    signals[cross_up] = 1
    signals[cross_dn] = -1
    return signals


STRATEGIES = {
    "ma_cross": ("MA 20/50 Golden Cross", strategy_ma_cross),
    "rsi_bounce": ("RSI(14) oversold bounce", strategy_rsi_bounce),
    "trend_ma20": ("Close cross MA20", strategy_trend_follow),
    "macd": ("MACD histogram cross", strategy_macd_cross),
}


def backtest_csv(path: str, hold_bars: int = 5) -> list[BacktestResult]:
    df = load_ohlcv_csv(path)
    results: list[BacktestResult] = []
    for key, (name, fn) in STRATEGIES.items():
        sig = fn(df)
        r = _run_trades(sig, df, hold_bars=hold_bars)
        r.strategy = name
        results.append(r)
    return results


def format_backtest_md(results: list[BacktestResult], label: str = "") -> str:
    title = f"## Backtest — {label}\n\n" if label else "## Backtest Results\n\n"
    lines = [
        title,
        "| Strategy | Trades | Win% | Avg ret | Total ret | Max DD | Sharpe~ |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for r in results:
        lines.append(
            f"| {r.strategy} | {r.trades} | {r.win_rate}% | {r.avg_return_pct:+.2f}% | "
            f"{r.total_return_pct:+.2f}% | {r.max_drawdown_pct:.2f}% | {r.sharpe_approx} |"
        )
    lines.append(
        "\n> ⚠️ Past performance ≠ future · EGX microcap has gap/slippage not modeled · "
        "hold period fixed · verify on your CSV"
    )
    return "\n".join(lines)

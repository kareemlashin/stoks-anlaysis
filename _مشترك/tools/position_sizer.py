"""Position sizing — Minervini-style risk percent model."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass
class SizeResult:
    capital: float
    risk_pct: float
    risk_egp: float
    entry: float
    stop: float
    stop_dist_pct: float
    max_shares: int
    position_value: float
    position_pct: float
    liquidity_days: float | None


def calc_position_size(
    capital: float,
    risk_pct: float,
    entry: float,
    stop: float,
    *,
    avg_daily_volume: float | None = None,
    max_pct_of_adv: float = 0.33,
) -> SizeResult:
    if entry <= 0 or stop <= 0:
        raise ValueError("entry and stop must be positive")
    if entry == stop:
        raise ValueError("entry and stop must differ")

    risk_egp = capital * (risk_pct / 100)
    stop_dist = abs(entry - stop)
    stop_dist_pct = stop_dist / entry * 100
    max_shares = int(risk_egp / stop_dist) if stop_dist else 0
    pos_value = max_shares * entry
    pos_pct = (pos_value / capital * 100) if capital else 0.0

    liq_days = None
    if avg_daily_volume and avg_daily_volume > 0:
        liq_days = max_shares / (avg_daily_volume * max_pct_of_adv)

    return SizeResult(
        capital=capital,
        risk_pct=risk_pct,
        risk_egp=round(risk_egp, 2),
        entry=entry,
        stop=stop,
        stop_dist_pct=round(stop_dist_pct, 2),
        max_shares=max_shares,
        position_value=round(pos_value, 2),
        position_pct=round(pos_pct, 2),
        liquidity_days=round(liq_days, 1) if liq_days is not None else None,
    )


def format_size_md(r: SizeResult) -> str:
    liq = f"{r.liquidity_days} days (33% ADV/day)" if r.liquidity_days is not None else "N/A (no vol data)"
    return (
        f"| Metric | Value |\n|---|---|\n"
        f"| Capital | {r.capital:,.0f} ج |\n"
        f"| Risk | {r.risk_pct}% = {r.risk_egp:,.2f} ج |\n"
        f"| Entry / Stop | {r.entry} / {r.stop} ({r.stop_dist_pct}% dist) |\n"
        f"| **Max shares** | **{r.max_shares:,}** |\n"
        f"| Position value | {r.position_value:,.2f} ج ({r.position_pct}% of capital) |\n"
        f"| Exit liquidity est | {liq} |\n"
    )

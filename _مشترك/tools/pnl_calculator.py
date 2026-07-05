"""PnL calculator with EGX tax and commission estimates."""

from __future__ import annotations

from dataclasses import dataclass


# EGX capital gains tax (verify current rate — default 10% on individuals)
DEFAULT_TAX_RATE = 0.10
DEFAULT_FEE_BPS = 12.5  # broker round-trip estimate in bps per side


@dataclass
class PnLResult:
    qty: int
    avg: float
    close: float
    gross_pnl: float
    gross_pnl_pct: float
    value: float
    cost_basis: float
    fees: float
    tax: float
    net_pnl: float
    net_pnl_pct: float


def calc_pnl(
    qty: int,
    avg: float,
    close: float,
    *,
    tax_rate: float = DEFAULT_TAX_RATE,
    fee_bps: float = DEFAULT_FEE_BPS,
    apply_tax: bool = True,
) -> PnLResult:
    cost = qty * avg
    value = qty * close
    gross = value - cost
    gross_pct = (gross / cost * 100) if cost else 0.0

    # fees on buy + sell notional
    fees = (cost + value) * (fee_bps / 10000)
    taxable_gain = max(gross - fees, 0.0)
    tax = taxable_gain * tax_rate if apply_tax and gross > 0 else 0.0
    net = gross - fees - tax
    net_pct = (net / cost * 100) if cost else 0.0

    return PnLResult(
        qty=qty,
        avg=avg,
        close=close,
        gross_pnl=round(gross, 2),
        gross_pnl_pct=round(gross_pct, 2),
        value=round(value, 2),
        cost_basis=round(cost, 2),
        fees=round(fees, 2),
        tax=round(tax, 2),
        net_pnl=round(net, 2),
        net_pnl_pct=round(net_pct, 2),
    )


def format_pnl_md(r: PnLResult) -> str:
    return (
        f"| Metric | Value |\n|---|---|\n"
        f"| Qty × Avg | {r.qty:,} @ {r.avg} |\n"
        f"| Close | {r.close} |\n"
        f"| Cost basis | {r.cost_basis:,.2f} ج |\n"
        f"| Market value | {r.value:,.2f} ج |\n"
        f"| Gross PnL | {r.gross_pnl:+,.2f} ج ({r.gross_pnl_pct:+.2f}%) |\n"
        f"| Fees (est) | −{r.fees:,.2f} ج |\n"
        f"| Tax (est) | −{r.tax:,.2f} ج |\n"
        f"| **Net PnL** | **{r.net_pnl:+,.2f} ج ({r.net_pnl_pct:+.2f}%)** |\n"
    )

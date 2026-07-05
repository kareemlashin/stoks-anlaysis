"""Murphy intermarket macro fetch — yfinance proxies for EGX gate."""

from __future__ import annotations

from dataclasses import dataclass

# EGX symbol on Yahoo for index
EGX30_SYMBOL = "^CASE30"

MACRO_SYMBOLS = {
    "us10y": ("^TNX", "US 10Y Yield"),
    "dxy": ("DX-Y.NYB", "Dollar Index"),
    "gold": ("GC=F", "Gold"),
    "oil": ("CL=F", "WTI Oil"),
    "vix": ("^VIX", "VIX Fear"),
}


@dataclass
class MacroRow:
    key: str
    name: str
    symbol: str
    close: float
    ma20: float
    trend: str
    vs_ma: str
    pass_long: bool
    note: str


def _fetch_history(symbol: str, period: str = "6mo"):
    try:
        import yfinance as yf
    except ImportError as exc:
        raise ImportError("Install yfinance: pip install yfinance") from exc

    try:
        t = yf.Ticker(symbol)
        h = t.history(period=period, auto_adjust=True)
        if h.empty:
            return None
        return h
    except Exception:
        return None


def _trend(close: float, ma20: float) -> str:
    if close > ma20 * 1.01:
        return "↑"
    if close < ma20 * 0.99:
        return "↓"
    return "→"


def _macro_pass(key: str, close: float, ma20: float) -> tuple[bool, str]:
    t = _trend(close, ma20)
    if key == "us10y":
        ok = t != "↑"
        return ok, "↑ yield = EM headwind" if not ok else "yields stable/down"
    if key == "dxy":
        ok = t != "↑"
        return ok, "strong $ = EM headwind" if not ok else "dollar soft/neutral"
    if key == "vix":
        ok = close < 25 and t != "↑"
        return ok, "elevated fear" if not ok else "fear contained"
    if key == "gold":
        ok = True
        return ok, "inflation/geopolitical context"
    if key == "oil":
        ok = t != "↑"
        return ok, "oil spike = cost pressure" if not ok else "oil stable"
    return True, ""


def fetch_macro(include_egx: bool = True) -> list[MacroRow]:
    rows: list[MacroRow] = []

    if include_egx:
        h = _fetch_history(EGX30_SYMBOL)
        if h is not None and len(h) >= 20:
            close = float(h["Close"].iloc[-1])
            ma20 = float(h["Close"].tail(20).mean())
            t = _trend(close, ma20)
            rows.append(
                MacroRow(
                    key="egx30",
                    name="EGX30 Index",
                    symbol=EGX30_SYMBOL,
                    close=close,
                    ma20=ma20,
                    trend=t,
                    vs_ma=f"{((close/ma20-1)*100):+.1f}%",
                    pass_long=t == "↑",
                    note="local gate (weight ×2)",
                )
            )

    for key, (sym, name) in MACRO_SYMBOLS.items():
        h = _fetch_history(sym)
        if h is None or len(h) < 20:
            continue
        close = float(h["Close"].iloc[-1])
        ma20 = float(h["Close"].tail(20).mean())
        t = _trend(close, ma20)
        ok, note = _macro_pass(key, close, ma20)
        rows.append(
            MacroRow(
                key=key,
                name=name,
                symbol=sym,
                close=round(close, 2),
                ma20=round(ma20, 2),
                trend=t,
                vs_ma=f"{((close/ma20-1)*100):+.1f}%",
                pass_long=ok,
                note=note,
            )
        )
    return rows


def gate_verdict(rows: list[MacroRow]) -> tuple[int, int, str]:
    egx = next((r for r in rows if r.key == "egx30"), None)
    global_rows = [r for r in rows if r.key != "egx30"]
    passes = sum(1 for r in global_rows if r.pass_long)
    local_ok = egx.pass_long if egx else False
    weighted = passes + (2 if local_ok else 0)
    total_weight = len(global_rows) + 2

    if local_ok and passes >= 2:
        verdict = "🟢 Full risk-on — new longs allowed (Tier A triggers)"
    elif local_ok or passes >= 2:
        verdict = "🟡 Mixed — Tier A only · tight stops"
    else:
        verdict = "🔴 Risk-off — no new longs · tighten existing"

    return weighted, total_weight, verdict


def format_macro_md(rows: list[MacroRow]) -> str:
    if not rows:
        return "No macro data — install yfinance and check network.\n"

    w, tw, verdict = gate_verdict(rows)
    lines = [
        "## 🌍 Intermarket Gate (Murphy)\n",
        f"**Gate score:** {w}/{tw} weighted · **Verdict:** {verdict}\n",
        "| Market | Symbol | Close | MA20 | Trend | vs MA20 | Pass long? | Note |",
        "|---|---|---:|---:|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r.name} | `{r.symbol}` | {r.close} | {r.ma20} | {r.trend} | "
            f"{r.vs_ma} | {'✅' if r.pass_long else '❌'} | {r.note} |"
        )
    lines.append(
        "\n> Rule: new EGX longs if local EGX not 🔴 AND ≥2/3 global gates pass · "
        "verify numbers before trading"
    )
    return "\n".join(lines)

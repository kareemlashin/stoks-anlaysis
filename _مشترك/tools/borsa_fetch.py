"""EGX quote fetch — Borsa API (local) with yfinance fallback."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from urllib.error import URLError
from urllib.request import Request, urlopen

# Yahoo Finance suffix for Cairo exchange
EGX_YAHOO = {
    "EAC": "EAC.CA",
    "COMI": "COMI.CA",
    "SWDY": "SWDY.CA",
    "TMGH": "TMGH.CA",
    "FWRY": "FWRY.CA",
    "EGX30": "^CASE30",
}


@dataclass
class Quote:
    symbol: str
    price: float
    change_pct: float | None
    volume: float | None
    source: str
    raw: dict | None = None


def _borsa_base() -> str:
    return os.environ.get("BORSA_URL", "http://localhost:8000").rstrip("/")


def fetch_borsa(symbol: str, timeout: float = 5.0) -> Quote | None:
    sym = symbol.upper().replace(".CA", "")
    url = f"{_borsa_base()}/v1/quote/{sym}"
    try:
        req = Request(url, headers={"Accept": "application/json"})
        with urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
        price = float(data.get("price") or data.get("close") or data.get("last") or 0)
        if price <= 0:
            return None
        ch = data.get("change_percent") or data.get("changePercent")
        vol = data.get("volume")
        return Quote(sym, price, float(ch) if ch is not None else None, float(vol) if vol else None, "borsa", data)
    except (URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError):
        return None


def fetch_yfinance(symbol: str) -> Quote | None:
    try:
        import yfinance as yf
    except ImportError:
        return None

    sym = symbol.upper().replace(".CA", "")
    ysym = EGX_YAHOO.get(sym, f"{sym}.CA")
    try:
        t = yf.Ticker(ysym)
        h = t.history(period="1mo", auto_adjust=True)
        if h.empty:
            return None
        price = float(h["Close"].iloc[-1])
        prev = float(h["Close"].iloc[-2]) if len(h) >= 2 else None
        ch_pct = ((price - prev) / prev * 100) if prev else None
        vol = float(h["Volume"].iloc[-1]) if "Volume" in h else None
        return Quote(sym, price, ch_pct, vol, "yfinance", {"yahoo": ysym})
    except Exception:
        return None


def fetch_quote(symbol: str) -> Quote:
    sym = symbol.upper().replace(".CA", "")
    q = fetch_borsa(sym)
    if q:
        return q
    q = fetch_yfinance(sym)
    if q:
        return q
    if sym == "EAC":
        return Quote(sym, 7.38, -2.12, 1_130_000, "manual-anchor", {"note": "Use TV CSV or Borsa"})
    raise RuntimeError(
        f"Could not fetch {symbol}. Start Borsa (docker), export TV CSV, or install yfinance"
    )


def fetch_history_yfinance(symbol: str, period: str = "2y", interval: str = "1d"):
    try:
        import yfinance as yf
    except ImportError as exc:
        raise ImportError("pip install yfinance") from exc

    sym = symbol.upper().replace(".CA", "")
    ysym = EGX_YAHOO.get(sym, f"{sym}.CA")
    try:
        t = yf.Ticker(ysym)
        h = t.history(period=period, interval=interval, auto_adjust=True)
        if h.empty:
            raise RuntimeError(f"No history for {symbol} ({ysym})")
        return h
    except RuntimeError:
        raise
    except Exception as exc:
        raise RuntimeError(f"No history for {symbol} ({ysym})") from exc


def save_ohlcv_csv(symbol: str, out_path: str, period: str = "2y") -> str:
    import pandas as pd

    sym = symbol.upper().replace(".CA", "")
    try:
        h = fetch_history_yfinance(symbol, period=period)
    except RuntimeError:
        if sym == "EAC":
            from sample_data import build_sample

            df = build_sample()
            df.to_csv(out_path, index=False)
            return out_path
        raise
    df = pd.DataFrame(
        {
            "time": h.index.strftime("%Y-%m-%d"),
            "open": h["Open"].values,
            "high": h["High"].values,
            "low": h["Low"].values,
            "close": h["Close"].values,
            "volume": h["Volume"].fillna(0).values,
        }
    )
    pd.DataFrame(df).to_csv(out_path, index=False)
    return out_path


def format_quote_md(q: Quote) -> str:
    ch = f"{q.change_pct:+.2f}%" if q.change_pct is not None else "—"
    vol = f"{int(q.volume):,}" if q.volume else "—"
    return (
        f"| Symbol | Price | Change | Volume | Source |\n"
        f"|---|---:|---:|---:|---|\n"
        f"| **{q.symbol}** | {q.price:.4f} | {ch} | {vol} | {q.source} |\n"
    )


def format_batch_md(quotes: list[Quote]) -> str:
    lines = ["| Symbol | Price | Change | Volume | Source |", "|---|---:|---:|---:|---|"]
    for q in quotes:
        ch = f"{q.change_pct:+.2f}%" if q.change_pct is not None else "—"
        vol = f"{int(q.volume):,}" if q.volume else "—"
        lines.append(f"| **{q.symbol}** | {q.price:.4f} | {ch} | {vol} | {q.source} |")
    return "\n".join(lines)

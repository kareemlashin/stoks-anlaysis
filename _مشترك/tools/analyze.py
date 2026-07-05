#!/usr/bin/env python3
"""EGX analysis CLI — indicators, PnL, sizing, Wyckoff, backtest, macro, fetch."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pnl_calculator import calc_pnl, format_pnl_md
from position_sizer import calc_position_size, format_size_md


def cmd_indicators(args: argparse.Namespace) -> int:
    from indicators import compute_snapshot, format_snapshot_md, load_ohlcv_csv

    df = load_ohlcv_csv(args.csv)
    snap = compute_snapshot(df)
    print(format_snapshot_md(snap, label=args.label or Path(args.csv).stem))
    return 0


def cmd_pnl(args: argparse.Namespace) -> int:
    r = calc_pnl(
        args.qty,
        args.avg,
        args.close,
        tax_rate=args.tax_rate,
        fee_bps=args.fee_bps,
        apply_tax=not args.no_tax,
    )
    print(format_pnl_md(r))
    return 0


def cmd_size(args: argparse.Namespace) -> int:
    r = calc_position_size(
        args.capital,
        args.risk_pct,
        args.entry,
        args.stop,
        avg_daily_volume=args.avg_vol,
    )
    print(format_size_md(r))
    if r.liquidity_days is not None and r.liquidity_days > 3:
        print(f"\n⚠️ Warning: exit may take {r.liquidity_days:.1f} days at 33% ADV — IPS limit is 3")
    return 0


def cmd_wyckoff(args: argparse.Namespace) -> int:
    from wyckoff_tests import format_wyckoff_md, wyckoff_from_csv

    res = wyckoff_from_csv(
        args.csv,
        stop=args.stop,
        target=args.target,
        support=args.support,
        bench_path=args.bench,
    )
    print(format_wyckoff_md(res, label=args.label or Path(args.csv).stem))
    return 0


def cmd_backtest(args: argparse.Namespace) -> int:
    from backtest_signals import backtest_csv, format_backtest_md

    results = backtest_csv(args.csv, hold_bars=args.hold)
    print(format_backtest_md(results, label=args.label or Path(args.csv).stem))
    return 0


def cmd_macro(args: argparse.Namespace) -> int:
    from macro_fetch import fetch_macro, format_macro_md

    rows = fetch_macro(include_egx=not args.no_egx)
    print(format_macro_md(rows))
    return 0


def cmd_fetch(args: argparse.Namespace) -> int:
    from borsa_fetch import fetch_quote, format_batch_md, format_quote_md, save_ohlcv_csv

    if args.save_csv:
        out = args.save_csv
        path = save_ohlcv_csv(args.symbol, out, period=args.period)
        print(f"Saved OHLCV → {path}")
        return 0

    if args.symbols:
        from borsa_fetch import fetch_quote as fq

        quotes = []
        for s in args.symbols.split(","):
            s = s.strip()
            if s:
                quotes.append(fq(s))
        print(format_batch_md(quotes))
        return 0

    q = fetch_quote(args.symbol)
    print(format_quote_md(q))
    return 0


def cmd_brief(args: argparse.Namespace) -> int:
    """Daily brief snippet: quote + macro + optional indicators/wyckoff from CSV."""
    import io

    from borsa_fetch import fetch_quote, format_quote_md
    from macro_fetch import fetch_macro, format_macro_md

    sym = args.symbol.upper()
    buf = io.StringIO()
    buf.write(f"# Daily Brief — {sym} · auto-generated\n\n")
    try:
        q = fetch_quote(sym)
        buf.write(format_quote_md(q) + "\n")
    except RuntimeError as e:
        buf.write(f"⚠️ Quote: {e}\n\n")

    if not args.no_macro:
        try:
            buf.write(format_macro_md(fetch_macro()) + "\n")
        except Exception as e:
            buf.write(f"⚠️ Macro: {e}\n\n")

    if args.csv:
        from indicators import compute_snapshot, format_snapshot_md, load_ohlcv_csv
        from wyckoff_tests import format_wyckoff_md, wyckoff_from_csv

        df = load_ohlcv_csv(args.csv)
        snap = compute_snapshot(df)
        buf.write(format_snapshot_md(snap, label=f"{sym} indicators") + "\n")
        res = wyckoff_from_csv(
            args.csv,
            stop=args.stop,
            target=args.target,
            support=args.support,
        )
        buf.write(format_wyckoff_md(res, label=sym) + "\n")

    text = buf.getvalue()
    print(text)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Saved → {args.out}")
    return 0


def cmd_openbb(args: argparse.Namespace) -> int:
    """Optional OpenBB — falls back to yfinance if OpenBB not installed."""
    sym = args.symbol.upper()
    try:
        from openbb import obb

        result = obb.equity.price.historical(sym, provider="yfinance")
        df = result.to_df()
        print(f"OpenBB historical {sym}: {len(df)} rows")
        print(df.tail(5).to_string())
        return 0
    except ImportError:
        from borsa_fetch import fetch_history_yfinance

        h = fetch_history_yfinance(sym, period=args.period)
        print(f"yfinance fallback {sym}: {len(h)} rows")
        print(h.tail(5).to_string())
        return 0


def main() -> int:
    p = argparse.ArgumentParser(description="EGX professional analysis tools")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("indicators", help="OHLCV snapshot from CSV")
    pi.add_argument("--csv", required=True)
    pi.add_argument("--label", default="")
    pi.set_defaults(func=cmd_indicators)

    pp = sub.add_parser("pnl", help="PnL with fees and tax")
    pp.add_argument("--qty", type=int, required=True)
    pp.add_argument("--avg", type=float, required=True)
    pp.add_argument("--close", type=float, required=True)
    pp.add_argument("--tax-rate", type=float, default=0.10)
    pp.add_argument("--fee-bps", type=float, default=12.5)
    pp.add_argument("--no-tax", action="store_true")
    pp.set_defaults(func=cmd_pnl)

    ps = sub.add_parser("size", help="Position size by risk %")
    ps.add_argument("--capital", type=float, required=True)
    ps.add_argument("--risk-pct", type=float, default=1.5)
    ps.add_argument("--entry", type=float, required=True)
    ps.add_argument("--stop", type=float, required=True)
    ps.add_argument("--avg-vol", type=float, default=None, help="Avg daily share volume")
    ps.set_defaults(func=cmd_size)

    pw = sub.add_parser("wyckoff", help="Wyckoff 9 tests from CSV")
    pw.add_argument("--csv", required=True)
    pw.add_argument("--stop", type=float, default=None)
    pw.add_argument("--target", type=float, default=None)
    pw.add_argument("--support", type=float, default=None)
    pw.add_argument("--bench", default=None, help="Benchmark CSV e.g. EGX30_W.csv")
    pw.add_argument("--label", default="")
    pw.set_defaults(func=cmd_wyckoff)

    pb = sub.add_parser("backtest", help="Backtest MA/RSI/MACD signals")
    pb.add_argument("--csv", required=True)
    pb.add_argument("--hold", type=int, default=5, help="Bars to hold")
    pb.add_argument("--label", default="")
    pb.set_defaults(func=cmd_backtest)

    pm = sub.add_parser("macro", help="Murphy intermarket gate (yfinance)")
    pm.add_argument("--no-egx", action="store_true")
    pm.set_defaults(func=cmd_macro)

    pf = sub.add_parser("fetch", help="Quote via Borsa or yfinance")
    pf.add_argument("--symbol", default="EAC")
    pf.add_argument("--symbols", default="", help="Comma-separated batch")
    pf.add_argument("--save-csv", default="", help="Save daily OHLCV to path")
    pf.add_argument("--period", default="2y")
    pf.set_defaults(func=cmd_fetch)

    pbr = sub.add_parser("brief", help="Daily brief: quote + macro + optional TA")
    pbr.add_argument("--symbol", default="EAC")
    pbr.add_argument("--csv", default="", help="Local CSV for indicators/wyckoff")
    pbr.add_argument("--stop", type=float, default=7.25)
    pbr.add_argument("--target", type=float, default=12.57)
    pbr.add_argument("--support", type=float, default=7.25)
    pbr.add_argument("--no-macro", action="store_true")
    pbr.add_argument("--out", default="", help="Write markdown to file")
    pbr.set_defaults(func=cmd_brief)

    po = sub.add_parser("openbb", help="OpenBB historical (optional)")
    po.add_argument("--symbol", default="EAC")
    po.add_argument("--period", default="1y")
    po.set_defaults(func=cmd_openbb)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

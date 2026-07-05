"""Generate sample EAC daily OHLCV when Yahoo/Borsa unavailable — use TV export for production."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


# Anchor closes from project analysis (approximate)
ANCHORS = [
    ("2025-10-01", 4.20),
    ("2025-12-01", 4.80),
    ("2026-01-15", 5.20),
    ("2026-03-01", 5.50),
    ("2026-04-15", 6.00),
    ("2026-05-15", 6.50),
    ("2026-06-01", 7.25),
    ("2026-06-15", 9.50),
    ("2026-06-25", 10.17),
    ("2026-07-01", 7.54),
    ("2026-07-02", 7.51),
    ("2026-07-03", 7.48),
    ("2026-07-04", 7.50),
    ("2026-07-05", 7.38),
]


def build_sample(start: str = "2025-09-01", end: str = "2026-07-05") -> pd.DataFrame:
    dates = pd.bdate_range(start=start, end=end)
    anchor_df = pd.DataFrame(ANCHORS, columns=["time", "close"])
    anchor_df["time"] = pd.to_datetime(anchor_df["time"])
    anchor_df = anchor_df.set_index("time").reindex(dates).interpolate(method="time")
    close = anchor_df["close"].bfill().ffill()

    rng = np.random.default_rng(42)
    noise = rng.normal(0, 0.015, len(close))
    close = close * (1 + noise)
    # Force last anchor
    close.iloc[-1] = 7.38

    rows = []
    for i, (dt, c) in enumerate(close.items()):
        vol_base = 400_000 if c < 7 else 900_000
        if c > 9.5:
            vol_base = 2_000_000
        if str(dt.date()) == "2026-07-05":
            vol_base = 1_130_000
        spread = c * 0.025
        o = float(close.iloc[i - 1]) if i else c * 0.99
        h = max(o, c) + spread * rng.uniform(0.2, 0.8)
        l = min(o, c) - spread * rng.uniform(0.2, 0.8)
        if str(dt.date()) == "2026-07-05":
            h, l = 7.72, 7.35
        vol = int(vol_base * rng.uniform(0.7, 1.3))
        rows.append(
            {
                "time": dt.strftime("%Y-%m-%d"),
                "open": round(o, 4),
                "high": round(h, 4),
                "low": round(l, 4),
                "close": round(float(c), 4),
                "volume": vol,
            }
        )
    return pd.DataFrame(rows)


def main() -> int:
    p = argparse.ArgumentParser(description="Generate sample EAC OHLCV CSV")
    p.add_argument("--out", default="_مشترك/data/EAC_D.csv")
    args = p.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df = build_sample()
    df.to_csv(out, index=False)
    print(f"Wrote {len(df)} rows → {out}")
    print(f"Last close: {df['close'].iloc[-1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

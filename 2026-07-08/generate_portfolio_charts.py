#!/usr/bin/env python3
"""Portfolio charts — 5 stocks · 8 Jul 2026"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 160
BG, PANEL, GRID = '#0a0e14', '#121820', '#1c2330'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9'

STOCKS = [
    dict(code='EAC', name='ثمار', qty=40_000, avg=7.75, now=7.07,
         stop=6.88, t1=7.45, t2=7.72, t3=8.14, action='EXIT', color=RED,
         lo=6.5, hi=10.5, resist=[7.25, 7.45, 7.72, 10.17], support=[6.88, 6.50]),
    dict(code='AALR', name='استصلاح', qty=1_000, avg=221, now=225.50,
         stop=215, t1=240, t2=257, t3=280, action='REDUCE', color=GREEN,
         lo=200, hi=285, resist=[248, 257, 280], support=[222, 210, 205]),
    dict(code='AFDI', name='أهلي تنمية', qty=3_000, avg=45, now=46.00,
         stop=44, t1=48, t2=51.86, t3=55, action='HOLD', color=GREEN,
         lo=41, hi=56, resist=[48, 51.86, 55], support=[44, 41.5, 36]),
    dict(code='UPMS', name='اتحاد صيدلي', qty=10_000, avg=12.61, now=12.56,
         stop=10.50, t1=14, t2=15, t3=16.50, action='HOLD', color=YELLOW,
         lo=10, hi=17, resist=[13.61, 14, 15, 16.50], support=[12, 11.5, 10.5]),
    dict(code='ACAP', name='ايه كابيتال', qty=20_000, avg=8.63, now=8.64,
         stop=7.85, t1=9.50, t2=10, t3=10.55, action='HOLD', color=YELLOW,
         lo=7.5, hi=11, resist=[9.50, 10, 10.55], support=[8.50, 8.00, 7.85]),
]

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL, 'axes.edgecolor': GRAY,
    'text.color': WHITE, 'xtick.color': GRAY, 'ytick.color': GRAY,
    'grid.color': GRID, 'font.size': 9,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def pnl(qty, avg, price):
    return int((price - avg) * qty)


def chart_portfolio_overview():
    fig, ax = plt.subplots(figsize=(14, 8))
    codes = [s['code'] for s in STOCKS]
    pnls = [pnl(s['qty'], s['avg'], s['now']) for s in STOCKS]
    colors = [GREEN if p >= 0 else RED for p in pnls]
    bars = ax.bar(codes, pnls, color=colors, edgecolor=WHITE, linewidth=0.8)
    ax.axhline(0, color=GRAY, lw=1)
    for bar, p, s in zip(bars, pnls, STOCKS):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + (800 if p >= 0 else -2500),
                f'{p:+,} ج\n{s["action"]}', ha='center', fontsize=8, fontweight='bold')
    total = sum(pnls)
    ax.set_title(f'محفظة — PnL @ 8 Jul 2026\nNet: {total:+,} EGP', fontsize=14, fontweight='bold')
    ax.set_ylabel('PnL (EGP)')
    ax.grid(True, alpha=0.3, axis='y')
    save(fig, 'PORT-01-PnL-محفظة-2026-07-08.png')


def chart_stock_decision(s):
    fig, ax = plt.subplots(figsize=(14, 9))
    x = np.linspace(0, 10, 100)
    mid = (s['lo'] + s['hi']) / 2
    wave = mid + (s['hi'] - s['lo']) * 0.15 * np.sin(x * 1.2) + (s['now'] - mid) * x / 10
    ax.plot(x, wave, color=BLUE, lw=2.5, label='Price path (schematic)')
    ax.axhspan(s['lo'], s['hi'], alpha=0.06, color=BLUE)

    for y in s['support']:
        ax.axhline(y, color=GREEN, ls='--', lw=1.2, alpha=0.8)
        ax.text(10.2, y, f' S {y}', color=GREEN, va='center', fontsize=7)
    for y in s['resist']:
        ax.axhline(y, color=RED, ls='--', lw=1.2, alpha=0.8)
        ax.text(10.2, y, f' R {y}', color=RED, va='center', fontsize=7)

    ax.axhline(s['avg'], color=ORANGE, ls='-', lw=2, label=f'Entry {s["avg"]}')
    ax.axhline(s['now'], color=WHITE, ls='-', lw=2.5, label=f'NOW {s["now"]}')
    ax.axhline(s['stop'], color=RED, ls=':', lw=2, label=f'Stop {s["stop"]}')
    for i, (lbl, y) in enumerate([('T1', s['t1']), ('T2', s['t2']), ('T3', s['t3'])], 1):
        ax.axhline(y, color=YELLOW, ls='-.', lw=1.5)
        ax.text(0.3, y, f' {lbl}={y}', color=YELLOW, fontsize=8, fontweight='bold')

    p = pnl(s['qty'], s['avg'], s['now'])
    ax.scatter([9], [s['now']], s=200, c=s['color'], edgecolors=WHITE, lw=2, zorder=10)
    ax.text(5, s['hi'] * 0.98,
            f"{s['code']} — {s['name']}\n{s['qty']:,} @ {s['avg']} | NOW {s['now']}\n"
            f"PnL {p:+,} EGP | Action: {s['action']}",
            fontsize=11, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=s['color'], lw=2))

    ax.set_ylim(s['lo'] * 0.98, s['hi'] * 1.02)
    ax.set_xlim(0, 10.5)
    ax.set_title(f"{s['code']} — مخطط قرار · {s['action']}", fontsize=13, fontweight='bold')
    ax.legend(loc='lower left', facecolor=PANEL, fontsize=8)
    ax.grid(True, alpha=0.25)
    save(fig, f"{s['code']}-08-13-مخطط-قرار-2026-07-08.png")


def chart_stock_pnl_ladder(s):
    fig, ax = plt.subplots(figsize=(12, 7))
    levels = [('Stop', s['stop'], RED), ('NOW', s['now'], WHITE),
              ('T1', s['t1'], YELLOW), ('T2', s['t2'], GREEN), ('T3', s['t3'], GREEN)]
    ys = [pnl(s['qty'], s['avg'], y) for _, y, _ in levels]
    labels = [f'{n}\n{y}\n{ys[i]:+,}ج' for i, (n, y, _) in enumerate(levels)]
    colors = [c for _, _, c in levels]
    ax.barh(range(len(levels)), ys, color=colors, edgecolor=GRAY, height=0.6)
    ax.set_yticks(range(len(levels)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.axvline(0, color=GRAY, lw=1)
    ax.set_xlabel('PnL (EGP)')
    ax.set_title(f"{s['code']} — PnL Ladder · {s['qty']:,} @ {s['avg']}", fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='x')
    save(fig, f"{s['code']}-08-12-اهداف-PnL-2026-07-08.png")


def chart_stock_sr(s):
    fig, ax = plt.subplots(figsize=(12, 8))
    prices = sorted(set(s['support'] + s['resist'] + [s['avg'], s['now'], s['stop']]))
    for i, y in enumerate(prices):
        if y in s['resist']:
            c, lbl = RED, 'R'
        elif y in s['support']:
            c, lbl = GREEN, 'S'
        elif y == s['now']:
            c, lbl = WHITE, 'NOW'
        elif y == s['avg']:
            c, lbl = ORANGE, 'AVG'
        else:
            c, lbl = GRAY, 'STOP'
        ax.barh(i, 1, left=0, color=c, alpha=0.7, height=0.7)
        ax.text(0.5, i, f'{lbl}  {y}', ha='center', va='center', fontweight='bold', fontsize=10)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, len(prices) - 0.5)
    ax.set_title(f"{s['code']} — دعم / مقاومة", fontsize=12, fontweight='bold')
    ax.axis('off')
    save(fig, f"{s['code']}-08-05-دعم-مقاومة-2026-07-08.png")


def main():
    print('Generating portfolio charts...')
    chart_portfolio_overview()
    for s in STOCKS:
        chart_stock_decision(s)
        chart_stock_pnl_ladder(s)
        chart_stock_sr(s)
    print(f'Done — {1 + len(STOCKS)*3} charts in {OUT}')


if __name__ == '__main__':
    main()

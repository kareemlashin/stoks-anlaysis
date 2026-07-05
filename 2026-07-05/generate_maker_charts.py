#!/usr/bin/env python3
"""Generate EAC maker behavior analysis charts."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
plt.rcParams.update({
    'figure.facecolor': '#0d1117',
    'axes.facecolor': '#161b22',
    'axes.edgecolor': '#30363d',
    'axes.labelcolor': '#c9d1d9',
    'text.color': '#c9d1d9',
    'xtick.color': '#8b949e',
    'ytick.color': '#8b949e',
    'grid.color': '#21262d',
    'font.size': 10,
})

GREEN = '#3fb950'
RED = '#f85149'
YELLOW = '#d29922'
BLUE = '#58a6ff'
PURPLE = '#bc8cff'
GRAY = '#8b949e'
ORANGE = '#f0883e'


def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f'Saved: {path}')


# ── Chart 1: Wyckoff Maker Timeline ──────────────────────────────────
def chart_wyckoff_timeline():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#0d1117')

    phases = [
        ('Silent Accum\n2025', 0, 3.2, GREEN, 'Buy cheap\nVol: dead'),
        ('Markup 1\nMar-Apr', 1, 4.8, GREEN, 'Gradual rise'),
        ('Re-Accum\nMay-Jun', 2, 5.0, YELLOW, 'Flat line 5.0\nAbsorption'),
        ('Explosive\nJun 11-17', 3, 10.17, ORANGE, 'Parabolic\n48M vol'),
        ('Distribution\nJun 17-18', 4, 9.5, RED, 'Sold climax\nat 10.17'),
        ('Freeze\nJun 22-Now', 5, 7.52, BLUE, 'Vol dying\nHold 7.50'),
        ('??? AGM\nJul 6', 6, 8.0, PURPLE, 'Next move\nTBD'),
    ]

    xs = [p[1] for p in phases]
    ys = [p[2] for p in phases]
    colors = [p[3] for p in phases]

    ax.plot(xs, ys, 'o-', color=GRAY, linewidth=2, markersize=0, alpha=0.5)
    for i, (name, x, y, c, note) in enumerate(phases):
        ax.scatter(x, y, s=200, c=c, zorder=5, edgecolors='white', linewidths=1.5)
        ax.annotate(name, (x, y), textcoords='offset points', xytext=(0, 18),
                    ha='center', fontsize=9, fontweight='bold', color=c)
        ax.annotate(note, (x, y), textcoords='offset points', xytext=(0, -35),
                    ha='center', fontsize=7, color=GRAY)

    # User entry line
    ax.axhline(7.75, color=RED, linestyle='--', alpha=0.7, linewidth=1.5)
    ax.text(6.3, 7.85, 'Your entry 7.75', color=RED, fontsize=9)
    ax.axhline(7.25, color=YELLOW, linestyle=':', alpha=0.8)
    ax.text(6.3, 7.15, 'Death line 7.25', color=YELLOW, fontsize=8)
    ax.axhline(7.50, color=BLUE, linestyle='-', alpha=0.5, linewidth=2)
    ax.text(-0.3, 7.55, 'POC 7.50', color=BLUE, fontsize=8)

    ax.set_xlim(-0.5, 6.8)
    ax.set_ylim(2.5, 11)
    ax.set_ylabel('Price (EGP)', fontsize=11)
    ax.set_title('EAC — Maker Playbook Timeline (Wyckoff)', fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.3)
    ax.set_xticks([])
    save(fig, 'EAC-الميكr-تايملاين-Wyckoff-2026-07-05.png')


# ── Chart 2: Three Scenarios ─────────────────────────────────────────
def chart_scenarios():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6), sharey=True)
    fig.patch.set_facecolor('#0d1117')
    fig.suptitle('EAC — What the Maker Might Do Next (3 Scenarios)', fontsize=14, fontweight='bold', y=1.02)

    days = np.arange(0, 15)
    price_now = 7.52

    scenarios = [
        ('A: Re-Accumulation (45%)', GREEN,
         [7.52, 7.48, 7.55, 7.60, 7.58, 7.65, 7.80, 8.00, 8.20, 8.50, 8.80, 9.20, 9.80, 10.50, 11.00],
         'AGM confirms free shares\nGap up → hold 7.50\nBreak 8.14 with volume\nTarget: 10.17 → 12.57'),
        ('B: Sell the News (35%)', RED,
         [7.52, 7.60, 7.55, 7.40, 7.30, 7.25, 7.35, 7.28, 7.20, 7.15, 7.30, 7.25, 7.10, 6.95, 6.88],
         'AGM "priced in"\nFake pop then dump\nBreak 7.25 on volume\nTarget: 6.88 → 5.00'),
        ('C: Extended Freeze (20%)', YELLOW,
         [7.52, 7.50, 7.53, 7.51, 7.50, 7.52, 7.49, 7.51, 7.50, 7.52, 7.51, 7.50, 7.52, 7.51, 7.50],
         'No catalyst reaction\nVol stays dead\nRange 7.45-7.72\nWait for H1 results'),
    ]

    for ax, (title, color, path, desc) in zip(axes, scenarios):
        ax.plot(days, path, color=color, linewidth=2.5, marker='o', markersize=4)
        ax.axhline(7.75, color=RED, linestyle='--', alpha=0.5, label='Entry 7.75')
        ax.axhline(7.25, color=YELLOW, linestyle=':', alpha=0.7, label='Stop 7.25')
        ax.axhline(8.14, color=GREEN, linestyle='--', alpha=0.5, label='Gate 8.14')
        ax.axhspan(7.45, 7.72, alpha=0.1, color=BLUE)
        ax.scatter([0], [price_now], s=120, c='white', zorder=5, edgecolors=color, linewidths=2)
        ax.set_title(title, fontsize=11, fontweight='bold', color=color)
        ax.set_xlabel('Trading Days from AGM', fontsize=9)
        ax.set_xlim(-0.5, 14.5)
        ax.set_ylim(6.5, 11.5)
        ax.grid(True, alpha=0.3)
        ax.text(0.02, 0.02, desc, transform=ax.transAxes, fontsize=7,
                verticalalignment='bottom', color=GRAY,
                bbox=dict(boxstyle='round', facecolor='#21262d', alpha=0.8))

    axes[0].set_ylabel('Price (EGP)', fontsize=11)
    axes[0].legend(loc='upper left', fontsize=7, facecolor='#21262d')
    save(fig, 'EAC-سيناريوهات-الميكr-2026-07-05.png')


# ── Chart 3: Order Book / Maker Defense ──────────────────────────────
def chart_orderbook():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [1.2, 1]})
    fig.patch.set_facecolor('#0d1117')
    fig.suptitle('EAC — Order Book: Maker Defense Map (Jul 5)', fontsize=14, fontweight='bold')

    # Depth chart
    bid_prices = [7.53, 7.52, 7.51, 7.50, 7.48, 7.45, 7.40]
    bid_vol = [1.0, 5.0, 10.0, 60.6, 50.3, 20.0, 31.1]
    ask_prices = [7.55, 7.57, 7.60, 7.62, 7.65, 7.69, 7.71]
    ask_vol = [0.4, 46.2, 8.0, 16.5, 10.0, 14.0, 14.0]

    cum_bid = np.cumsum(bid_vol[::-1])[::-1]
    cum_ask = np.cumsum(ask_vol)

    ax1.fill_betweenx(bid_prices, 0, cum_bid, alpha=0.6, color=GREEN, label='Bids (28%)')
    ax1.fill_betweenx(ask_prices, 0, cum_ask, alpha=0.6, color=RED, label='Offers (72%)')
    ax1.axhline(7.50, color=BLUE, linewidth=2, linestyle='-')
    ax1.annotate('WALL 60.6K\nMaker Defense', xy=(60, 7.50), xytext=(90, 7.42),
                 arrowprops=dict(arrowstyle='->', color=BLUE), color=BLUE, fontsize=9, fontweight='bold')
    ax1.annotate('CEILING 46.2K\n@ 7.57', xy=(46, 7.57), xytext=(80, 7.65),
                 arrowprops=dict(arrowstyle='->', color=RED), color=RED, fontsize=8)
    ax1.axhline(7.75, color=ORANGE, linestyle='--', alpha=0.7)
    ax1.text(5, 7.78, 'Your entry 7.75', color=ORANGE, fontsize=8)

    # Market sell simulation
    sell_qty = 128.4
    levels = [(7.53, 5), (7.52, 5), (7.51, 10), (7.50, 60.6), (7.48, 50.3)]
    remaining = sell_qty
    avg_prices = []
    for p, liq in levels:
        take = min(remaining, liq)
        if take > 0:
            avg_prices.extend([p] * int(take * 10))
            remaining -= take
    if remaining > 0:
        avg_prices.extend([7.45] * int(remaining * 10))
    sim_avg = np.mean(avg_prices) if avg_prices else 7.48
    ax1.axvline(sell_qty, color=PURPLE, linestyle=':', alpha=0.8)
    ax1.text(sell_qty + 2, 7.35, f'Market sell 128.4K\nAvg ~{sim_avg:.2f}', color=PURPLE, fontsize=8)

    ax1.set_xlabel('Cumulative Volume (K shares)', fontsize=10)
    ax1.set_ylabel('Price (EGP)', fontsize=10)
    ax1.set_title('Depth Chart + Your 128.4K Impact', fontsize=11)
    ax1.legend(loc='upper right', fontsize=8, facecolor='#21262d')
    ax1.set_xlim(0, 150)
    ax1.set_ylim(7.35, 7.85)
    ax1.grid(True, alpha=0.3)

    # Pie + stats
    ax2.pie([472.78, 1240], labels=['Bids 28%\n473K', 'Offers 72%\n1.24M'],
            colors=[GREEN, RED], autopct='%1.0f%%', startangle=90,
            textprops={'color': 'white', 'fontsize': 10})
    ax2.set_title('Bid/Offer Imbalance', fontsize=11)
    stats = (
        f"Spread: 0.02 (7.53-7.55)\n"
        f"Best Bid Wall: 60.6K @ 7.50\n"
        f"Best Ask Block: 46.2K @ 7.57\n"
        f"Your position: 128.4K\n"
        f"= 27% of ALL bids visible\n"
        f"Market sell avg: ~{sim_avg:.2f}\n"
        f"Loss vs 7.75: ~{(7.75-sim_avg)*128.4:.0f}K EGP"
    )
    fig.text(0.72, 0.08, stats, fontsize=9, color=GRAY,
             bbox=dict(boxstyle='round', facecolor='#21262d', alpha=0.9))
    save(fig, 'EAC-دفتر-الاوامر-الميكr-2026-07-05.png')


# ── Chart 4: Maker Fingerprints ──────────────────────────────────────
def chart_fingerprints():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#0d1117')

    # Price path Jun 20 - Jul 5 (approximate)
    dates = np.arange(0, 16)
    prices = [8.0, 7.8, 7.5, 7.6, 8.6, 8.2, 7.8, 7.5, 7.54, 7.54, 7.54, 7.50, 7.51, 7.52, 7.52, 7.52]
    vol = [2.5, 2.0, 1.8, 1.5, 3.0, 2.2, 1.5, 1.2, 0.8, 0.6, 0.5, 0.49, 0.49, 0.49, 0.49, 0.49]

    ax2 = ax.twinx()
    ax.plot(dates, prices, color=BLUE, linewidth=2, marker='o', markersize=5, label='Price', zorder=3)
    ax2.bar(dates, vol, alpha=0.4, color=GRAY, width=0.6, label='Volume (M)')

    # Annotate fingerprints
    markers = [
        (4, 8.6, 'STOP HUNT\nUpthrust @ 8.6\nSold into breakout', RED, 30),
        (7, 7.5, 'ABSORPTION\nBounce from 7.25', GREEN, -50),
        (8, 7.54, 'PIN\n3 days @ 7.54', YELLOW, 25),
        (11, 7.50, 'FREEZE\nVol → 493K\nO=H=L=C', BLUE, -45),
        (0, 8.0, 'Lower High\n10.17→8.6', ORANGE, 25),
    ]
    for x, y, txt, c, off in markers:
        ax.annotate(txt, (x, y), textcoords='offset points', xytext=(0, off),
                    ha='center', fontsize=8, color=c, fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.5),
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='#21262d', edgecolor=c, alpha=0.9))

    ax.axhspan(7.45, 7.72, alpha=0.08, color=BLUE, label='Maker Range')
    ax.axhline(7.25, color=YELLOW, linestyle=':', linewidth=1.5)
    ax.axhline(8.14, color=GREEN, linestyle='--', alpha=0.6)
    ax.axhline(7.75, color=RED, linestyle='--', alpha=0.6)

    ax.set_xlabel('Days (Jun 20 → Jul 5)', fontsize=10)
    ax.set_ylabel('Price (EGP)', fontsize=10, color=BLUE)
    ax2.set_ylabel('Volume (M)', fontsize=10, color=GRAY)
    ax.set_title('EAC — Maker Fingerprints: Stop Hunts · Absorption · Freeze', fontsize=13, fontweight='bold')
    ax.set_ylim(7.0, 9.0)
    ax.grid(True, alpha=0.3)
    date_labels = ['Jun20','21','22','23','24','25','26','27','28','29','30','Jul1','2','3','4','5']
    ax.set_xticks(dates)
    ax.set_xticklabels(date_labels, rotation=45, fontsize=7)
    save(fig, 'EAC-بصمات-الميكr-2026-07-05.png')


# ── Chart 5: Detection Playbook ──────────────────────────────────────
def chart_playbook():
    fig, ax = plt.subplots(figsize=(13, 9))
    fig.patch.set_facecolor('#0d1117')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('EAC — Maker Intent Detection Playbook', fontsize=14, fontweight='bold', pad=20)

    boxes = [
        (5, 9, 'CURRENT STATE\nPrice 7.52 · Vol dead · AGM tomorrow\nMaker HOLDING 7.50', BLUE, 8, 0.8),
        (2.5, 7, 'Break 8.14\n+ Vol +40%', GREEN, 3.5, 1.2),
        (5, 7, 'Break 8.0\n+ Vol weak', YELLOW, 3.5, 1.2),
        (7.5, 7, 'Close below 7.25\n+ Vol high', RED, 3.5, 1.2),
        (2.5, 4.5, 'REAL BREAKOUT\nMaker re-accum done\nHOLD + add small', GREEN, 3.5, 1.4),
        (5, 4.5, 'UPTHRUST TRAP\nFake breakout\nDO NOT chase', YELLOW, 3.5, 1.4),
        (7.5, 4.5, 'DISTRIBUTION\nExit 3 limit batches\nStop triggered', RED, 3.5, 1.4),
        (2.5, 2, 'Spring 7.25\nQuick rebound\nSTRONGEST buy signal', GREEN, 3.5, 1.2),
        (5, 2, 'Extended freeze\n7.45-7.72 range\nWAIT · no action', YELLOW, 3.5, 1.2),
    ]

    for x, y, text, color, w, h in boxes:
        box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle='round,pad=0.05',
                               facecolor='#21262d', edgecolor=color, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=8, color='white', fontweight='bold')

    arrows = [
        (5, 8.6, 2.5, 7.6, GREEN),
        (5, 8.6, 5, 7.6, YELLOW),
        (5, 8.6, 7.5, 7.6, RED),
        (2.5, 6.4, 2.5, 5.2, GREEN),
        (5, 6.4, 5, 5.2, YELLOW),
        (7.5, 6.4, 7.5, 5.2, RED),
        (2.5, 3.8, 2.5, 2.6, GREEN),
        (5, 3.8, 5, 2.6, YELLOW),
    ]
    for x1, y1, x2, y2, c in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=c, lw=2))

    ax.text(5, 0.5, 'Rule: NO volume = NO intent · Volume reveals true maker direction',
            ha='center', fontsize=10, color=ORANGE, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#21262d', edgecolor=ORANGE))
    save(fig, 'EAC-Playbook-كشف-نية-الميكr-2026-07-05.png')


# ── Chart 6: Price map with maker zones ────────────────────────────────
def chart_price_map():
    fig, ax = plt.subplots(figsize=(10, 12))
    fig.patch.set_facecolor('#0d1117')

    zones = [
        (10.17, 10.5, RED, 'DISTRIBUTION / Climax\nMaker SOLD here'),
        (8.50, 9.50, ORANGE, 'SUPPLY ZONE\nProfit-taking wall'),
        (8.11, 8.43, GREEN, 'GATE / Pivot\nBreak = Phase 2'),
        (7.72, 8.04, YELLOW, 'RESISTANCE\nAVWAP · Lower highs'),
        (7.45, 7.72, BLUE, 'MAKER RANGE\nCurrent battle · YOU ARE HERE'),
        (7.25, 7.45, PURPLE, 'SPRING ZONE\nStop hunt · Wyckoff'),
        (5.00, 7.25, GRAY, 'GAP / Weak support'),
        (4.50, 5.25, GREEN, 'ACCUMULATION BASE\n2025-2026'),
    ]

    for y1, y2, c, label in zones:
        ax.axhspan(y1, y2, alpha=0.35, color=c)
        ax.text(0.5, (y1+y2)/2, label, va='center', ha='left', fontsize=9,
                color='white', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='#0d1117', alpha=0.7))

    ax.axhline(7.75, color=RED, linewidth=2, linestyle='--')
    ax.scatter([0.85], [7.52], s=300, c='white', zorder=10, edgecolors=BLUE, linewidths=3)
    ax.annotate('NOW 7.52\n128,400 shares', xy=(0.85, 7.52), xytext=(0.92, 7.35),
                arrowprops=dict(arrowstyle='->', color='white'), color='white', fontsize=10, fontweight='bold')

    ax.set_xlim(0.4, 1.0)
    ax.set_ylim(4.0, 11.0)
    ax.set_ylabel('Price (EGP)', fontsize=11)
    ax.set_title('EAC — Maker Zone Map (What Each Level Means)', fontsize=13, fontweight='bold')
    ax.set_xticks([])
    ax.grid(True, axis='y', alpha=0.3)
    save(fig, 'EAC-خريطة-مناطق-الميكr-2026-07-05.png')


if __name__ == '__main__':
    chart_wyckoff_timeline()
    chart_scenarios()
    chart_orderbook()
    chart_fingerprints()
    chart_playbook()
    chart_price_map()
    print('Done — 6 charts generated.')

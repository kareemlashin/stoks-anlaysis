#!/usr/bin/env python3
"""Draw EAC classical chart patterns - annotated PNGs."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon, Arc, Rectangle
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
BG = '#0d1117'
PANEL = '#161b22'
GRID = '#21262d'
TXT = '#c9d1d9'
GREEN = '#3fb950'
RED = '#f85149'
YELLOW = '#d29922'
BLUE = '#58a6ff'
PURPLE = '#bc8cff'
ORANGE = '#f0883e'
GRAY = '#8b949e'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL,
    'axes.edgecolor': GRAY, 'text.color': TXT,
    'xtick.color': GRAY, 'ytick.color': GRAY, 'grid.color': GRID,
})


def save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'Saved: {p}')


def style_ax(ax, title, ylabel='Price (EGP)'):
    ax.set_title(title, fontsize=13, fontweight='bold', pad=12, color='white')
    ax.set_ylabel(ylabel, fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor(PANEL)


# ── Chart 1: Master pattern map on simplified price path ───────────────
def chart_master_map():
    fig, ax = plt.subplots(figsize=(16, 10))

    # Simplified daily path May-Jul (approximate)
    days = np.linspace(0, 60, 200)
    price = np.piecewise(days,
        [days < 25, (days >= 25) & (days < 32), (days >= 32) & (days < 38), days >= 38],
        [lambda d: 4.8 + 0.008*(d-0) + 0.002*np.sin(d*0.5),
         lambda d: 5.0 + (d-25)*0.85,
         lambda d: 10.17 - (d-32)*0.45,
         lambda d: 7.5 + 0.08*np.sin((d-38)*0.4)])

    ax.plot(days, price, color=BLUE, linewidth=2.5, label='EAC Price', zorder=3)
    ax.fill_between(days, price, 4, alpha=0.08, color=BLUE)

    # Ascending triangle zone
    tri_x = [5, 22, 25, 22, 5]
    tri_y = [4.82, 5.07, 5.20, 5.20, 4.82]
    ax.fill(tri_x, tri_y, alpha=0.15, color=GREEN)
    ax.plot([5, 25], [5.20, 5.20], '--', color=GREEN, lw=2)
    ax.plot([5, 25], [4.82, 5.07], '--', color=GREEN, lw=1.5)
    ax.annotate('Ascending Triangle\n(DONE ✓ Target 7.40)', xy=(15, 5.05), fontsize=9,
                color=GREEN, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=GREEN, alpha=0.9))

    # Bull flag
    flag_top = [32, 38, 55, 38]
    flag_bot = [32, 38, 55, 38]
    ax.plot([28, 32], [5.0, 10.17], color=ORANGE, lw=3, label='Pole')
    ax.plot([32, 55], [10.17, 8.04], '--', color=RED, lw=2)
    ax.plot([32, 55], [7.25, 7.50], '--', color=GREEN, lw=2)
    ax.fill([32, 55, 55, 32], [10.17, 8.04, 7.50, 7.25], alpha=0.12, color=YELLOW)
    ax.annotate('BULL FLAG\n(ACTIVE) Break > 8.14\nTarget ~13', xy=(44, 8.8), fontsize=9,
                color=YELLOW, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=YELLOW))

    # Rectangle
    ax.axhspan(7.25, 8.04, alpha=0.1, color=PURPLE)
    ax.axhline(7.25, color=RED, ls=':', lw=1.5)
    ax.axhline(8.04, color=RED, ls=':', lw=1.5)
    ax.text(52, 7.65, 'Rectangle\n7.25-8.04', color=PURPLE, fontsize=9, fontweight='bold')

    # Cup & Handle (weekly overlay)
    cup_t = np.linspace(10, 55, 100)
    cup_p = 8.0 - 6.1 * np.sin(np.pi * (cup_t - 10) / 45) ** 1.2
    cup_p = np.clip(cup_p, 1.9, 8.5)
    ax.plot(cup_t, cup_p + 0.5, '--', color=PURPLE, lw=1.5, alpha=0.6)
    ax.annotate('Cup & Handle\nTarget ~14', xy=(35, 3.5), fontsize=9,
                color=PURPLE, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=PURPLE))

    # Key levels
    levels = [(7.50, 'NOW 7.50', BLUE), (7.75, 'Entry 7.75', RED),
              (8.14, 'Gate 8.14', GREEN), (10.17, 'Peak 10.17', ORANGE),
              (7.25, 'Death 7.25', RED)]
    for y, lbl, c in levels:
        ax.axhline(y, color=c, alpha=0.5, lw=1)
        ax.text(57, y + 0.08, lbl, color=c, fontsize=8, fontweight='bold')

    ax.scatter([55], [7.50], s=200, c='white', zorder=10, edgecolors=BLUE, linewidths=2)
    ax.annotate('YOU\n128,400 @ 7.75', xy=(55, 7.50), xytext=(48, 6.8),
                arrowprops=dict(arrowstyle='->', color='white'), color='white',
                fontsize=10, fontweight='bold')

    ax.set_xlim(0, 60)
    ax.set_ylim(1.5, 11.5)
    ax.set_xlabel('Timeline (May → Jul 2026)', fontsize=10)
    style_ax(ax, 'EAC — All Classical Patterns Map (7.50 · AGM Tomorrow)')

    legend = [
        Line2D([0], [0], color=GREEN, lw=2, label='Completed patterns'),
        Line2D([0], [0], color=YELLOW, lw=2, label='Active patterns'),
        Line2D([0], [0], color=PURPLE, lw=2, ls='--', label='Long-term patterns'),
    ]
    ax.legend(handles=legend, loc='upper left', facecolor=PANEL, fontsize=8)
    save(fig, 'EAC-خريطة-كل-النماذj-الكلاسيكية-2026-07-05.png')


# ── Chart 2: Bull Flag detail ────────────────────────────────────────
def chart_bull_flag():
    fig, ax = plt.subplots(figsize=(12, 9))

    # Pole
    ax.plot([0, 1], [5.0, 10.17], color=ORANGE, lw=4)
    ax.text(0.3, 7.5, 'POLE\n+95%\n5.0→10.17', color=ORANGE, fontsize=11, fontweight='bold')

    # Flag channel
    x = np.array([1, 2, 3, 4, 5])
    top = [10.17, 8.60, 8.33, 8.04, 8.04]
    bot = [7.25, 7.34, 7.45, 7.50, 7.50]
    ax.plot(x, top, 'r--', lw=2, marker='o')
    ax.plot(x, bot, 'g--', lw=2, marker='o')
    ax.fill_between(x, top, bot, alpha=0.15, color=YELLOW)

    ax.scatter([5], [7.50], s=250, c='white', zorder=5, edgecolors=BLUE, lw=3)
    ax.annotate('NOW 7.50', xy=(5, 7.50), xytext=(4.2, 6.9), fontsize=11,
                fontweight='bold', color='white',
                arrowprops=dict(arrowstyle='->', color=BLUE))

    # Breakout arrow
    ax.annotate('', xy=(6.5, 12.5), xytext=(5.2, 8.14),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.text(5.8, 11, 'Breakout\n> 8.14 + Vol', color=GREEN, fontsize=10, fontweight='bold')

    # Target
    ax.axhline(13.0, color=GREEN, ls='--', alpha=0.7)
    ax.text(0.2, 13.2, 'Target ~13.0 (Measured Move)', color=GREEN, fontsize=9)

    # Fail line
    ax.axhline(7.25, color=RED, lw=2)
    ax.text(0.2, 7.0, 'FAIL < 7.25 → 5.0', color=RED, fontsize=10, fontweight='bold')

    ax.set_xlim(-0.2, 7)
    ax.set_ylim(4.5, 14)
    ax.set_xticks([])
    style_ax(ax, 'Bull Flag (علم الثور) — EAC Active Pattern', ylabel='')
    save(fig, 'EAC-نموذj-علم-الثور-2026-07-05.png')


# ── Chart 3: Cup & Handle ────────────────────────────────────────────
def chart_cup_handle():
    fig, ax = plt.subplots(figsize=(14, 8))

    x = np.linspace(0, 10, 200)
    # Cup shape
    cup = np.where(x < 7,
                   8.0 - 6.1 * np.sin(np.pi * x / 7) ** 1.1,
                   8.0 + (x - 7) * 0.3)
    cup = np.clip(cup, 1.9, 10.5)
    ax.plot(x, cup, color=PURPLE, lw=3)

    # Handle
    hx = np.linspace(7, 9.5, 50)
    handle = 8.5 - 0.8 * np.sin(np.pi * (hx - 7) / 2.5) + (hx - 7) * 0.05
    ax.plot(hx, handle, color=YELLOW, lw=3)

    ax.axhline(8.0, color=GRAY, ls='--', alpha=0.7)
    ax.text(0.3, 8.15, 'Neckline ~8.00', color=GRAY, fontsize=9)

    ax.fill_between(x[x <= 7], cup[x <= 7], 1.5, alpha=0.1, color=PURPLE)
    ax.fill_between(hx, handle, 7, alpha=0.15, color=YELLOW)

    ax.annotate('CUP\n2024-2025\nLow 1.90', xy=(3.5, 2.5), fontsize=10,
                color=PURPLE, fontweight='bold', ha='center')
    ax.annotate('HANDLE\n7.25-8.33\n← YOU @ 7.50', xy=(8.2, 7.8), fontsize=10,
                color=YELLOW, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=YELLOW))

    ax.annotate('', xy=(10, 14), xytext=(9, 8.5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.axhline(14.0, color=GREEN, ls='--')
    ax.text(6, 14.3, 'Target ~14.0 (Cup depth + Neckline)', color=GREEN, fontsize=10, fontweight='bold')

    ax.scatter([8.5], [7.50], s=200, c='white', edgecolors=BLUE, lw=2, zorder=5)

    ax.set_xlim(0, 10.5)
    ax.set_ylim(1, 15.5)
    ax.set_xticks([])
    style_ax(ax, 'Cup & Handle (كوب وعروة) — EAC Long-Term Pattern', ylabel='')
    save(fig, 'EAC-نموذj-كوب-وعروة-2026-07-05.png')


# ── Chart 4: 10 Patterns Status Grid ─────────────────────────────────
def chart_10_patterns():
    fig, axes = plt.subplots(2, 5, figsize=(18, 9))
    fig.suptitle('EAC × 10 Chart Patterns — Status @ 7.50', fontsize=14,
                 fontweight='bold', color='white', y=1.02)

    patterns = [
        ('1. Ascending\nTriangle', 'DONE ✓', GREEN, 'Target 7.40 hit'),
        ('2. Descending\nTriangle', 'NO ✗', GRAY, 'Lows rising'),
        ('3. Head &\nShoulders', 'NO ✗', GRAY, 'No shoulders'),
        ('4. Inv. H&S', 'NO ✗', GRAY, 'Wrong context'),
        ('5. Double\nBottom', 'DONE ✓', GREEN, 'Target 4.00 hit'),
        ('6. Double\nTop', 'MAYBE ⚠', YELLOW, 'If rejects @ 10'),
        ('7. Bull\nFlag', 'ACTIVE 🔄', YELLOW, 'Break > 8.14'),
        ('8. Bear\nFlag', 'NO ✗', GRAY, 'After uptrend'),
        ('9. Symmetrical\nTriangle', 'NO ✗', GRAY, 'Falling wedge instead'),
        ('10. Cup &\nHandle', 'ACTIVE 🔄', YELLOW, 'Target ~14'),
    ]

    for ax, (name, status, color, note) in zip(axes.flat, patterns):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Mini schematic
        if 'Ascending' in name:
            ax.plot([1, 9], [7, 7], 'g--')
            ax.plot([1, 9], [3, 6.5], 'g-')
            ax.fill([1, 9, 9, 1], [3, 6.5, 7, 7], alpha=0.2, color=GREEN)
        elif 'Bull' in name and 'Flag' in name:
            ax.plot([1, 3], [3, 9], color=ORANGE, lw=3)
            ax.plot([3, 9], [9, 7.5], 'r--')
            ax.plot([3, 9], [5, 6], 'g--')
            ax.scatter([9], [6.2], s=80, c='white', edgecolors=BLUE)
        elif 'Cup' in name:
            t = np.linspace(1, 9, 50)
            ax.plot(t, 5 - 3 * np.sin(np.pi * (t - 1) / 8) ** 1.2)
            ax.plot([7, 9], [5.5, 5.2], color=YELLOW, lw=2)
        elif 'Double' in name and 'Bottom' in name:
            ax.plot([1, 3, 5, 7, 9], [6, 3, 5, 3, 7], 'g-', lw=2)
        elif 'Double' in name:
            ax.plot([1, 3, 5, 7, 9], [4, 7, 5, 7, 3], 'r-', lw=2)
        elif 'Wedge' in name or 'Symmetrical' in name:
            ax.plot([1, 9], [8, 5], 'r--')
            ax.plot([1, 9], [3, 5.5], 'g--')
        else:
            ax.text(5, 5, '—', ha='center', va='center', fontsize=20, color=GRAY)

        box = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, boxstyle='round,pad=0.1',
                             facecolor=PANEL, edgecolor=color, linewidth=2.5)
        ax.add_patch(box)
        ax.text(5, 8.5, name, ha='center', fontsize=9, fontweight='bold', color='white')
        ax.text(5, 1.8, status, ha='center', fontsize=11, fontweight='bold', color=color)
        ax.text(5, 0.8, note, ha='center', fontsize=7, color=GRAY)

    save(fig, 'EAC-10-نماذj-حالة-2026-07-05.png')


# ── Chart 5: Falling Wedge + Rectangle ───────────────────────────────
def chart_wedge_rectangle():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('EAC — Falling Wedge + Rectangle (Active)', fontsize=14,
                 fontweight='bold', color='white')

    # Falling Wedge
    x = np.array([0, 1, 2, 3, 4, 5])
    tops = [10.17, 8.60, 8.33, 8.04, 7.72, 7.60]
    bots = [7.10, 7.25, 7.34, 7.45, 7.48, 7.50]
    ax1.plot(x, tops, 'r-o', lw=2, label='Falling highs')
    ax1.plot(x, bots, 'g-o', lw=2, label='Rising lows')
    ax1.fill_between(x, tops, bots, alpha=0.15, color=YELLOW)
    ax1.scatter([5], [7.50], s=200, c='white', edgecolors=BLUE, lw=2, zorder=5)
    ax1.annotate('NOW', xy=(5, 7.50), xytext=(3.5, 9), fontsize=10,
                 color='white', arrowprops=dict(arrowstyle='->', color=BLUE))
    ax1.annotate('', xy=(6, 10), xytext=(5.2, 8),
                 arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    ax1.text(5.5, 9.5, 'Breakout UP\n(Bullish Wedge)', color=GREEN, fontsize=9, fontweight='bold')
    ax1.set_xlim(-0.2, 6.5)
    ax1.set_ylim(6.5, 11)
    ax1.set_xticks([])
    style_ax(ax1, 'Falling Wedge (وتد هابط = Bullish)', ylabel='')
    ax1.legend(facecolor=PANEL, fontsize=8)

    # Rectangle
    ax2.axhspan(7.25, 8.04, alpha=0.2, color=PURPLE)
    ax2.axhline(8.04, color=RED, lw=2, label='Resistance 8.04')
    ax2.axhline(7.25, color=GREEN, lw=2, label='Support 7.25')
    ax2.axhline(7.50, color=BLUE, lw=2, ls='--', label='NOW 7.50')
    ax2.axhline(7.75, color=ORANGE, lw=1.5, ls=':', label='Entry 7.75')

    rx = np.linspace(0, 10, 50)
    ry = 7.625 + 0.2 * np.sin(rx * 1.5) + 0.05 * np.sin(rx * 3.7)
    ax2.plot(rx, ry, color=BLUE, lw=2)
    ax2.scatter([10], [7.50], s=200, c='white', edgecolors=BLUE, lw=2, zorder=5)

    ax2.text(5, 8.25, 'RESISTANCE 8.04', ha='center', color=RED, fontsize=9, fontweight='bold')
    ax2.text(5, 7.05, 'SUPPORT 7.25', ha='center', color=GREEN, fontsize=9, fontweight='bold')
    ax2.text(5, 7.55, '← YOU 7.50', ha='center', color=BLUE, fontsize=10, fontweight='bold')
    ax2.set_xlim(0, 10.5)
    ax2.set_ylim(7, 8.5)
    ax2.set_xticks([])
    style_ax(ax2, 'Rectangle / Range (مستطيل 7.25-8.04)', ylabel='')
    ax2.legend(facecolor=PANEL, fontsize=7, loc='upper right')

    save(fig, 'EAC-وتد-ومستطيل-2026-07-05.png')


# ── Chart 6: Candlestick patterns timeline ───────────────────────────
def chart_candles():
    fig, ax = plt.subplots(figsize=(14, 6))

    events = [
        (0, 'Jun 17', 'Marubozu\nBreakout', GREEN, 'Triangle break'),
        (1, 'Jun 19', 'Shooting Star\n@ 10.17', RED, 'Climax top'),
        (2, 'Jun 24', 'Hammer\n@ 7.10', GREEN, 'Spring bounce'),
        (3, 'Jun 25', 'Bull Engulfing', GREEN, 'Recovery'),
        (4, 'Jun 29', 'Hanging Man\n@ 8.33', RED, 'Rejection'),
        (5, 'Jul 1-5', 'Doji Cluster\n@ 7.50', YELLOW, 'Indecision'),
        (6, 'Jul 5 H', 'Shooting Star\n@ 7.72', RED, 'AVWAP reject'),
    ]

    for i, (x, date, name, color, desc) in enumerate(events):
        ax.add_patch(FancyBboxPatch((x - 0.35, 0.3), 0.7, 1.4, boxstyle='round,pad=0.05',
                                    facecolor=PANEL, edgecolor=color, linewidth=2))
        ax.text(x, 1.5, date, ha='center', fontsize=8, color=GRAY)
        ax.text(x, 1.0, name, ha='center', fontsize=8, fontweight='bold', color=color)
        ax.text(x, 0.5, desc, ha='center', fontsize=7, color=GRAY)
        if i < len(events) - 1:
            ax.annotate('', xy=(i + 0.65, 1.0), xytext=(i + 0.35, 1.0),
                        arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))

    ax.set_xlim(-0.8, 6.8)
    ax.set_ylim(0, 2.2)
    ax.axis('off')
    ax.set_title('EAC — Japanese Candlestick Patterns Timeline', fontsize=13,
                 fontweight='bold', color='white', pad=15)
    save(fig, 'EAC-شموع-يابانية-2026-07-05.png')


# ── Chart 7: Activation decision ─────────────────────────────────────
def chart_decision():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('EAC — Pattern Activation Map @ 7.50', fontsize=14,
                 fontweight='bold', color='white', pad=15)

    # Price ladder
    prices = [(10.17, 'Peak / Climax', RED), (8.60, 'Sell zone', ORANGE),
              (8.14, 'GATE — Breakout', GREEN), (7.75, 'Your entry', ORANGE),
              (7.50, 'NOW — Flag floor', BLUE), (7.25, 'DEATH — All fail', RED),
              (5.20, 'Triangle base', GREEN), (1.90, 'Cup bottom', PURPLE)]

    for i, (p, lbl, c) in enumerate(prices):
        y = 9 - i * 1.05
        ax.plot([1, 9], [y, y], color=c, alpha=0.4, lw=1)
        ax.text(0.3, y, f'{p}', color=c, fontsize=10, fontweight='bold', ha='right')
        ax.text(9.2, y, lbl, color=c, fontsize=9, va='center')

    ax.scatter([5], [9 - 4 * 1.05], s=300, c='white', edgecolors=BLUE, lw=3, zorder=5)
    ax.text(5, 9 - 4 * 1.05 - 0.35, 'YOU ARE HERE', ha='center', color='white',
             fontsize=11, fontweight='bold')

    # Arrows
    ax.annotate('', xy=(5, 9 - 2 * 1.05), xytext=(5, 9 - 4 * 1.05 + 0.2),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.text(5.5, 9 - 3 * 1.05, 'Break > 8.14\n→ Targets 13-14', color=GREEN, fontsize=9, fontweight='bold')

    ax.annotate('', xy=(5, 9 - 5 * 1.05), xytext=(5, 9 - 4 * 1.05 - 0.2),
                arrowprops=dict(arrowstyle='->', color=RED, lw=3))
    ax.text(5.5, 9 - 4.7 * 1.05, 'Break < 7.25\n→ Target 5.0', color=RED, fontsize=9, fontweight='bold')

    ax.text(5, 0.5, 'WAIT for confirmation — AGM tomorrow is the catalyst',
            ha='center', fontsize=11, color=YELLOW, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=YELLOW))
    save(fig, 'EAC-خريطة-تفعيل-النماذj-2026-07-05.png')


if __name__ == '__main__':
    chart_master_map()
    chart_bull_flag()
    chart_cup_handle()
    chart_10_patterns()
    chart_wedge_rectangle()
    chart_candles()
    chart_decision()
    print('Done — 7 pattern charts generated.')

#!/usr/bin/env python3
"""EAC v2 — All detailed charts (patterns + maker)."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
BG, PANEL, GRID = '#0a0e14', '#121820', '#1c2330'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL, 'axes.edgecolor': GRAY,
    'text.color': WHITE, 'xtick.color': GRAY, 'ytick.color': GRAY,
    'grid.color': GRID, 'font.size': 9,
})


def save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def box(ax, x, y, text, color, fs=8, w=0.02):
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, color=WHITE,
            fontweight='bold', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=PANEL, edgecolor=color, linewidth=1.5))


def hline(ax, y, label, color, ls='--', lw=1.2):
    ax.axhline(y, color=color, ls=ls, lw=lw, alpha=0.85)
    ax.text(1.02, y, label, transform=ax.get_yaxis_transform(), fontsize=7,
            color=color, va='center', fontweight='bold')


# ═══════════════════════════════════════════════════════════════════════
# 1. MASTER MAP
# ═══════════════════════════════════════════════════════════════════════
def chart01_master():
    fig, ax = plt.subplots(figsize=(18, 11))
    t = np.linspace(0, 70, 300)
    p = np.piecewise(t,
        [t < 20, (t >= 20) & (t < 28), (t >= 28) & (t < 35), (t >= 35) & (t < 42), t >= 42],
        [lambda x: 4.85 + 0.015*(x) + 0.01*np.sin(x*0.4),
         lambda x: 5.0 + (x-20)*0.65,
         lambda x: 10.17 - (x-28)*0.38,
         lambda x: 8.6 - (x-35)*0.18,
         lambda x: 7.5 + 0.06*np.sin((x-42)*0.35)])
    ax.plot(t, p, color=BLUE, lw=2.5, zorder=5)
    ax.fill_between(t, p, 1.5, alpha=0.06, color=BLUE)

    # Double bottom zone
    ax.add_patch(Rectangle((2, 2.7), 12, 0.8, fill=True, alpha=0.12, color=GREEN))
    box(ax, 8, 2.2, 'Double Bottom\n2.88/2.90 | Neck 3.45\nTarget 4.00 DONE', GREEN, 7)

    # Asc triangle
    ax.plot([15, 28, 28], [5.20, 5.20, 5.20], '--', color=GREEN, lw=2)
    ax.plot([15, 28], [4.82, 5.07], '--', color=GREEN, lw=1.5)
    ax.fill([15, 28, 28, 15], [4.82, 5.07, 5.20, 5.20], alpha=0.1, color=GREEN)
    box(ax, 22, 4.5, 'Ascending Triangle\nRes 5.20 | Lows rising\nBreak Jun 17 | Target 7.40 DONE', GREEN, 7)

    # Pole + flag
    ax.plot([28, 32], [5.0, 10.17], color=ORANGE, lw=4, zorder=4)
    ax.plot([32, 65, 65, 32], [10.17, 8.04, 7.50, 7.25], '--', color=YELLOW, lw=2)
    ax.plot([32, 65], [7.25, 7.50], '--', color=GREEN, lw=2)
    ax.fill([32, 65, 65, 32], [10.17, 8.04, 7.50, 7.25], alpha=0.08, color=YELLOW)
    box(ax, 50, 9.2, 'BULL FLAG (ACTIVE)\nPole 5.0->10.17 (+95%)\nFlag 7.25-8.04\nBreak > 8.14 | Target ~13.0', YELLOW, 8)

    # Rectangle
    ax.axhspan(7.25, 8.04, alpha=0.08, color=PURPLE)
    box(ax, 62, 7.65, 'Rectangle\n7.25 - 8.04\nBreak = direction', PURPLE, 7)

    # Cup overlay
    cup_x = np.linspace(5, 55, 120)
    cup_y = 8.2 - 6.3 * np.sin(np.pi * np.clip((cup_x - 5) / 50, 0, 1)) ** 1.15
    ax.plot(cup_x, np.clip(cup_y, 1.9, 8.5), '--', color=PURPLE, lw=1.5, alpha=0.7)
    box(ax, 35, 3.2, 'Cup & Handle (ACTIVE)\nCup low 1.90 | Neck ~8.0\nHandle 7.25-8.33\nTarget ~14.0 (months)', PURPLE, 7)

    levels = [
        (10.17, 'Peak 10.17 | Climax', RED, '-'),
        (8.60, 'Res 8.60 | Q sell zone', ORANGE, ':'),
        (8.14, 'GATE 8.14 | Pivot break', GREEN, '-'),
        (7.75, 'YOUR ENTRY 7.75', RED, '-'),
        (7.50, 'NOW 7.50 | POC/Fibo50', BLUE, '-'),
        (7.25, 'DEATH 7.25 | All patterns fail', RED, '-'),
        (5.20, 'Triangle base 5.20', GREEN, ':'),
    ]
    for y, lbl, c, ls in levels:
        hline(ax, y, f' {lbl}', c, ls)

    ax.scatter([65], [7.50], s=280, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    box(ax, 58, 6.85, 'YOU: 128,400 @ 7.75\nLoss: -32,100 EGP (-3.2%)\nAGM Tomorrow Jul 6', BLUE, 8)

    ax.set_xlim(0, 72)
    ax.set_ylim(1.2, 11.2)
    ax.set_xlabel('Timeline: Feb 2026 ──────────────── Jul 6 AGM', fontsize=10)
    ax.set_ylabel('Price (EGP)', fontsize=10)
    ax.set_title('EAC — Complete Classical Patterns Map v2\nAll patterns · Levels · Your position @ 7.50',
                 fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.25)
    leg = [Line2D([0], [0], color=GREEN, lw=2, label='Completed (Done)'),
           Line2D([0], [0], color=YELLOW, lw=2, label='Active (Now)'),
           Line2D([0], [0], color=PURPLE, lw=2, ls='--', label='Long-term')]
    ax.legend(handles=leg, loc='upper left', facecolor=PANEL, fontsize=8)
    save(fig, 'EAC-v2-01-خريطة-شاملة-كل-النماذj.png')


# ═══════════════════════════════════════════════════════════════════════
# 2. BULL FLAG — detailed measurements
# ═══════════════════════════════════════════════════════════════════════
def chart02_bull_flag():
    fig, ax = plt.subplots(figsize=(14, 10))
    # Pole
    ax.plot([0, 1.2], [5.0, 10.17], color=ORANGE, lw=5, solid_capstyle='round')
    ax.annotate('', xy=(1.2, 10.17), xytext=(0, 5.0),
                arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2))
    box(ax, 0.55, 7.2, 'POLE\nStart: 5.00\nEnd: 10.17\nHeight: +5.17 (+103%)\nDuration: 5 sessions', ORANGE, 9)

    x = np.array([1.2, 2, 3, 4, 5, 5.8])
    top = [10.17, 8.60, 8.33, 8.04, 7.72, 7.60]
    bot = [7.25, 7.34, 7.45, 7.48, 7.50, 7.50]
    ax.plot(x, top, 'r-o', lw=2, ms=8, label='Falling highs')
    ax.plot(x, bot, 'g-o', lw=2, ms=8, label='Rising lows')
    ax.fill_between(x, top, bot, alpha=0.12, color=YELLOW)

    for i, (tx, ty, by) in enumerate(zip(x, top, bot)):
        ax.text(tx, ty + 0.15, f'{ty:.2f}', ha='center', fontsize=7, color=RED)
        ax.text(tx, by - 0.25, f'{by:.2f}', ha='center', fontsize=7, color=GREEN)

    ax.scatter([5.8], [7.50], s=350, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    box(ax, 5.8, 6.85, 'NOW 7.50\nJul 5 close', BLUE, 9)

    # Measured move
    ax.annotate('', xy=(7.5, 13.07), xytext=(5.8, 8.14),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.axhline(8.14, color=GREEN, ls='--', lw=2)
    ax.axhline(13.07, color=GREEN, ls='--', lw=1.5)
    ax.axhline(7.25, color=RED, lw=2)
    ax.axhline(5.0, color=RED, ls=':', lw=1.5)

    box(ax, 6.8, 12.2, 'MEASURED MOVE\nBreakout: 8.14\n+ Pole height 5.17\n= Target 13.07 EGP\n(+74% from 7.50)', GREEN, 9)
    box(ax, 3.5, 8.5, 'FLAG ZONE\nUpper: 8.04-8.33\nLower: 7.25-7.50\nDuration: 18 days\nVol: declining (healthy)', YELLOW, 8)
    box(ax, 3.5, 6.5, 'FAIL SCENARIO\nClose < 7.25\nTarget: 5.20 (base)\nLoss on 128K: ~80K EGP', RED, 8)

    ax.set_xlim(-0.3, 8)
    ax.set_ylim(4.2, 14.5)
    ax.set_xticks([])
    ax.legend(facecolor=PANEL, fontsize=9, loc='upper right')
    ax.set_title('Bull Flag (علم الثور) — Full Measurements\nBrandt Classical | Minervini VCP | Active @ 7.50',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-v2-02-علم-الثور-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 3. CUP & HANDLE
# ═══════════════════════════════════════════════════════════════════════
def chart03_cup():
    fig, ax = plt.subplots(figsize=(15, 9))
    x = np.linspace(0, 12, 250)
    cup = np.where(x <= 8, 8.0 - 6.1 * np.sin(np.pi * x / 8) ** 1.08, 8.0)
    cup = np.clip(cup, 1.9, 10.5)
    ax.plot(x[x <= 8], cup[x <= 8], color=PURPLE, lw=3)
    hx = np.linspace(8, 11, 60)
    h = 8.3 - 0.9 * np.sin(np.pi * (hx - 8) / 2.8) + 0.04 * (hx - 8)
    ax.plot(hx, h, color=YELLOW, lw=3)

    ax.axhline(8.0, color=GRAY, ls='--', lw=1.5)
    ax.fill_between(x[x <= 8], cup[x <= 8], 1.5, alpha=0.08, color=PURPLE)
    ax.fill_between(hx, h, 7, alpha=0.1, color=YELLOW)

    box(ax, 4, 2.8, 'CUP LEFT\n2024 peak ~8.0\n2025 low 1.90\nDepth: 6.1 EGP\nDuration: 12+ months', PURPLE, 8)
    box(ax, 9.5, 7.6, 'HANDLE (YOU HERE)\nRange: 7.25-8.33\nCurrent: 7.50\n"Simple rest above neckline"\nO\'Neil / William O\'Neil style', YELLOW, 8)
    box(ax, 6, 8.35, 'NECKLINE ~8.00\n2024 historical resistance\nNow support (polarity flip)', GRAY, 7)

    ax.annotate('', xy=(12, 14.1), xytext=(10.5, 8.5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.axhline(14.1, color=GREEN, ls='--')
    box(ax, 10, 14.5, 'TARGET 14.10 EGP\nNeck 8.0 + Cup depth 6.1\nTimeline: MONTHS not days\nAfter free shares 1:4: ~11.28', GREEN, 9)

    ax.scatter([10], [7.50], s=300, c=WHITE, edgecolors=BLUE, lw=3, zorder=5)
    ax.set_xlim(0, 12.5)
    ax.set_ylim(1, 16)
    ax.set_xticks([])
    ax.set_title('Cup & Handle (كوب وعروة) — Full Anatomy\nLongest pattern | Target ~14 | Handle = current zone',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-v2-03-كوب-وعروة-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 4. 10 PATTERNS GRID
# ═══════════════════════════════════════════════════════════════════════
def chart04_ten_patterns():
    fig, axes = plt.subplots(2, 5, figsize=(20, 10))
    fig.suptitle('EAC x 10 Chart Patterns — Detailed Status @ 7.50 | Jul 5 2026',
                 fontsize=14, fontweight='bold', y=1.01)

    data = [
        ('1. Ascending Triangle', 'DONE', GREEN,
         'Res 5.20 x5 touches\nLows: 4.82->5.07\nBreak Jun 17 + vol\nTarget 7.40 HIT'),
        ('2. Descending Triangle', 'NO', GRAY,
         'Needs flat support\nEAC lows RISING\n= Not this pattern\n= Falling wedge instead'),
        ('3. Head & Shoulders', 'NO', GRAY,
         'Needs 3 peaks\n10.17/8.60/8.04\nNo symmetric shoulders\n= Lower highs only'),
        ('4. Inverse H&S', 'NO', GRAY,
         'Needs after long downtrend\nWe are in uptrend correction\nWrong context'),
        ('5. Double Bottom', 'DONE', GREEN,
         'Bottoms 2.88 & 2.90\nNeckline 3.45\nTarget 4.00 HIT\nFeb-Mar 2026'),
        ('6. Double Top', 'MAYBE', YELLOW,
         'Need 2 touches ~same peak\n10.17 vs 8.60 = 15% gap\nIF rejects 9.8-10.2\nNeckline = 7.25'),
        ('7. Bull Flag', 'ACTIVE', YELLOW,
         'Pole +95% | Flag 18d\nBreak > 8.14 + vol +40%\nTarget 13.07\nStop < 7.25'),
        ('8. Bear Flag', 'NO', GRAY,
         'Needs prior downtrend\nFlag after UP move\n= Bull flag not bear'),
        ('9. Symmetrical Triangle', 'NO', GRAY,
         'Needs equal slopes\nEAC = flat bottom\n+ falling top = Wedge'),
        ('10. Cup & Handle', 'ACTIVE', YELLOW,
         'Cup 1.90-8.0 | Handle now\nBreak > 8.14\nTarget 14.10\nMonths timeframe'),
    ]

    for ax, (title, status, color, details) in zip(axes.flat, data):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        # mini chart
        if 'Ascending' in title:
            ax.plot([1, 9], [7, 7], 'g-', lw=2)
            ax.plot([1, 9], [3, 6.5], 'g-', lw=2)
            ax.fill([1, 9, 9, 1], [3, 6.5, 7, 7], alpha=0.2, color=GREEN)
        elif 'Bull Flag' in title:
            ax.plot([1, 3], [2, 9], color=ORANGE, lw=3)
            ax.plot([3, 9], [9, 7], 'r--', lw=1.5)
            ax.plot([3, 9], [4, 5.5], 'g--', lw=1.5)
            ax.scatter([9], [5.5], s=60, c=WHITE, edgecolors=BLUE, lw=2)
        elif 'Cup' in title:
            t = np.linspace(1, 9, 40)
            ax.plot(t, 5 - 3.2 * np.sin(np.pi * (t - 1) / 8) ** 1.1)
            ax.plot([7, 9], [5.3, 5], color=YELLOW, lw=2)
        elif 'Double Bottom' in title:
            ax.plot([1, 3, 5, 7, 9], [6, 3, 5, 3, 7], 'g-', lw=2.5)
        elif 'Double Top' in title:
            ax.plot([1, 3, 5, 7, 9], [3, 7, 5, 6.8, 3], 'r-', lw=2)
        elif 'Wedge' in title or 'Symmetrical' in title:
            ax.plot([1, 9], [8, 5.5], 'r--')
            ax.plot([1, 9], [3, 5.8], 'g--')

        rect = FancyBboxPatch((0.15, 0.15), 9.7, 9.7, boxstyle='round,pad=0.08',
                              facecolor=PANEL, edgecolor=color, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(5, 9.2, title, ha='center', fontsize=9, fontweight='bold', color=WHITE)
        ax.text(5, 8.3, status, ha='center', fontsize=12, fontweight='bold', color=color)
        ax.text(5, 4.5, details, ha='center', fontsize=6.5, color=GRAY, linespacing=1.4)

    save(fig, 'EAC-v2-04-10-نماذj-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 5. WEDGE + RECTANGLE
# ═══════════════════════════════════════════════════════════════════════
def chart05_wedge_rect():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(17, 8))
    fig.suptitle('Falling Wedge + Rectangle — Active Patterns Detail', fontsize=14, fontweight='bold')

    x = np.arange(6)
    tops = [10.17, 8.60, 8.33, 8.04, 7.72, 7.60]
    bots = [7.10, 7.25, 7.34, 7.45, 7.48, 7.50]
    a1.plot(x, tops, 'r-o', lw=2, ms=10)
    a1.plot(x, bots, 'g-o', lw=2, ms=10)
    a1.fill_between(x, tops, bots, alpha=0.12, color=YELLOW)
    dates = ['Jun19', 'Jun25', 'Jun28', 'Jul1', 'Jul4', 'Jul5']
    a1.set_xticks(x)
    a1.set_xticklabels(dates, fontsize=7, rotation=30)
    for i in range(6):
        a1.annotate(f'{tops[i]:.2f}', (i, tops[i]), textcoords='offset points', xytext=(0, 8), fontsize=7, color=RED, ha='center')
        a1.annotate(f'{bots[i]:.2f}', (i, bots[i]), textcoords='offset points', xytext=(0, -12), fontsize=7, color=GREEN, ha='center')
    a1.scatter([5], [7.50], s=250, c=WHITE, edgecolors=BLUE, lw=3, zorder=5)
    box(a1, 2.5, 9.5, 'FALLING WEDGE = BULLISH\nAfter uptrend | Converging lines\nRising lows = sellers weakening\nBreak > 8.04-8.14', YELLOW, 8)
    a1.set_ylim(6.8, 11)
    a1.set_title('Falling Wedge (وتد هابط)', fontweight='bold')
    a1.grid(True, alpha=0.2)

    rx = np.linspace(0, 12, 80)
    ry = 7.62 + 0.15 * np.sin(rx * 1.2) + 0.08 * np.sin(rx * 2.8)
    a2.plot(rx, ry, color=BLUE, lw=2.5)
    a2.axhspan(7.25, 8.04, alpha=0.15, color=PURPLE)
    for y, lbl, c in [(8.04, 'RESISTANCE 8.04', RED), (7.75, 'ENTRY 7.75', ORANGE),
                      (7.50, 'NOW 7.50', BLUE), (7.25, 'SUPPORT 7.25', GREEN)]:
        a2.axhline(y, color=c, lw=1.5, ls='--' if y != 7.50 else '-')
        a2.text(12.3, y, lbl, fontsize=7, color=c, va='center', fontweight='bold')
    a2.scatter([12], [7.50], s=250, c=WHITE, edgecolors=BLUE, lw=3)
    box(a2, 6, 7.85, 'Brooks TTR 7.25-8.04\nAlways-In: NEUTRAL\nNo trade inside range\nBreak = direction', PURPLE, 8)
    a2.set_xlim(0, 13)
    a2.set_ylim(7, 8.5)
    a2.set_title('Rectangle / Trading Range (مستطيل)', fontweight='bold')
    a2.grid(True, alpha=0.2)
    save(fig, 'EAC-v2-05-وتد-ومستطيل-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 6. CANDLESTICKS
# ═══════════════════════════════════════════════════════════════════════
def chart06_candles():
    fig, ax = plt.subplots(figsize=(16, 7))
    events = [
        ('Jun 17', 'Marubozu\nBullish', GREEN, 'Triangle break\nVol spike\n5.2 -> 6.2', 'BUY signal'),
        ('Jun 19', 'Shooting Star\n@ 10.17', RED, 'Long upper wick 2.6 EGP\nClimax top\nO\'Neil distribution', 'SELL zone'),
        ('Jun 24', 'Hammer\n@ 7.10', GREEN, 'Long lower wick\nSpring / Wyckoff\nBounce +8%', 'HOLD stronger'),
        ('Jun 25', 'Bull Engulfing', GREEN, 'Absorbs prior red\nRecovery to 8.6\nVol confirms', 'BUY signal'),
        ('Jun 29', 'Hanging Man\n@ 8.33', RED, 'Rejection #2\nLower high formed\nUpthrust trap', 'NO chase'),
        ('Jul 1-5', 'Doji Cluster\n@ 7.50', YELLOW, '4-5 sessions\nO=H=L=C ~7.50\nAGM wait', 'WAIT'),
        ('Jul 5', 'Small Star\nH=7.72 C=7.50', RED, 'AVWAP reject\nBear close near low\nThen bounce to 7.50', 'HOLD'),
    ]
    for i, (date, name, color, detail, action) in enumerate(events):
        x = i * 2.2
        ax.add_patch(FancyBboxPatch((x - 0.85, 1), 1.7, 5.5, boxstyle='round,pad=0.06',
                                    facecolor=PANEL, edgecolor=color, linewidth=2))
        ax.text(x, 6.0, date, ha='center', fontsize=9, color=GRAY, fontweight='bold')
        ax.text(x, 5.2, name, ha='center', fontsize=9, color=color, fontweight='bold')
        ax.text(x, 3.8, detail, ha='center', fontsize=6.5, color=GRAY, linespacing=1.3)
        ax.text(x, 1.5, action, ha='center', fontsize=8, color=color, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=BG, edgecolor=color, alpha=0.8))
        if i < len(events) - 1:
            ax.annotate('', xy=(x + 1.35, 3.5), xytext=(x + 0.85, 3.5),
                        arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))
    ax.set_xlim(-1.5, 15)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Japanese Candlestick Patterns — EAC Timeline with Actions',
                 fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-v2-06-شموع-يابانية-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 7. ACTIVATION LADDER
# ═══════════════════════════════════════════════════════════════════════
def chart07_activation():
    fig, ax = plt.subplots(figsize=(13, 11))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    items = [
        (9.5, '10.17', 'Climax / Distribution / Double Top zone', RED, 'Sell strength if returns'),
        (8.8, '8.60-9.00', 'Qullamaggie partial sell 43K shares', ORANGE, 'After confirmed break'),
        (8.3, '8.14-8.43', 'GATE — All patterns activate UP', GREEN, 'Break + vol +40% = GO'),
        (7.9, '7.75', 'YOUR ENTRY — Breakeven line', ORANGE, '128,400 shares'),
        (7.5, '7.50', 'NOW — Flag floor / POC / Fibo 50%', BLUE, 'YOU ARE HERE'),
        (7.1, '7.25-7.45', 'Spring zone — Wyckoff test', PURPLE, 'Hold if quick rebound'),
        (6.7, '7.25', 'DEATH LINE — All patterns FAIL', RED, 'Exit 3 limit batches'),
        (6.0, '6.88', 'Final exit — All schools agree', RED, 'Full exit'),
        (4.5, '5.20', 'Triangle base — Major support', GREEN, 'Historical'),
        (2.5, '1.90', 'Cup bottom 2025', PURPLE, 'Cycle low'),
    ]
    for y, price, title, color, action in items:
        ax.plot([1.5, 8.5], [y, y], color=color, alpha=0.35, lw=1.5)
        ax.add_patch(FancyBboxPatch((0.2, y - 0.22), 1.2, 0.44, boxstyle='round', facecolor=PANEL, edgecolor=color, lw=1.5))
        ax.text(0.8, y, price, ha='center', va='center', fontsize=8, fontweight='bold', color=color)
        ax.text(5, y + 0.05, title, ha='center', va='center', fontsize=8, fontweight='bold', color=WHITE)
        ax.text(8.7, y, action, ha='left', va='center', fontsize=7, color=GRAY)

    ax.scatter([5], [7.5], s=400, c=WHITE, edgecolors=BLUE, lw=4, zorder=10)
    ax.annotate('', xy=(5, 8.3), xytext=(5, 7.65), arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax.annotate('', xy=(5, 6.7), xytext=(5, 7.35), arrowprops=dict(arrowstyle='->', color=RED, lw=3))

    box(ax, 5, 0.8, 'RULE: Wait for CLOSE above 8.14 or below 7.25 with VOLUME\nAGM Jul 6 = catalyst | Free shares 1:4 | Do NOT market sell 128K',
        YELLOW, 9)
    ax.set_title('Pattern Activation Ladder — Every Level Explained\n128,400 @ 7.75 | Current 7.50',
                 fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-v2-07-سلم-التفعيل-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 8. MAKER WYCKOFF
# ═══════════════════════════════════════════════════════════════════════
def chart08_maker():
    fig, ax = plt.subplots(figsize=(16, 8))
    phases = [
        ('A\nSilent Accum\n2025', 0, 3.2, GREEN, 'Vol dead\nBuy 3.0-3.5'),
        ('B\nMarkup 1\nMar-Apr', 1.2, 4.8, GREEN, 'Gradual\n3.3->5.0'),
        ('C\nRe-Accum\nMay-Jun', 2.4, 5.0, YELLOW, 'Flat 5.0\n1 month'),
        ('D\nExplosion\nJun 11-17', 3.6, 10.17, ORANGE, 'Parabolic\n48M vol'),
        ('E\nDistribution\nJun 17-18', 4.8, 9.2, RED, 'Sold @ 10.17\nClimax'),
        ('F\nFreeze\nJun 22-Jul5', 6, 7.50, BLUE, 'Vol 666K\nHold 7.50'),
        ('G\nAGM\nJul 6', 7.2, 8.0, PURPLE, 'Free 1:4\nCatalyst'),
    ]
    xs = [p[1] for p in phases]
    ys = [p[2] for p in phases]
    ax.plot(xs, ys, 'o-', color=GRAY, lw=2, ms=12, markerfacecolor=GRAY, markeredgecolor=WHITE, markeredgewidth=1.5)
    for name, x, y, c, note in phases:
        ax.scatter(x, y, s=350, c=c, zorder=5, edgecolors=WHITE, lw=2)
        ax.text(x, y + 0.55, name, ha='center', fontsize=8, fontweight='bold', color=c)
        ax.text(x, y - 0.65, note, ha='center', fontsize=7, color=GRAY)
    hline(ax, 7.75, ' Entry 7.75', RED)
    hline(ax, 7.50, ' NOW 7.50', BLUE)
    hline(ax, 7.25, ' Death 7.25', YELLOW, ':')
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(2, 11.5)
    ax.set_title('Maker Wyckoff Timeline — 7 Phases + AGM Tomorrow\nWhat the market maker did and might do next',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-v2-08-الميكr-Wyckoff-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 9. THREE SCENARIOS
# ═══════════════════════════════════════════════════════════════════════
def chart09_scenarios():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
    fig.suptitle('Maker Scenarios After AGM — 128,400 @ 7.75', fontsize=14, fontweight='bold', y=1.02)
    days = np.arange(0, 12)
    sc = [
        ('A: Re-Accumulation (45%)', GREEN,
         [7.5, 7.45, 7.55, 7.65, 7.8, 8.0, 8.2, 8.5, 9.0, 9.8, 10.5, 11.0],
         'AGM confirms free shares\nGap to 7.80\nBreak 8.14 day 5-7\nTarget 10.17 then 13\nACTION: HOLD + sell 43K @ 8.6'),
        ('B: Sell the News (35%)', RED,
         [7.5, 7.65, 7.55, 7.35, 7.25, 7.15, 7.30, 7.20, 7.05, 6.95, 6.88, 6.80],
         'Fake pop to 7.65\nBreak 7.25 day 4\nTarget 6.88 then 5.0\nACTION: Exit if close < 7.25\nLoss: ~80K on stop'),
        ('C: Extended Freeze (20%)', YELLOW,
         [7.5] * 12,
         'No AGM reaction\nRange 7.45-7.60\nVol stays dead\nACTION: HOLD patience\nStop still 7.25'),
    ]
    for ax, (title, color, path, desc) in zip(axes, sc):
        ax.plot(days, path, color=color, lw=3, marker='o', ms=5)
        ax.axhline(7.75, color=ORANGE, ls='--', alpha=0.6)
        ax.axhline(7.25, color=RED, ls=':', lw=2)
        ax.axhline(8.14, color=GREEN, ls='--', alpha=0.6)
        ax.axhspan(7.45, 7.72, alpha=0.06, color=BLUE)
        ax.scatter([0], [7.5], s=120, c=WHITE, edgecolors=color, lw=2, zorder=5)
        ax.set_title(title, fontsize=10, fontweight='bold', color=color)
        ax.text(0.02, 0.02, desc, transform=ax.transAxes, fontsize=6.5, color=GRAY, va='bottom',
                bbox=dict(boxstyle='round', facecolor=PANEL, alpha=0.9))
        ax.set_xlabel('Days after AGM', fontsize=9)
        ax.set_ylim(6.5, 11.5)
        ax.grid(True, alpha=0.2)
    axes[0].set_ylabel('Price (EGP)', fontsize=10)
    save(fig, 'EAC-v2-09-3-سيناريوهات-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 10. ORDER BOOK
# ═══════════════════════════════════════════════════════════════════════
def chart10_orderbook():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
    fig.suptitle('Order Book — Maker Defense + Your 128,400 Impact', fontsize=13, fontweight='bold')

    bid_p = [7.53, 7.52, 7.51, 7.50, 7.48, 7.45]
    bid_v = [1, 5, 10, 60.6, 50.3, 20]
    ask_p = [7.55, 7.57, 7.60, 7.62, 7.69, 7.71]
    ask_v = [0.4, 46.2, 8, 16.5, 14, 14]
    cum_b = np.cumsum(bid_v[::-1])[::-1]
    cum_a = np.cumsum(ask_v)

    ax1.fill_betweenx(bid_p, 0, cum_b, alpha=0.55, color=GREEN)
    ax1.fill_betweenx(ask_p, 0, cum_a, alpha=0.55, color=RED)
    ax1.axhline(7.50, color=BLUE, lw=2)
    ax1.axhline(7.75, color=ORANGE, ls='--')
    box(ax1, 55, 7.50, 'WALL 60.6K\nMaker pin', BLUE, 8)
    box(ax1, 50, 7.57, 'CEILING 46.2K', RED, 7)
    box(ax1, 100, 7.35, 'Market sell 128.4K\nAvg exec ~7.48-7.50\nLoss ~32K + miss 32K free shares', PURPLE, 7)
    ax1.set_xlabel('Cumulative Volume (K)', fontsize=10)
    ax1.set_ylabel('Price (EGP)', fontsize=10)
    ax1.set_title('Depth Chart', fontweight='bold')
    ax1.set_xlim(0, 140)
    ax1.set_ylim(7.3, 7.85)
    ax1.grid(True, alpha=0.2)

    ax2.pie([473, 1240], labels=['Bids 28%\n473K', 'Offers 72%\n1.24M'],
            colors=[GREEN, RED], autopct='%1.0f%%', startangle=90,
            textprops={'color': WHITE, 'fontsize': 10})
    stats = ('Spread: 0.02 (7.53-7.55)\nYour 128,400 = 27% of ALL bids\nBest bid wall: 60.6K @ 7.50\nBest ask block: 46.2K @ 7.57\nMarket sell avg: ~7.48\nPaper loss if sell: ~32K EGP\nFree shares forfeited: 32,100 (~241K)')
    fig.text(0.68, 0.08, stats, fontsize=8, color=GRAY,
             bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=GRAY))
    ax2.set_title('Bid/Offer Imbalance 72/28', fontweight='bold')
    save(fig, 'EAC-v2-10-دفتر-الاوامr-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 11. COMPLETED PATTERNS
# ═══════════════════════════════════════════════════════════════════════
def chart11_completed():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('Completed Patterns — Already Played Out (Proof of Maker Ability)', fontsize=13, fontweight='bold')

    # Double bottom
    x1 = [0, 1, 2, 3, 4, 5]
    y1 = [3.2, 2.88, 3.32, 2.90, 3.45, 4.0]
    a1.plot(x1, y1, 'g-o', lw=2.5, ms=8)
    a1.axhline(3.45, color=GRAY, ls='--', label='Neckline 3.45')
    a1.axhline(4.0, color=GREEN, ls='--', label='Target 4.00 HIT')
    a1.annotate('B1: 2.88', (1, 2.88), fontsize=8, color=GREEN)
    a1.annotate('B2: 2.90', (3, 2.90), fontsize=8, color=GREEN)
    box(a1, 4, 3.6, 'Double Bottom\nFeb-Mar 2026\nTarget 4.00 ACHIEVED', GREEN, 8)
    a1.set_title('Double Bottom (قاع مزدوج)', fontweight='bold')
    a1.legend(facecolor=PANEL, fontsize=8)
    a1.grid(True, alpha=0.2)
    a1.set_ylim(2.5, 4.3)

    # Asc triangle
    a2.plot([0, 4, 4], [5.20, 5.20, 5.20], 'g--', lw=2)
    a2.plot([0, 4], [4.82, 5.07], 'g-', lw=2)
    a2.fill([0, 4, 4, 0], [4.82, 5.07, 5.20, 5.20], alpha=0.15, color=GREEN)
    a2.annotate('', xy=(5, 7.4), xytext=(4.2, 5.25), arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
    a2.axhline(7.40, color=GREEN, ls='--')
    box(a2, 2, 4.9, 'Ascending Triangle\nMay-Jun 2026\nRes 5.20 x5\nTarget 7.40 HIT', GREEN, 8)
    box(a2, 4.5, 6.5, 'Break Jun 17\nThen parabolic\nto 10.17', ORANGE, 8)
    a2.set_title('Ascending Triangle (مثلث صاعد)', fontweight='bold')
    a2.set_ylim(4.5, 8)
    a2.grid(True, alpha=0.2)
    save(fig, 'EAC-v2-11-نماذj-مكتملة-تفاصيل.png')


# ═══════════════════════════════════════════════════════════════════════
# 12. DECISION FLOWCHART
# ═══════════════════════════════════════════════════════════════════════
def chart12_flowchart():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    nodes = [
        (5, 9.2, 'NOW: 7.50 | 128,400 @ 7.75 | AGM Tomorrow', BLUE, 9, 7.5),
        (2.5, 7.2, 'Close > 8.14\n+ Vol +40%', GREEN, 8, 3.2),
        (5, 7.2, 'Range 7.25-8.04\nNo break', YELLOW, 8, 3.2),
        (7.5, 7.2, 'Close < 7.25\n+ Vol high', RED, 8, 3.2),
        (2.5, 4.8, 'HOLD + add small\nSell 43K @ 8.6-9.0\nTargets 13-14', GREEN, 8, 3.5),
        (5, 4.8, 'HOLD patience\nStop 7.25\nWait catalyst', YELLOW, 8, 3.5),
        (7.5, 4.8, 'EXIT limit\n3 batches\nLoss ~80K', RED, 8, 3.5),
        (2.5, 2.2, 'Spring 7.45\nrebound <=3 days\n= Strongest hold', GREEN, 7, 3.2),
    ]
    for x, y, txt, c, fs, w in nodes:
        ax.add_patch(FancyBboxPatch((x - w/2, y - 0.55), w, 1.1, boxstyle='round,pad=0.06',
                                    facecolor=PANEL, edgecolor=c, linewidth=2))
        ax.text(x, y, txt, ha='center', va='center', fontsize=fs, color=WHITE, fontweight='bold')

    arrows = [(5, 8.65, 2.5, 7.75, GREEN), (5, 8.65, 5, 7.75, YELLOW),
              (5, 8.65, 7.5, 7.75, RED), (2.5, 6.85, 2.5, 5.35, GREEN),
              (5, 6.85, 5, 5.35, YELLOW), (7.5, 6.85, 7.5, 5.35, RED),
              (5, 6.85, 2.5, 2.75, GREEN)]
    for x1, y1, x2, y2, c in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', color=c, lw=2))

    box(ax, 5, 0.6, 'NEVER: Market sell 128K on microcap | NEVER: Sell before AGM (forfeit 32,100 free shares)',
        RED, 9)
    ax.set_title('Decision Flowchart — What To Do Based on Pattern Break\nAll 15 professionals + 10 patterns converge here',
                 fontsize=12, fontweight='bold', pad=15)
    save(fig, 'EAC-v2-12-مخطط-القرار-تفاصيل.png')


if __name__ == '__main__':
    print('Generating 12 detailed charts v2...')
    chart01_master()
    chart02_bull_flag()
    chart03_cup()
    chart04_ten_patterns()
    chart05_wedge_rect()
    chart06_candles()
    chart07_activation()
    chart08_maker()
    chart09_scenarios()
    chart10_orderbook()
    chart11_completed()
    chart12_flowchart()
    print('Done — 12 charts v2.')

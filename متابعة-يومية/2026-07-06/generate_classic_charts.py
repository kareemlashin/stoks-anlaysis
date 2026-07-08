#!/usr/bin/env python3
"""EAC @ 7.38 — كل الرسوم الكلاسيكية · 6 Jul 2026"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
NOW = 7.38
ENTRY = 7.75
SHARES = 128_400
PNL = int((NOW - ENTRY) * SHARES)
BG, PANEL, GRID = '#0a0e14', '#121820', '#1c2330'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE, CYAN = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9', '#06b6d4'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL, 'axes.edgecolor': GRAY,
    'text.color': WHITE, 'xtick.color': GRAY, 'ytick.color': GRAY,
    'grid.color': GRID, 'font.size': 9,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def box(ax, x, y, text, color, fs=8, ha='center'):
    ax.text(x, y, text, ha=ha, va='center', fontsize=fs, color=WHITE, fontweight='bold', zorder=20,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=PANEL, edgecolor=color, linewidth=1.5))


def hline(ax, y, label, color, ls='--', lw=1.5):
    ax.axhline(y, color=color, ls=ls, lw=lw, alpha=0.9)
    ax.text(1.02, y, f' {label}', transform=ax.get_yaxis_transform(), fontsize=7,
            color=color, va='center', fontweight='bold')


def mark_now(ax, x, y=NOW):
    ax.scatter([x], [y], s=280, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    box(ax, x, y - 0.35, f'NOW {NOW}\n128,400 @ {ENTRY}\nPnL {PNL:,} EGP', BLUE, 8)


# ── 01 Master Map ────────────────────────────────────────────────────
def chart01_master():
    fig, ax = plt.subplots(figsize=(18, 11))
    t = np.linspace(0, 70, 300)
    p = np.piecewise(t,
        [t < 20, (t >= 20) & (t < 28), (t >= 28) & (t < 42), t >= 42],
        [lambda x: 4.85 + 0.015 * x,
         lambda x: 5.0 + (x - 20) * 0.65,
         lambda x: 10.17 - (x - 28) * 0.22,
         lambda x: 7.38 + 0.05 * np.sin((x - 42) * 0.4)])
    ax.plot(t, p, color=BLUE, lw=2.5, zorder=5)
    ax.fill_between(t, p, 1.5, alpha=0.06, color=BLUE)

    ax.add_patch(Rectangle((2, 2.7), 12, 0.8, fill=True, alpha=0.12, color=GREEN))
    box(ax, 8, 2.2, 'Double Bottom\n2.88/2.90 | Neck 3.45\nTarget 4.00 DONE', GREEN, 7)

    ax.plot([15, 28, 28], [5.20, 5.20, 5.20], '--', color=GREEN, lw=2)
    ax.plot([15, 28], [4.82, 5.07], '--', color=GREEN, lw=1.5)
    box(ax, 22, 4.5, 'Ascending Triangle\nBreak Jun 17 | Target 7.40 DONE', GREEN, 7)

    ax.plot([28, 32], [5.0, 10.17], color=ORANGE, lw=4)
    ax.plot([32, 68, 68, 32], [10.17, 8.04, 7.36, 7.25], '--', color=YELLOW, lw=2)
    ax.plot([32, 68], [7.25, 7.50], '--', color=GREEN, lw=2)
    ax.fill([32, 68, 68, 32], [10.17, 8.04, 7.50, 7.25], alpha=0.08, color=YELLOW)
    box(ax, 52, 9.0, 'BULL FLAG (ACTIVE)\nPole 5->10.25\nFlag 7.25-8.50\nBreak > 8.14', YELLOW, 8)

    ax.axhspan(7.25, 8.50, alpha=0.08, color=PURPLE)
    box(ax, 62, 8.0, 'Rectangle\n7.25-8.50\nUp 9.70 | Down 6.10', PURPLE, 7)

    for y, lbl, c, ls in [
        (10.25, 'Peak 10.25 | Blow-off', RED, '-'),
        (8.14, 'GATE 8.14', GREEN, '-'),
        (7.75, 'YOUR ENTRY 7.75', ORANGE, '-'),
        (7.53, 'H today 7.53', GRAY, ':'),
        (NOW, f'NOW {NOW} | POC', BLUE, '-'),
        (7.36, 'L today 7.36', GRAY, ':'),
        (7.25, 'DEATH 7.25 | EXIT', RED, '-'),
        (7.24, 'STOP 7.24 Limit', RED, ':'),
    ]:
        hline(ax, y, lbl, c, ls)

    mark_now(ax, 66)
    ax.set_xlim(0, 72)
    ax.set_ylim(1.2, 11.2)
    ax.set_xlabel('Timeline: Feb 2026 ──────────────── Jul 6 2026')
    ax.set_ylabel('Price (EGP)')
    ax.set_title('EAC — خريطة كلاسيكية شاملة\nكل النماذj · المستويات · مركزك @ 7.38', fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.25)
    ax.legend(handles=[
        Line2D([0], [0], color=GREEN, lw=2, label='Done'),
        Line2D([0], [0], color=YELLOW, lw=2, label='Active'),
    ], loc='upper left', facecolor=PANEL, fontsize=8)
    save(fig, 'EAC-738-01-خريطة-كلاسيكي-شاملة-2026-07-06.png')


# ── 02 Bull Flag ─────────────────────────────────────────────────────
def chart02_bull_flag():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.plot([0, 1.2], [5.0, 10.25], color=ORANGE, lw=5)
    box(ax, 0.55, 7.5, 'POLE\n5.00 -> 10.25\n+5.25 (+105%)\n5 sessions', ORANGE, 9)

    x = np.array([1.2, 2, 3, 4, 5, 6, 6.5])
    top = [10.25, 8.60, 8.33, 8.04, 7.72, 7.53, 7.45]
    bot = [7.25, 7.34, 7.35, 7.36, 7.36, 7.36, 7.36]
    ax.plot(x, top, 'r-o', lw=2, ms=8, label='Lower highs')
    ax.plot(x, bot, 'g-o', lw=2, ms=8, label='Lows / Spring zone')
    ax.fill_between(x, top, bot, alpha=0.12, color=YELLOW)
    mark_now(ax, 6.5)

    ax.annotate('', xy=(8, 13.39), xytext=(6.5, 8.14),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    for y, lbl in [(8.14, 'Break 8.14'), (13.39, 'Target 13.39 (+pole)'), (7.25, 'FAIL 7.25'), (7.24, 'STOP 7.24')]:
        ax.axhline(y, color=GREEN if y > 8 else RED, ls='--' if y != 7.25 else '-', lw=2 if y in (7.25, 8.14) else 1.5)
        ax.text(8.2, y, lbl, fontsize=8, color=GREEN if y > 8 else RED, va='center')

    box(ax, 4, 8.8, 'FLAG\nUpper: 7.53-8.50\nLower: 7.25-7.36\nVol declining = healthy flag', YELLOW, 8)
    box(ax, 4, 6.2, 'FAIL\nClose < 7.25\nTarget 5.00 base', RED, 8)
    ax.set_xlim(-0.3, 8.5)
    ax.set_ylim(4.5, 14.5)
    ax.legend(facecolor=PANEL, fontsize=9)
    ax.set_title('Bull Flag (علم الثور) — قياسات كاملة @ 7.38', fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-738-02-علم-الثور-2026-07-06.png')


# ── 03 Fibonacci ─────────────────────────────────────────────────────
def chart03_fib():
    fig, ax = plt.subplots(figsize=(14, 9))
    low, high = 5.00, 10.25
    levels = [
        (0.0, high, '0% 10.25', RED),
        (0.236, high - 0.236 * (high - low), '23.6% 8.76', GRAY),
        (0.382, high - 0.382 * (high - low), '38.2% 8.24', ORANGE),
        (0.5, high - 0.5 * (high - low), '50% 7.63', YELLOW),
        (0.618, high - 0.618 * (high - low), '61.8% 7.01', GREEN),
        (0.786, high - 0.786 * (high - low), '78.6% 6.12', GRAY),
        (1.0, low, '100% 5.00', GREEN),
    ]
    ax.plot([0, 10], [high, low], color=BLUE, lw=3)
    ax.annotate('', xy=(10, low), xytext=(0, high), arrowprops=dict(arrowstyle='<->', color=BLUE, lw=2))
    box(ax, 5, 10.6, f'Fib Retrace: {low} -> {high}\nCorrection from pole', BLUE, 9)

    for pct, price, lbl, c in levels:
        ax.axhline(price, color=c, ls='--', lw=1.2, alpha=0.85)
        ax.text(10.3, price, f'{lbl} ({price:.2f})', fontsize=8, color=c, va='center', fontweight='bold')

    ax.axhspan(7.36, 7.45, alpha=0.2, color=BLUE)
    mark_now(ax, 5)
    box(ax, 5, 7.0, f'NOW {NOW}\nBetween 50%-61.8%\nHealthy correction zone', BLUE, 9)
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(5.5, 11)
    ax.set_ylabel('Price (EGP)')
    ax.set_title('Fibonacci Retracement — Pole 5.00 -> 10.25 @ 7.38', fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-738-03-فibo-2026-07-06.png')


# ── 04 Dow Theory ────────────────────────────────────────────────────
def chart04_dow():
    fig, axes = plt.subplots(3, 1, figsize=(14, 12), sharex=False)
    fig.suptitle('Dow Theory — 3 Trends @ EAC 7.38', fontsize=14, fontweight='bold', y=0.98)

    specs = [
        ('Primary (Monthly/Weekly)', 1.80, 10.25, GREEN, 'Uptrend intact\n1.80 -> 10.25\nHigher highs + lows'),
        ('Secondary (Weekly correction)', 10.25, 7.36, RED, 'Pullback -27%\nValid while > 7.25\nDeath = pattern fail'),
        ('Minor (Daily/Intraday)', 7.53, 7.36, YELLOW, f'Sideways 7.36-7.53\nNOW {NOW} @ POC\nSqueeze / range'),
    ]
    for ax, (title, start, end, color, note) in zip(axes, specs):
        x = np.linspace(0, 10, 50)
        if 'Minor' in title:
            y = 7.45 + 0.08 * np.sin(x * 2) - 0.01 * x
        elif 'Secondary' in title:
            y = start - (start - end) * (x / 10) ** 0.7 + 0.05 * np.sin(x)
        else:
            y = start + (end - start) * (x / 10) ** 1.2
        ax.plot(x, y, color=color, lw=3)
        ax.axhline(7.25, color=RED, ls='--', lw=1.5)
        ax.text(10.2, 7.25, 'Death 7.25', fontsize=7, color=RED, va='center')
        mark_now(ax, 9) if 'Minor' in title else None
        box(ax, 5, ax.get_ylim()[1] * 0.15 + y.max() * 0.85 if 'Minor' not in title else 7.55, note, color, 8)
        ax.set_title(title, fontweight='bold', color=color)
        ax.grid(True, alpha=0.2)
        ax.set_ylabel('EGP')
    save(fig, 'EAC-738-04-داو-2026-07-06.png')


# ── 05 S/R Map ───────────────────────────────────────────────────────
def chart05_sr():
    fig, ax = plt.subplots(figsize=(12, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(5.5, 11.5)
    ax.axis('off')

    levels = [
        (10.25, 'R4 ATH / Blow-off / Climax sell', RED),
        (8.90, 'R3 Extension target', ORANGE),
        (8.14, 'R2 GATE — Minervini pivot', GREEN),
        (7.72, 'R1 AVWAP / T1 breakeven', CYAN),
        (7.50, 'POC / Fib 50%', YELLOW),
        (7.43, 'Order book wall 36K', ORANGE),
        (NOW, f'NOW {NOW} — VWAP/POC cluster', BLUE),
        (7.36, 'L today / support cluster', GREEN),
        (7.35, 'L weekly', GREEN),
        (7.25, 'DEATH — EXIT trigger', RED),
        (7.24, 'STOP Limit (128,400)', RED),
        (6.88, 'Bear target / full exit zone', RED),
        (5.00, 'Base / pole start', GRAY),
    ]
    for i, (price, lbl, c) in enumerate(levels):
        y = 10.8 - i * 0.42
        ax.plot([1, 9], [price, price], color=c, lw=3 if price in (NOW, 7.25, 8.14) else 1.5,
                ls='-' if price in (NOW, 7.25) else '--')
        ax.scatter([5], [price], s=120 if price == NOW else 60, c=c, zorder=5)
        ax.text(0.5, price, f'{price:.2f}', fontsize=9, color=c, va='center', fontweight='bold', ha='right')
        ax.text(9.2, price, lbl, fontsize=8, color=c, va='center', ha='left')

    box(ax, 5, 5.8, f'128,400 @ {ENTRY}\nPnL: {PNL:,} EGP ({(NOW-ENTRY)/ENTRY*100:.1f}%)\nAction: HOLD حرج', BLUE, 10)
    ax.set_title('Support & Resistance Map — كل المستويات @ 7.38', fontsize=14, fontweight='bold', pad=15)
    save(fig, 'EAC-738-05-دعم-مقاومة-2026-07-06.png')


# ── 06 10 Patterns Grid ──────────────────────────────────────────────
def chart06_patterns():
    fig, axes = plt.subplots(2, 5, figsize=(20, 10))
    fig.suptitle('10 Chart Patterns — EAC @ 7.38 · 6 Jul 2026', fontsize=14, fontweight='bold', y=1.01)
    data = [
        ('1. Asc Triangle', 'DONE', GREEN, 'Break Jun 17\nTarget 7.40 HIT'),
        ('2. Desc Triangle', '1H ONLY', YELLOW, 'Lower highs 8.5->7.53\nFlat 7.36\nBearish short-term'),
        ('3. Head & Shoulders', 'NO', GRAY, 'No symmetric shoulders\nLower highs only'),
        ('4. Inv H&S', 'NO', GRAY, 'Wrong context\nUptrend correction'),
        ('5. Double Bottom', 'PARTIAL', YELLOW, '7.35 + 7.36 lows\nNeck 8.50 pending\nTarget 9.65'),
        ('6. Double Top', 'MAYBE', YELLOW, '10.25 vs 8.60\nIF reject 9.8\nNeck 7.25'),
        ('7. Bull Flag', 'ACTIVE', YELLOW, 'Break > 8.14\nTarget 13.39\nFail < 7.25'),
        ('8. Bear Flag', 'NO', GRAY, 'After uptrend\n= Bull flag'),
        ('9. Rectangle', 'ACTIVE', PURPLE, '7.25-8.50\nNOW inside\nUp 9.70 Down 6.10'),
        ('10. Falling Wedge', 'ACTIVE', GREEN, 'Rising lows\nBreak > 8.04\nBullish bias'),
    ]
    for ax, (title, status, color, details) in zip(axes.flat, data):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        if 'Bull Flag' in title:
            ax.plot([1, 3], [2, 9], color=ORANGE, lw=3)
            ax.plot([3, 9], [9, 6.5], 'r--', lw=1.5)
            ax.plot([3, 9], [4, 4.5], 'g--', lw=1.5)
            ax.scatter([9], [4.5], s=60, c=WHITE, edgecolors=BLUE, lw=2)
        elif 'Rectangle' in title:
            ax.axhspan(4, 7, alpha=0.2, color=PURPLE)
            ax.plot(np.linspace(1, 9, 30), 5.5 + 0.3 * np.sin(np.linspace(0, 6, 30)), color=BLUE, lw=2)
        elif 'Double Bottom' in title:
            ax.plot([1, 3, 5, 7, 9], [6, 3.5, 5, 3.5, 7], 'g-', lw=2.5)
        elif 'Desc' in title:
            ax.plot([1, 9], [8, 5], 'r--', lw=2)
            ax.plot([1, 9], [3.5, 3.5], 'g-', lw=2)
        rect = FancyBboxPatch((0.15, 0.15), 9.7, 9.7, boxstyle='round,pad=0.08',
                              facecolor=PANEL, edgecolor=color, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(5, 9.2, title, ha='center', fontsize=9, fontweight='bold', color=WHITE)
        ax.text(5, 8.3, status, ha='center', fontsize=12, fontweight='bold', color=color)
        ax.text(5, 4.5, details, ha='center', fontsize=6.5, color=GRAY, linespacing=1.4)
    save(fig, 'EAC-738-06-10-نماذj-2026-07-06.png')


# ── 07 Rectangle + Wedge ─────────────────────────────────────────────
def chart07_rect_wedge():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(17, 8))
    fig.suptitle('Rectangle + Falling Wedge @ 7.38', fontsize=14, fontweight='bold')

    x = np.arange(7)
    tops = [10.25, 8.60, 8.15, 8.00, 7.53, 7.45, 7.43]
    bots = [7.25, 7.35, 7.35, 7.36, 7.36, 7.36, 7.36]
    a1.plot(x, tops, 'r-o', lw=2, ms=10)
    a1.plot(x, bots, 'g-o', lw=2, ms=10)
    a1.fill_between(x, tops, bots, alpha=0.12, color=YELLOW)
    a1.set_xticks(x)
    a1.set_xticklabels(['Jun19', 'Jun25', 'Jun28', 'Jul1', 'Jul4', 'Jul5', 'Jul6'], fontsize=7, rotation=30)
    mark_now(a1, 6)
    box(a1, 3, 9.5, 'FALLING WEDGE\nConverging lines\nRising lows = bullish\nBreak > 8.04', YELLOW, 8)
    a1.set_ylim(6.8, 11)
    a1.set_title('Falling Wedge (وتد هابط)', fontweight='bold')
    a1.grid(True, alpha=0.2)

    rx = np.linspace(0, 12, 80)
    ry = 7.55 + 0.12 * np.sin(rx * 1.2)
    a2.plot(rx, ry, color=BLUE, lw=2.5)
    a2.axhspan(7.25, 8.50, alpha=0.15, color=PURPLE)
    for y, lbl, c in [(8.50, 'RES 8.50', RED), (8.14, 'GATE 8.14', GREEN), (7.75, 'ENTRY 7.75', ORANGE),
                      (NOW, f'NOW {NOW}', BLUE), (7.36, 'L 7.36', GRAY), (7.25, 'SUPPORT 7.25', GREEN)]:
        a2.axhline(y, color=c, lw=1.5, ls='--' if y not in (NOW, 7.25) else '-')
        a2.text(12.3, y, lbl, fontsize=7, color=c, va='center', fontweight='bold')
    mark_now(a2, 12)
    box(a2, 6, 8.2, 'Brooks TTR 7.25-8.50\nAlways-In: NEUTRAL\nBreak = direction', PURPLE, 8)
    a2.set_xlim(0, 13)
    a2.set_ylim(7, 9)
    a2.set_title('Rectangle (مستطيل)', fontweight='bold')
    a2.grid(True, alpha=0.2)
    save(fig, 'EAC-738-07-مستطيل-وتد-2026-07-06.png')


# ── 08 Candlesticks ──────────────────────────────────────────────────
def chart08_candles():
    fig, ax = plt.subplots(figsize=(17, 7))
    events = [
        ('Jun 17', 'Marubozu Bull', GREEN, 'Triangle break\nVol spike', 'BUY'),
        ('Jun 19', 'Shooting Star\n@ 10.25', RED, 'Climax top\nBlow-off', 'SELL zone'),
        ('Jun 24', 'Hammer\n@ 7.35', GREEN, 'Wyckoff Spring\nBounce', 'HOLD+'),
        ('Jun 29', 'Hanging Man\n@ 8.33', RED, 'Rejection #2\nLower high', 'NO chase'),
        ('Jul 4', 'Doji cluster\n@ 7.45', YELLOW, 'Indecision\nSqueeze', 'WAIT'),
        ('Jul 6 AM', 'Red push\nL=7.36', RED, 'New session low\nDistribution vol', 'HOLD حرج'),
        ('Jul 6 PM', 'Small green\n@ 7.38', GREEN, 'Bounce from L\n@ POC/VWAP', 'HOLD'),
    ]
    for i, (date, name, color, detail, action) in enumerate(events):
        x = i * 2.3
        ax.add_patch(FancyBboxPatch((x - 0.9, 1), 1.8, 5.5, boxstyle='round,pad=0.06',
                                    facecolor=PANEL, edgecolor=color, linewidth=2))
        ax.text(x, 6.0, date, ha='center', fontsize=9, color=GRAY, fontweight='bold')
        ax.text(x, 5.2, name, ha='center', fontsize=9, color=color, fontweight='bold')
        ax.text(x, 3.8, detail, ha='center', fontsize=6.5, color=GRAY, linespacing=1.3)
        ax.text(x, 1.5, action, ha='center', fontsize=8, color=color, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=BG, edgecolor=color, alpha=0.8))
    ax.set_xlim(-1.5, 16)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('Japanese Candlesticks — EAC Timeline @ 7.38', fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-738-08-شموع-يابانية-2026-07-06.png')


# ── 09 Wyckoff Spring ────────────────────────────────────────────────
def chart09_wyckoff():
    fig, ax = plt.subplots(figsize=(14, 9))
    phases = ['PS', 'SC', 'AR', 'ST', 'Spring', 'SOS', 'LPS', 'Markup']
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    y = np.array([8, 6.5, 9, 7, 6.8, 7.5, 8.5, 9.5, 10.5])
    ax.plot(x[:5], y[:5], color=GRAY, lw=2, ls='--')
    ax.plot(x[4:], y[4:], color=GREEN, lw=3)
    ax.axhspan(7.25, 7.45, alpha=0.25, color=CYAN)
    ax.scatter([4], [6.8], s=200, c=YELLOW, zorder=10, edgecolors=WHITE, lw=2)
    box(ax, 4, 6.2, 'SPRING\nSweep 7.25-7.40\nL=7.36 today\nReclaim > 7.45 = confirm', YELLOW, 9)
    mark_now(ax, 4.3, 7.38)
    for i, ph in enumerate(phases):
        ax.text(i, y[i] + 0.4, ph, ha='center', fontsize=8, color=GRAY, fontweight='bold')
    hline(ax, 7.25, 'Death 7.25', RED, lw=2)
    hline(ax, 8.14, 'SOS break 8.14', GREEN)
    ax.set_ylim(6, 11.5)
    ax.set_xticks([])
    ax.set_title('Wyckoff Re-Accumulation — Spring Zone @ 7.36-7.45 (3/5)', fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-738-09-وايكوف-Spring-2026-07-06.png')


# ── 10 Trend Lines ───────────────────────────────────────────────────
def chart10_trendlines():
    fig, ax = plt.subplots(figsize=(14, 9))
    t = np.linspace(0, 60, 200)
    price = np.piecewise(t, [t < 25, t >= 25], [lambda x: 4.9 + 0.04 * x, lambda x: 10.25 - 0.05 * (x - 25)])
    ax.plot(t, price, color=BLUE, lw=2, label='Price path')

    ax.plot([10, 55], [5.0, 8.0], color=GREEN, lw=2, ls='--', label='Primary uptrend')
    ax.plot([25, 55], [10.25, 7.36], color=RED, lw=2, ls='--', label='Correction trendline')
    ax.plot([35, 55], [8.50, 7.43], color=ORANGE, lw=2, ls=':', label='1H descending resistance')

    ax.scatter([55], [NOW], s=250, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    box(ax, 48, 7.0, f'NOW {NOW}\nOn correction line\nBreak up = 7.43-7.45', BLUE, 9)
    ax.set_ylim(4.5, 11)
    ax.set_xlabel('Sessions')
    ax.set_ylabel('EGP')
    ax.legend(facecolor=PANEL, fontsize=8)
    ax.set_title('Trend Lines — Primary · Correction · 1H Descending', fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-738-10-خطوط-ترند-2026-07-06.png')


# ── 11 Volume Profile ────────────────────────────────────────────────
def chart11_vpvr():
    fig, ax = plt.subplots(figsize=(12, 10))
    prices = np.array([6.66, 6.86, 7.10, 7.30, 7.35, 7.36, 7.39, 7.42, 7.50, 7.72, 8.14, 8.50])
    vol = np.array([15, 25, 20, 30, 35, 40, 55, 50, 45, 30, 25, 20])
    colors = [GRAY] * len(prices)
    idx = np.argmin(np.abs(prices - NOW))
    colors[idx] = BLUE
    ax.barh(prices, vol, height=0.08, color=colors, alpha=0.85, edgecolor=GRAY)
    ax.axhline(NOW, color=BLUE, lw=2)
    box(ax, 45, NOW, f'POC cluster\n7.39-7.42\nNOW @ {NOW}\nOrder book wall 7.43', BLUE, 9)
    hline(ax, 7.25, 'Death 7.25', RED, lw=2)
    ax.set_xlabel('Relative Volume (VPVR schematic)')
    ax.set_ylabel('Price (EGP)')
    ax.set_title('Volume Profile (VPVR) + Order Book @ 7.38', fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2, axis='x')
    save(fig, 'EAC-738-11-حجم-بروفايل-2026-07-06.png')


# ── 12 Target Ladder ─────────────────────────────────────────────────
def chart12_targets():
    fig, ax = plt.subplots(figsize=(11, 13))
    ax.set_xlim(0, 10)
    ax.axis('off')

    targets = [
        (10.17, 'T4 Climax sell 1/3', RED, '+311K'),
        (8.90, 'T3 Partial', ORANGE, '+148K'),
        (8.14, 'T2 GATE', GREEN, '+50K'),
        (7.72, 'T1 AVWAP ~BE', CYAN, '+0'),
        (7.50, 'POC reclaim', YELLOW, '-32K'),
        (7.45, 'Spring confirm', YELLOW, '-39K'),
        (NOW, f'NOW {NOW}', BLUE, f'{PNL:,}'),
        (7.36, 'L today', GRAY, '-50K'),
        (7.25, 'DEATH EXIT', RED, '-64K'),
        (7.24, 'STOP Limit', RED, '-65K'),
        (6.88, 'Bear full exit', RED, '-112K'),
    ]
    for i, (price, lbl, c, pnl) in enumerate(targets):
        y = 11 - i * 0.95
        w = 2.5 if price == NOW else 1.8
        ax.add_patch(FancyBboxPatch((2, y - 0.25), 6, 0.5, boxstyle='round,pad=0.05',
                                    facecolor=PANEL, edgecolor=c, linewidth=3 if price == NOW else 1.5))
        ax.text(1.5, y, f'{price:.2f}', fontsize=10, color=c, va='center', ha='right', fontweight='bold')
        ax.text(5, y, lbl, fontsize=9, color=WHITE, va='center', ha='center', fontweight='bold')
        ax.text(8.5, y, pnl, fontsize=8, color=c, va='center', ha='left')

    ax.set_title('Target Ladder + PnL @ 128,400 shares\nMeasured moves · Fib · Flag · Rectangle', fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-738-12-اهداف-PnL-2026-07-06.png')


# ── 13 Decision Master ───────────────────────────────────────────────
def chart13_decision():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.text(5, 9.5, f'EAC Decision Master @ {NOW} · 6 Jul 2026', ha='center', fontsize=14, fontweight='bold')

    nodes = [
        (5, 8.2, f'NOW {NOW}\nHOLD حرج', BLUE),
        (2, 6.5, 'Bear\n< 7.25', RED),
        (5, 6.5, 'Range\n7.36-7.50', YELLOW),
        (8, 6.5, 'Bull\n> 7.45', GREEN),
        (1, 4.5, 'EXIT x3 Limit\n7.35/7.32/7.30', RED),
        (5, 4.5, 'WAIT\nSTOP 7.24', YELLOW),
        (8, 4.5, 'HOLD+\n> 7.50 POC', GREEN),
        (8, 2.5, 'T1 7.72\nT2 8.14 Gate', GREEN),
    ]
    for x, y, txt, c in nodes:
        ax.add_patch(FancyBboxPatch((x - 1.1, y - 0.45), 2.2, 0.9, boxstyle='round,pad=0.08',
                                    facecolor=PANEL, edgecolor=c, linewidth=2))
        ax.text(x, y, txt, ha='center', va='center', fontsize=8, color=WHITE, fontweight='bold')

    for x1, y1, x2, y2, c in [
        (5, 7.75, 2, 7.0, RED), (5, 7.75, 5, 7.0, YELLOW), (5, 7.75, 8, 7.0, GREEN),
        (2, 6.05, 1, 5.0, RED), (5, 6.05, 5, 5.0, YELLOW), (8, 6.05, 8, 5.0, GREEN),
        (8, 4.05, 8, 3.0, GREEN),
    ]:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', color=c, lw=2))

    box(ax, 5, 1.2, 'STOP 7.24 Limit — NEVER CANCEL\n128,400 shares · microcap · Limit only', RED, 9)
    save(fig, 'EAC-738-13-مخطط-قرار-2026-07-06.png')


if __name__ == '__main__':
    print('Generating EAC classic charts @ 7.38 ...')
    chart01_master()
    chart02_bull_flag()
    chart03_fib()
    chart04_dow()
    chart05_sr()
    chart06_patterns()
    chart07_rect_wedge()
    chart08_candles()
    chart09_wyckoff()
    chart10_trendlines()
    chart11_vpvr()
    chart12_targets()
    chart13_decision()
    print('Done — 13 charts in', OUT)

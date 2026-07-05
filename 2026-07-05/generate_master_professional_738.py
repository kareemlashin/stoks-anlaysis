#!/usr/bin/env python3
"""
EAC @ 7.38 — Master Professional Chart Pack
Classical · Wyckoff · Elliott · SMC · Fib · Gann · Candles · 15 Pros · Indicators
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Arc, Wedge, Polygon
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
NOW, ENTRY, SHARES = 7.38, 7.75, 128_400
BG, PANEL, GRID = '#0a0e14', '#121820', '#1c2330'
G, R, Y = '#22c55e', '#ef4444', '#eab308'
B, P, O, GR, W, C = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9', '#06b6d4'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': PANEL, 'axes.edgecolor': GR,
    'text.color': W, 'xtick.color': GR, 'ytick.color': GR, 'grid.color': GRID, 'font.size': 9,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def box(ax, x, y, txt, col, fs=8, axc=None):
    kw = dict(ha='center', va='center', fontsize=fs, color=W, fontweight='bold', zorder=20,
              bbox=dict(boxstyle='round,pad=0.35', facecolor=PANEL, edgecolor=col, linewidth=1.5))
    (ax if axc is None else axc).text(x, y, txt, **kw)


def hln(ax, y, lbl, col, ls='--', lw=1.5):
    ax.axhline(y, color=col, ls=ls, lw=lw, alpha=0.9)
    ax.text(1.01, y, lbl, transform=ax.get_yaxis_transform(), fontsize=7, color=col, va='center', fontweight='bold')


def price_path_extended():
    """May-Jul schematic daily path ending @ 7.38."""
    t = np.linspace(0, 65, 260)
    p = np.piecewise(t,
        [t < 20, (t >= 20) & (t < 28), (t >= 28) & (t < 35), (t >= 35) & (t < 48), t >= 48],
        [lambda x: 4.85 + 0.012 * x,
         lambda x: 5.0 + (x - 20) * 0.65,
         lambda x: 10.17 - (x - 28) * 0.38,
         lambda x: 8.0 - (x - 35) * 0.05,
         lambda x: 7.55 - (x - 48) * 0.012 + 0.02 * np.sin((x - 48) * 0.6)])
    p[-5:] = [7.52, 7.48, 7.45, 7.35, 7.38]
    return t, p


# ═══ 01 MASTER CLASSICAL MAP @ 7.38 ═══════════════════════════════════
def c01_master_classical():
    fig, ax = plt.subplots(figsize=(18, 11))
    t, p = price_path_extended()
    ax.plot(t, p, color=B, lw=2.5, zorder=5)
    ax.fill_between(t, p, 1.5, alpha=0.06, color=B)
    ax.scatter([63], [NOW], s=220, c=Y, zorder=10, edgecolors=W, lw=2)
    box(ax, 63, NOW + 0.4, f'NOW {NOW}', Y, 10)

    # Asc triangle (done)
    ax.fill([8, 24, 24, 8], [4.82, 5.07, 5.20, 5.20], alpha=0.12, color=G)
    box(ax, 16, 4.5, 'Ascending Triangle\nDONE | Target 7.40 HIT', G, 7)

    # Double bottom
    ax.add_patch(Rectangle((2, 2.7), 10, 0.7, alpha=0.12, facecolor=G))
    box(ax, 7, 2.2, 'Double Bottom 2.88/2.90\nNeck 3.45 | DONE', G, 7)

    # Bull flag
    ax.plot([28, 32], [5.0, 10.17], color=O, lw=4)
    ax.plot([32, 63, 63, 32], [10.17, 8.04, 7.35, 7.25], '--', color=Y, lw=2)
    ax.plot([32, 63], [7.25, 7.38], '--', color=G, lw=2)
    ax.fill([32, 63, 63, 32], [10.17, 8.04, 7.38, 7.25], alpha=0.1, color=Y)
    box(ax, 48, 9.0, 'BULL FLAG ACTIVE\nPole +95% | Flag 7.25-8.04\nBreak > 8.14 | Target 13.0', Y, 8)

    # Falling wedge
    ax.plot([35, 40, 45, 50, 55, 63], [10.17, 8.6, 8.33, 8.04, 7.72, 7.72], 'r--', lw=1.5, alpha=0.7)
    ax.plot([35, 40, 45, 50, 55, 63], [7.25, 7.34, 7.45, 7.48, 7.35, 7.38], 'g--', lw=1.5, alpha=0.7)

    # Cup overlay
    cx = np.linspace(8, 58, 120)
    cup = 8.0 - 5.5 * np.sin(np.pi * (cx - 8) / 50) ** 1.05
    cup = np.clip(cup, 1.9, 8.5)
    ax.plot(cx, cup, '--', color=P, lw=1.5, alpha=0.6)
    box(ax, 30, 3.2, 'Cup & Handle\nTarget ~14 | Handle NOW', P, 7)

    # Rectangle
    ax.axhspan(7.25, 8.04, alpha=0.08, color=P)
    for y, lb, c in [(10.17, 'ATH 10.17', O), (8.14, 'Gate 8.14', Y), (7.72, 'AVWAP 7.72', C),
                     (7.50, 'POC 7.50', GR), (7.25, 'Death 7.25', R), (5.0, 'Base 5.0', G)]:
        hln(ax, y, lb, c)
    ax.set_xlim(0, 68)
    ax.set_ylim(1.5, 11.5)
    ax.set_title('EAC Master Classical Map @ 7.38 — All Patterns · Brandt · O\'Neil · Minervini',
                 fontsize=14, fontweight='bold', pad=14)
    ax.grid(True, alpha=0.2)
    ax.legend(handles=[
        Line2D([0], [0], color=G, lw=2, label='Done'),
        Line2D([0], [0], color=Y, lw=2, label='Active'),
        Line2D([0], [0], color=P, lw=2, ls='--', label='Long-term'),
    ], loc='upper left', facecolor=PANEL, fontsize=8)
    save(fig, 'EAC-PRO-01-خريطة-كلاسيكي-شاملة-738.png')


# ═══ 02 TEN PATTERNS GRID @ 7.38 ════════════════════════════════════
def c02_ten_patterns():
    fig, axes = plt.subplots(2, 5, figsize=(20, 10))
    fig.suptitle(f'EAC x 10 Classical Patterns @ {NOW} | Jul 5 2026 · AGM Tomorrow',
                 fontsize=14, fontweight='bold', y=1.01)
    data = [
        ('1. Asc Triangle', 'DONE', G, 'Res 5.20 | Break Jun 17\nTarget 7.40 HIT'),
        ('2. Desc Triangle', 'NO', GR, 'Lows RISING\n= Not this pattern'),
        ('3. Head & Shoulders', 'NO', GR, 'No symmetric shoulders\nLower highs only'),
        ('4. Inv H&S', 'NO', GR, 'Wrong context\nUptrend correction'),
        ('5. Double Bottom', 'DONE', G, '2.88/2.90 | Neck 3.45\nTarget 4.00 HIT'),
        ('6. Double Top', 'WATCH', Y, '10.17 vs 8.60\nIF reject 9.8-10.2\nNeck = 7.25'),
        ('7. Bull Flag', 'ACTIVE', Y, f'NOW {NOW} | Break 8.14\nTarget 13.07\nStop 7.25'),
        ('8. Bear Flag', 'NO', GR, 'After UP move\n= Bull flag'),
        ('9. Falling Wedge', 'ACTIVE', Y, 'Converging lines\nRising lows\nBreak 8.04'),
        ('10. Cup & Handle', 'ACTIVE', Y, 'Handle zone\nBreak 8.14\nTarget 14.10'),
    ]
    for ax, (title, st, col, det) in zip(axes.flat, data):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        if 'Triangle' in title and 'Asc' in title:
            ax.plot([1, 9], [7, 7], 'g-', lw=2)
            ax.plot([1, 9], [3, 6.5], 'g-', lw=2)
        elif 'Bull Flag' in title:
            ax.plot([1, 3], [2, 9], color=O, lw=3)
            ax.plot([3, 9], [9, 7.2], 'r--')
            ax.plot([3, 9], [4, 5.8], 'g--')
            ax.scatter([9], [5.8], s=50, c=W, edgecolors=B, lw=2)
        elif 'Wedge' in title:
            ax.plot([1, 9], [9, 6.5], 'r--')
            ax.plot([1, 9], [3, 6.2], 'g--')
        elif 'Cup' in title:
            tt = np.linspace(1, 9, 40)
            ax.plot(tt, 5 - 3 * np.sin(np.pi * (tt - 1) / 8) ** 1.1)
        elif 'Double Bottom' in title:
            ax.plot([1, 3, 5, 7, 9], [6, 3, 5, 3, 7], 'g-', lw=2)
        elif 'Double Top' in title:
            ax.plot([1, 3, 5, 7, 9], [3, 7, 5, 6.5, 3], 'r-', lw=2)
        rect = FancyBboxPatch((0.1, 0.1), 9.8, 9.8, boxstyle='round,pad=0.06',
                               facecolor=PANEL, edgecolor=col, linewidth=2.5)
        ax.add_patch(rect)
        ax.text(5, 9.2, title, ha='center', fontsize=9, fontweight='bold')
        ax.text(5, 8.2, st, ha='center', fontsize=12, fontweight='bold', color=col)
        ax.text(5, 4.5, det, ha='center', fontsize=6.5, color=GR, linespacing=1.4)
    save(fig, 'EAC-PRO-02-10-نماذj-كلاسيكية-738.png')


# ═══ 03 BULL FLAG DETAIL @ 7.38 ═════════════════════════════════════
def c03_bull_flag():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.plot([0, 1.2], [5.0, 10.17], color=O, lw=5)
    box(ax, 0.6, 7.5, 'POLE +103%\n5.00 -> 10.17\n5 sessions', O, 9)
    x = np.array([1.2, 2, 3, 4, 5, 5.8, 6.2])
    top = [10.17, 8.60, 8.33, 8.04, 7.72, 7.72, 7.72]
    bot = [7.25, 7.34, 7.45, 7.48, 7.50, 7.35, 7.38]
    ax.plot(x, top, 'r-o', lw=2, ms=8)
    ax.plot(x, bot, 'g-o', lw=2, ms=8)
    ax.fill_between(x, top, bot, alpha=0.12, color=Y)
    ax.scatter([6.2], [NOW], s=350, c=W, edgecolors=B, lw=3, zorder=10)
    box(ax, 6.2, 6.7, f'NOW {NOW}\nL=7.35 sweep\nBrandt | Minervini', B, 9)
    ax.annotate('', xy=(7.8, 13.0), xytext=(6.2, 8.14), arrowprops=dict(arrowstyle='->', color=G, lw=3))
    for y, lb, c in [(8.14, 'BREAKOUT 8.14', G), (13.07, 'TARGET 13.07', G), (7.25, 'FAIL 7.25', R)]:
        ax.axhline(y, color=c, ls='--', lw=2 if y == 7.25 else 1.5)
        ax.text(0.1, y, lb, color=c, fontsize=8, fontweight='bold')
    ax.set_xlim(-0.2, 8.5)
    ax.set_ylim(4.5, 14.5)
    ax.set_title('Bull Flag (Brandt/Minervini) @ 7.38 — Measured Move to 13.07', fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-03-علم-الثور-738.png')


# ═══ 04 SHOOTING STAR + O'NEIL CLIMAX ═══════════════════════════════
def c04_shooting_star():
    fig, ax = plt.subplots(figsize=(14, 8))
    # Daily candles schematic Jun-Jul
    candles = [
        (0, 7.0, 8.5, 6.8, 8.2, G), (1, 8.2, 9.5, 8.0, 9.2, G), (2, 9.2, 10.5, 9.0, 10.0, G),
        (3, 10.0, 10.20, 7.5, 8.5, R),  # shooting star
        (4, 8.5, 8.8, 7.8, 8.0, R), (5, 8.0, 8.2, 7.5, 7.7, R),
        (6, 7.7, 7.9, 7.3, 7.5, R), (7, 7.5, 7.72, 7.35, NOW, R),
    ]
    for i, (xi, o, h, l, c, col) in enumerate(candles):
        col = G if c >= o else R
        ax.plot([xi, xi], [l, h], color=col, lw=1.5)
        body_lo, body_hi = min(o, c), max(o, c)
        ax.add_patch(Rectangle((xi - 0.3, body_lo), 0.6, max(body_hi - body_lo, 0.05),
                                facecolor=col, edgecolor=col))
    ax.annotate('SHOOTING STAR\nO\'Neil Climax Top\nH=10.20 | Long upper wick\nExhaustion gap warning',
                xy=(3, 10.20), xytext=(4.5, 10.8), arrowprops=dict(arrowstyle='->', color=R),
                fontsize=9, color=R, fontweight='bold')
    ax.axhline(10.17, color=O, ls='--', label='ATH zone')
    ax.axhline(8.14, color=Y, ls='--')
    ax.axhline(7.25, color=R, lw=2)
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(6.8, 11.2)
    ax.set_xticks(range(8))
    ax.set_xticklabels(['Jun24', 'Jun25', 'Jun26', 'Jun27', 'Jun30', 'Jul1', 'Jul3', 'Jul5'])
    ax.set_title("O'Neil Climax Analysis — Shooting Star @ 10.20 · 3 Red Follow-through", fontweight='bold')
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-04-شهاب-اونيل-738.png')


# ═══ 05 WYCKOFF PHASES ══════════════════════════════════════════════
def c05_wyckoff():
    fig, ax = plt.subplots(figsize=(16, 9))
    phases = [
        (0, 8, 3.2, G, 'Accumulation\n2025\nVol: dead'),
        (8, 14, 4.8, G, 'Markup 1\nGradual'),
        (14, 20, 5.0, Y, 'Re-Accum\nFlat 5.0\nAbsorption'),
        (20, 26, 10.17, O, 'Markup 2\nParabolic\nJun 11-17'),
        (26, 32, 8.5, R, 'Distribution?\nVol climax\nat peak'),
        (32, 50, 7.38, Y, f'Re-Accum?\nNOW {NOW}\nSpring zone'),
        (50, 56, 8.5, P, 'AGM Jul 6\nCatalyst\nTBD'),
    ]
    xp = np.linspace(0, 56, 300)
    yp = np.piecewise(xp,
        [xp < 8, (xp >= 8) & (xp < 20), (xp >= 20) & (xp < 26), (xp >= 26) & (xp < 32),
         (xp >= 32) & (xp < 50), xp >= 50],
        [lambda x: 3.0 + 0.02 * x, lambda x: 3.5 + (x - 8) * 0.12,
         lambda x: 5.0 + (x - 20) * 0.86, lambda x: 10.17 - (x - 26) * 0.28,
         lambda x: 8.5 - (x - 32) * 0.04, lambda x: 7.38 + 0.02 * np.sin(x)])
    ax.plot(xp, yp, color=B, lw=2.5)
    for x0, x1, peak, col, txt in phases:
        ax.axvspan(x0, x1, alpha=0.08, color=col)
        ax.text((x0 + x1) / 2, peak + 0.3 if peak < 9 else peak + 0.5, txt, ha='center',
                fontsize=7, color=col, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=col, alpha=0.9))
    ax.axhline(7.25, color=R, ls='--', lw=2)
    ax.scatter([48], [NOW], s=200, c=Y, edgecolors=W, lw=2, zorder=5)
    box(ax, 48, 6.8, f'SPRING ZONE\nL=7.35 sweep\n3/5 re-accum', Y, 8)
    ax.set_ylim(2, 11.5)
    ax.set_title('Wyckoff Phase Analysis @ 7.38 — Accumulation vs Distribution', fontweight='bold')
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-05-وايكوف-مراحل-738.png')


# ═══ 06 ELLIOTT WAVE @ 7.38 ═════════════════════════════════════════
def c06_elliott():
    fig, ax = plt.subplots(figsize=(16, 10))
    # Waves from 1.90
    wx = [0, 8, 18, 28, 38, 48, 55]
    wy = [1.90, 3.6, 2.9, 10.17, 7.25, 7.35, NOW]
    labels = ['(2)', '(3)', '', '(4)', 'Spring?', f'(5)?\n{NOW}']
    ax.plot(wx[:5], wy[:5], 'o-', color=B, lw=3, ms=10)
    ax.plot(wx[4:7], wy[4:7], 'o-', color=Y, lw=3, ms=10)
    ax.annotate('', xy=(55, 11.7), xytext=(48, NOW),
                arrowprops=dict(arrowstyle='->', color=G, lw=3))
    for i, (x, y, lb) in enumerate(zip(wx[1:], wy[1:], ['(1)', '(2)', '(3)', '(4)', '', ''])):
        if lb:
            ax.text(x, y + 0.4, lb, ha='center', fontsize=10, fontweight='bold', color=B)
    ax.text(0, 1.5, 'Start\n1.90', fontsize=8, color=GR)
    ax.text(28, 10.6, 'Wave 3\n10.17\n+250%', fontsize=9, color=G, fontweight='bold')
    ax.text(38, 6.9, 'Wave 4\n0.382=7.39\nNOW testing', fontsize=9, color=Y, fontweight='bold')
    box(ax, 52, 12.0, 'Wave 5 Targets\nMin 8.95\nBase 11.7\nExt 14.4', G, 9)
    ax.axhline(7.25, color=R, ls='--', lw=2)
    ax.axhline(6.88, color=R, ls=':', label='Alt count invalidation')
    ax.set_ylim(0.5, 13)
    ax.set_title('Elliott Wave Count @ 7.38 — Wave 4 Near Complete · W5 Targets 8.95-14.4', fontweight='bold')
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-06-إليott-738.png')


# ═══ 07 FIBONACCI RETRACEMENT ═══════════════════════════════════════
def c07_fibonacci():
    fig, ax = plt.subplots(figsize=(14, 10))
    low, high = 4.85, 10.17
    levels = [
        (0.0, high, '100% 10.17', O), (0.236, 8.92, '23.6%', GR), (0.382, 8.14, '38.2% Gate', Y),
        (0.5, 7.51, '50% POC', GR), (0.618, 6.88, '61.8%', G), (0.786, 5.99, '78.6%', G),
        (1.0, low, '0% 4.85', G),
    ]
    t, p = price_path_extended()
    ax.plot(t[-30:], p[-30:], color=B, lw=2.5)
    ax.scatter([t[-1]], [NOW], s=200, c=Y, edgecolors=W, lw=2, zorder=5)
    for fib, price, lbl, col in levels:
        ax.axhline(price, color=col, ls='--', alpha=0.7, lw=1.5 if fib in (0.382, 0.5) else 1)
        ax.text(0.5, price, f'  {lbl} = {price:.2f}', fontsize=8, color=col, va='center')
    ax.axhspan(7.25, 7.45, alpha=0.15, color=Y)
    box(ax, t[-15], 7.1, f'NOW {NOW}\nBelow 50% & POC\nAbove 61.8%', Y, 9)
    ax.set_ylim(5.5, 10.8)
    ax.set_title('Fibonacci Retracement 4.85-10.17 @ 7.38 — 50% Broken · 61.8% Hold Critical', fontweight='bold')
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-07-فibo-738.png')


# ═══ 08 GANN SQUARE OF 9 ════════════════════════════════════════════
def c08_gann():
    fig, ax = plt.subplots(figsize=(12, 10))
    sqrt_high = np.sqrt(10.17)
    angles = [
        ('+90', 13.61, P), ('+45', 11.83, G), ('0', 10.17, O),
        ('-45', 8.64, Y), ('-90', 7.23, G), ('-135', 5.95, G), ('-180', 4.79, G),
    ]
    y_pos = np.arange(len(angles))
    prices = [a[1] for a in angles]
    cols = [a[2] for a in angles]
    ax.barh(y_pos, prices, color=cols, edgecolor=W, height=0.55, alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"Gann {a[0]} = {a[1]:.2f}" for a in angles], fontsize=9)
    ax.axvline(NOW, color=Y, ls='-', lw=3, label=f'NOW {NOW}')
    ax.text(NOW + 0.1, 4, f'NOW {NOW}\nNear -90 (7.23)\nL=7.35', color=Y, fontsize=9, fontweight='bold')
    ax.set_xlabel('Price (EGP)')
    ax.set_title('Gann Square of 9 from ATH 10.17 — NOW @ -90 Degree (7.23)', fontweight='bold')
    ax.grid(axis='x', alpha=0.2)
    save(fig, 'EAC-PRO-08-جان-738.png')


# ═══ 09 SMC FULL MAP ══════════════════════════════════════════════════
def c09_smc():
    fig, ax = plt.subplots(figsize=(16, 10))
    t, p = price_path_extended()
    ax.plot(t, p, color=B, lw=2)
    zones = [
        (4.84, 5.25, G, 'OB Buy\n4.84-5.25'),
        (6.90, 7.33, P, 'FVG\n6.90-7.33'),
        (7.25, 7.45, O, 'Breaker\n7.25-7.45'),
        (7.35, 7.72, R, 'Spring Zone\nDiscount'),
    ]
    for y0, y1, col, txt in zones:
        ax.axhspan(y0, y1, alpha=0.15, color=col)
    ax.scatter([63], [NOW], s=200, c=Y, zorder=5, edgecolors=W, lw=2)
    # BSL markers
    for y in [8.33, 8.60, 10.17]:
        ax.axhline(y, color=C, ls=':', alpha=0.6)
        ax.text(64, y, f'BSL {y}', fontsize=7, color=C)
    ax.annotate('SSL sweep\nL=7.35', xy=(62, 7.35), xytext=(55, 6.8),
                arrowprops=dict(arrowstyle='->', color=R), color=R, fontsize=8)
    box(ax, 10, 4.8, zones[0][3], G, 7)
    box(ax, 45, 7.0, zones[1][3], P, 7)
    box(ax, 58, 7.55, 'ICT Discount\nSweep 7.25\n-> Reclaim 7.45\n-> BSL 8.33', Y, 8)
    hln(ax, 7.25, 'SSL 7.25', R, lw=2)
    hln(ax, 8.11, 'BOS 8.11', Y)
    ax.set_ylim(4, 11)
    ax.set_title('SMC/ICT Full Map @ 7.38 — Order Blocks · FVG · Liquidity · BOS', fontweight='bold')
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-PRO-09-SMC-ICT-738.png')


# ═══ 10 DARVAS BOX + BROOKS RANGE ═══════════════════════════════════
def c10_darvas_brooks():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('Darvas Box + Al Brooks Trading Range @ 7.38', fontsize=13, fontweight='bold')
    # Darvas
    a1.axhspan(7.25, 8.33, alpha=0.2, color=P)
    a1.axhline(8.33, color=R, lw=2, label='Box top 8.33')
    a1.axhline(7.25, color=G, lw=2, label='Box bottom 7.25')
    a1.axhline(NOW, color=Y, lw=2)
    a1.scatter([5], [NOW], s=250, c=W, edgecolors=B, lw=3)
    a1.plot([0, 5], [8.0, NOW], 'r--', alpha=0.5)
    box(a1, 2.5, 7.8, 'Darvas Box\n7.25 - 8.33\nBuy: break 8.33+vol\nStop: below 7.25', P, 8, axc=a1)
    box(a1, 2.5, 6.9, f'NOW {NOW}\nNear FLOOR\n13 pts above stop', Y, 8, axc=a1)
    a1.set_ylim(6.8, 9.0)
    a1.set_xlim(0, 6)
    a1.set_title('Darvas Box Theory', fontweight='bold')
    a1.grid(True, alpha=0.2)
    # Brooks
    rx = np.linspace(0, 15, 80)
    ry = 7.65 + 0.12 * np.sin(rx * 1.1) + 0.06 * np.sin(rx * 2.5)
    ry[-20:] = np.linspace(7.65, NOW, 20)
    a2.plot(rx, ry, color=B, lw=2.5)
    a2.axhspan(7.25, 8.04, alpha=0.12, color=P)
    for y, lb, c in [(8.04, 'Resistance', R), (7.75, 'Entry', O), (7.50, 'POC', GR),
                     (NOW, f'NOW {NOW}', Y), (7.25, 'Support', G)]:
        a2.axhline(y, color=c, ls='--' if y != NOW else '-', lw=2 if y in (NOW, 7.25) else 1)
        a2.text(15.5, y, lb, fontsize=7, color=c, va='center')
    box(a2, 7, 8.3, 'Brooks TTR\nAlways-In: NEUTRAL\nH2 buy > 7.45\nL2 sell < 7.25', P, 8, axc=a2)
    a2.set_xlim(0, 16)
    a2.set_ylim(6.9, 8.6)
    a2.set_title('Al Brooks Trading Range', fontweight='bold')
    a2.grid(True, alpha=0.2)
    plt.tight_layout()
    save(fig, 'EAC-PRO-10-دارvas-بrooks-738.png')


# ═══ 11 INDICATORS SIMULATED PANEL ════════════════════════════════════
def c11_indicators():
    fig, axes = plt.subplots(4, 1, figsize=(14, 12), gridspec_kw={'height_ratios': [3, 1, 1, 1]})
    fig.suptitle(f'EAC Professional Indicators Panel @ {NOW}', fontsize=13, fontweight='bold')
    t = np.arange(30)
    price = 7.8 - 0.015 * t + 0.08 * np.sin(t * 0.4)
    price[-8:] = [7.72, 7.65, 7.58, 7.52, 7.48, 7.42, 7.35, NOW]
    ax = axes[0]
    ax.plot(t, price, color=B, lw=2)
    ax.plot(t, np.full(30, 7.50), '--', color=GR, alpha=0.5, label='Kijun/POC 7.50')
    ax.plot(t, 7.08 + 0.005 * t, color=G, alpha=0.7, label='MA20 ~7.08')
    ax.axhline(7.72, color=C, ls=':', label='AVWAP 7.72')
    ax.axhline(7.25, color=R, lw=2, label='Death 7.25')
    ax.scatter([29], [NOW], s=150, c=Y, zorder=5)
    ax.set_ylabel('Price')
    ax.legend(facecolor=PANEL, fontsize=7, loc='upper right')
    ax.grid(True, alpha=0.2)
    # RSI
    rsi = 60 - 0.8 * t + 2 * np.sin(t * 0.3)
    rsi[-5:] = [52, 48, 42, 38, 35]
    axes[1].plot(t, rsi, color=P, lw=1.5)
    axes[1].axhline(50, color=GR, ls=':')
    axes[1].axhline(30, color=G, ls='--', alpha=0.5)
    axes[1].fill_between(t, 0, rsi, alpha=0.2, color=P)
    axes[1].set_ylabel('RSI(14)')
    axes[1].set_ylim(20, 80)
    axes[1].grid(True, alpha=0.2)
    # MACD
    macd = 0.3 - 0.04 * t
    macd[-5:] = [-0.05, -0.08, -0.10, -0.12, -0.14]
    axes[2].bar(t, macd, color=[G if v >= 0 else R for v in macd], alpha=0.7)
    axes[2].axhline(0, color=GR)
    axes[2].set_ylabel('MACD hist')
    axes[2].grid(True, alpha=0.2)
    # StochRSI
    stoch = 50 - 2 * t
    stoch[-3:] = [8, 4, 2]
    axes[3].plot(t, stoch, color=G, lw=2)
    axes[3].axhline(5, color=G, ls='--', label='Extreme oversold')
    axes[3].fill_between(t, 0, stoch, alpha=0.2, color=G)
    axes[3].set_ylabel('StochRSI')
    axes[3].set_xlabel('Sessions')
    axes[3].set_ylim(0, 100)
    axes[3].legend(facecolor=PANEL, fontsize=7)
    axes[3].grid(True, alpha=0.2)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save(fig, 'EAC-PRO-11-مؤشرات-احترافية-738.png')


# ═══ 12 15 PROFESSIONALS VISUAL ═══════════════════════════════════════
def c12_15_pros():
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.axis('off')
    ax.text(0.5, 0.98, f'15 Trading Legends — EAC @ {NOW} · 128,400 @ {ENTRY} · AGM Tomorrow',
            ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes)
    pros = [
        ('Minervini\nSEPA/VCP', 'HOLD', 'Stop 7.25\nPivot 8.11', G),
        ('Qullamaggie\nFlags', 'HOLD', 'Sell 43K @ 8.6\nMA10 trail', G),
        ('Wyckoff\nInstitutional', 'HOLD+', 'Spring 7.35\n3/5 re-accum', Y),
        ('Shannon\nAVWAP', 'WAIT', 'Decision 7.72\nGate 8.13', Y),
        ('Livermore\nPivots', 'NO TRADE', 'Inside range\nPyramid 8.11', GR),
        ("O'Neil\nCANSLIM", 'CAUTION', 'Climax 10.17\nM = red', O),
        ('Weinstein\nStages', 'HOLD', 'Stage 2\nNot Stage 3', G),
        ('Darvas\nBox', 'HOLD', 'Box 7.25-8.33\nNear floor', G),
        ('Al Brooks\nPrice Action', 'NEUTRAL', 'TTR 7.25-8.04\nBear+bounce', Y),
        ('Raschke\nTurtle Soup', 'WATCH', 'Sweep 7.25\nAGM 1st 30m', Y),
        ('Brandt\nClassical', 'HOLD', 'Flag valid\nFail = 7.25', G),
        ('Connors\nRSI-2', 'NEAR', 'RSI-2 ~35\nTrigger 7.25', Y),
        ('Williams\n%R', 'NEAR', 'Oversold -75', Y),
        ('Mark Douglas\nPsychology', 'HOLD PLAN', 'No fear sell\n13 pts above stop', G),
        ('Elliott/Gann\nWaves', 'HOLD', 'W4 @ 7.39\nTarget 11.7', G),
    ]
    for i, (name, act, det, col) in enumerate(pros):
        row, col_i = divmod(i, 5)
        x, y = 0.02 + col_i * 0.196, 0.88 - row * 0.22
        rect = FancyBboxPatch((x, y - 0.08), 0.18, 0.18, boxstyle='round,pad=0.01',
                               facecolor=PANEL, edgecolor=col, linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + 0.01, y + 0.06, name, fontsize=8, fontweight='bold', color=col, transform=ax.transAxes, va='top')
        ax.text(x + 0.01, y + 0.01, act, fontsize=9, fontweight='bold', transform=ax.transAxes, va='top')
        ax.text(x + 0.01, y - 0.04, det, fontsize=7, color=GR, transform=ax.transAxes, va='top')
    rect = FancyBboxPatch((0.02, 0.02), 0.96, 0.06, boxstyle='round', facecolor='#1a1a2e',
                           edgecolor=R, linewidth=2, transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.5, 0.05, 'UNIFIED: Hold above 7.25 | Spring reclaim = strongest | Close < 7.25 x2 = EXIT | NO MARKET 128K',
            ha='center', fontsize=10, color=R, fontweight='bold', transform=ax.transAxes)
    save(fig, 'EAC-PRO-12-15-محترف-738.png')


# ═══ 13 TARGET CLUSTERS + PnL ═════════════════════════════════════════
def c13_targets_pnl():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(16, 10))
    fig.suptitle(f'EAC Target Clusters + Your P&L @ {NOW} · {SHARES:,} shares', fontsize=13, fontweight='bold')
    targets = [
        (7.25, 'Stop', R, -64200), (NOW, 'NOW', GR, -47508), (7.75, 'Entry', O, 0),
        (8.14, 'Gate', Y, 50076), (8.90, 'Stn 1', G, 147660), (10.17, 'ATH', G, 310848),
        (11.74, 'Elliot', P, 511824), (12.57, 'Magnet', P, 618888), (13.36, 'Flag', P, 720384),
    ]
    a1.barh([t[1] for t in targets], [t[3] for t in targets], color=[t[2] for t in targets], edgecolor=W, height=0.55)
    a1.axvline(0, color=W, lw=1)
    a1.set_xlabel('P&L (EGP)')
    a1.set_title('P&L at Each Level', fontweight='bold')
    a1.grid(axis='x', alpha=0.2)
    clusters = [
        (7.25, 8.95, 'Breakout Zone', Y), (10.9, 11.9, 'Cluster 1', G),
        (12.5, 13.2, 'Magnet Zone', P), (15.0, 15.9, 'Ceiling', R),
    ]
    for y0, y1, name, col in clusters:
        a2.axhspan(y0, y1, alpha=0.15, color=col)
        a2.text(0.5, (y0 + y1) / 2, name, ha='center', fontsize=9, color=col, fontweight='bold')
    for p, name, col, _ in targets:
        a2.axhline(p, color=col, ls='-' if p == NOW else '--', lw=2 if p == NOW else 1)
    a2.scatter([0.5], [NOW], s=200, c=Y, zorder=5)
    a2.set_xlim(0, 1)
    a2.set_ylim(6.8, 14.5)
    a2.set_xticks([])
    a2.set_title('Target Clusters (Minervini/Gann/Elliott/P&F)', fontweight='bold')
    a2.grid(True, alpha=0.2)
    plt.tight_layout()
    save(fig, 'EAC-PRO-13-اهداف-PnL-738.png')


# ═══ 14 CANDLESTICK PATTERNS RECENT ═══════════════════════════════════
def c14_candles():
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Japanese Candlestick Patterns — EAC Recent Action', fontsize=13, fontweight='bold')
    patterns = [
        ('Shooting Star', 'Jun 27 @ 10.20', R, lambda ax: (
            ax.plot([0.5, 0.5], [0.2, 0.95], 'r-', lw=2),
            ax.add_patch(Rectangle((0.35, 0.2), 0.3, 0.25, facecolor=R)))),
        ('Three Black Crows', 'Jul 1-3', R, lambda ax: (
            [ax.add_patch(Rectangle((0.2 + i * 0.25, 0.3 + i * 0.15), 0.15, 0.35 - i * 0.05, facecolor=R)) for i in range(3)])),
        ('Hammer / Bounce', 'Jul 5 L=7.35', G, lambda ax: (
            ax.plot([0.5, 0.5], [0.15, 0.7], 'g-', lw=2),
            ax.add_patch(Rectangle((0.35, 0.55), 0.3, 0.15, facecolor=G)))),
        ('Doji Freeze', '15m-1m NOW', Y, lambda ax: (
            ax.plot([0.5, 0.5], [0.45, 0.55], color=Y, lw=2),
            ax.plot([0.3, 0.7], [0.5, 0.5], color=Y, lw=3))),
        ('Harami', 'Inside day', Y, lambda ax: (
            ax.add_patch(Rectangle((0.25, 0.25), 0.5, 0.5, facecolor=R, alpha=0.5)),
            ax.add_patch(Rectangle((0.35, 0.4), 0.3, 0.2, facecolor=G)))),
        ('Spinning Top', 'Consolidation', GR, lambda ax: (
            ax.plot([0.5, 0.5], [0.3, 0.7], color=GR, lw=1.5),
            ax.add_patch(Rectangle((0.4, 0.45), 0.2, 0.1, facecolor=GR)))),
    ]
    for ax, (name, when, col, draw) in zip(axes.flat, patterns):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        draw(ax)
        ax.set_title(f'{name}\n{when}', fontsize=10, fontweight='bold', color=col)
        ax.axis('off')
        rect = FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle='round', facecolor=PANEL,
                               edgecolor=col, linewidth=2, transform=ax.transAxes)
        ax.add_patch(rect)
    save(fig, 'EAC-PRO-14-شموع-يابانية-738.png')


# ═══ 15 DECISION FLOWCHART MASTER ═════════════════════════════════════
def c15_decision():
    fig, ax = plt.subplots(figsize=(16, 14))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')
    ax.set_title(f'EAC Master Decision Flow @ {NOW} — Classical + Wyckoff + 15 Pros + SMC',
                 fontsize=13, fontweight='bold', pad=15)
    nodes = [
        (5, 13, f'NOW {NOW}\n128,400 @ {ENTRY}\nAGM Tomorrow', Y, 2.8, 0.8),
        (5, 11.2, 'AGM Session\nFirst 30 min\n(Raschke Rule)', P, 2.5, 0.7),
        (2, 9.2, 'Spring\n7.25-7.35\n+ reclaim 7.45', G, 2.2, 0.8),
        (5, 9.2, 'Freeze\n7.35-7.65', Y, 2.0, 0.7),
        (8, 9.2, 'Break\n< 7.25', R, 2.0, 0.7),
        (2, 7.2, 'HOLD STRONG\nWyckoff+ICT', G, 2.2, 0.7),
        (5, 7.2, 'HOLD\nWait', Y, 1.8, 0.6),
        (8, 7.2, 'EXIT x3\n7.35/7.32/7.30', R, 2.4, 0.7),
        (2, 5.2, 'Break 8.11-8.43\n+ vol +40%', G, 2.6, 0.7),
        (5, 5.2, 'Sell 43K @ 8.6-9\nQullamaggie', O, 2.6, 0.7),
        (8, 5.2, 'Loss ~65K\nStop 7.24', R, 2.0, 0.6),
        (3.5, 3.2, 'Trail MA10\nTarget 12.57', G, 2.4, 0.6),
        (6.5, 3.2, 'Climax sell\n@ 10.17 O\'Neil', O, 2.4, 0.6),
        (5, 1.2, 'NEVER Market 128K | NEVER Cancel Stop 7.24 | Forfeit 32,100 free shares if panic sell', R, 7, 0.6),
    ]
    for x, y, txt, col, w, h in nodes:
        rect = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.02',
                               facecolor=PANEL, edgecolor=col, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, txt, ha='center', va='center', fontsize=7.5, fontweight='bold')
    for x1, y1, x2, y2 in [(5, 12.6, 5, 11.55), (5, 10.85, 2, 9.6), (5, 10.85, 5, 9.55), (5, 10.85, 8, 9.6),
                            (2, 8.8, 2, 7.55), (5, 8.85, 5, 7.5), (8, 8.8, 8, 7.55),
                            (2, 6.85, 2, 5.55), (2, 4.85, 3.5, 3.5), (5, 6.85, 5, 5.55), (8, 6.85, 8, 5.55)]:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', color=GR, lw=1.5))
    save(fig, 'EAC-PRO-15-مخطط-قرار-ماستر-738.png')


# ═══ 16 MTF COMPOSITE ═════════════════════════════════════════════════
def c16_mtf():
    fig, axes = plt.subplots(6, 1, figsize=(14, 14))
    fig.suptitle(f'EAC Multi-Timeframe Composite @ {NOW}', fontsize=13, fontweight='bold')
    specs = [
        ('Monthly', 'Parabolic + Shooting star 10+ | 3 red | Above 7.25', G,
         lambda n: np.interp(np.linspace(0, 1, n), [0, 0.25, 0.5, 1], [3, 5, 10.5, NOW])),
        ('Weekly', 'Blow-off top | 3 red post-peak | Spring zone', Y,
         lambda n: np.interp(np.linspace(0, 1, n), [0, 0.3, 0.5, 1], [4, 8, 10.5, NOW])),
        ('Daily', 'Bull flag 7.30-8.50 | H=7.72 reject | L=7.35', Y,
         lambda n: np.interp(np.linspace(0, 1, n), [0, 0.35, 0.7, 1], [5, 10, 7.72, NOW])),
        ('4H', 'Range 7.30-8.50 since Jun 18 | Vol declining', GR,
         lambda n: NOW + 0.15 * np.sin(np.linspace(0, 4 * np.pi, n))),
        ('1H', 'Failed 8.50 bounce | Slow drift down', GR,
         lambda n: np.linspace(8.0, NOW, n)),
        ('15M-1M', f'FREEZE @ {NOW} | Absorption | AGM prep', C,
         lambda n: np.full(n, NOW)),
    ]
    for ax, (name, msg, col, fn) in zip(axes, specs):
        n = 40
        y = fn(n)
        ax.plot(range(n), y, color=col, lw=2)
        ax.axhline(7.25, color=R, ls=':', alpha=0.7)
        ax.axhline(8.14, color=Y, ls=':', alpha=0.5)
        ax.fill_between(range(n), 7.25, 8.04, alpha=0.05, color=P)
        ax.set_ylabel(name, fontweight='bold')
        ax.text(0.98, 0.85, msg, transform=ax.transAxes, ha='right', fontsize=7, color=GR)
        ax.set_ylim(min(6.8, NOW - 0.5), max(11, 10.5) if 'Monthly' in name or 'Weekly' in name else 8.8)
        ax.grid(True, alpha=0.2)
    axes[-1].set_xlabel('Bars (schematic)')
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    save(fig, 'EAC-PRO-16-MTF-مركb-738.png')


if __name__ == '__main__':
    print('Generating 16 PRO master charts @ 7.38...')
    c01_master_classical()
    c02_ten_patterns()
    c03_bull_flag()
    c04_shooting_star()
    c05_wyckoff()
    c06_elliott()
    c07_fibonacci()
    c08_gann()
    c09_smc()
    c10_darvas_brooks()
    c11_indicators()
    c12_15_pros()
    c13_targets_pnl()
    c14_candles()
    c15_decision()
    c16_mtf()
    print('Done — 16 PRO charts @ 7.38.')

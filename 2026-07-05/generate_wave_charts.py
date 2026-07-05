#!/usr/bin/env python3
"""EAC Elliott Wave charts — all waves."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
BG, PANEL = '#0a0e14', '#121820'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9'
W1, W2, W3, W4, W5 = '#3b82f6', '#ef4444', '#22c55e', '#eab308', '#a855f7'

plt.rcParams.update({'figure.facecolor': BG, 'axes.facecolor': PANEL,
                     'text.color': WHITE, 'grid.color': '#1c2330'})


def save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def wave_label(ax, x, y, text, color, dy=0.35, fs=11):
    ax.annotate(text, (x, y), textcoords='offset points', xytext=(0, dy * 25),
                fontsize=fs, fontweight='bold', color=color, ha='center',
                bbox=dict(boxstyle='circle,pad=0.25', facecolor=PANEL, edgecolor=color, lw=1.5))


def box(ax, x, y, txt, color, fs=8):
    ax.text(x, y, txt, ha='center', va='center', fontsize=fs, color=WHITE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=PANEL, edgecolor=color, lw=1.5))


# ═══════════════════════════════════════════════════════════════════════
# 1. MASTER — Primary cycle 2022-2026
# ═══════════════════════════════════════════════════════════════════════
def chart01_master():
    fig, ax = plt.subplots(figsize=(18, 10))
    # Primary wave path
    xs = [0, 8, 14, 22, 30, 38, 48, 58, 68]
    ys = [0.8, 2.5, 1.0, 5.5, 1.9, 3.5, 5.0, 10.17, 7.50]
    ax.plot(xs, ys, color=WHITE, lw=2, alpha=0.3, zorder=1)
    ax.plot(xs, ys, 'o-', color=BLUE, lw=2.5, ms=6, zorder=3)

    labels = [
        (0, 0.8, 'Start\n2022', GRAY, 0.2),
        (8, 2.5, '(I)\n2.5', W1, 0.4),
        (14, 1.0, '(II)\n1.0', W2, -0.5),
        (22, 5.5, '(III)\n5.5', W3, 0.4),
        (30, 1.9, '(IV)\n1.9', W4, -0.6),
        (38, 3.5, 'a', ORANGE, 0.3),
        (48, 5.0, 'b\nRe-accum', YELLOW, 0.3),
        (58, 10.17, '(V)\n10.17\nCLimax', W5, 0.5),
        (68, 7.50, 'W4?\n7.50\nNOW', W4, -0.5),
    ]
    for x, y, t, c, dy in labels:
        wave_label(ax, x, y, t, c, dy, 9)

    # Wave 5 projections
    proj_x = [68, 78, 88]
    proj_y = [7.50, 12.57, 14.52]
    ax.plot(proj_x, proj_y, '--', color=PURPLE, lw=2, alpha=0.8)
    ax.scatter([78, 88], [12.57, 14.52], s=100, c=PURPLE, zorder=5, edgecolors=WHITE)
    box(ax, 78, 13.2, 'Wave 5 target 1\n12.57 (Elliott + Fib + Hosoda N)', PURPLE, 7)
    box(ax, 88, 15.1, 'Wave 5 target 2\n14.52 (5=Wave1)', PURPLE, 7)

    ax.axhline(7.25, color=RED, ls=':', lw=1.5)
    ax.text(69, 7.05, 'Invalidation 7.25', color=RED, fontsize=8)
    ax.axhline(7.75, color=ORANGE, ls='--', lw=1, alpha=0.7)
    ax.text(69, 7.9, 'Entry 7.75', color=ORANGE, fontsize=8)

    box(ax, 35, 8.5, 'PRIMARY DEGREE CYCLE\n(I) 2022-23: 0.8->2.5\n(II) 2023: 2.5->1.0 (deep)\n(III) 2023: 1.0->5.5\n(IV) 2024: 5.5->1.9 (-75%)\n(V) 2026: 5.0->10.17 (+103%)', BLUE, 7)
    box(ax, 55, 4.5, 'INTERMEDIATE WAVE 4 (NOW)\nCorrection from 10.17\nTarget zone 7.25-7.50\nFib 50% = 7.60\nFib 61.8% = 7.00', YELLOW, 7)

    ax.set_xlim(-2, 92)
    ax.set_ylim(0, 16)
    ax.set_ylabel('Price (EGP)', fontsize=10)
    ax.set_xlabel('Timeline 2022 ──────────────────────────── 2026+ Projections', fontsize=10)
    ax.set_title('EAC — Elliott Wave Master Map\nPrimary + Intermediate + Wave 5 Projections @ 7.50',
                 fontsize=14, fontweight='bold', pad=15)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-موجات-01-خريطة-رئيسية.png')


# ═══════════════════════════════════════════════════════════════════════
# 2. INTERMEDIATE — Jun 2026 impulse 1-2-3-4-5
# ═══════════════════════════════════════════════════════════════════════
def chart02_intermediate():
    fig, ax = plt.subplots(figsize=(16, 9))
    # Jun impulse: 5.0 -> 10.17 with wave 4 now
    xs = [0, 3, 6, 9, 12, 15, 18, 22]
    ys = [5.0, 6.2, 5.5, 8.0, 7.1, 10.17, 7.25, 7.50]
    ax.plot(xs, ys, color=WHITE, lw=3, zorder=2)

    waves = [(0, 5.0, '1\n5.00', W1), (3, 6.2, '2\n6.20', W2),
             (6, 5.5, '2\n5.50', W2), (9, 8.0, '3\n8.00', W3),
             (12, 7.1, '4\n7.10', W4), (15, 10.17, '5\n10.17', W5),
             (18, 7.25, 'A\n7.25', RED), (22, 7.50, 'NOW\n7.50', BLUE)]
    for x, y, t, c in waves:
        wave_label(ax, x, y, t, c, 0.35 if y > 6 else -0.45, 10)

    # Sub-waves of wave 5
    ax.plot([9, 12, 15], [8.0, 7.1, 10.17], '--', color=GREEN, lw=1.5, alpha=0.6)
    for x, y, t in [(9.5, 7.8, 'iii'), (11, 8.6, 'iv'), (13, 9.5, 'v')]:
        ax.text(x, y, t, fontsize=8, color=GREEN, fontstyle='italic')

    # Wave 5 extension projection
    ax.plot([22, 28, 34], [7.50, 12.57, 14.52], '--', color=PURPLE, lw=2)
    ax.annotate('', xy=(28, 12.57), xytext=(22, 7.50),
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2))
    box(ax, 28, 13.3, 'Extended Wave 5\n12.57 (0.618×3)\n14.52 (5=1)', PURPLE, 8)

    # Fib retracement of 5
    ax.axhspan(7.25, 7.72, alpha=0.08, color=YELLOW)
    ax.axhline(7.60, color=YELLOW, ls=':', alpha=0.6)
    ax.text(23, 7.65, 'Fib 50% = 7.60', fontsize=7, color=YELLOW)
    ax.axhline(7.00, color=YELLOW, ls=':', alpha=0.6)
    ax.text(23, 7.05, 'Fib 61.8% = 7.00', fontsize=7, color=YELLOW)

    box(ax, 4, 9.5, 'INTERMEDIATE COUNT\nWave 1: 5.0->6.2\nWave 2: 6.2->5.5 (flat)\nWave 3: 5.5->8.0 (strongest)\nWave 4: 8.0->7.1 (7.25 spring)\nWave 5: 7.1->10.17 (extended)\nNOW: Wave 4 of larger degree OR A of ABC', YELLOW, 7)

    ax.set_xlim(-1, 36)
    ax.set_ylim(4.5, 15.5)
    ax.set_title('Intermediate Elliott Waves — Jun 2026 Impulse\nWave count 1-2-3-4-5 + Current correction @ 7.50',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-موجات-02-Intermediate-1-2-3-4-5.png')


# ═══════════════════════════════════════════════════════════════════════
# 3. CURRENT WAVE 4 — ABC correction detail
# ═══════════════════════════════════════════════════════════════════════
def chart03_wave4_abc():
    fig, ax = plt.subplots(figsize=(14, 9))
    xs = [0, 4, 8, 12, 16, 20, 24]
    ys = [10.17, 8.60, 7.25, 8.60, 7.45, 7.72, 7.50]
    ax.plot(xs, ys, color=WHITE, lw=3)

    labels = [(0, 10.17, '5 top\n10.17', W5), (4, 8.60, 'a\n8.60', RED),
              (8, 7.25, 'b\n7.25\n(Spring)', GREEN), (12, 8.60, 'c\n8.60\n(Dead cat)', ORANGE),
              (16, 7.45, 'd?\n7.45', YELLOW), (20, 7.72, 'e?\n7.72\n(AVWAP)', RED),
              (24, 7.50, 'NOW\n7.50', BLUE)]
    for x, y, t, c in labels:
        wave_label(ax, x, y, t, c, 0.3 if y > 8 else -0.4, 9)

    # Flat pattern box
    box(ax, 12, 9.8, 'FLAT CORRECTION (A-B-C)\nA: 10.17->7.25 (-29%)\nB: 7.25->8.60 (+19%)\nC: 8.60->7.50 (-13%)\nC nearly complete if holds 7.25', YELLOW, 8)

    # Alternate: triangle in wave 4
    ax.plot([16, 20, 24], [7.45, 7.72, 7.50], '--', color=PURPLE, lw=1.5)
    box(ax, 20, 6.5, 'ALT: Ending diagonal / Triangle\nin Wave 4 — breakout pending', PURPLE, 7)

    ax.axhline(7.25, color=RED, lw=2)
    ax.text(25, 7.1, 'W4 invalid < 7.25', color=RED, fontsize=9, fontweight='bold')
    ax.axhline(8.14, color=GREEN, ls='--')
    ax.text(25, 8.25, 'W5 start > 8.14', color=GREEN, fontsize=9, fontweight='bold')

    ax.set_xlim(-1, 28)
    ax.set_ylim(6.5, 11)
    ax.set_title('Wave 4 Correction — ABC Flat + Ending Triangle\nCurrent position @ 7.50 before Wave 5',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-موجات-03-تصحيح-موجة-4-ABC.png')


# ═══════════════════════════════════════════════════════════════════════
# 4. WAVE 5 TARGETS — all Elliott projections
# ═══════════════════════════════════════════════════════════════════════
def chart04_wave5_targets():
    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    targets = [
        (9.2, '8.85', 'Elliott 5=1 (min)', 'Wave1 length from 7.25', GREEN),
        (8.8, '9.65', 'Hosoda NT', 'Ichimoku target', GREEN),
        (8.4, '10.17', 'Retest ATH', 'Previous peak', YELLOW),
        (8.0, '10.94', 'Murrey +1/8', '', GREEN),
        (7.6, '11.74', 'Elliott 5=0.618×3', 'Common extension', PURPLE),
        (7.2, '12.57', 'MAGNET', 'Elliott + Fib100% + Hosoda N + AB=CD', PURPLE),
        (6.8, '13.36', 'Flag target', 'Measured move', PURPLE),
        (6.4, '14.52', 'Elliott 5=3', 'Wave5 = Wave1×3', ORANGE),
        (6.0, '15.49', 'Hosoda E', 'Maximum Japanese target', ORANGE),
        (5.6, '17.89', 'Fib 200%', 'Extreme — low prob', RED),
    ]

    for y, price, name, desc, color in targets:
        ax.plot([1, 7], [y, y], color=color, alpha=0.4, lw=1.5)
        ax.add_patch(FancyBboxPatch((0.3, y - 0.18), 1.4, 0.36, boxstyle='round',
                                    facecolor=PANEL, edgecolor=color, lw=1.5))
        ax.text(1, y, price, ha='center', va='center', fontsize=9, fontweight='bold', color=color)
        ax.text(4, y + 0.05, name, ha='center', va='center', fontsize=9, fontweight='bold', color=WHITE)
        ax.text(8.5, y, desc, ha='left', va='center', fontsize=7, color=GRAY)

    ax.scatter([4], [7.2], s=350, c=WHITE, edgecolors=PURPLE, lw=3, zorder=10)
    box(ax, 4, 6.5, 'PRIMARY W5 TARGET\n12.57 EGP\n3 tools converge', PURPLE, 9)

    ax.scatter([4], [9.2], s=200, c=WHITE, edgecolors=BLUE, lw=2, zorder=10)
    box(ax, 4, 8.5, 'NOW 7.50\nWave 4 completing', BLUE, 8)

    ax.set_title('EAC — Elliott Wave 5 Targets (All Projections)\nFrom correction low 7.25 · Base 7.50',
                 fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-موجات-04-اهداف-موجة-5.png')


# ═══════════════════════════════════════════════════════════════════════
# 5. MULTI-TIMEFRAME
# ═══════════════════════════════════════════════════════════════════════
def chart05_multitimeframe():
    fig, axes = plt.subplots(3, 1, figsize=(16, 14))
    fig.suptitle('EAC — Elliott Wave Multi-Timeframe Count', fontsize=14, fontweight='bold', y=1.01)

    # Monthly
    ax = axes[0]
    mx = [0, 2, 4, 6, 8, 10, 12]
    my = [0.8, 2.5, 1.9, 5.0, 3.0, 10.17, 7.50]
    ax.plot(mx, my, 'o-', color=BLUE, lw=2.5, ms=8)
    for x, y, t, c in [(2, 2.5, 'I', W1), (4, 1.9, 'II/IV', W4), (6, 5.0, 'Base', YELLOW),
                       (10, 10.17, 'V', W5), (12, 7.50, '4?', W4)]:
        wave_label(ax, x, y, t, c, 0.3, 11)
    ax.set_title('MONTHLY — Primary Degree', fontweight='bold', fontsize=11)
    ax.set_ylabel('EGP')
    ax.grid(True, alpha=0.2)
    ax.set_ylim(0, 12)

    # Weekly
    ax = axes[1]
    wx = [0, 2, 4, 6, 8, 10, 12, 14]
    wy = [3.0, 5.0, 4.8, 7.0, 5.0, 10.17, 7.25, 7.50]
    ax.plot(wx, wy, 'o-', color=GREEN, lw=2.5, ms=8)
    for x, y, t, c in [(2, 5.0, '1', W1), (4, 4.8, '2', W2), (6, 7.0, '3', W3),
                       (8, 5.0, '4', W4), (10, 10.17, '5', W5), (12, 7.25, 'A', RED),
                       (14, 7.50, 'B?', YELLOW)]:
        wave_label(ax, x, y, t, c, 0.25, 10)
    ax.set_title('WEEKLY — Intermediate Degree', fontweight='bold', fontsize=11)
    ax.set_ylabel('EGP')
    ax.grid(True, alpha=0.2)

    # Daily (Jun-Jul)
    ax = axes[2]
    dx = np.arange(0, 20)
    dy = [5.0, 5.5, 6.5, 7.5, 8.5, 9.5, 10.17, 9.0, 8.0, 7.25, 8.6, 8.0, 7.8, 7.6, 7.5, 7.48, 7.50, 7.50, 7.50, 7.50]
    ax.plot(dx, dy, color=ORANGE, lw=2.5)
    for x, y, t, c in [(2, 5.5, 'i', W1), (5, 8.5, 'iii', W3), (6, 10.17, 'v', W5),
                       (9, 7.25, 'a', RED), (10, 8.6, 'b', YELLOW), (19, 7.50, 'c?', BLUE)]:
        wave_label(ax, x, y, t, c, 0.2 if y > 7.8 else -0.35, 9)
    ax.axhline(8.14, color=GREEN, ls='--', alpha=0.7)
    ax.axhline(7.25, color=RED, ls=':', lw=2)
    ax.set_title('DAILY — Minor Degree (Jun-Jul 2026)', fontweight='bold', fontsize=11)
    ax.set_xlabel('Sessions')
    ax.set_ylabel('EGP')
    ax.grid(True, alpha=0.2)

    save(fig, 'EAC-موجات-05-متعدد-الفريمات.png')


# ═══════════════════════════════════════════════════════════════════════
# 6. FIBONACCI + ELLIOTT
# ═══════════════════════════════════════════════════════════════════════
def chart06_fib_elliott():
    fig, ax = plt.subplots(figsize=(14, 10))
    low, high, now = 5.0, 10.17, 7.50

    ax.axhspan(low, high, alpha=0.06, color=BLUE)
    ax.axhline(high, color=RED, lw=2, label=f'Wave 5 top {high}')
    ax.axhline(low, color=GREEN, lw=2, label=f'Wave 1/Start {low}')

    fibs = [
        (0.236, 8.95, '23.6%'), (0.382, 8.20, '38.2%'), (0.500, 7.60, '50%'),
        (0.618, 7.00, '61.8%'), (0.786, 6.10, '78.6%'),
    ]
    for pct, price, lbl in fibs:
        c = YELLOW if abs(price - now) < 0.15 else GRAY
        ax.axhline(price, color=c, ls='--', alpha=0.7, lw=1.5 if c == YELLOW else 1)
        ax.text(0.5, price + 0.08, f'{lbl} = {price:.2f}', fontsize=8, color=c)

    ax.scatter([1], [now], s=350, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    box(ax, 0.5, 7.15, 'NOW 7.50\nBetween Fib 50% (7.60)\nand prior support zone\n= Wave 4 typical zone', BLUE, 8)

    # Extensions for wave 5
    ext = [(1.0, 8.85, '5=1'), (1.618, 11.74, '5=1.618×3'), (2.618, 14.52, '5=3')]
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    for i, (mult, tgt, lbl) in enumerate(ext):
        ax.annotate('', xy=(1.5 + i * 0.3, tgt), xytext=(1, now),
                    arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5))
        ax.text(1.55 + i * 0.3, tgt + 0.2, f'{lbl}\n{tgt}', fontsize=8, color=PURPLE, fontweight='bold')

    ax.set_xlim(0, 2)
    ax.set_ylim(5.5, 15.5)
    ax.set_title('Elliott + Fibonacci — Wave 4 Retracement & Wave 5 Extensions\nImpulse 5.0 -> 10.17 · Now 7.50',
                 fontsize=13, fontweight='bold', pad=12)
    ax.legend(loc='upper left', facecolor=PANEL, fontsize=8)
    ax.grid(True, alpha=0.2)
    save(fig, 'EAC-موجات-06-فibo-وإليوت.png')


# ═══════════════════════════════════════════════════════════════════════
# 7. BULLISH vs BEARISH alternate counts
# ═══════════════════════════════════════════════════════════════════════
def chart07_alternates():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(17, 8))
    fig.suptitle('EAC — Elliott Alternate Wave Counts @ 7.50', fontsize=14, fontweight='bold')

    # Bullish (primary)
    bx = [0, 2, 4, 6, 8, 10, 14, 18]
    by = [5.0, 6.2, 5.5, 8.0, 7.1, 10.17, 7.50, 12.57]
    a1.plot(bx, by, 'o-', color=GREEN, lw=2.5, ms=8)
    for x, y, t in [(0, 5.0, '1'), (2, 6.2, '2'), (4, 5.5, '2'), (6, 8.0, '3'),
                    (8, 7.1, '4'), (10, 10.17, '5'), (12, 7.50, '4'), (16, 12.57, '5')]:
        wave_label(a1, x, y, t, GREEN if y > 8 else YELLOW, 0.25, 10)
    box(a1, 8, 13.5, 'PRIMARY (60%)\nWave 4 completing\nWave 5 -> 12.57-14.52\nTrigger: break 8.14\nInvalid: close < 7.25', GREEN, 8)
    a1.set_title('BULLISH — Wave 4 done, Wave 5 next', fontweight='bold', color=GREEN)
    a1.set_ylim(4, 15)
    a1.grid(True, alpha=0.2)

    # Bearish alternate
    bx2 = [0, 2, 4, 6, 8, 10, 14, 18]
    by2 = [5.0, 8.0, 7.0, 10.17, 8.6, 7.50, 6.88, 5.20]
    a2.plot(bx2, by2, 'o-', color=RED, lw=2.5, ms=8)
    for x, y, t in [(0, 5.0, '1'), (4, 7.0, '2'), (6, 10.17, '3'), (8, 8.6, '4'),
                    (10, 7.50, '5?'), (12, 6.88, 'A'), (16, 5.20, 'B')]:
        wave_label(a2, x, y, t, RED, 0.25, 10)
    box(a2, 8, 4.5, 'BEARISH ALT (40%)\n5=top at 10.17 (extended)\nABC correction underway\nTarget 5.20 (2024 repeat)\nTrigger: close < 7.25', RED, 8)
    a2.set_title('BEARISH — 5 complete, ABC down', fontweight='bold', color=RED)
    a2.set_ylim(4, 12)
    a2.grid(True, alpha=0.2)

    save(fig, 'EAC-موجات-07-بديل-صعود-وهبوط.png')


# ═══════════════════════════════════════════════════════════════════════
# 8. FULL ROADMAP wave by wave
# ═══════════════════════════════════════════════════════════════════════
def chart08_roadmap():
    fig, ax = plt.subplots(figsize=(18, 8))
    stages = [
        ('DONE', 'W1-W2-W3', '5.0->8.0', 'Jun 11-24', GREEN),
        ('DONE', 'W5 climax', '8.0->10.17', 'Jun 17-19', ORANGE),
        ('NOW', 'W4 ABC', '10.17->7.50', 'Jun 20-Jul 5', BLUE),
        ('NEXT', 'W5 start', 'Break 8.14', 'Jul 6+ AGM', YELLOW),
        ('TARGET', 'W5 mid', '10.17 retest', '+2-4 weeks', PURPLE),
        ('TARGET', 'W5 magnet', '12.57', 'Primary', PURPLE),
        ('TARGET', 'W5 ext', '14.52', 'Extended', ORANGE),
        ('CEILING', 'W5 max', '15.49 Hosoda E', 'Distribution', RED),
    ]
    for i, (status, name, move, time, color) in enumerate(stages):
        x = i * 2.2
        ax.add_patch(FancyBboxPatch((x - 0.9, 2), 1.8, 5, boxstyle='round,pad=0.08',
                                    facecolor=PANEL, edgecolor=color, linewidth=2.5))
        ax.text(x, 6.2, status, ha='center', fontsize=10, fontweight='bold', color=color)
        ax.text(x, 5.2, name, ha='center', fontsize=9, fontweight='bold', color=WHITE)
        ax.text(x, 4.2, move, ha='center', fontsize=8, color=GRAY)
        ax.text(x, 3.2, time, ha='center', fontsize=7, color=GRAY)
        if i < len(stages) - 1:
            ax.annotate('', xy=(x + 1.3, 4.5), xytext=(x + 0.9, 4.5),
                        arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

    ax.scatter([4.4], [1.2], s=200, c=WHITE, edgecolors=BLUE, lw=2)
    ax.text(4.4, 0.6, 'YOU @ 7.50', ha='center', fontsize=10, color=BLUE, fontweight='bold')
    ax.set_xlim(-1, 17)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    ax.set_title('EAC — Elliott Wave Roadmap: Past → Now → Future\n128,400 @ 7.75 · AGM Jul 6',
                 fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-موجات-08-خريطة-طريق.png')


if __name__ == '__main__':
    print('Generating 8 Elliott Wave charts...')
    chart01_master()
    chart02_intermediate()
    chart03_wave4_abc()
    chart04_wave5_targets()
    chart05_multitimeframe()
    chart06_fib_elliott()
    chart07_alternates()
    chart08_roadmap()
    print('Done — 8 wave charts.')

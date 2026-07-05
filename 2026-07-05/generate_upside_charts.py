#!/usr/bin/env python3
"""EAC upside target charts — how high can we go."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
BG, PANEL = '#0a0e14', '#121820'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9'

ENTRY, NOW, SHARES = 7.75, 7.50, 128400

plt.rcParams.update({'figure.facecolor': BG, 'axes.facecolor': PANEL, 'text.color': WHITE})

TARGETS = [
    (7.50, 'NOW', 100, GRAY, ''),
    (7.75, 'Entry', 100, ORANGE, 'Breakeven'),
    (8.14, 'Gate / Pivot', 45, YELLOW, 'Minervini · SMC · Breakout'),
    (8.75, 'Cluster 0', 42, GREEN, 'DeMark TD · First station'),
    (8.85, 'Elliott W5 min', 40, GREEN, 'Wave5 = Wave1'),
    (9.65, 'Hosoda NT', 35, GREEN, 'Ichimoku target'),
    (10.17, 'ATH Retest', 35, GREEN, 'Previous peak · O\'Neil'),
    (10.94, 'Murrey +1/8', 30, GREEN, 'Murrey Math'),
    (11.74, 'Elliott ext', 28, PURPLE, '5 = 0.618 x 3'),
    (12.57, 'MAGNET', 30, PURPLE, 'Hosoda N + Fib100% + AB=CD'),
    (13.36, 'Flag target', 22, PURPLE, 'Bull Flag measured move'),
    (14.52, 'Elliott 5=3', 18, ORANGE, 'Wave5 = 3 x Wave1'),
    (15.49, 'Hosoda E', 12, ORANGE, 'Max Japanese target'),
    (15.86, 'Fib 161.8%', 10, ORANGE, 'Fib extension'),
    (17.89, 'Extreme', 5, RED, 'Fib 200% · Low prob'),
]

CLUSTERS = [
    (7.25, 8.95, 'Station 0\nBreakout zone', YELLOW, 2),
    (10.9, 11.9, 'Cluster 1\nFirst profit zone', GREEN, 5),
    (12.5, 13.2, 'Cluster 2\nMAGNET zone', PURPLE, 6),
    (13.4, 14.5, 'Cluster 3\nExtension', ORANGE, 5),
    (15.0, 15.9, 'CEILING\nMax realistic', RED, 4),
]


def save(fig, name):
    fig.savefig(OUT / name, dpi=DPI, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  OK: {name}')


def pnl(price):
    return SHARES * (price - ENTRY)


def gain_pct(price):
    return (price - ENTRY) / ENTRY * 100


def box(ax, x, y, txt, color, fs=8):
    ax.text(x, y, txt, ha='center', va='center', fontsize=fs, color=WHITE, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=PANEL, edgecolor=color, lw=1.5))


# ═══════════════════════════════════════════════════════════════════════
# 1. MAIN UPSIDE LADDER — price + P&L + probability
# ═══════════════════════════════════════════════════════════════════════
def chart01_ladder():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 12), gridspec_kw={'width_ratios': [1.2, 1]})
    fig.suptitle(f'EAC — How High Can We Go? | 128,400 shares @ {ENTRY} EGP | Now {NOW}',
                 fontsize=14, fontweight='bold', y=0.98)

    prices = [t[0] for t in TARGETS]
    y_pos = np.arange(len(TARGETS))

    for i, (price, name, prob, color, tool) in enumerate(TARGETS):
        g = gain_pct(price)
        p = pnl(price)
        ax1.barh(i, g, color=color, alpha=0.7, height=0.7)
        ax1.text(-2, i, f'{price:.2f}', ha='right', va='center', fontsize=9, fontweight='bold', color=color)
        ax1.text(g / 2, i, f'+{g:.0f}%', ha='center', va='center', fontsize=8, color=WHITE, fontweight='bold')
        if p > 0:
            ax1.text(g + 3, i, f'+{p/1000:.0f}K EGP', ha='left', va='center', fontsize=7, color=GRAY)
        ax1.text(-18, i, name, ha='left', va='center', fontsize=8, color=WHITE)

    ax1.axvline(0, color=WHITE, lw=1)
    ax1.set_yticks([])
    ax1.set_xlabel('Gain % from entry 7.75', fontsize=10)
    ax1.set_title('Upside Ladder — Every Target', fontweight='bold', fontsize=11)
    ax1.set_xlim(-20, 145)
    ax1.grid(True, axis='x', alpha=0.2)

    # Probability column
    probs = [t[2] for t in TARGETS[2:]]  # skip NOW and entry
    names_p = [t[1] for t in TARGETS[2:]]
    colors_p = [t[3] for t in TARGETS[2:]]
    y_p = np.arange(len(probs))
    ax2.barh(y_p, probs, color=colors_p, alpha=0.7, height=0.7)
    for i, (prob, name) in enumerate(zip(probs, names_p)):
        ax2.text(prob + 1, i, f'{prob}%', va='center', fontsize=8, color=WHITE)
        ax2.text(-2, i, name, ha='left', va='center', fontsize=7, color=GRAY)
    ax2.set_xlabel('Probability %', fontsize=10)
    ax2.set_title('Reach Probability', fontweight='bold', fontsize=11)
    ax2.set_xlim(0, 55)
    ax2.set_yticks([])
    ax2.invert_yaxis()
    ax2.grid(True, axis='x', alpha=0.2)

    save(fig, 'EAC-صعود-01-سلm-الاهداف-والارباح.png')


# ═══════════════════════════════════════════════════════════════════════
# 2. CLUSTER MAP — target zones visual
# ═══════════════════════════════════════════════════════════════════════
def chart02_clusters():
    fig, ax = plt.subplots(figsize=(14, 14))

    for y1, y2, label, color, count in CLUSTERS:
        ax.axhspan(y1, y2, alpha=0.25, color=color)
        mid = (y1 + y2) / 2
        ax.text(0.5, mid, f'{label}\n{count} tools converge\n{y1:.2f} - {y2:.2f}',
                ha='center', va='center', fontsize=9, fontweight='bold', color=WHITE,
                bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=color, alpha=0.9))

    # Key lines
    lines = [
        (NOW, 'NOW 7.50', BLUE, '-'),
        (ENTRY, 'ENTRY 7.75', ORANGE, '--'),
        (8.14, 'GATE 8.14', YELLOW, '-'),
        (10.17, 'ATH 10.17', GREEN, ':'),
        (12.57, 'MAGNET 12.57', PURPLE, '-'),
        (15.49, 'CEILING 15.49', RED, '-'),
        (7.25, 'DEATH 7.25', RED, ':'),
    ]
    for y, lbl, c, ls in lines:
        ax.axhline(y, color=c, ls=ls, lw=2 if y in (NOW, 12.57, 15.49) else 1.5)
        ax.text(0.92, y + 0.08, lbl, fontsize=8, color=c, fontweight='bold')

    ax.scatter([0.5], [NOW], s=400, c=WHITE, edgecolors=BLUE, lw=3, zorder=10)
    ax.annotate('YOU\n128,400 shares', xy=(0.5, NOW), xytext=(0.75, 6.5),
                arrowprops=dict(arrowstyle='->', color=BLUE), fontsize=10, color=WHITE, fontweight='bold')

    # Arrow path up
    path_y = [7.50, 8.14, 8.90, 10.17, 11.50, 12.57, 13.80, 14.52, 15.49]
    path_x = np.linspace(0.15, 0.85, len(path_y))
    ax.plot(path_x, path_y, '--', color=GREEN, lw=2, alpha=0.6)
    ax.annotate('', xy=(0.85, 15.49), xytext=(0.15, 7.50),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2, alpha=0.5))

    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(6.8, 16.5)
    ax.set_ylabel('Price (EGP)', fontsize=11)
    ax.set_title('Target Clusters — Where Tools Converge\nRoad: 8.14 → 10.17 → 12.57 → 15.49',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xticks([])
    ax.grid(True, axis='y', alpha=0.2)
    save(fig, 'EAC-صعود-02-عناقيد-الاهداف.png')


# ═══════════════════════════════════════════════════════════════════════
# 3. P&L TABLE — money on your position
# ═══════════════════════════════════════════════════════════════════════
def chart03_pnl():
    fig, ax = plt.subplots(figsize=(16, 10))
    key_targets = [
        (8.14, 'Gate', 45), (8.85, 'Elliott min', 40), (9.65, 'Hosoda NT', 35),
        (10.17, 'ATH', 35), (11.74, 'Elliott ext', 28), (12.57, 'MAGNET', 30),
        (13.36, 'Flag', 22), (14.52, 'Elliott 5=3', 18), (15.49, 'Ceiling', 12),
    ]
    prices = [t[0] for t in key_targets]
    pnls = [pnl(p) / 1000 for p in prices]  # in K
    probs = [t[2] for t in key_targets]
    names = [t[1] for t in key_targets]
    colors = [GREEN if p < 300 else PURPLE if p < 700 else ORANGE for p in pnls]

    bars = ax.bar(range(len(prices)), pnls, color=colors, alpha=0.8, edgecolor=WHITE, lw=1)
    ax2 = ax.twinx()
    ax2.plot(range(len(prices)), probs, 'o--', color=YELLOW, lw=2, ms=10, label='Probability %')
    ax2.set_ylabel('Probability %', color=YELLOW, fontsize=10)
    ax2.set_ylim(0, 55)

    for i, (price, name, prob) in enumerate(key_targets):
        g = gain_pct(price)
        ax.text(i, pnls[i] + 20, f'{price:.2f}\n+{g:.0f}%\n+{pnls[i]:.0f}K', ha='center', fontsize=8,
                color=WHITE, fontweight='bold')
        ax.text(i, -80, name, ha='center', fontsize=9, color=GRAY, rotation=0)

    ax.axhline(0, color=WHITE, lw=1)
    ax.set_xticks(range(len(prices)))
    ax.set_xticklabels([f'{p:.2f}' for p in prices], fontsize=9)
    ax.set_ylabel('Profit (K EGP) on 128,400 shares', fontsize=10)
    ax.set_xlabel('Target Price (EGP)', fontsize=10)
    ax.set_title(f'Your Profit at Each Target | Entry {ENTRY} | Cost {SHARES*ENTRY/1e6:.2f}M EGP',
                 fontsize=13, fontweight='bold', pad=12)
    ax.set_ylim(-100, 1100)
    ax.grid(True, axis='y', alpha=0.2)
    ax2.legend(loc='upper left', facecolor=PANEL)
    save(fig, 'EAC-صعود-03-ارباحك-بالجنيه.png')


# ═══════════════════════════════════════════════════════════════════════
# 4. ROADMAP stations
# ═══════════════════════════════════════════════════════════════════════
def chart04_roadmap():
    fig, ax = plt.subplots(figsize=(18, 7))
    stations = [
        ('NOW', '7.50', 'Here', BLUE, '-32K'),
        ('S1', '8.14', 'Gate\nBreakout', YELLOW, '+50K'),
        ('S2', '8.90', 'Cluster 0\nPartial?', YELLOW, '+149K'),
        ('S3', '10.17', 'ATH\nSell 1/3?', GREEN, '+311K'),
        ('S4', '11.50', 'Cluster 1\nHold rest', GREEN, '+480K'),
        ('S5', '12.57', 'MAGNET\nMain target', PURPLE, '+619K'),
        ('S6', '14.52', 'Extended\nSell more', ORANGE, '+869K'),
        ('S7', '15.49', 'CEILING\nExit all', RED, '+994K'),
    ]
    for i, (code, price, label, color, profit) in enumerate(stations):
        x = i * 2.3
        ax.add_patch(FancyBboxPatch((x - 0.85, 1.5), 1.7, 4.5, boxstyle='round,pad=0.08',
                                    facecolor=PANEL, edgecolor=color, linewidth=2.5))
        ax.text(x, 5.3, code, ha='center', fontsize=11, fontweight='bold', color=color)
        ax.text(x, 4.5, price, ha='center', fontsize=14, fontweight='bold', color=WHITE)
        ax.text(x, 3.5, label, ha='center', fontsize=8, color=GRAY, linespacing=1.3)
        ax.text(x, 2.2, profit, ha='center', fontsize=10, fontweight='bold',
                color=GREEN if '+' in profit and profit != '+50K' else (YELLOW if '+' in profit else RED))
        if i < len(stations) - 1:
            ax.annotate('', xy=(x + 1.45, 3.8), xytext=(x + 0.85, 3.8),
                        arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

    # Y scale on left
    ax2 = ax.twinx()
    ax2.set_ylim(6, 17)
    ax2.set_ylabel('Price (EGP)', fontsize=10)
    for _, price, _, color, _ in stations:
        ax2.axhline(float(price), color=color, alpha=0.15, lw=3)

    ax.set_xlim(-1, 17)
    ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('Upside Roadmap — Station by Station | What You Earn at Each Stop',
                 fontsize=13, fontweight='bold', pad=15)
    save(fig, 'EAC-صعود-04-خريطة-طريق-المحطات.png')


# ═══════════════════════════════════════════════════════════════════════
# 5. MAX SUMMARY — 3 tiers
# ═══════════════════════════════════════════════════════════════════════
def chart05_summary():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis('off')

    tiers = [
        ('CONSERVATIVE\n(45% prob)', '8.14 — 10.17', '+5% to +31%', '+50K to +311K',
         'Gate break → ATH retest\nSell 1/3 at 8.6-9.0', YELLOW),
        ('REALISTIC\n(30% prob)', '12.57 MAGNET', '+62%', '+619K',
         '3 tools converge\nMain Wave 5 target\nStrongest magnet above ATH', PURPLE),
        ('MAXIMUM\n(12% prob)', '15.0 — 15.9', '+100%', '+994K',
         'Hosoda E · Fib 161.8 · Gann\nDistribution zone\nSELL not hold', ORANGE),
        ('EXTREME\n(5% prob)', '17.5 — 20.6', '+130%+', '+1.3M+',
         'Theoretical only\nDo NOT plan for this', RED),
    ]

    for i, (title, range_p, gain, money, desc, color) in enumerate(tiers):
        y = 8.5 - i * 2.1
        ax.add_patch(FancyBboxPatch((0.5, y - 0.85), 13, 1.7, boxstyle='round,pad=0.1',
                                    facecolor=PANEL, edgecolor=color, linewidth=2.5))
        ax.text(1.5, y, title, ha='center', va='center', fontsize=10, fontweight='bold', color=color)
        ax.text(4.5, y + 0.25, range_p, ha='center', va='center', fontsize=11, fontweight='bold', color=WHITE)
        ax.text(4.5, y - 0.35, gain, ha='center', va='center', fontsize=10, color=GREEN)
        ax.text(7, y + 0.25, money, ha='center', va='center', fontsize=11, fontweight='bold', color=GREEN)
        ax.text(7, y - 0.35, 'on 128,400 shares', ha='center', va='center', fontsize=8, color=GRAY)
        ax.text(10.5, y, desc, ha='center', va='center', fontsize=8, color=GRAY, linespacing=1.4)

    ax.text(7, 0.5, f'Entry: {ENTRY} | Now: {NOW} | After free shares 1:4: entry becomes 6.20 | All targets x0.8',
            ha='center', fontsize=9, color=YELLOW, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=PANEL, edgecolor=YELLOW))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9.5)
    ax.set_title('EAC — How High? Summary: 4 Tiers of Upside\n128,400 @ 7.75 EGP',
                 fontsize=14, fontweight='bold', pad=15)
    save(fig, 'EAC-صعود-05-ملخص-4-مستويات.png')


# ═══════════════════════════════════════════════════════════════════════
# 6. AFTER FREE SHARES — adjusted targets
# ═══════════════════════════════════════════════════════════════════════
def chart06_after_bonus():
    fig, ax = plt.subplots(figsize=(14, 10))
    mult = 0.8
    new_shares = int(SHARES * 1.25)  # 1:4 bonus
    new_entry = ENTRY * mult

    targets_adj = [
        (8.14 * mult, 'Gate 6.51'),
        (10.17 * mult, 'ATH 8.14'),
        (12.57 * mult, 'Magnet 10.06'),
        (14.52 * mult, 'Ext 11.62'),
        (15.49 * mult, 'Ceiling 12.39'),
    ]

    x = np.arange(len(targets_adj))
    orig = [t[0] / mult for t in targets_adj]
    adj = [t[0] for t in targets_adj]
    labels = [t[1] for t in targets_adj]

    w = 0.35
    ax.bar(x - w/2, orig, w, label='Before bonus (price)', color=BLUE, alpha=0.7)
    ax.bar(x + w/2, adj, w, label='After bonus x0.8 (price)', color=PURPLE, alpha=0.7)

    for i, (o, a, lbl) in enumerate(zip(orig, adj, labels)):
        ax.text(i - w/2, o + 0.2, f'{o:.2f}', ha='center', fontsize=8, color=BLUE)
        ax.text(i + w/2, a + 0.2, f'{a:.2f}', ha='center', fontsize=8, color=PURPLE)
        pnl_adj = new_shares * (a - new_entry)
        ax.text(i, -1.5, f'{lbl}\nP&L: +{pnl_adj/1000:.0f}K', ha='center', fontsize=8, color=GRAY)

    ax.set_xticks(x)
    ax.set_xticklabels(['Gate', 'ATH', 'Magnet', 'Extended', 'Ceiling'], fontsize=10)
    ax.set_ylabel('Price (EGP)', fontsize=10)
    ax.legend(facecolor=PANEL)
    box(ax, 0.5, 14, f'After 1:4 bonus:\nShares: {SHARES:,} -> {new_shares:,}\nEntry: {ENTRY} -> {new_entry:.2f}',
        GREEN, 9)
    ax.set_title('Targets After Free Shares 1:4 (x0.8 adjustment)\n160,500 shares @ 6.20 effective entry',
                 fontsize=12, fontweight='bold', pad=12)
    ax.set_ylim(0, 16)
    ax.grid(True, axis='y', alpha=0.2)
    save(fig, 'EAC-صعود-06-بعد-المجانية.png')


if __name__ == '__main__':
    print('Generating 6 upside target charts...')
    chart01_ladder()
    chart02_clusters()
    chart03_pnl()
    chart04_roadmap()
    chart05_summary()
    chart06_after_bonus()
    print('Done — 6 upside charts.')

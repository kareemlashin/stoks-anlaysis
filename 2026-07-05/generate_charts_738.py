#!/usr/bin/env python3
"""EAC @ 7.38 — Professional indicators + strategies charts (Jul 5 2026)."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Wedge
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
DPI = 180
NOW = 7.38
ENTRY = 7.75
SHARES = 128_400
BG, PANEL, GRID = '#0a0e14', '#121820', '#1c2330'
GREEN, RED, YELLOW = '#22c55e', '#ef4444', '#eab308'
BLUE, PURPLE, ORANGE, GRAY, WHITE, CYAN = '#3b82f6', '#a855f7', '#f97316', '#94a3b8', '#f1f5f9', '#06b6d4'

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


def lbl(ax, x, y, text, color, fs=8):
    ax.text(x, y, text, ha='center', va='center', fontsize=fs, color=WHITE,
            fontweight='bold', zorder=20,
            bbox=dict(boxstyle='round,pad=0.35', facecolor=PANEL, edgecolor=color, linewidth=1.5))


def hline(ax, y, label, color, ls='--', lw=1.5):
    ax.axhline(y, color=color, ls=ls, lw=lw, alpha=0.9)
    ax.text(1.01, y, label, transform=ax.get_yaxis_transform(), fontsize=7,
            color=color, va='center', fontweight='bold')


# ── 1. SMC + Levels @ 7.38 ─────────────────────────────────────────
def chart_smc_levels():
    fig, ax = plt.subplots(figsize=(16, 10))
    t = np.linspace(0, 55, 220)
    p = np.piecewise(t,
        [t < 8, (t >= 8) & (t < 18), (t >= 18) & (t < 28), (t >= 28) & (t < 38), t >= 38],
        [lambda x: 4.85 + 0.02 * x,
         lambda x: 5.0 + (x - 8) * 0.52,
         lambda x: 10.17 - (x - 18) * 0.28,
         lambda x: 8.0 - (x - 28) * 0.06,
         lambda x: 7.38 + 0.04 * np.sin((x - 38) * 0.5)])
    ax.plot(t, p, color=BLUE, lw=2.5, zorder=5)
    ax.scatter([52], [NOW], s=200, c=YELLOW, zorder=10, edgecolors=WHITE, linewidths=2)
    lbl(ax, 52, NOW + 0.35, f'NOW {NOW}', YELLOW, 10)

    zones = [
        (4.84, 5.25, GREEN, 'Order Block\n(Buy) 4.84-5.25'),
        (6.90, 7.33, PURPLE, 'FVG\n6.90-7.33'),
        (7.25, 7.45, ORANGE, 'Breaker\n7.25-7.45'),
        (7.35, 7.72, RED, 'Spring Zone\nL=7.35 sweep'),
    ]
    for y0, y1, c, txt in zones:
        ax.axhspan(y0, y1, alpha=0.12, color=c)
    hline(ax, 7.25, 'DEATH 7.25', RED, lw=2.5)
    hline(ax, 7.50, 'POC 7.50 (broken)', GRAY)
    hline(ax, 7.72, 'AVWAP 7.72', CYAN)
    hline(ax, 8.11, 'Gate/BOS 8.11', YELLOW)
    hline(ax, 8.43, 'IBD 8.43', GREEN)
    hline(ax, 10.17, 'ATH 10.17', ORANGE)
    lbl(ax, 8, 4.5, zones[0][3], GREEN, 7)
    lbl(ax, 25, 7.1, zones[1][3], PURPLE, 7)
    lbl(ax, 45, 7.55, zones[3][3], RED, 8)
    ax.set_ylim(4.0, 11.0)
    ax.set_xlabel('Sessions (approx May–Jul 2026)')
    ax.set_ylabel('Price (EGP)')
    ax.set_title('EAC SMC Map @ 7.38 — Liquidity · FVG · Spring Zone · AGM Tomorrow',
                 fontsize=13, fontweight='bold', pad=12)
    ax.grid(True, alpha=0.25)
    save(fig, 'EAC-738-01-خريطة-SMC-ومستويات.png')


# ── 2. 100 Tools Dashboard ───────────────────────────────────────────
def chart_100_tools():
    fig, axes = plt.subplots(2, 4, figsize=(18, 10))
    fig.suptitle('EAC @ 7.38 — 100 Professional Tools Dashboard\n40🟢 / 44🟡 / 16🔴 → Score +0.24',
                 fontsize=14, fontweight='bold', y=0.98)

    groups = [
        ('Momentum (20)', [11, 6, 3], ['StochRSI extreme🟢', 'MACD 🔴', 'RSI 🟡']),
        ('Trend (15)', [9, 3, 3], ['ADX=50 🟢🟢', 'SuperTrend 🔴', 'Ichimoku 🔴']),
        ('Volume (15)', [8, 4, 3], ['NVI/OBV 🟢', 'A/D 🔴', 'POC broken 🔴']),
        ('Volatility (10)', [3, 6, 1], ['TTM hr ON 🟢', 'Chandelier 🔴', 'ATR high 🟡']),
        ('SMC/ICT (10)', [5, 4, 1], ['FVG hold 🟢', 'Discount zone 🔴', 'Sweep 🟡']),
        ('Waves/Fibo (12)', [7, 4, 1], ['Elliott W4 🟢', 'Gann 7.23 🟢', 'Fib50 broken 🔴']),
        ('Systems (12)', [5, 5, 2], ['VCP 🟢', 'Wyckoff 🟡', 'CANSLIM M 🔴']),
        ('Profile (6)', [4, 1, 1], ['DeMark Buy 🟢', 'POC 🔴', 'LuxAlgo 🟡']),
    ]
    colors_bar = [GREEN, YELLOW, RED]
    for ax, (name, counts, notes) in zip(axes.flat, groups):
        bars = ax.bar(['🟢', '🟡', '🔴'], counts, color=colors_bar, edgecolor=WHITE, linewidth=0.5)
        for b, v in zip(bars, counts):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.3, str(v), ha='center', fontweight='bold', fontsize=11)
        ax.set_ylim(0, 14)
        ax.set_title(name, fontweight='bold', fontsize=10)
        ax.grid(axis='y', alpha=0.2)
        note = '\n'.join(notes)
        ax.text(0.5, -0.22, note, transform=ax.transAxes, ha='center', fontsize=7, color=GRAY)

    fig.text(0.5, 0.02, 'Trigger: Spring 7.25-7.35 reclaim OR Break 8.11-8.43 + vol | Cancel: close < 6.90',
             ha='center', fontsize=10, color=YELLOW)
    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    save(fig, 'EAC-738-02-لوحة-100-اداة.png')


# ── 3. 15 Professionals Matrix ───────────────────────────────────────
def chart_15_pros():
    fig, ax = plt.subplots(figsize=(16, 11))
    ax.axis('off')
    pros = [
        ('Minervini', 'HOLD', 'Stop 7.25 · No add before 8.11', GREEN),
        ('Qullamaggie', 'HOLD', 'In flag · Sell 43K @ 8.6-9.0 after break', GREEN),
        ('Wyckoff', 'HOLD+', 'Spring zone L=7.35 · 3/5 re-accum', YELLOW),
        ('Shannon AVWAP', 'WAIT', 'Decision at 7.72 & 8.13 not 7.38', YELLOW),
        ('Livermore', 'NO TRADE', 'No moves inside range', GRAY),
        ("O'Neil CANSLIM", 'CAUTION', 'M 🔴 · Climax sell @ 10.17', ORANGE),
        ('Weinstein', 'HOLD', 'Stage 2 pullback · not Stage 3', GREEN),
        ('Darvas', 'HOLD', 'Box 7.25-8.33 · near floor', GREEN),
        ('Al Brooks', 'NEUTRAL', 'Bear bar + bounce · Range 7.25-8.04', YELLOW),
        ('Raschke', 'WATCH', 'Turtle Soup @ 7.25 · 1st 30min AGM', YELLOW),
        ('Brandt', 'HOLD', 'Flag valid · Fail = 7.25', GREEN),
        ('Connors RSI-2', 'NEAR', 'RSI-2 ~35 · trigger near 7.25', YELLOW),
        ('Williams %R', 'NEAR', '%R -75 oversold zone', YELLOW),
        ('Mark Douglas', 'HOLD PLAN', '13 pts above stop ≠ sell fear', GREEN),
        ('Elliott/Gann', 'HOLD', 'W4 @ 7.39 · Target 11.7-12.57', GREEN),
    ]
    y = 0.95
    ax.text(0.5, 0.99, '15 Professionals @ EAC 7.38 — 128,400 @ 7.75 · AGM Tomorrow',
            ha='center', fontsize=14, fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.965, '0 say MARKET SELL · All: hold above 7.25',
            ha='center', fontsize=11, color=GREEN, transform=ax.transAxes)
    for i, (name, action, detail, color) in enumerate(pros):
        row, col = divmod(i, 3)
        x = 0.02 + col * 0.33
        y_pos = 0.88 - row * 0.17
        rect = FancyBboxPatch((x, y_pos - 0.06), 0.31, 0.14, boxstyle='round,pad=0.01',
                               facecolor=PANEL, edgecolor=color, linewidth=2,
                               transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + 0.015, y_pos + 0.04, name, fontsize=10, fontweight='bold', color=color,
                transform=ax.transAxes, va='top')
        ax.text(x + 0.015, y_pos + 0.01, action, fontsize=9, fontweight='bold',
                transform=ax.transAxes, va='top')
        ax.text(x + 0.015, y_pos - 0.03, detail, fontsize=7, color=GRAY,
                transform=ax.transAxes, va='top')

    # Legend box
    rect = FancyBboxPatch((0.02, 0.02), 0.96, 0.08, boxstyle='round,pad=0.02',
                           facecolor='#1a2332', edgecolor=RED, linewidth=2, transform=ax.transAxes)
    ax.add_patch(rect)
    ax.text(0.5, 0.06, 'UNIFIED RULE: Close < 7.25 (2 days) = EXIT limit×3  |  Spring 7.25-7.35 + reclaim = STRONGEST HOLD  |  NO MARKET 128K',
            ha='center', fontsize=9, color=RED, fontweight='bold', transform=ax.transAxes)
    save(fig, 'EAC-738-03-15-محترف-مصفوفة.png')


# ── 4. Wyckoff Spring Diagram ────────────────────────────────────────
def chart_wyckoff_spring():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('Wyckoff @ 7.38 — Spring Zone vs Distribution', fontsize=13, fontweight='bold')

    # Left: Spring scenario
    t = np.linspace(0, 20, 100)
    spring_p = 7.55 - 0.08 * t + 0.15 * np.maximum(0, np.sin(t * 0.8)) 
    spring_p[60:65] = 7.28  # sweep
    spring_p[65:] = 7.28 + (t[65:] - t[65]) * 0.08
    ax1.plot(t, spring_p, color=GREEN, lw=2.5)
    ax1.axhspan(7.25, 7.45, alpha=0.15, color=GREEN)
    ax1.axhline(7.25, color=RED, ls='--', lw=2)
    ax1.scatter([12.5], [7.28], s=150, c=YELLOW, zorder=5)
    lbl(ax1, 12.5, 6.95, 'Spring\nSweep 7.25-7.35', YELLOW, 8)
    lbl(ax1, 17, 7.65, 'Reclaim 7.45\n= STRONG HOLD', GREEN, 8)
    ax1.set_title('Scenario A: Spring (40%) — Wyckoff Buy Signal', color=GREEN, fontweight='bold')
    ax1.set_ylabel('Price')
    ax1.set_ylim(7.0, 7.9)
    ax1.grid(True, alpha=0.25)

    # Right: Distribution
    dist_p = 7.55 - 0.06 * t
    dist_p[55:] = 7.22 - (t[55:] - t[55]) * 0.04
    ax2.plot(t, dist_p, color=RED, lw=2.5)
    ax2.axhline(7.25, color=RED, ls='--', lw=2)
    ax2.fill_between(t[55:], 6.5, dist_p[55:], alpha=0.2, color=RED)
    lbl(ax2, 14, 7.0, 'Close < 7.25\n2+ days', RED, 8)
    lbl(ax2, 17, 6.7, 'EXIT limit×3\nTarget 6.88', RED, 8)
    ax2.set_title('Scenario B: Distribution (35%) — Sell the News', color=RED, fontweight='bold')
    ax2.set_ylim(6.5, 7.9)
    ax2.grid(True, alpha=0.25)

    criteria = 'Wyckoff Score: 3/5 re-accum | Vol declining ✅ | Net sell week 🔴 | Spring pending ⏳'
    fig.text(0.5, 0.02, criteria, ha='center', fontsize=10, color=YELLOW)
    plt.tight_layout(rect=[0, 0.05, 1, 0.93])
    save(fig, 'EAC-738-04-وايكوف-Spring.png')


# ── 5. MTF Structure ─────────────────────────────────────────────────
def chart_mtf():
    fig, axes = plt.subplots(5, 1, figsize=(14, 12), sharex=False)
    fig.suptitle('EAC Multi-Timeframe @ 7.38 — Top-Down Analysis', fontsize=13, fontweight='bold')

    frames = [
        ('Monthly / Weekly', 'Parabolic Jun → 3 red candles · Still above 7.25 ✅', GREEN, 7.38, 7.35, 7.72),
        ('Daily', 'H=7.72 reject · L=7.35 sweep · C=7.38 bounce · Vol 1.13M', YELLOW, 7.38, 7.35, 7.72),
        ('4H / 1H', 'Quiet drift 7.36-7.42 · Low vol consolidation', GRAY, 7.38, 7.36, 7.42),
        ('15M / 10M', 'FREEZE @ 7.38 · Maker pattern 3/3 ✅', CYAN, 7.38, 7.38, 7.38),
        ('1M', 'O=H=L=C=7.38 · Microcap lock', PURPLE, 7.38, 7.38, 7.38),
    ]
    for ax, (name, msg, color, c, l, h) in zip(axes, frames):
        x = np.arange(20)
        if 'Monthly' in name:
            y = np.concatenate([np.linspace(5, 10.17, 12), np.linspace(10.17, 7.38, 8)])
        elif 'Daily' in name:
            y = 7.55 + 0.1 * np.sin(x * 0.5)
            y[-3:] = [7.72, 7.35, 7.38]
        elif '4H' in name:
            y = 7.38 + 0.02 * np.sin(x * 0.7)
        else:
            y = np.full(20, 7.38)
        ax.plot(x, y, color=color, lw=2)
        ax.axhline(7.25, color=RED, ls=':', alpha=0.7)
        ax.axhline(7.50, color=GRAY, ls=':', alpha=0.5)
        ax.fill_between(x, l, h, alpha=0.1, color=color)
        ax.set_ylabel(name, fontweight='bold', fontsize=9)
        ax.text(0.98, 0.85, msg, transform=ax.transAxes, ha='right', fontsize=7, color=GRAY)
        ax.set_ylim(7.0, 10.5 if 'Monthly' in name else 7.8)
        ax.grid(True, alpha=0.2)
    axes[-1].set_xlabel('Bars (schematic)')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    save(fig, 'EAC-738-05-MTF-متعدد-الفريمات.png')


# ── 6. Paid Tools Summary ────────────────────────────────────────────
def chart_paid_tools():
    fig, ax = plt.subplots(figsize=(14, 10))
    tools = [
        ('Market Cipher', '🟡', 'No Green Dot · WT bear cross', 0.3),
        ('TTM Squeeze Pro', '🟡', 'Daily OFF · Intraday ORANGE ON', 0.45),
        ('AVWAP Shannon', '🔴', 'Below 7.72 (-34 pts) · Gate 8.13', 0.2),
        ('SuperTrend/Chandelier', '🔴', 'Swing trend OFF · Exit @ 8.42', 0.15),
        ('Minervini VCP', '🟢', 'Valid · Pivot 8.04-8.11 + vol', 0.75),
        ('DeMark Bloomberg', '🟢', 'Buy Setup · Reversal window', 0.7),
        ('IBD MarketSurge', '🟢', 'Base Stage 2 · Blue Dot · Trigger 8.43', 0.72),
        ('LuxAlgo Confluence', '🟡', '2/5 · Retracement not reversal', 0.4),
        ('Holly AI', '🟡', 'Oversold Bounce active near 7.25', 0.42),
        ('TrendSpider MTF', '🔴', 'No Alignment · No Trade', 0.1),
        ('Bookmap/ATAS', '🟡', 'Absorption @ freeze · Exhaustion ✅', 0.5),
        ('SMRT Algo 5-factor', '🟡', '2-3/5 · No trigger', 0.35),
    ]
    y_pos = np.arange(len(tools))
    scores = [t[3] for t in tools]
    colors = [GREEN if t[1] == '🟢' else YELLOW if t[1] == '🟡' else RED for t in tools]
    ax.barh(y_pos, scores, color=colors, edgecolor=WHITE, height=0.6, alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"{t[0]}  {t[1]}" for t in tools], fontsize=9)
    for i, t in enumerate(tools):
        ax.text(scores[i] + 0.02, i, t[2], va='center', fontsize=7, color=GRAY)
    ax.set_xlim(0, 1.05)
    ax.set_xlabel('Signal Strength (simulated)')
    ax.set_title('38+ Paid Platforms @ 7.38 — ALL Trigger-Based · No Buy/Sell Now', fontweight='bold', pad=12)
    ax.axvline(0.5, color=YELLOW, ls='--', alpha=0.5, label='Trigger threshold')
    ax.grid(axis='x', alpha=0.2)
    fig.text(0.5, 0.02, 'Activate: 8.11-8.43 + vol  |  Defend: 7.25  |  Cancel: < 6.90',
             ha='center', fontsize=10, color=YELLOW)
    plt.tight_layout(rect=[0, 0.04, 1, 1])
    save(fig, 'EAC-738-06-38-اداة-مدفouعة.png')


# ── 7. Key Indicators Detail ─────────────────────────────────────────
def chart_key_indicators():
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('Key Professional Indicators @ 7.38 — Detail Panel', fontsize=13, fontweight='bold')

    # ADX gauge
    ax = axes[0, 0]
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.3, 1.3)
    ax.axis('off')
    wedge = Wedge((0, 0), 1, 0, 180, width=0.3, facecolor=PANEL, edgecolor=GRAY)
    ax.add_patch(wedge)
    needle_angle = 180 - (50 / 60 * 180)  # ADX=50
    rad = np.radians(needle_angle)
    ax.plot([0, 0.85 * np.cos(rad)], [0, 0.85 * np.sin(rad)], color=GREEN, lw=4)
    ax.text(0, -0.15, 'ADX = 50\nMEGA TREND 🟢🟢', ha='center', fontsize=12, fontweight='bold', color=GREEN)
    ax.set_title('Trend Strength', fontweight='bold')

    # StochRSI
    ax = axes[0, 1]
    ax.bar(['StochRSI', 'RSI', 'MACD hist', 'Williams %R'], [3, 55, -14, -75],
           color=[GREEN, YELLOW, RED, YELLOW], edgecolor=WHITE)
    ax.axhline(0, color=GRAY, lw=0.5)
    ax.set_title('Momentum Panel', fontweight='bold')
    ax.text(0, 8, 'StochRSI <5 = EXTREME oversold', fontsize=8, color=GREEN)
    ax.grid(axis='y', alpha=0.2)

    # Volume split
    ax = axes[1, 0]
    labels = ['OBV', 'NVI', 'CMF', 'A/D', 'Weis', 'POC']
    vals = [1, 1, 0.6, -0.8, 0.7, -0.5]
    colors_v = [GREEN if v > 0 else RED for v in vals]
    ax.barh(labels, vals, color=colors_v, edgecolor=WHITE)
    ax.axvline(0, color=WHITE, lw=0.5)
    ax.set_title('Volume/Flow Split — OBV vs A/D Divergence', fontweight='bold')
    ax.set_xlim(-1.2, 1.2)
    ax.grid(axis='x', alpha=0.2)

    # Confluence levels
    ax = axes[1, 1]
    levels = [7.25, 7.38, 7.50, 7.72, 8.11, 8.43, 10.17, 12.57]
    counts = [8, 1, 5, 3, 6, 2, 2, 4]
    cols = [RED, YELLOW, GRAY, CYAN, YELLOW, GREEN, ORANGE, PURPLE]
    ax.barh([str(l) for l in levels], counts, color=cols, edgecolor=WHITE)
    ax.set_xlabel('# of independent schools agreeing')
    ax.set_title('Level Confluence (4+ schools = key)', fontweight='bold')
    ax.grid(axis='x', alpha=0.2)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    save(fig, 'EAC-738-07-مؤشرات-رئيسية-تفصيل.png')


# ── 8. AGM Scenarios ─────────────────────────────────────────────────
def chart_agm_scenarios():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle('AGM Tomorrow (Jul 6) — 3 Scenarios @ Entry from 7.38', fontsize=13, fontweight='bold')

    scenarios = [
        ('A: Spring → Pop (40%)', GREEN, [7.38, 7.30, 7.55, 7.80, 8.0],
         'Sweep 7.25-7.35 → reclaim 7.45\nSTRONGEST HOLD signal'),
        ('B: Sell the News (35%)', RED, [7.38, 7.20, 7.05, 6.95, 6.88],
         'Break 7.25 → distribution\nEXIT limit ×3'),
        ('C: Freeze (25%)', YELLOW, [7.38, 7.40, 7.42, 7.38, 7.41],
         'Range 7.35-7.65\nWait for catalyst'),
    ]
    days = ['Sun', 'Mon AGM', 'Tue', 'Wed', 'Thu']
    for ax, (title, color, prices, note) in zip(axes, scenarios):
        ax.plot(days, prices, 'o-', color=color, lw=3, markersize=10)
        ax.axhline(7.25, color=RED, ls='--', alpha=0.7)
        ax.axhline(7.75, color=ORANGE, ls=':', alpha=0.7, label='Entry 7.75')
        ax.fill_between(range(5), 7.25, 8.14, alpha=0.05, color=GREEN)
        ax.set_title(title, color=color, fontweight='bold')
        ax.set_ylabel('Price (EGP)')
        ax.set_ylim(6.7, 8.3)
        ax.text(0.5, 0.05, note, transform=ax.transAxes, ha='center', fontsize=8, color=GRAY)
        ax.grid(True, alpha=0.25)
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    save(fig, 'EAC-738-08-سيناريوهات-AGM.png')


# ── 9. PnL + Targets from 7.38 ───────────────────────────────────────
def chart_pnl_targets():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle(f'EAC @ 7.38 — PnL & Target Ladder · {SHARES:,} shares @ {ENTRY}',
                 fontsize=13, fontweight='bold')

    targets = [
        (7.25, 'Stop', RED, -64_200),
        (7.38, 'NOW', GRAY, -47_508),
        (7.75, 'Entry', ORANGE, 0),
        (8.14, 'Gate', YELLOW, 50_076),
        (8.90, 'Station 1', GREEN, 147_660),
        (10.17, 'ATH', GREEN, 310_848),
        (12.57, 'Magnet', PURPLE, 618_888),
    ]
    prices = [t[0] for t in targets]
    pnls = [t[3] for t in targets]
    colors = [t[2] for t in targets]
    ax1.barh([t[1] for t in targets], pnls, color=colors, edgecolor=WHITE, height=0.55)
    ax1.axvline(0, color=WHITE, lw=1)
    ax1.set_xlabel('P&L (EGP)')
    ax1.set_title('Your P&L at Each Level', fontweight='bold')
    for i, (p, name, c, pnl) in enumerate(targets):
        ax1.text(pnl + (8000 if pnl >= 0 else -8000), i, f'{p:.2f} → {pnl:+,} EGP',
                 va='center', fontsize=7, color=c)
    ax1.grid(axis='x', alpha=0.2)

    ax2.axhspan(7.25, 8.14, alpha=0.1, color=YELLOW, label='Breakout zone')
    ax2.axhspan(10.9, 11.9, alpha=0.1, color=GREEN, label='Cluster 1')
    ax2.axhspan(12.5, 13.2, alpha=0.1, color=PURPLE, label='Magnet zone')
    for p, name, c, _ in targets:
        ax2.axhline(p, color=c, ls='--' if p != NOW else '-', lw=2 if p == NOW else 1)
        ax2.text(1.02, p, f'{p} {name}', transform=ax2.get_yaxis_transform(), fontsize=7, color=c)
    ax2.set_ylim(6.8, 13.5)
    ax2.set_xlim(0, 1)
    ax2.set_xticks([])
    ax2.set_title('Target Clusters (post ×0.8 free shares)', fontweight='bold')
    ax2.grid(True, alpha=0.2)

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    save(fig, 'EAC-738-09-PnL-والاهداف.png')


# ── 10. Decision Flowchart ───────────────────────────────────────────
def chart_decision_flow():
    fig, ax = plt.subplots(figsize=(14, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('EAC @ 7.38 — Decision Flowchart (15 Pros + 100 Tools + 38 Paid)',
                 fontsize=13, fontweight='bold', pad=15)

    boxes = [
        (5, 11, 'NOW: 7.38\n13 pts above Death 7.25', YELLOW, 2.2, 0.7),
        (5, 9.5, 'AGM Tomorrow?\nWatch first 30 min', PURPLE, 2.5, 0.7),
        (2, 7.5, 'Spring\n7.25-7.35\n+ reclaim', GREEN, 2.0, 0.9),
        (5, 7.5, 'Freeze\n7.35-7.65', YELLOW, 1.8, 0.7),
        (8, 7.5, 'Break\n< 7.25', RED, 1.8, 0.7),
        (2, 5.5, 'HOLD STRONG\nWyckoff+Raschke', GREEN, 2.2, 0.7),
        (5, 5.5, 'HOLD\nWait catalyst', YELLOW, 1.8, 0.7),
        (8, 5.5, 'EXIT limit×3\n7.35/7.32/7.30', RED, 2.4, 0.7),
        (2, 3.5, 'Break 8.11-8.43\n+ vol +40%', GREEN, 2.4, 0.7),
        (5, 3.5, 'Sell 43K @ 8.6-9.0\n(Qullamaggie)', ORANGE, 2.6, 0.7),
        (8, 3.5, 'Loss ~-65K\nStop executed', RED, 2.0, 0.7),
        (5, 1.5, 'NEVER: Market 128K\nNEVER: Cancel stop 7.24', RED, 4.5, 0.6),
    ]
    for x, y, txt, c, w, h in boxes:
        rect = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0.02',
                               facecolor=PANEL, edgecolor=c, linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y, txt, ha='center', va='center', fontsize=8, fontweight='bold', color=WHITE)

    arrows = [
        (5, 10.65, 5, 9.85), (5, 9.15, 2, 8.0), (5, 9.15, 5, 7.85), (5, 9.15, 8, 8.0),
        (2, 7.05, 2, 5.85), (5, 7.15, 5, 5.85), (8, 7.05, 8, 5.85),
        (2, 5.15, 2, 3.85), (2, 3.15, 5, 3.85),
    ]
    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))
    save(fig, 'EAC-738-10-مخطط-القرار.png')


if __name__ == '__main__':
    print('Generating 10 charts @ 7.38 (professional indicators + strategies)...')
    chart_smc_levels()
    chart_100_tools()
    chart_15_pros()
    chart_wyckoff_spring()
    chart_mtf()
    chart_paid_tools()
    chart_key_indicators()
    chart_agm_scenarios()
    chart_pnl_targets()
    chart_decision_flow()
    print('Done — 10 charts @ 7.38.')

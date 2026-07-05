# 🌍 Intermarket Gate — Murphy · {{DATE}}

> **Rule:** New longs on individual EGX stocks only if **≥ 2/3 macro gates** align  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ Local EGX (primary — weight ×2)

| Check | Value | Signal | Pass? |
|-------|-------|--------|-------|
| EGX30 W close vs MA20/50 | | ↑/↓/→ | ☐ |
| EGX70 breadth (advancers %) | | | ☐ |
| Distribution days (25 sessions) | {{DD}}/5 max | 🟢/🟡/🔴 | ☐ |
| EGX30 RS trend (4W) | | | ☐ |

**Local gate:** {{LOCAL_VERDICT}} 🟢/🟡/🔴

---

## 2️⃣ Global Macro Proxies

| Market | Symbol | Trend W | vs 20MA | Risk signal | Pass long? |
|--------|--------|---------|---------|-------------|------------|
| US 10Y Yield | ^TNX | | | ↑ yield = pressure | ☐ |
| Dollar Index | DXY | | | Strong $ = EM headwind | ☐ |
| Gold | GC / XAUUSD | | | Inflation fear | ☐ |
| Oil | CL / Brent | | | Cost pressure | ☐ |
| VIX | ^VIX | | | Fear gauge | ☐ |

---

## 3️⃣ Murphy Classic Correlations (context)

| Relationship | Expected | Now | Align? |
|--------------|----------|-----|--------|
| Bonds ↑ → Stocks ↑ (risk-on) | Positive | | ☐ |
| $ ↑ → Commodities ↓ | Inverse | | ☐ |
| Commodities ↑ → Bonds ↓ | Inverse | | ☐ |

> **Note:** Correlations shift in crises — reassess weekly

---

## 4️⃣ EGX-Specific Macro

| Factor | Current | Impact on EGX |
|--------|---------|---------------|
| EGP/USD trend | | |
| Egypt inflation trend | | |
| CBE rate direction | | |
| Foreign flow (if known) | | |

---

## 5️⃣ Gate Score

| Gate | Weight | Status |
|------|--------|--------|
| EGX local (index + dist days) | 2 | 🟢/🟡/🔴 |
| Global risk (VIX + yields) | 1 | 🟢/🟡/🔴 |
| Dollar/EM | 1 | 🟢/🟡/🔴 |
| Commodity inflation | 1 | 🟢/🟡/🔴 |

**Total passes:** {{PASSES}}/5 weighted · **Required for new longs:** ≥ 2/3 macro + local not 🔴

---

## 6️⃣ Portfolio Action

| Regime | New longs | Existing positions |
|--------|-----------|-------------------|
| 🟢 Full risk-on | Buy List full size | Hold / trail |
| 🟡 Mixed | Tier A only · tight triggers | Tighten stops |
| 🔴 Risk-off | **No new longs** | Reduce / exit weak |

---

## Verdict

> **{{VERDICT}}** — Murphy gate: {{GATE_RESULT}}

---

*Intermarket EGX v1 · Murphy + local EGX adaptation · Run every Thursday*

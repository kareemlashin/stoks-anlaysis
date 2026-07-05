# 🛡️ Risk Dashboard — Portfolio · {{DATE}}

> **مصدر المراكز:** [`../محفظتي.md`](../محفظتي.md)  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ Portfolio Summary

| Metric | Value | IPS Limit | Status |
|---|---|---|---|
| **Total value (EGP)** | {{TOTAL}} | | |
| **Total unrealized PnL** | {{PNL}} ({{PNL_PCT}}%) | | |
| **Cash / dry powder** | {{CASH}} | min {{MIN_CASH}}% | 🟢/🔴 |
| **# positions** | {{N}} | max {{MAX_POS}} | |
| **Largest position %** | {{LARGEST_PCT}}% | max {{MAX_SINGLE}}% | 🟢/🔴 |

---

## 2️⃣ Position Heat Map

| Code | Value | % Port | PnL % | Stop dist | Liquidity days | Sector | Risk |
|---|---|---|---|---|---|---|---|
| {{CODE}} | {{VALUE}} | {{PCT}}% | {{PNL}}% | {{STOP_DIST}}% | {{LIQ_DAYS}}d | {{SECT}} | 🟢/🟡/🔴 |

---

## 3️⃣ Correlation / Concentration

| Risk type | Exposure | Limit | OK? |
|---|---|---|---|
| Single stock max | {{CODE}} {{PCT}}% | {{MAX_SINGLE}}% | ☐ |
| Sector max | {{SECTOR}} {{SECT_PCT}}% | {{MAX_SECTOR}}% | ☐ |
| Microcap total | {{MICRO_PCT}}% | {{MAX_MICRO}}% | ☐ |
| Event cluster (same week) | {{EVENTS}} | | ☐ |

---

## 4️⃣ Market Regime Overlay

| | EGX30 | EGX70 |
|---|---|---|
| Close W | | |
| Trend | | |
| Distribution days (25) | {{DD}} | |
| **Regime** | 🟢/🟡/🔴 | |
| **New longs allowed?** | ☐ Yes ☐ Tier A only ☐ No |

---

## 5️⃣ Stress Test

| Scenario | Portfolio impact (EGP) | % drawdown |
|---|---|---|
| Largest position hits stop | {{STRESS_1}} | |
| EGX -5% gap | {{STRESS_2}} | |
| All stops hit | {{STRESS_3}} | |
| **Max acceptable (IPS)** | {{MAX_DD}} | |

---

## 6️⃣ Action Items

| Priority | Action | Code | By when |
|---|---|---|---|
| 🔴 | {{ACTION_1}} | {{CODE}} | {{DATE}} |
| 🟡 | {{ACTION_2}} | | |

---

## 7️⃣ Verdict

> **Portfolio risk level:** 🟢 Low / 🟡 Moderate / 🔴 Elevated  
> **{{VERDICT}}**

---

*Risk Dashboard v1 · Run weekly (Thursday) + before any add*

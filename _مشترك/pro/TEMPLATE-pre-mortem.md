# 💀 Pre-Mortem — {{CODE}} · {{NAME}}

> **التاريخ:** {{DATE}} · **قبل:** {{ACTION}} (buy/add/hold through event)  
> **السؤال:** "لو خسرت فلوسي في الصفقة دي بعد 30 يوم — **ليه**؟"  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ Setup Summary

| | |
|---|---|
| **Action considered** | {{ACTION}} |
| **Entry** | {{ENTRY}} |
| **Size** | {{QTY}} @ {{AVG}} |
| **Stop** | {{STOP}} |
| **Target** | {{TARGET}} |
| **Event risk** | {{EVENT}} |

---

## 2️⃣ Failure Scenarios (minimum 5)

| # | Scenario | Prob % | Loss (EGP) | Early warning sign |
|---|---|---|---|---|
| 1 | {{SCENARIO_1}} | | | |
| 2 | {{SCENARIO_2}} | | | |
| 3 | {{SCENARIO_3}} | | | |
| 4 | {{SCENARIO_4}} | | | |
| 5 | {{SCENARIO_5}} | | | |

---

## 3️⃣ Historical Precedents

| Similar event (this stock or sector) | What happened | Lesson |
|---|---|---|
| {{HIST_1}} | | |
| {{HIST_2}} | | |

---

## 4️⃣ "What could I be wrong about?"

- [ ] **Thesis:** {{WRONG_THESIS}}
- [ ] **Timing:** {{WRONG_TIMING}}
- [ ] **Size:** {{WRONG_SIZE}}
- [ ] **Liquidity:** {{WRONG_LIQUIDITY}}
- [ ] **Macro/EGX:** {{WRONG_MARKET}}

---

## 5️⃣ Kill Switches (automatic exit rules)

| Trigger | Action | No debate |
|---|---|---|
| close < {{STOP}} | EXIT 100% | ✅ |
| {{KILL_2}} | {{ACTION_2}} | ✅ |
| {{KILL_3}} | {{ACTION_3}} | ✅ |

---

## 6️⃣ Worst Case PnL

| Scenario | Price | PnL (EGP) | % of portfolio |
|---|---|---|---|
| Stop hit | {{STOP}} | {{PNL_STOP}} | {{PCT_STOP}}% |
| Gap down | {{GAP}} | {{PNL_GAP}} | {{PCT_GAP}}% |
| Total loss | 0 | {{PNL_TOTAL}} | {{PCT_TOTAL}}% |

> **Max acceptable loss (IPS):** {{MAX_LOSS_EGP}} ج · **This trade risk:** {{TRADE_RISK_EGP}} ج — **OK?** ☐ Yes ☐ No

---

## 7️⃣ Go / No-Go

| Check | Pass? |
|---|---|
| Worst case ≤ IPS max loss | ☐ |
| Kill switches defined | ☐ |
| Liquidity exit ≤ {{MAX_EXIT_DAYS}} days | ☐ |
| No emotional override planned | ☐ |

### Decision

> **{{GO_NOGO}}** — {{REASON}}

---

*Pre-Mortem v1 · Run BEFORE every new position or size increase*

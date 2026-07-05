# ⚡ Playbook — {{EVENT}} · {{CODE}} · {{DATE}}

> **حدث:** {{EVENT}} (AGM / Results / Dividend / News / Gap)  
> **Position:** {{QTY}} @ {{AVG}} · Close ref: {{CLOSE}}  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ Event Facts

| Field | Value |
|---|---|
| **Event** | {{EVENT}} |
| **Date / Time** | {{DATETIME}} |
| **Venue / Source** | {{SOURCE}} |
| **Expected outcome** | {{EXPECTED}} |
| **Binary?** | ☐ Yes (pass/fail) ☐ Spectrum |

---

## 2️⃣ Scenarios (pre-event)

| # | Scenario | Prob | Price reaction | Your PnL | Action |
|---|---|---|---|---|---|
| A | Best case | {{P_A}}% | +{{MOVE_A}}% → {{PRICE_A}} | {{PNL_A}} | {{ACT_A}} |
| B | Base case | {{P_B}}% | {{MOVE_B}}% | {{PNL_B}} | {{ACT_B}} |
| C | Sell the news | {{P_C}}% | −{{MOVE_C}}% | {{PNL_C}} | {{ACT_C}} |
| D | Disaster | {{P_D}}% | −{{MOVE_D}}% | {{PNL_D}} | {{ACT_D}} |

---

## 3️⃣ Session Timeline (EGX)

| Time | Phase | Allowed | Forbidden |
|---|---|---|---|
| Pre-open | | Watch only | Market orders |
| 10:30–11:30 | First hour (Raschke) | {{ALLOW_1}} | {{FORBID_1}} |
| 11:30–13:00 | Mid session | Minimal action | Big adds |
| 13:00–14:30 | Last hour | {{ALLOW_2}} | |
| After close | | Update journal | Emotional trades |

---

## 4️⃣ Order Sheet (fill before event)

| Order ID | Type | Trigger | Price | Qty | Valid until | Purpose |
|---|---|---|---|---|---|---|
| PB-1 | Limit Sell | if gap > {{GAP}} | {{PRICE}} | {{QTY_PARTIAL}} | EOD | Take profit |
| PB-2 | Limit Sell | stop | {{STOP}} | {{QTY}} | GTC | Protection |
| PB-3 | Limit Buy | dip to {{DIP}} | {{PRICE}} | {{QTY_ADD}} | EOD | Add on dip |
| PB-4 | Cancel all | if {{CONDITION}} | — | — | — | Abort |

> **Microcap rule:** Limit ONLY · split {{N}} tranches · max {{MAX_QTY}} per tranche

---

## 5️⃣ Level Map (event day)

| Level | Role today | If touched |
|---|---|---|
| {{LEVEL_1}} | {{ROLE_1}} | {{ACTION_1}} |
| {{LEVEL_2}} | | |
| {{DEATH}} | Hard stop | EXIT 100% |

---

## 6️⃣ Post-Event Checklist (within 1 hour of close)

- [ ] Record actual outcome vs scenario
- [ ] Adjust all levels for bonus/split if applicable (×{{FACTOR}})
- [ ] Update [`../محفظتي.md`](../محفظتي.md)
- [ ] Update Scorecard
- [ ] Write trade journal entry
- [ ] Schedule next deep review if thesis changed

---

## 7️⃣ Mark Douglas — Event Day Rules

- [ ] Plan written **before** open — not reactive
- [ ] Max loss today defined: {{MAX_DAY_LOSS}} ج
- [ ] No "hope hold" through invalidation
- [ ] If scenario D → execute PB-2 without debate

---

## 8️⃣ Verdict (pre-event)

> **{{PRE_EVENT_VERDICT}}**

---

*Event Playbook v1 · Use for AGM, earnings, rights, major news*

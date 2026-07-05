# 🔬 تحليل {{CODE}} — رؤية شاملة · {{DATE}}

> **Layer:** L3 Deep · **Conviction:** {{CONVICTION}}/10  
> **Thesis:** [`{{CODE}}-thesis-{{DATE}}.md`](TEMPLATE-investment-thesis.md)  
> **Checklist:** [`MASTER-CHECKLIST-تحليل-احترافي.md`](MASTER-CHECKLIST-تحليل-احترافي.md)  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## ⚡ الحكم في سطرين

> **{{VERDICT_LINE_1}}**  
> **{{VERDICT_LINE_2}}**

---

## 0️⃣ Position Context

| | |
|---|---|
| **Qty × Avg** | {{QTY}} @ {{AVG}} |
| **Close** | {{CLOSE}} ({{CHANGE}}%) |
| **Unrealized PnL** | {{PNL_EGP}} ج ({{PNL_PCT}}%) |
| **Market regime** | {{REGIME}} 🟢/🟡/🔴 |

---

## 1️⃣ MTF Snapshot (all frames)

| TF | Close | Trend | RSI | MACD hist | BBW | Key level | Signal |
|---|---|---|---|---|---|---|---|
| M | | | | | | | 🟢/🟡/🔴 |
| W | | | | | | | |
| D | | | | | | | |
| 4H | | | | | | | |
| 1H | | | | | | | |

**Confluence levels (4+ schools):**

| Level | Schools agreeing | Role |
|---|---|---|
| {{LEVEL}} | {{SCHOOLS}} | Death/POC/Gate/... |

---

## 2️⃣ 100 Tools Summary

| Group | 🟢 | 🟡 | 🔴 | Net |
|---|---|---|---|---|
| Momentum (20) | | | | |
| Trend (15) | | | | |
| Volume (15) | | | | |
| Volatility (10) | | | | |
| SMC (10) | | | | |
| Waves (12) | | | | |
| Systems (12) | | | | |
| Profile (6) | | | | |
| **Total** | **{{G}}** | **{{Y}}** | **{{R}}** | **{{SCORE}}** |

→ تفصيل: `تحليل-{{CODE}}-100-اداة-{{DATE}}.md`

---

## 3️⃣ 15 Professionals Matrix

| Pro | Rule applied | Verdict on YOUR position | Action |
|---|---|---|---|
| Minervini | stop 7-8% | | |
| Qullamaggie | ADR stop | | |
| Wyckoff | phase | | |
| O'Neil | distribution days | | |
| Weinstein | stage | | |
| ... | | | |

→ تفصيل: `استراتيجيات-المحترفين-{{CODE}}-{{DATE}}.md`

---

## 4️⃣ Maker + Historical Cycle

| Maker behavior | Evidence | Implication |
|---|---|---|
| {{BEHAVIOR}} | | |

| Cycle match | 2024 (or prior) | Now | Similarity |
|---|---|---|---|
| Phase | | | {{PCT}}% |

---

## 5️⃣ Fundamentals (summary)

→ [`TEMPLATE-fundamentals-EGX.md`](TEMPLATE-fundamentals-EGX.md) — filled: ☐

| Catalyst | Date | Impact |
|---|---|---|
| {{CATALYST}} | {{DATE}} | |

---

## 6️⃣ Scenarios + EV

| Scenario | Prob | Target | PnL (EGP) | R:R |
|---|---|---|---|---|
| Bull | {{P_BULL}}% | {{T_BULL}} | {{PNL_BULL}} | |
| Base | {{P_BASE}}% | {{T_BASE}} | {{PNL_BASE}} | |
| Bear | {{P_BEAR}}% | {{T_BEAR}} | {{PNL_BEAR}} | |
| Crash | {{P_CRASH}}% | {{T_CRASH}} | {{PNL_CRASH}} | |

**Expected Value:** {{EV}} ج · **R:R to T1:** {{RR}}:1 · **EV positive?** ☐

---

## 7️⃣ Position Sizing

| Method | Max shares | Your qty | Status |
|---|---|---|---|
| Minervini 1.5% risk | {{MAX_M}} | {{QTY}} | 🟢/🔴 over |
| Liquidity (3d exit) | {{MAX_L}} | | |
| IPS max single | {{MAX_IPS}} | | |

---

## 8️⃣ Decision Table (print this)

| Event | Trigger | Action | Qty | Order type |
|---|---|---|---|---|
| Reclaim POC | close > {{POC}} + vol | HOLD/add | | Limit |
| Death break | close < {{DEATH}} | EXIT | {{QTY}} | Limit |
| Gate break | close > {{GATE}} + vol | add/trail | | Limit |
| {{EVENT}} | {{TRIGGER}} | {{ACTION}} | | |

---

## 9️⃣ Alerts (copy to TradingView)

```
{{CODE}}: alert @ {{LEVEL_1}} — {{DESC_1}}
{{CODE}}: stop @ {{STOP}} — valid
{{CODE}}: cancel {{OLD}} → {{NEW}}
```

---

## 🔟 Charts

| File | Description |
|---|---|
| `{{CODE}}-SMC-{{DATE}}.png` | Liquidity map |
| `{{CODE}}-100-tools-{{DATE}}.png` | Tool dashboard |
| `{{CODE}}-MTF-{{DATE}}.png` | Multi-timeframe |
| `{{CODE}}-decision-{{DATE}}.png` | Master decision map |

---

## 1️⃣1️⃣ Scorecard Update

→ [`TEMPLATE-scorecard.md`](TEMPLATE-scorecard.md)

---

## 1️⃣2️⃣ Next Review Triggers

- [ ] close {{TRIGGER_1}}
- [ ] Event: {{EVENT}} on {{DATE}}
- [ ] 2 weeks passed
- [ ] User request

---

## 🔗 Series Links

| File | |
|---|---|
| Thesis | `{{CODE}}-thesis-{{DATE}}.md` |
| Pre-mortem | `{{CODE}}-premortem-{{DATE}}.md` |
| Playbook | `{{CODE}}-playbook-{{DATE}}.md` |
| Prior update | `تحليل-{{CODE}}-محدث-{{PRIOR}}.md` |

---

*Deep Analysis Output v1 · Institutional template*

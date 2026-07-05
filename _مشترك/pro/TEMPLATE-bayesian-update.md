# 📐 Bayesian Update — {{CODE}} · {{DATE}}

> **Purpose:** Update conviction with evidence — not hope  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## Prior State

| Field | Value |
|-------|-------|
| **Prior conviction** | {{PRIOR}}/10 |
| **Prior date** | {{PRIOR_DATE}} |
| **Thesis summary** | {{THESIS_ONE_LINE}} |

---

## New Evidence (since last update)

| # | Event / Data | Direction | Magnitude | Source |
|---|--------------|-----------|-----------|--------|
| 1 | {{EVIDENCE_1}} | 🟢/🔴/🟡 | +/−/0 | |
| 2 | {{EVIDENCE_2}} | | | |
| 3 | {{EVIDENCE_3}} | | | |

---

## Conviction Adjustments

| Rule | Adjustment |
|------|------------|
| Trigger hit as planned | +0.5 to +1.0 |
| Key level rejected (AVWAP/POC) | −0.5 to −1.0 |
| Catalyst positive surprise | +1.0 to +2.0 |
| Catalyst negative surprise | −1.0 to −3.0 |
| Thesis pillar challenged | −1.0 per pillar |
| Distribution day on index | −0.5 |
| Wyckoff test failed | −1.0 |
| Scorecard tool 2/2 hit | +0.5 weight that tool |

---

## Calculation

```
Prior:     {{PRIOR}}/10
{{EVIDENCE_1}}:  {{DELTA_1}}
{{EVIDENCE_2}}:  {{DELTA_2}}
{{EVIDENCE_3}}:  {{DELTA_3}}
─────────────────
Posterior: {{POSTERIOR}}/10
```

---

## Action Thresholds

| Posterior | Action |
|-----------|--------|
| ≥ 8 | Full size on trigger · trail aggressively |
| 6–7.9 | Hold · add only on confirmation |
| 4–5.9 | Reduce · no new adds |
| < 4 | Exit plan · pre-mortem killers active |

**Current posterior:** {{POSTERIOR}}/10 → **{{ACTION}}**

---

## What Would Change My Mind (explicit)

| To increase conviction | To decrease |
|------------------------|-------------|
| {{BULLISH_CHANGE}} | {{BEARISH_CHANGE}} |

---

*Bayesian Update v1 · Run after every material event*

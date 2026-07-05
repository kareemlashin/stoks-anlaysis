# 📅 فحص أسبوعي — تجهيز شراء — {{WEEK_DATE}}

> **Layer:** L1 Weekly · **الهدف:** **نشتري إيه الأسبوع ده؟**  
> **المدخلات:** {{COUNT}} سهم × 5 TF · فلتر: {{FILTER}}  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ حالة السوق — EGX Regime

| | EGX30 | EGX70 |
|---|---|---|
| **Close W** | | |
| **Trend** | | |
| **Change W** | | |

| Gate | القيمة |
|---|---|
| **Distribution days (25j)** | {{DD_COUNT}} |
| **Regime** | {{MARKET_REGIME}} 🟢 / 🟡 / 🔴 |
| **قرار الأسبوع** | {{BUY_DECISION}} |
| **Murphy intermarket (2/3)** | {{INTERMARKET}} |

> 🟢 = full Buy List · 🟡 = Tier A بس · 🔴 = **ممنوع longs جديدة**

---

## 2️⃣ إحصائيات الفحص

| | العدد |
|---|---|
| **إجمالي المرشحين** | {{COUNT}} |
| **Passed** | {{PASSED}} |
| **Rejected (Out)** | {{REJECTED}} |
| **Tier A** | {{TIER_A}} |
| **Tier B** | {{TIER_B}} |

---

## 3️⃣ 🏆 Buy List — Top 15

| Rk | Code | Name | Score | Tier | W | D | Setup | Trigger 🎯 | Stop | R:R | Size | {{SIGNAL}} |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {{CODE}} | {{NAME}} | {{SCORE}} | {{TIER}} | | | | close > {{TRIGGER}} | {{STOP}} | | | |
| 2 | | | | | | | | | | | | |
| 3 | | | | | | | | | | | | |
| … | | | | | | | | | | | | |
| 15 | | | | | | | | | | | | |

**قاعدة:** مفيش شراء إلا **بعد** trigger · Weekly = تجهيز فقط

---

## 4️⃣ Tier Lists

### Tier A (≥75) — راقب trigger · sizing كامل

| Code | Trigger | Stop | Setup |
|---|---|---|---|
| {{CODE}} | close > {{TRIGGER}} | {{STOP}} | {{SETUP}} |

### Tier B (60–74) — watchlist · نصف size

| Code | Trigger | Stop | Setup |
|---|---|---|---|
| | | | |

### Tier C (45–59) — مراقبة · لا دخول

| Code | Score | ملاحظة |
|---|---|---|
| | | |

---

## 5️⃣ Watchlist — Alerts جاهزة

```
{{CODE}}: BUY CHECK — close > {{TRIGGER}} — vol > avg — {{SETUP}}
{{CODE}}: alert @ {{TRIGGER}} — {{TRIGGER_DESC}}
...
```

---

## 6️⃣ 🚫 Out List — Rejected

| Code | Score | سبب الرفض |
|---|---|---|
| {{CODE}} | | below MA200W / low liq / extended / dead money / DD supply / … |
| | | |

---

## 7️⃣ قطاعات Hot / Cold

| القطاع | # في Top 25 | Trend | ملاحظة |
|---|---|---|---|
| {{SECTOR}} | | | wave / avoid |

---

## 8️⃣ Deep Dive — Top {{N}} (optional)

| Code | Tier | Trigger | Deep file | قرار |
|---|---|---|---|---|
| {{CODE}} | A | {{TRIGGER}} | [link/analysis] | buy on trigger / skip |

📖 Deep = [`استاندرد-الرؤية-الشاملة`](../استاندرد-الرؤية-الشاملة-لأي-سهم.md)

---

## 9️⃣ Position Sizing (رأس المال {{CAPITAL}} EGP)

| Code | Trigger | Stop | Risk 1-2% | Max shares | R:R |
|---|---|---|---|---|---|
| {{CODE}} | | | {{RISK_EGP}} ج | {{MAX_QTY}} | |

**Formula:** `shares = (capital × risk%) / (entry − stop)`

---

## 🔟 Scorecard — توقعات الأسبوع الماضي

| Code | Trigger كان | حصل؟ | Action كان | صح؟ |
|---|---|---|---|---|
| | | ✅/❌/⏳ | | |

---

## 1️⃣1️⃣ دورة الأسبوع الجاي

```
1. حط alerts من §5
2. ⏳ انتظر trigger (close > X)
3. trigger → Limit buy (مش market)
4. ابعت: 💼 bought {{CODE}} qty @ price
5. → محفظتي.md → Daily يتابع
6. خميس الجاي: فحص جديد
```

---

## الحكم النهائي

> **{{FINAL_WEEKLY_VERDICT}}**

---

*Template v1 · Output Weekly · Input: [`TEMPLATE-input-weekly.md`](TEMPLATE-input-weekly.md)*

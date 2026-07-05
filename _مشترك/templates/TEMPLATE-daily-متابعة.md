# 📆 متابعة يومية — {{SESSION_DATE}}

> **Layer:** L2 Daily · **المحفظة:** [`محفظتي.md`](../محفظتي.md)  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ ملخص سريع (سطرين لكل سهم)

<!-- كرّر القسم لكل سهم في المحفظة -->

### {{CODE}} — {{NAME}} @ {{CLOSE}} · {{CHANGE_PCT}}%

| | |
|---|---|
| **Action** | **{{ACTION}}** |
| **Signal** | {{SIGNAL}} |
| **PnL** | {{PNL_EGP}} ج ({{PNL_PCT}}%) · قيمة {{VALUE_EGP}} ج |
| **Trigger القادم** | {{NEXT_TRIGGER}} |
| **Stop** | {{STOP}} · مسافة {{STOP_DIST}}% |

> {{ONE_LINE_VERDICT}}

---

## 2️⃣ جدول المحفظة — PnL

| الكود | Qty | Avg | Close | High | Low | Vol | PnL ج | PnL % | Value | {{SIGNAL}} |
|---|---|---|---|---|---|---|---|---|---|---|
| {{CODE}} | {{QTY}} | {{AVG}} | {{CLOSE}} | {{HIGH}} | {{LOW}} | {{VOL}} | | | | |

**إجمالي المحفظة:** {{TOTAL_VALUE}} ج · PnL: {{TOTAL_PNL}} ج ({{TOTAL_PNL_PCT}}%)

---

## 3️⃣ مستويات vs الخطة

| الكود | Close | دعم | مقاومة | Death/Gate | مسافة Stop | {{SIGNAL}} |
|---|---|---|---|---|---|---|
| {{CODE}} | | | | | | |

---

## 4️⃣ قرار اليوم — Action

| الكود | Action | السبب | مسموح | ممنوع |
|---|---|---|---|---|
| {{CODE}} | **{{ACTION}}** | {{REASON}} | {{ALLOWED}} | {{FORBIDDEN}} |

**Actions:** `HOLD` · `WAIT` · `ADD` · `REDUCE` · `EXIT` · `NO TRADE`

---

## 5️⃣ تنفيذ (لو في action)

| الكود | الأمر | النوع | السعر | الكمية | ملاحظة |
|---|---|---|---|---|---|
| {{CODE}} | | Limit Buy/Sell | | | |

> **Microcap rule:** Limit فقط · ممنوع Market على حجم كبير

---

## 6️⃣ سوق EGX

| المؤشر | Close | Change | ملاحظة |
|---|---|---|---|
| EGX30 | | | |
| EGX70 | | | |

| | |
|---|---|
| **Distribution days** | {{DD_COUNT}} / 25 جلسة |
| **Risk** | {{MARKET_RISK}} 🟢/🟡/🔴 |
| **تأثير على المحفظة** | {{PORTFOLIO_IMPACT}} |

---

## 7️⃣ أحداث اليوم

| الحدث | السهم | التأثير | Action |
|---|---|---|---|
| {{EVENT}} | {{CODE}} | | |

---

## 8️⃣ تنبيهات محدّثة

```
{{CODE}}: alert @ {{TRIGGER}} — {{TRIGGER_DESC}}
{{CODE}}: stop @ {{STOP}} — [valid / update to {{NEW_STOP}}]
{{CODE}}: cancel {{OLD_ALERT}} → new {{NEW_ALERT}}
```

---

## 9️⃣ Scorecard (لو توقع اتحقق/فشل)

| توقع سابق | المستوى | حصل؟ | ملاحظة |
|---|---|---|---|
| | | ✅ / ❌ / ⏳ | |

---

## 🔟 محفز Deep Dive

- [ ] كسر Death / Gate → Deep + Playbook
- [ ] حدث مؤسسي → Playbook
- [ ] لا — brief كافي اليوم

---

## الحكم النهائي

> **{{FINAL_VERDICT}}**

---

*Template v1 · Output Daily · Input: [`TEMPLATE-input-daily.md`](TEMPLATE-input-daily.md)*

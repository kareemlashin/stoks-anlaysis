# 📋 قوالب Workflow — Templates

> **قوالب ديناميكية** — تتعبّى كل أسبوع/يوم · **مش مربوطة بتاريخ ثابت**  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## إزاي تستخدم

| Template | متى | مين يعبّيه |
|---|---|---|
| [`TEMPLATE-input-daily.md`](TEMPLATE-input-daily.md) | كل يوم | **أنت** — المدخلات |
| [`TEMPLATE-daily-متابعة.md`](TEMPLATE-daily-متابعة.md) | كل يوم | **أنا** — المخرج |
| [`TEMPLATE-input-weekly.md`](TEMPLATE-input-weekly.md) | كل خميس | **أنت** — المدخلات |
| [`TEMPLATE-weekly-فحص.md`](TEMPLATE-weekly-فحص.md) | كل خميس | **أنا** — المخرج |
| [`symbols.txt.example`](symbols.txt.example) | weekly | قائمة 200 سهم |

### حفظ النسخة المعبّأة (optional)

```
متابعة-يومية/{{SESSION_DATE}}/متابعة-{{SESSION_DATE}}.md
فحص-أسبوعي/{{WEEK_DATE}}/فحص-{{WEEK_DATE}}.md
```

> `{{SESSION_DATE}}` = تاريخ جلسة الإغلاق · `{{WEEK_DATE}}` = تاريخ خميس الإغلاق الأسبوعي

---

## Placeholders

| Variable | معناه |
|---|---|
| `{{SESSION_DATE}}` | تاريخ جلسة اليوم |
| `{{WEEK_DATE}}` | تاريخ خميس الأسبوع |
| `{{CODE}}` | كود السهم |
| `{{NAME}}` | اسم الشركة |
| `{{QTY}}` | الكمية |
| `{{AVG}}` | متوسط الدخول |
| `{{CLOSE}}` | إغلاق |
| `{{HIGH}}` | أعلى |
| `{{LOW}}` | أدنى |
| `{{VOL}}` | حجم |
| `{{TRIGGER}}` | مستوى trigger |
| `{{STOP}}` | وقف |
| `{{SCORE}}` | نقاط الفحص |
| `{{TIER}}` | A/B/C/OUT |
| `{{ACTION}}` | HOLD/EXIT/... |
| `{{SIGNAL}}` | 🟢/🟡/🔴 |

---

## Workflow

```
Input template (أنت)  →  Analysis  →  Output template (أنا)
```

📖 [`WORKFLOW-daily-weekly.md`](../WORKFLOW-daily-weekly.md)

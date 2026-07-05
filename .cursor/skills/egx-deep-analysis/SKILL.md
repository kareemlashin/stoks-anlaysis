---
name: egx-deep-analysis
description: تحليل EGX عميق احترافي — 16 مرحلة · 100 أداة · 15 محترف · EV/R:R. لما المستخدم يبعت صور شارت أو يطلب رؤية شاملة. المدخل = صور (مفيش CSV).
---

# مهارة التحليل العميق — EGX

## متى تستخدم
- طلب تحليل شامل/عميق لأي سهم EGX
- سهم جديد خارج المتابعة اليومية
- trigger كبير (Gate · Death · AGM · نتائج)
- المستخدم يقول: رؤية شاملة · تحليل عميق · 100 أداة · محترفين

## Workflow (بالترتيب)

1. **حوكمة**
   - `_مشترك/pro/IPS-محفظتي.md` — الصفقة مسموحة؟
   - `_مشترك/pro/TEMPLATE-pre-mortem.md`
   - `_مشترك/pro/TEMPLATE-investment-thesis.md` (3 أعمدة)

2. **بيانات (صور أولاً)**
   - **أساسي:** سكرين شوتات — `_مشترك/استاندرد-تحليل-صور-EGX.md`
   - المستخدم **مش محتاج CSV** — استخرج O/H/L/C/Vol + المؤشرات
   - CSV/`analyze.py` = تحقق optional
   - ويب: `_مشترك/pro/مصادر-EGX.md`

3. **تحليل** — `_مشترك/استاندرد-الرؤية-الشاملة-لأي-سهم.md` (16 مرحلة)
   - Python **بس لو CSV موجود** · غير كده من OCR
   - `_مشترك/دليل-التحليلات-المدفوعة-الاحترافية.md`

4. **مخاطر**
   - PnL · size · scenarios · EV · R:R
   - `_مشترك/pro/TEMPLATE-risk-dashboard.md`

5. **مخرج**
   - `_مشترك/pro/TEMPLATE-deep-رؤية-شاملة.md`
   - `YYYY-MM-DD/تحليل-{{CODE}}-رؤية-شاملة-YYYY-MM-DD.md`
   - PNG · Scorecard

6. **قبل التسليم**
   - `_مشترك/pro/MASTER-CHECKLIST-تحليل-احترافي.md`

## أوامر Python (اختياري)

```bash
python _مشترك/tools/analyze.py pnl --qty Q --avg A --close C
python _مشترك/tools/analyze.py size --capital C --risk-pct 1.5 --entry E --stop S
```

## ملفات فرعية (لو التحليل كبير)
- `تحليل-{{CODE}}-100-اداة-{{DATE}}.md`
- `استراتيجيات-المحترفين-{{CODE}}-{{DATE}}.md`
- `{{CODE}}-playbook-{{EVENT}}-{{DATE}}.md`

## ممنوع
- تخطي أساسيات أو بحث ويب للأحداث
- شراء/بيع بدون trigger
- تجاهل qty × avg في PnL

**اللغة:** عربي مصري · تنويه في كل ملف

# 📥 INPUT — فحص أسبوعي (تجهيز شراء)

> **انسخ → عبّي → ابعت كل خميس** — بعد إغلاق شمعة Weekly

---

## رسالة سريعة

```
📅 weekly

السوق: EGX
الأسهم: {{COUNT}} (symbols.txt)
الفريمات: M · W · D · 4H · 1H
المدخلات: [CSV / صور]
فلتر: [VCP / breakout / mean-reversion / الكل]
Deep dive Top {{N}}: [نعم / لا]
رأس المال sizing: {{CAPITAL}} EGP
```

---

## هيكل المجلد (CSV)

```
فحص-أسبوعي/{{WEEK_DATE}}/
├── symbols.txt
├── _market/EGX30.csv          ← optional
└── data/
    ├── {{CODE}}_M.csv
    ├── {{CODE}}_W.csv
    ├── {{CODE}}_D.csv
    ├── {{CODE}}_4H.csv
    └── {{CODE}}_1H.csv
```

**CSV columns:** `time, open, high, low, close, volume`

---

## هيكل الصور (alternative)

```
فحص-أسبوعي/{{WEEK_DATE}}/charts/{{CODE}}/
├── M.png · W.png · D.png · 4H.png · 1H.png
```

---

## symbols.txt

```
{{CODE_1}}
{{CODE_2}}
...
# {{COUNT}} سطر
```

📄 نموذج: [`symbols.txt.example`](symbols.txt.example)

---

*Template · Input Weekly · [`TEMPLATE-weekly-فحص.md`](TEMPLATE-weekly-فحص.md) ← المخرج*

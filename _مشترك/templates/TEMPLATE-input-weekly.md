# 📥 INPUT — فحص أسبوعي (صور أو CSV)

> **الأسهل: صور Weekly + Daily** — CSV optional للـ `weekly_scan.py` بس

---

## رسالة سريعة (صور) ✅

```
📅 weekly
```

+ صور **W + D** لكل سهم (أو قائمة أسهم في رسالة)
+ optional: `symbols.txt` لو عندك 200 سهم

---

## رسالة سريعة (CSV — optional)

```
📅 weekly · CSV mode
```

```
فحص-أسبوعي/{{WEEK_DATE}}/
├── symbols.txt
└── data/{{CODE}}_D.csv ...
```

> CSV = للسcanner الآلي · **مش مطلوب** لو هتبعت صور

---

## هيكل الصور (preferred)

```
فحص-أسبوعي/{{WEEK_DATE}}/charts/{{CODE}}/
├── W.png
├── D.png
├── 4H.png    ← optional
└── 1H.png    ← optional
```

---

## symbols.txt (optional)

```
COMI
SWDY
EAC
...
```

---

*Input Weekly · Image-first · [`WORKFLOW-IMAGE-ONLY.md`](../WORKFLOW-IMAGE-ONLY.md)*

# 📥 INPUT — متابعة يومية

> **انسخ → عبّي → ابعت** — القالب ده للمدخلات بس

---

## رسالة سريعة

```
📆 daily

{{CODE}}: close={{CLOSE}} · high={{HIGH}} · low={{LOW}} · vol={{VOL}}
[{{CODE_2}}: close= · vol=]

حدث: [لا / {{EVENT}}]
سؤال: [optional]
```

---

## جدول (لو أكتر من سهم)

| الكود | Close | High | Low | Vol | حدث |
|---|---|---|---|---|---|
| {{CODE}} | | | | | |
| {{CODE_2}} | | | | | |

---

## مرفقات (optional)

- [ ] صورة Daily: `charts/{{CODE}}_D.png`
- [ ] CSV: `data/{{CODE}}_D.csv`

---

## مرجع المحفظة

> من [`محفظتي.md`](../محفظتي.md) — **مش لازم تكتبها كل يوم** إلا لو اتغيرت

| الكود | Qty | Avg |
|---|---|---|
| {{CODE}} | {{QTY}} | {{AVG}} |

---

*Template · Input Daily · [`TEMPLATE-daily-متابعة.md`](TEMPLATE-daily-متابعة.md) ← المخرج*

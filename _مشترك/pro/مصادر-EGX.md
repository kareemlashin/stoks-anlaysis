# 🔗 مصادر بيانات EGX — Data Sources

> **استخدم في Phase 1 (Data) و Phase 3 (Fundamentals)**  
> ⚠️ تحقق من الأرقام — AI ممكن يغلط في figures

---

## 📊 Price & Charts

| Source | URL | Use |
|---|---|---|
| **TradingView** | https://www.tradingview.com/symbols/EGX-{{CODE}}/ | Charts · CSV export |
| **Mubasher** | https://www.mubasher.info/countries/eg/stocks/{{CODE}} | Quotes · news · financials |
| **EGX Official** | https://www.egx.com.eg/ | Listings · indices |
| **Investing.com EGX** | https://www.investing.com/equities/ | Backup quotes |

**CSV export (TradingView):**
1. Open chart → right-click → Export chart data
2. Save as `{{CODE}}_D.csv` (columns: time, open, high, low, close, volume)
3. Repeat per timeframe: `_W`, `_M`, `_4H`, `_1H`

---

## 📰 Disclosures & News

| Source | URL | Use |
|---|---|---|
| **EGX News** | https://www.egx.com.eg/en/news.aspx | Official disclosures |
| **Company IR page** | (search: "{{NAME}} investor relations") | AGM · results |
| **Mubasher news** | mubasher.info | Arabic news flow |
| **Enterprise / Al Mal** | business news sites | Sector context |

**Search prompts (web):**
```
"{{CODE}}" site:egx.com.eg
"{{NAME}}" جمعية عمومية {{YEAR}}
"{{CODE}}" نتائج أعمال {{YEAR}}
"{{CODE}}" توزيعات أرباح
```

---

## 🏛️ Fundamentals

| Field | Primary source | Backup |
|---|---|---|
| Market cap / shares | Mubasher · EGX | TradingView |
| Ownership / free float | EGX disclosure · annual report | Mubasher |
| Financials | Company PDF · Mubasher | |
| Sector peers | EGX sector index · Mubasher sector | |

---

## 📅 Calendar

| Event type | Where to find |
|---|---|
| AGM / EGM | EGX disclosure · company IR |
| Dividend ex-date | EGX · Mubasher |
| Results | Quarterly IR · EGX |
| Rights / capital increase | EGX mandatory disclosure |

---

## 🌍 Market Context

| Index | Symbol (TV) | Use |
|---|---|---|
| EGX30 | EGX:EGX30 | Large cap regime |
| EGX70 | EGX:EGX70 | Broader market |
| Sector index | (if listed) | Relative strength |

**Distribution days:** count EGX30 down days on volume > prior on Daily — O'Neil rule (5 in 25 = caution)

---

## ⚙️ Local Project Paths

```
فحص-YYYY-MM-DD/
├── symbols.txt
├── data/{{CODE}}_W.csv
├── data/{{CODE}}_D.csv
└── _market/EGX30_W.csv

متابعة-يومية/YYYY-MM-DD/
└── charts/{{CODE}}_D.png
```

---

## ✅ Data Quality Checklist

- [ ] CSV has ≥ 200 bars on Weekly for MA200
- [ ] Volume column not all zeros
- [ ] Dates align with EGX calendar (Sun–Thu)
- [ ] Corporate action adjustment noted (bonus/split factor)
- [ ] Cross-check close vs Mubasher same day

---

*EGX Sources v1 · Update URLs if broken*

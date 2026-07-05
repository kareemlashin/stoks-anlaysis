# 🏆 Pro Analysis Kit — تحليل احترافي مؤسسي

> **الهدف:** تحلل أي سهم على EGX بنفس منهج أفضل المحللين — TA + Fundamentals + Risk + Execution  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 🗂️ ابدأ منين؟

| لو عايز... | افتح |
|---|---|
| **تحليل عميق لأول مرة** | [`MASTER-CHECKLIST-تحليل-احترافي.md`](MASTER-CHECKLIST-تحليل-احترافي.md) |
| **ملف المخرج الجاهز** | [`TEMPLATE-deep-رؤية-شاملة.md`](TEMPLATE-deep-رؤية-شاملة.md) |
| **Investment Thesis (3 أعمدة)** | [`TEMPLATE-investment-thesis.md`](TEMPLATE-investment-thesis.md) |
| **Pre-Mortem قبل أي صفقة** | [`TEMPLATE-pre-mortem.md`](TEMPLATE-pre-mortem.md) |
| **Playbook يوم حدث (AGM/نتائج)** | [`TEMPLATE-playbook-حدث.md`](TEMPLATE-playbook-حدث.md) |
| **Scorecard (توقعات vs واقع)** | [`TEMPLATE-scorecard.md`](TEMPLATE-scorecard.md) |
| **Trade Journal** | [`TEMPLATE-trade-journal.md`](TEMPLATE-trade-journal.md) |
| **Fundamentals EGX** | [`TEMPLATE-fundamentals-EGX.md`](TEMPLATE-fundamentals-EGX.md) |
| **Risk Dashboard المحفظة** | [`TEMPLATE-risk-dashboard.md`](TEMPLATE-risk-dashboard.md) |
| **قواعدك الشخصية (IPS)** | [`IPS-محفظتي.md`](IPS-محفظتي.md) |
| **مصادر بيانات EGX** | [`مصادر-EGX.md`](مصادر-EGX.md) |
| **🔬 بحث عميق Elite vs أنت** | [`DEEP-RESEARCH-2026-07-05.md`](DEEP-RESEARCH-2026-07-05.md) |
| **🌍 بحث عالمي شامل** | [`GLOBAL-RESEARCH-WORLD-2026.md`](GLOBAL-RESEARCH-WORLD-2026.md) |
| **🔌 Data APIs (Borsa/Stockastic)** | [`DATA-STACK-EGX.md`](DATA-STACK-EGX.md) |
| **Wyckoff 9 Tests** | [`TEMPLATE-wyckoff-9-tests.md`](TEMPLATE-wyckoff-9-tests.md) |
| **Murphy Intermarket Gate** | [`TEMPLATE-intermarket-EGX.md`](TEMPLATE-intermarket-EGX.md) |
| **Thesis Monitor 🚦** | [`TEMPLATE-thesis-monitor.md`](TEMPLATE-thesis-monitor.md) |
| **Quality of Earnings** | [`TEMPLATE-quality-of-earnings-EGX.md`](TEMPLATE-quality-of-earnings-EGX.md) |
| **Bayesian Update** | [`TEMPLATE-bayesian-update.md`](TEMPLATE-bayesian-update.md) |
| **IC Memo (one page)** | [`TEMPLATE-IC-memo.md`](TEMPLATE-IC-memo.md) |
| **SMB Playbook (10 variables)** | [`TEMPLATE-smb-playbook-trade.md`](TEMPLATE-smb-playbook-trade.md) |
| **📂 EAC live examples** | [`examples/EAC/README.md`](examples/EAC/README.md) |

---

## 🔄 ترتيب الاستخدام (Institutional Flow)

```
0. Intermarket gate   → TEMPLATE-intermarket-EGX.md (Murphy 2/3)
1. IPS check          → IPS-محفظتي.md
2. IC Memo draft      → TEMPLATE-IC-memo.md (one page)
3. Pre-Mortem         → TEMPLATE-pre-mortem.md
4. Investment Thesis  → TEMPLATE-investment-thesis.md (variant perception)
5. QoE                → TEMPLATE-quality-of-earnings-EGX.md
6. Wyckoff 9 tests    → TEMPLATE-wyckoff-9-tests.md (≥5/9)
7. Deep Analysis      → MASTER-CHECKLIST + TEMPLATE-deep-رؤية-شاملة
8. Event Playbook     → TEMPLATE-playbook-حدث.md (if catalyst)
9. Risk Dashboard     → TEMPLATE-risk-dashboard.md
10. Scorecard         → TEMPLATE-scorecard.md
11. Thesis Monitor    → TEMPLATE-thesis-monitor.md (each review)
12. Bayesian Update   → TEMPLATE-bayesian-update.md (each event)
13. SMB Playbook      → TEMPLATE-smb-playbook-trade.md (≥80/100)
14. Trade Journal     → TEMPLATE-trade-journal.md
```

---

## 🐍 أدوات Python

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Sample EAC CSV (if no TV export / Yahoo)
python _مشترك/tools/sample_data.py

# PnL + ضريبة + عمولة
python _مشترك/tools/analyze.py pnl --qty 128400 --avg 7.75 --close 7.38

# Position sizing (Minervini)
python _مشترك/tools/analyze.py size --capital 1000000 --risk-pct 1.5 --entry 7.75 --stop 7.25

# مؤشرات من CSV
python _مشترك/tools/analyze.py indicators --csv _مشترك/data/EAC_D.csv

# Wyckoff 9 tests (auto-score)
python _مشترك/tools/analyze.py wyckoff --csv _مشترك/data/EAC_D.csv --stop 7.25 --target 12.57

# Backtest MA/RSI/MACD
python _مشترك/tools/analyze.py backtest --csv _مشترك/data/EAC_D.csv

# Murphy intermarket (yfinance)
python _مشترك/tools/analyze.py macro

# Quote: Borsa local أو yfinance
python _مشترك/tools/analyze.py fetch --symbol EAC
python _مشترك/tools/analyze.py fetch --symbol EAC --save-csv _مشترك/data/EAC_D.csv

# Daily brief (quote + macro + TA)
python _مشترك/tools/analyze.py brief --symbol EAC --csv _مشترك/data/EAC_D.csv

# OpenBB (optional — falls back yfinance)
python _مشترك/tools/analyze.py openbb --symbol EAC

# فحص أسبوعي (موجود)
python _مشترك/weekly_scan.py --input فحص-YYYY-MM-DD --md نتيجة.md
```

---

## 🤖 Cursor Agents (تلقائي)

| Agent | متى |
|---|---|
| `egx-deep-dive` | تحليل 16 مرحلة لسهم واحد |
| `egx-daily-brief` | متابعة يومية المحفظة |
| `egx-weekly-scanner` | فحص 200 → Buy List |

---

## 🔗 مراجع مشتركة

- [`../استاندرد-الرؤية-الشاملة-لأي-سهم.md`](../استاندرد-الرؤية-الشاملة-لأي-سهم.md) — 16 مرحلة تفصيلية
- [`../WORKFLOW-daily-weekly.md`](../WORKFLOW-daily-weekly.md) — Daily · Weekly · Deep
- [`../templates/`](../templates/) — قوالب المتابعة اليومية والأسبوعية
- [`../دليل-التحليلات-المدفوعة-الاحترافية.md`](../دليل-التحليلات-المدفوعة-الاحترافية.md) — 150+ أداة

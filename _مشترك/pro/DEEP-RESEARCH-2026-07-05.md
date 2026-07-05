# 🔬 Deep Research — إيه اللي بيعمله أفضل محلل في العالم (2026)

> **تاريخ البحث:** 5 يوليو 2026  
> **المقارنة:** Institutional buy-side vs مشروعك الحالي  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 1️⃣ الـ Stack المؤسسي الكامل (5 طبقات)

أفضل المحللين **مش** بيعتمدوا على TA بس. عندهم 5 طبقات متسلسلة:

```
Governance → Data → Research → Risk → Monitor
```

| الطبقة | إيه اللي بيعملوه | عندك | الفجوة |
|--------|------------------|------|--------|
| **Governance** | IPS + Pre-mortem + IC Memo | ✅ IPS + Pre-mortem | 🟡 IC Memo ناقص |
| **Data** | Filings + API + Alt-data | 🟡 CSV manual | 🔴 Automation |
| **Research** | Thesis 3 pillars + Variant perception | ✅ Thesis template | 🟡 QoE ناقص |
| **Technical** | Wyckoff 9 tests + MTF + 100 tools | ✅ 16 مرحلة | 🟡 9 tests formal |
| **Risk** | EV + R:R + Position size + Stress | ✅ في الاستاندرد | 🟡 Stress test formal |
| **Monitor** | Traffic-light thesis + Bayesian update | 🟡 Scorecard | 🔴 Thesis monitor |

**المصادر:** [DataToBrief Thesis Framework](https://datatobrief.com/blog/how-to-build-investment-thesis-framework) · [Minalyst Due Diligence](https://minalyst.com/blog/research-guides/due-diligence-checklist) · [Equity Analyst Cheat Sheet](https://stocksunderrocks.substack.com/p/the-equity-analyst-cheat-sheet)

---

## 2️⃣ Investment Thesis — اللي بيفرق المحترف عن الهواة

### Variant Perception (3 مكونات إلزامية)

| # | السؤال | مثال EAC |
|---|--------|----------|
| 1 | **إيه consensus؟** | "Microcap مضاربي · AGM = pump then dump" |
| 2 | **إيه رأيك المختلف؟** | "Re-accumulation range · Spring 7.35 · catalyst 1:4" |
| 3 | **ليه الفجوة موجودة؟** | "السوق بي priced AGM كـ distribution مش re-accumulation" |

### Pre-Mortem (Gary Klein — institutional standard)

> "تخيّل بعد 18 شهر السهم نزل 50% — **إيه حصل بالظبط؟**"

- مش "risk section" عامة — **5 سيناريوهات محددة** باحتمال وخسارة بالجنيه
- Kill switches **automatic** — مفيش debate وقت الإ stress

### Thesis Monitor (Traffic Light — كل ربع / كل earnings)

| Pillar | Status | Action |
|--------|--------|--------|
| Pillar 1 | 🟢/🟡/🔴 | maintain / watch / reduce |
| Pillar 2 | | |
| Pillar 3 | | |

**قاعدة مؤسسية:** 2 quarters 🔴 متتاليين = **exit** (مش wait)

→ قالب: [`TEMPLATE-thesis-monitor.md`](TEMPLATE-thesis-monitor.md)

---

## 3️⃣ Due Diligence — 5 مراحل (Minalyst / Buy-side)

**الترتيب مهم** — اللي بيبدأ بـ valuation بيعمل reverse-engineering:

| Stage | Focus | EGX adaptation |
|-------|-------|----------------|
| **1. Business** | Revenue model · moat · customers | IR + Mubasher + annual report PDF |
| **2. Financials** | 5Y trends · FCF vs NI · accruals | QoE checklist |
| **3. Management** | Insider buying · governance · proxy | EGX ownership disclosures |
| **4. Risk** | Pre-mortem · regulatory · concentration | AGM · hot stock · price limits |
| **5. Valuation** | Comps · reverse DCF · sensitivity | P/E vs sector · reality ceiling |

→ قالب: [`TEMPLATE-quality-of-earnings-EGX.md`](TEMPLATE-quality-of-earnings-EGX.md)

---

## 4️⃣ Wyckoff — اللي معظم الـ TA guides بتتخطاه

**9 Buying Tests** (accumulation complete → markup):
1. Downside objective accomplished (P&F)
2. PS + SC + ST occurred
3. Bullish activity (vol up on rallies)
4. Downward stride broken
5. Higher lows
6. Higher highs
7. **Stronger than market** (RS vs EGX30)
8. Base forming (horizontal)
9. **Upside ≥ 3× stop risk**

**قاعدة Wyckoff:** ≥ **5/9 tests** قبل long — مش 2-3

**Selling tests:** 9 mirror tests للـ distribution

→ قالب: [`TEMPLATE-wyckoff-9-tests.md`](TEMPLATE-wyckoff-9-tests.md)  
**Quant spec:** [go-wyckoff WYCKOFF_SPEC](https://github.com/gopheroid/go-wyckoff/blob/main/docs/go-wyckoff/WYCKOFF_SPEC.md)

---

## 5️⃣ Wyckoff + SMC + Minervini — الـ Stack المدمج (Elite)

```
Wyckoff (W/M)     → WHY — phase: accumulation/markup/distribution
Minervini (W/D)   → WHAT — Trend Template 8/8 + VCP + RS
SMC (4H/1H)       → WHERE — Order Block · FVG · sweep · OTE
Raschke (1H)      → WHEN — first/last hour · Turtle Soup
```

**قاعدة ذهبية:** Wyckoff context **يحكم** على SMC — OB bullish في distribution = trap

---

## 6️⃣ Intermarket — Murphy Gate (قبل أي long جديد)

Murphy: **2/3 macro align** قبل long على سهم individual

| Market | EGX proxy | Bullish signal |
|--------|-----------|----------------|
| Bonds/Yields | US 10Y · Egypt T-bills trend | Yields falling = risk-on |
| Dollar | DXY | Weak USD = EM friendly |
| Commodities | Gold · Oil | Context for inflation |
| **Local** | EGX30 trend · EGX70 breadth | Index above MA · low dist days |

→ قالب: [`TEMPLATE-intermarket-EGX.md`](TEMPLATE-intermarket-EGX.md)

**Murphy watchlist يومي:** EGX30 · EGX70 · Gold · DXY · (Egypt yields if available)

---

## 7️⃣ Bayesian Updates — مش thesis ثابت

Elite analysts **يحدّثوا** conviction بعد كل datum:

```
Prior conviction: 7/10 (AGM catalyst)
+ Spring 7.35 confirmed     → +1
+ Vol still weak post-sweep → −0.5
+ EGX30 distribution day    → −1
Posterior conviction: 6.5/10
```

→ قالب: [`TEMPLATE-bayesian-update.md`](TEMPLATE-bayesian-update.md)

---

## 8️⃣ Investment Committee Memo — (PE/Hedge fund format)

صفحة واحدة للـ PM — even for personal portfolio:

| Section | Length |
|---------|--------|
| Executive Summary | 1 para |
| Variant Perception | 3 bullets |
| Bull / Base / Bear | table + IRR/PnL |
| Top 3 Risks + mitigants | |
| Recommendation | Proceed / Pass / Conditional |

→ قالب: [`TEMPLATE-IC-memo.md`](TEMPLATE-IC-memo.md)

---

## 9️⃣ EGX Data Stack — إيه المتاح فعلاً (2026)

| Source | Type | EGX | Cost | Use |
|--------|------|-----|------|-----|
| **TradingView CSV** | OHLCV | ✅ | Free | Primary TA |
| **Mubasher** | Quotes + news | ✅ | Free web | Fundamentals |
| **EGX disclosures** | Official | ✅ | Free | AGM · results |
| [**Borsa API**](https://github.com/7ashraf/borsa) | Self-hosted REST | ✅ 200+ | Free BYOK | Automation |
| [**Stockastic API**](https://stockastic.app/en/api-integration) | Sentiment + ratios | ✅ EGX100 | API tiers | Alt-data |
| [**EGXAPI**](https://egxapi.com/) | Trading + data | ✅ | Free tier | Paper trade + quotes |
| Bloomberg/Reuters | Institutional | ✅ | $20K+/yr | ❌ retail |

**التوصية:** Borsa (local) + Stockastic (sentiment) + TV CSV (precision)

→ دليل: [`DATA-STACK-EGX.md`](DATA-STACK-EGX.md)

---

## 🔟 Skills من ecosystem (global — adapt لـ EGX)

| Skill | Installs | Use |
|-------|----------|-----|
| `gracefullight/stock-checker@stock-analysis` | 10.8K | General framework |
| `gracefullight/stock-checker@trading-analysis` | 2.6K | TA workflow |
| `himself65/finance-skills@tradingview-reader` | 690 | TV integration |

```bash
npx skills add gracefullight/stock-checker@stock-analysis
npx skills add himself65/finance-skills@tradingview-reader
```

**ملاحظة:** مفيش skill EGX-native — **skill بتاعك** (`egx-deep-analysis`) أهم

---

## 1️⃣1️⃣ مقارنة: أنت vs Elite Analyst

| Capability | Elite | أنت | Gap priority |
|------------|-------|-----|--------------|
| 16-stage TA | 🟡 rare | ✅ **best-in-class** | — |
| 150+ paid tool simulation | ❌ | ✅ unique | — |
| 15 pros by name | 🟡 | ✅ | — |
| Investment Thesis + Variant | ✅ | ✅ template | Fill on use |
| Pre-mortem | ✅ | ✅ template | Fill on use |
| Wyckoff 9 tests formal | ✅ | 🟡 mentioned | **HIGH** |
| QoE / Accruals | ✅ | ❌ | **HIGH** |
| Thesis traffic-light monitor | ✅ | ❌ | **HIGH** |
| Bayesian conviction updates | ✅ | ❌ | **MEDIUM** |
| IC Memo one-pager | ✅ | ❌ | **MEDIUM** |
| Intermarket Murphy gate | ✅ | 🟡 in weekly | **MEDIUM** |
| Backtesting signals | ✅ | ❌ | **HIGH** |
| Automated EGX data | ✅ | ❌ | **HIGH** |
| Sentiment/NLP | ✅ | ❌ | **MEDIUM** (Stockastic) |
| Options flow / GEX | ✅ US | ❌ EGX | N/A for EGX |
| L2 order book | ✅ | 🟡 screenshot | EGX limited |

---

## 1️⃣2️⃣ الـ 10 قواعد اللي Elite بيطبقوها (ومذكورة عندك)

من [`دليل-التحليلات-المدفوعة`](../دليل-التحليلات-المدفوعة-الاحترافية.md) — **26 rule** — أهم 10:

1. Trigger-based — no "buy now" in mid-range
2. MTF No Alignment = No Trade
3. Don't decide at equilibrium (POC/AVWAP/mid)
4. Absorption ≠ direction until exit
5. SEPA 8-gate — skip any = skip trade
6. 7-8% stop universal (Minervini/IBD)
7. Effort vs Result (Wyckoff/VSA)
8. Confluence ≥ 3/5 independent sources
9. Intermarket 2/3 gate before new longs
10. EGX alt-data = disclosures not COT/options

---

## 1️⃣3️⃣ خطة إكمال الـ Elite Stack

### فوري (قوالب — اتضافت)
- [x] Wyckoff 9 tests
- [x] Intermarket EGX
- [x] Thesis monitor (traffic light)
- [x] Quality of earnings EGX
- [x] Bayesian update
- [x] IC Memo
- [x] DATA-STACK EGX

### قريب (Python)
- [ ] `wyckoff_tests.py` — score 0-9 from CSV
- [ ] `backtest_signals.py` — AVWAP/POC win rate on history
- [ ] `borsa_fetch.py` — auto quotes from Borsa API
- [ ] `intermarket_gate.py` — Murphy 2/3 check

### متوسط (Automation)
- [ ] MCP server for EGX data (Borsa / Stockastic)
- [ ] `/loop 1d` daily brief after 14:30
- [ ] Hook: block analysis without trigger in output

---

## 1️⃣4️⃣ Golden Chart Rule (Institutional)

> **Every elite report has ONE chart** that tells the whole story in 30 seconds.

Examples:
- EAC: AVWAP anchors + Spring zone + AGM date vertical line
- COMI: RS line vs EGX30 + VCP contractions count
- Growth stock: Revenue + margin expansion 5Y

**Action:** every deep analysis must include **Golden Chart** PNG identified in thesis.

---

## 🔗 References

- [Investment Thesis Framework — DataToBrief](https://datatobrief.com/blog/how-to-build-investment-thesis-framework)
- [Due Diligence Checklist 2026 — Minalyst](https://minalyst.com/blog/research-guides/due-diligence-checklist)
- [Equity Analyst Cheat Sheet — Stocks Under Rocks](https://stocksunderrocks.substack.com/p/the-equity-analyst-cheat-sheet)
- [Wyckoff 9 Tests — Wyckoff Analytics PDF](https://www.wyckoffanalytics.com/wp-content/uploads/2022/06/Wyckoff-Method-Wyckoff-Analytics-English-V2.pdf)
- [Borsa EGX API — GitHub](https://github.com/7ashraf/borsa)
- [Stockastic EGX API](https://stockastic.app/en/api-integration)
- [EGXAPI Trading API](https://egxapi.com/)
- [Murphy Intermarket — StockCharts](https://chartschool.stockcharts.com/table-of-contents/market-analysis/intermarket-analysis)

---

*Deep Research v1 · Pro Kit extension*

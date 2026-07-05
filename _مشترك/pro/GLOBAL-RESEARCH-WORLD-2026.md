# 🌍 GLOBAL RESEARCH — أفضل محلل في العالم (World Map 2026)

> **بحث شامل** من مصادر عالمية: Wall Street · Hedge Funds · CFA · Quant · Alt-Data · EGX  
> **تاريخ:** 5 يوليو 2026  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## 🗺️ الخريطة الكاملة — 7 عوالم

```
1. INSTITUTIONAL TERMINALS    → Bloomberg · FactSet · Capital IQ
2. AI RESEARCH PLATFORMS      → AlphaSense · Hebbia · Tegus
3. TECHNICAL / SCANNING       → TrendSpider · TC2000 · Trade Ideas
4. FUNDAMENTALS / DATA        → Koyfin · GuruFocus · OpenBB · yfinance
5. QUANT / BACKTEST           → QuantConnect LEAN · Backtrader
6. ALT-DATA / SENTIMENT       → Similarweb · Satellite · Veil · Stockastic
7. PROCESS / DISCIPLINE       → CFA · SMB Playbook · Edgewonk · Wyckoff
```

**مشروعك (`stoks-analysis`)** = عالم 3 + 7 + جزء من 6 — **فوق 95% retail**  
**الفجوة** = عوالم 1 · 2 · 4 · 5 · 6 (automation)

---

## 1️⃣ Institutional Terminals ($$$)

| Platform | Cost/yr | Best for | EGX |
|----------|---------|----------|-----|
| [Bloomberg Terminal](https://www.bloomberg.com/professional/solution/bloomberg-terminal/) | ~$24K+ | Real-time · IB chat · news · execution | ✅ full |
| [FactSet](https://www.factset.com/) | Modular | Buy-side · Excel · portfolio analytics | ✅ |
| [S&P Capital IQ Pro](https://www.spglobal.com/marketintelligence/) | Enterprise | Comps · screening · credit | ✅ |
| [Refinitiv Eikon](https://www.refinitiv.com/) | Institutional | Cross-asset · news | ✅ |

**Budget alternative:** [Koyfin](https://www.koyfin.com/) ~$35-50/mo — charts · screening · fundamentals  
**EGX budget:** Mubasher + TradingView + Borsa API (see [`DATA-STACK-EGX.md`](DATA-STACK-EGX.md))

---

## 2️⃣ AI Research Platforms (2026 wave)

| Platform | Cost | What it does | Link |
|----------|------|--------------|------|
| [AlphaSense](https://www.alpha-sense.com/) | $15K-50K+/yr | 500M docs · earnings agents · Tegus transcripts | Enterprise |
| [Hebbia](https://www.hebbia.com/) | $30K-500K/yr | Multi-doc AI reasoning · matrix analysis | Hedge funds |
| [Tegus](https://www.tegus.com/) | Enterprise | Expert call transcripts · primary research | PE/HF |
| [Koyfin](https://www.koyfin.com/) | ~$40/mo | AI screening · charts · NOT deep doc search | Retail/pro |
| [Fiscal.ai](https://fiscal.ai/) | Subscription | Conversational fundamentals · stress tests | Retail |
| [FinChat](https://finchat.io/) | Tiered | Chat with financials | Retail |

**Hedge fund AI stack 2026** ([source](https://www.tommasomariaricci.com/blog/ai-for-hedge-funds)):
```
Research:  Hebbia / AlphaSense ($30K-500K)
Drafting:  ChatGPT Enterprise / Claude for Work
Risk:      MSCI Risk Insights / Axioma
Surveillance: SteelEye / NICE Actimize
Alpha:     Proprietary stack on cloud GPU (not off-shelf)
```

**EGX substitute:** Cursor + your `egx-deep-dive` agent + web search + Stockastic API

---

## 3️⃣ Technical Analysis & Scanning (Global)

| Platform | $/mo | Strength | Backtest | EGX |
|----------|------|----------|----------|-----|
| [TrendSpider](https://trendspider.com/) | $52-155 | MTF · AI patterns · NLP scanner | ✅ 50yr | 🟡 limited |
| [TradingView](https://www.tradingview.com/) | $0-60 | Global markets · Pine Script | 🟡 | ✅ **primary** |
| [TC2000](https://www.tc2000.com/) | $10-100 | EasyScan speed · US focus | ❌ | ❌ |
| [Trade Ideas](https://www.tradeideas.com/) | $127-254 | Holly AI signals | ✅ OddsMaker | ❌ US |
| [Finviz Elite](https://finviz.com/) | $39.50 | Heatmap · 70+ filters | 🟡 basic | 🟡 US |
| [MarketSurge/IBD](https://www.investors.com/product/marketsurge/) | ~$150 | CANSLIM · VCP · RS | 🟡 | ❌ US |
| [Stock Rover](https://www.stockrover.com/) | $0-280/yr | Fundamentals + TA US | 🟡 | ❌ |

**Winner 2026 tests:** TrendSpider (systematic) · TradingView (global) · Finviz (free visual)

**أنت:** تحاكي TrendSpider + MarketSurge + LuxAlgo + Holly **بالكود** — [`دليل-التحليلات-المدفوعة`](../دليل-التحليلات-المدفوعة-الاحترافية.md)

---

## 4️⃣ Fundamentals & Free Data Stack

### Open Source (Python)

| Tool | Use | Install |
|------|-----|---------|
| [OpenBB](https://github.com/OpenBB-finance/OpenBB) | Unified API: yfinance · FMP · Polygon · SEC | `pip install openbb` |
| [yfinance](https://github.com/ranaroussi/yfinance) | Yahoo OHLCV · fundamentals | `pip install yfinance` |
| [pandas-ta](https://github.com/twopirllc/pandas-ta) | 130+ indicators | pip |
| [ta-lib](https://ta-lib.org/) | Industry standard indicators | brew + pip |

```python
# OpenBB example
from openbb import obb
df = obb.equity.price.historical("AAPL", provider="yfinance", start_date="2024-01-01").to_df()
```

### Paid fundamentals (global)

| Platform | Focus |
|----------|-------|
| [GuruFocus](https://www.gurufocus.com/) | Value · guru portfolios · Buffett tracker |
| [Stockopedia](https://www.stockopedia.com/) | Factor scores · UK/EU/US |
| [Simply Wall St](https://simplywall.st/) | Visual fundamentals |
| [Morningstar Direct](https://www.morningstar.com/products/direct) | Funds · institutional |

---

## 5️⃣ Quant & Backtesting

| Platform | Language | Cost | Best for |
|----------|----------|------|----------|
| [QuantConnect LEAN](https://github.com/QuantConnect/Lean) | Python/C# | Free OSS + cloud tiers | Institutional backtest |
| [Backtrader](https://www.backtrader.com/) | Python | Free | Simple strategies |
| TrendSpider Strategy Tester | No-code | $52+/mo | Visual backtest |
| [Portfolio123](https://www.portfolio123.com/) | Rules | ~$50/mo | Factor screening US |

```bash
pip install lean
lean research   # Jupyter
lean backtest   # local Docker
```

**EGX gap:** LEAN has no native EGX — use your CSV + custom `backtest_signals.py`

---

## 6️⃣ Alternative Data (90% of funds use it — 2025 survey)

| Data type | Examples | EGX applicable? |
|-----------|----------|-----------------|
| Web traffic | Similarweb | 🟡 if company has web |
| Credit card | Second Measure | ❌ US |
| Satellite | Orbital Insight · SpaceKnow | 🟡 factories · agriculture |
| Sentiment/NLP | Stockastic · Veil · TradeAlgo | 🟡 Stockastic EGX100 |
| Insider trades | SEC Form 4 | 🟡 EGX disclosures instead |
| Social | StockTwits · Reddit | 🟡 low EGX coverage |
| Geolocation | foot traffic | ❌ US retail |

**EGX alt-data substitutes:**
- EGX official disclosures (instead of SEC)
- Mubasher news flow
- Stockastic sentiment API
- Block trade reports (if available from broker)

Sources: [Mondaq Alt-Data Report 2025](https://www.mondaq.com/pdf/alt-data-report-2025_final.pdf) · [Similarweb](https://www.similarweb.com/blog/investor/asset-research/what-is-alternative-data/)

---

## 7️⃣ Professional PROCESS (most important)

### CFA Institute — 5-step valuation

1. Understand the business
2. Forecast performance
3. Select valuation model
4. Convert to valuation
5. Apply recommendations

**Report sections:** Business · Industry · Investment Summary · Valuation · Financial Analysis · Risks · ESG  
Source: [CFA Equity Research Essentials (PDF)](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf)

### Investment Thesis — 4 phases (institutional)

1. Idea generation (7+ channels)
2. Thesis construction (3-5 pillars + **variant perception**)
3. Stress-test (**pre-mortem** · devil's advocate · scenarios)
4. Monitor (**traffic light** 🟢🟡🔴 quarterly)

Source: [DataToBrief Thesis Framework](https://datatobrief.com/blog/how-to-build-investment-thesis-framework)

### Due Diligence — 5 stages (Minalyst)

1. Business understanding
2. Financial statements (5Y · FCF vs NI · accruals)
3. Management & governance
4. Risk assessment
5. Valuation

Source: [Minalyst Checklist 2026](https://minalyst.com/blog/research-guides/due-diligence-checklist)

### Wyckoff — 9 Buying Tests (≥5/9 to enter)

1. Downside objective done
2. PS + SC + ST
3. Bullish volume activity
4. Downward stride broken
5. Higher lows
6. Higher highs
7. Stronger than market
8. Base forming
9. Upside ≥ 3× stop risk

Source: [Wyckoff Analytics PDF](https://www.wyckoffanalytics.com/wp-content/uploads/2022/06/Wyckoff-Method-Wyckoff-Analytics-English-V2.pdf)  
→ [`TEMPLATE-wyckoff-9-tests.md`](TEMPLATE-wyckoff-9-tests.md)

### SMB Capital Playbook — 10 variables per trade

1. Big Picture · 2. Intraday Fundamentals · 3. Reading the Tape  
4. Risk Management · 5. Trade Strategy · 6. Technical Analysis  
7. Stock Selection · 8. Diligence · 9. Trade Review · 10. Technology  

**Score ≥80/100 = professional execution**  
**Need 50-100 samples per setup before playbook is valid**  
Source: [SMB Training](https://www.smbtraining.com/blog/how-to-become-a-consistently-profitable-trader) · Mike Bellafiore *The Playbook*

### Trading Journals (discipline)

| App | $/yr | Best for |
|-----|------|----------|
| [TraderSync](https://tradersync.com/) | $360-960 | AI Cypher · 900 brokers · replay |
| [Edgewonk](https://edgewonk.com/) | $197 | Tiltmeter psychology · deep stats |
| [Tradervue](https://www.tradervue.com/) | $360 | Industry standard |
| [TradeZella](https://www.tradezella.com/) | $348 | Day traders |

→ Your substitute: [`TEMPLATE-trade-journal.md`](TEMPLATE-trade-journal.md)

---

## 8️⃣ Intermarket — John Murphy (global macro gate)

| Relationship | Classic correlation |
|--------------|---------------------|
| Bonds ↑ → Stocks ↑ | Risk-on lead |
| Dollar ↑ → Commodities ↓ | Inverse |
| Commodities ↑ → Bonds ↓ | Inflation |
| VIX ↑ → Stocks ↓ | Fear |

**Murphy rule:** Monitor daily · 2/3 align before new longs  
Source: [StockCharts Intermarket](https://chartschool.stockcharts.com/table-of-contents/market-analysis/intermarket-analysis)  
→ [`TEMPLATE-intermarket-EGX.md`](TEMPLATE-intermarket-EGX.md)

---

## 9️⃣ Frontier Markets (EGX = frontier class)

**3-layer framework** ([StockAlpha](https://stockalpha.ai/alpha-learning/frontier-markets-hidden-investment-opportunities-at-the-edge-of-the-global-econo)):

| Layer | EGX application |
|-------|-----------------|
| **Macro** | EGP · CBE rates · inflation · political |
| **Market structure** | Free float · foreign ownership · settlement T+2 |
| **Corporate quality** | Governance · related-party · transparent financials |

**Liquidity rules (institutional):**
- Min ADV turnover: $1M-7M/day (WFE survey)
- Limit orders · 2-3 tranches · exit ≤ 3 days
- Wider bid-ask · scenario stress tests

**You already have this** in IPS + microcap rules + [`WORKFLOW-daily-weekly.md`](../WORKFLOW-daily-weekly.md)

---

## 🔟 EGX-Specific Global Tools

| Tool | URL | Type |
|------|-----|------|
| [Borsa API](https://github.com/7ashraf/borsa) | GitHub | Self-hosted EGX quotes |
| [Stockastic](https://stockastic.app/) | Web/API | EGX100 sentiment + ratios |
| [EGXAPI](https://egxapi.com/) | API | Paper + live EGX |
| Mubasher | mubasher.info | Retail standard Egypt |
| TradingView | EGX symbols | Charts + CSV |

---

## 📊 GLOBAL vs YOUR STACK — Final Scorecard

| Capability | Wall Street | Your Project | Gap |
|------------|-------------|--------------|-----|
| Real-time terminal | Bloomberg | TV + manual | 🟡 |
| AI doc research | AlphaSense | Cursor agents | 🟡 |
| TA depth (100 tools) | TrendSpider partial | ✅ **exceeds** | — |
| Paid tool simulation | ❌ none | ✅ **unique** | — |
| 15 pro strategies | Books/courses | ✅ coded | — |
| Fundamentals QoE | FactSet | 🟡 template | fill |
| Backtesting | QuantConnect | ❌ | build |
| Alt-data | $1M budgets | Stockastic | 🟡 |
| Playbook discipline | SMB | 🟡 playbook template | fill |
| Journal/analytics | Edgewonk | 🟡 template | fill |
| Frontier liquidity rules | Meketa/WFE | ✅ IPS | — |
| Wyckoff 9 tests | Wyckoff Analytics | ✅ template | code |
| IC Memo / Thesis monitor | Every fund | ✅ templates | fill |

---

## 🎯 Top 20 Global Resources (bookmark list)

### Must-read (free)
1. [CFA Equity Research Essentials PDF](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/research-challenge/challenge/rc-equity-research-report-essentials.pdf)
2. [Wyckoff Method PDF](https://www.wyckoffanalytics.com/wp-content/uploads/2022/06/Wyckoff-Method-Wyckoff-Analytics-English-V2.pdf)
3. [Murphy Intermarket — StockCharts](https://chartschool.stockcharts.com/table-of-contents/market-analysis/intermarket-analysis)
4. [Minalyst Due Diligence 2026](https://minalyst.com/blog/research-guides/due-diligence-checklist)
5. [DataToBrief Investment Thesis](https://datatobrief.com/blog/how-to-build-investment-thesis-framework)
6. [Equity Analyst Cheat Sheet](https://stocksunderrocks.substack.com/p/the-equity-analyst-cheat-sheet)

### Must-use (free code)
7. [OpenBB Platform](https://github.com/OpenBB-finance/OpenBB)
8. [yfinance](https://github.com/ranaroussi/yfinance)
9. [QuantConnect LEAN](https://github.com/QuantConnect/Lean)
10. [Borsa EGX API](https://github.com/7ashraf/borsa)

### Books (pro canon)
11. *The Playbook* — Mike Bellafiore (SMB Capital)
12. *Trading with Intermarket Analysis* — John Murphy
13. *Trade Like a Stock Market Wizard* — Mark Minervini
14. *Reminiscences of a Stock Operator* — Livermore
15. *Thinking in Bets* — Annie Duke (Bayesian)

### Platforms (if budget allows)
16. TradingView Pro — EGX charts
17. Koyfin — fundamentals global
18. TrendSpider — backtest US strategies (port logic to EGX)
19. Stockastic API — EGX sentiment
20. Edgewonk — journal psychology

---

## 🚀 Recommended Global Stack for EGX (practical)

```
FREE TIER ($0/mo):
  TradingView CSV + Mubasher + EGX disclosures
  + OpenBB/yfinance (macro: DXY, gold, yields)
  + Your Python tools (_مشترك/tools/)
  + Cursor agents (egx-deep-dive)
  + All pro templates (_مشترك/pro/)

MID TIER (~$50-100/mo):
  + TradingView Pro
  + Stockastic API (EGX100 sentiment)
  + Edgewonk journal ($197/yr)

PRO TIER (~$200+/mo):
  + TrendSpider (backtest logic port)
  + Koyfin (fundamentals)
  + Borsa self-hosted automation

INSTITUTIONAL ($20K+/yr):
  Bloomberg / FactSet — only if managing others' money
```

---

## 📁 Related files in this project

| File | Content |
|------|---------|
| [`DEEP-RESEARCH-2026-07-05.md`](DEEP-RESEARCH-2026-07-05.md) | Institutional vs you (first research) |
| [`DATA-STACK-EGX.md`](DATA-STACK-EGX.md) | EGX APIs |
| [`pro/README.md`](README.md) | All templates index |
| [`../دليل-التحليلات-المدفوعة`](../دليل-التحليلات-المدفوعة-الاحترافية.md) | 150+ paid tools catalog |

---

*Global Research v1 · Sources: AlphaSense · Hebbia · CFA · Wyckoff Analytics · Murphy · SMB · Minalyst · WFE · OpenBB · QuantConnect · Mondaq Alt-Data 2025*

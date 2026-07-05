# 🔌 DATA STACK — EGX Automation Guide

> **Goal:** move from manual CSV → semi-automated pipeline  
> ⚠️ Verify all API terms · numbers need human check

---

## Tier 1 — Free (use now)

| Tool | URL | What you get | Setup |
|------|-----|--------------|-------|
| **TradingView** | tradingview.com | OHLCV CSV export | Manual export per TF |
| **Mubasher** | mubasher.info | Quotes · news · financials | Web |
| **EGX Official** | egx.com.eg | Disclosures · indices | Web |

---

## Tier 2 — API (automate)

### Borsa (self-hosted — recommended)

- **Repo:** https://github.com/7ashraf/borsa
- **Coverage:** 200+ EGX symbols
- **Providers:** Alpha Vantage · Finnhub · Yahoo (BYOK)
- **Endpoints:** `/v1/quote/{symbol}` · batch quotes

```bash
git clone https://github.com/7ashraf/borsa
cd borsa && cp .env.example .env
# Add ALPHA_VANTAGE_KEY or FINNHUB_KEY
docker compose up
curl localhost:8000/v1/quote/COMI
```

**Use in project:** daily close fetch → auto-fill daily brief input

---

### Stockastic (EGX100 fundamentals + sentiment)

- **URL:** https://stockastic.app/en/api-integration
- **API base:** `https://api.stockastic.app/v1/`
- **Endpoints:**
  - `GET /newsapi/headlines?companies=AMER.EGX` — sentiment
  - `GET /companies/{Ticker}/financial-ratios`
  - `GET /companies/{Ticker}/trend-analysis`
- **Limits:** 300-1000 req/day by endpoint

**Use:** fundamentals template auto-fill · news sentiment flag

---

### EGXAPI (trading + market data)

- **URL:** https://egxapi.com/
- **Features:** REST orders · WebSocket quotes · paper trading
- **Status:** EGX equities live · free tier

**Use:** paper-test triggers · live quotes without manual TV

---

## Tier 3 — Institutional (reference only)

| Tool | Cost | EGX |
|------|------|-----|
| Bloomberg Terminal | ~$24K/yr | ✅ full |
| Refinitiv Eikon | Institutional | ✅ |
| Bookmap L2 | $49+/mo | ❌ no EGX L2 |

---

## Recommended Pipeline

```
┌─────────────┐     ┌──────────┐     ┌─────────────────┐
│ Borsa API   │────▶│ analyze  │────▶│ Daily Brief MD  │
│ (quotes)    │     │ .py      │     │                 │
└─────────────┘     └──────────┘     └─────────────────┘
┌─────────────┐            │
│ TV CSV (W/D)│────────────┤
└─────────────┘            ▼
┌─────────────┐     ┌──────────────────┐
│ Stockastic  │────▶│ Fundamentals MD  │
│ (ratios)    │     │                  │
└─────────────┘     └──────────────────┘
```

### CLI commands (implemented)

```bash
source .venv/bin/activate   # project venv

python _مشترك/tools/analyze.py fetch --symbol EAC --save-csv _مشترك/data/EAC_D.csv
python _مشترك/tools/analyze.py wyckoff --csv _مشترك/data/EAC_D.csv --stop 7.25 --target 12.57
python _مشترك/tools/analyze.py backtest --csv _مشترك/data/EAC_D.csv
python _مشترك/tools/analyze.py macro
python _مشترك/tools/analyze.py brief --symbol EAC --csv _مشترك/data/EAC_D.csv
python _مشترك/tools/sample_data.py   # EAC not on Yahoo — fallback anchors
```

---

## MCP / Agent Integration (future)

```json
// .cursor/mcp.json concept
{
  "borsa": { "url": "http://localhost:8000" },
  "stockastic": { "apiKey": "..." }
}
```

Agent prompt: "Fetch COMI quote from Borsa + fill TEMPLATE-fundamentals"

---

## Data Quality Rules

1. **Cross-check** Borsa close vs Mubasher same day
2. **Corporate actions** — adjust levels × factor after bonus/split
3. **Never trust AI numbers** — verify against source PDF
4. **CSV > API > screenshot** for TA precision

---

## Skills to install (global TA)

```bash
npx skills add gracefullight/stock-checker@stock-analysis
npx skills add himself65/finance-skills@tradingview-reader
```

Project skill (already local): `.cursor/skills/egx-deep-analysis/`

---

*DATA STACK v1 · July 2026*

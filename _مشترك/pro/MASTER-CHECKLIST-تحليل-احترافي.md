# ✅ MASTER CHECKLIST — تحليل احترافي (Institutional Grade)

> **استخدمه قبل تسليم أي تحليل.** كل بند إلزامي إلا لو مكتوب "optional".  
> 📋 المخرج: [`TEMPLATE-deep-رؤية-شاملة.md`](TEMPLATE-deep-رؤية-شاملة.md)  
> ⚠️ تحليل تعليمي — مش نصيحة استثمارية

---

## Phase 0 — Governance (قبل ما تفتح الشارت)

- [ ] **IPS:** قرأت [`IPS-محفظتي.md`](IPS-محفظتي.md) — الصفقة مسموحة؟
- [ ] **Pre-Mortem:** [`TEMPLATE-pre-mortem.md`](TEMPLATE-pre-mortem.md) — 3+ طرق الفكرة تموت
- [ ] **Investment Thesis:** [`TEMPLATE-investment-thesis.md`](TEMPLATE-investment-thesis.md) — 3 أعمدة + invalidation
- [ ] **Market Regime:** EGX30/70 · distribution days · Risk 🟢/🟡/🔴
- [ ] **Liquidity gate:** avg daily vol × close ≥ 3× حجم مركزك؟

---

## Phase 1 — Data Quality (جودة البيانات)

- [ ] **CSV preferred:** TradingView export (time, OHLC, volume) لكل فريم
- [ ] **الفريمات:** M → W → D → 4H → 1H (أو 15m) — كل المتاح
- [ ] **Order book** (optional): bid/ask walls · spoofing · absorption
- [ ] **مركز المستخدم:** qty × avg entry — كل الأرقام بالجنيه
- [ ] **مصادر EGX:** [`مصادر-EGX.md`](مصادر-EGX.md) — إفصاحات · AGM · نتائج

---

## Phase 2 — Technical (16 Layer Stack)

### 2A — Multi-Timeframe Structure
- [ ] جدول لقطة واحدة: RSI · StochRSI · MACD · BBW × كل الفريمات
- [ ] دعوم + مقاومات من الشموع (مصدر كل مستوى)
- [ ] MTF alignment: W/D/4H نفس الاتجاه؟ (TrendSpider rule: No Alignment = No Trade)

### 2B — 100 Tools (Python)
- [ ] 8 مجموعات: Momentum · Trend · Volume · Volatility · SMC · Waves · Systems · Profile
- [ ] عد نهائي 🟢/🟡/🔴 + درجة aggregate
- [ ] Confluence: مستويات 4+ مدارس متفقة

### 2C — Paid Tools Simulation
- [ ] SMC/ICT map · WaveTrend · TTM Squeeze · AVWAP (Shannon) · DeMark · Order Flow logic
- [ ] مرجع: [`../دليل-التحليلات-المدفوعة-الاحترافية.md`](../دليل-التحليلات-المدفوعة-الاحترافية.md)

### 2D — 15 Professionals (by name, by numbers)
- [ ] Minervini · Qullamaggie · Wyckoff · O'Neil · Weinstein · Darvas · Livermore
- [ ] Shannon · Al Brooks · Raschke · Connors · Williams · Brandt · Douglas · Gann/Elliott/Hosoda
- [ ] **حكم كل محترف على وضع المستخدم** (qty × avg)

### 2E — Patterns + Maker Behavior
- [ ] كل النماذج الكلاسيكية على كل TF
- [ ] Maker fingerprint: freeze · sweep · absorption · defense zones
- [ ] **Historical cycle match:** دورة سابقة مشابهة؟ (مثل EAC 2024)

---

## Phase 3 — Fundamentals & Off-Chart

- [ ] [`TEMPLATE-fundamentals-EGX.md`](TEMPLATE-fundamentals-EGX.md) مكتمل
- [ ] أخبار + إفصاحات + AGM/EGM + توزيعات (معامل تعديل المستويات)
- [ ] Sector peers: رايد موجة قطاع ولا لعبة منفردة؟
- [ ] Hidden costs: ضريبة · عمولة · T+2 · price limits · hot stock rules

---

## Phase 4 — Targets & Scenarios

- [ ] أهداف: Hosoda · Elliott · Gann · Murrey · Darvas · Fib · P&F · AB=CD
- [ ] **Clusters:** 3+ أدوات على نفس السعر = هدف حقيقي
- [ ] **Reality ceiling:** مكرر ربحية عند أعلى هدف — منطقي؟
- [ ] 3–4 سيناريوهات: احتمال % · PnL بالجنيه · **EV** · **R:R ≥ 2:1**

---

## Phase 5 — Risk & Execution

- [ ] Position size: (capital × risk%) ÷ stop distance
- [ ] Liquidity exit: المركز يتباع في كام يوم؟
- [ ] [`TEMPLATE-risk-dashboard.md`](TEMPLATE-risk-dashboard.md) — exposure check
- [ ] جدول قرارات جاهز: كل حدث → تصرف + سعر + qty
- [ ] تنبيهات TradingView جاهزة للنسخ
- [ ] Raschke timing: قرارات كبيرة أول/آخر ساعة — مش وسط الجلسة
- [ ] **Microcap:** Limit فقط · 2–3 دفعات · ممنوع market blind

---

## Phase 6 — Deliverables

- [ ] `تحليل-{{CODE}}-رؤية-شاملة-{{DATE}}.md`
- [ ] PNG charts (SMC · 100 tools · MTF · decision map)
- [ ] Playbook لو حدث: [`TEMPLATE-playbook-حدث.md`](TEMPLATE-playbook-حدث.md)
- [ ] Scorecard update: [`TEMPLATE-scorecard.md`](TEMPLATE-scorecard.md)
- [ ] **الحكم النهائي في سطرين** (blockquote)
- [ ] Disclaimer في كل ملف

---

## 🚫 Red Flags — توقف فوراً

| Flag | Action |
|---|---|
| EV سالب | "الصفقة رياضياً خسرانة" — لا long جديد |
| R:R < 2:1 | تحذير صريح |
| Distribution days ≥ 5 | ممنوع longs جديدة (O'Neil) |
| Liquidity < 1 day exit | تقليل حجم أو ممنوع |
| Thesis invalidated | EXIT plan — مش hope |
| Pre-mortem hit | أعد التحليل أو abort |

---

## 📊 Quality Score (self-grade قبل التسليم)

| Dimension | /10 | Notes |
|---|---|---|
| Data quality | | |
| MTF alignment | | |
| 100 tools computed | | |
| Fundamentals | | |
| Risk/EV/R:R | | |
| Execution plan | | |
| **Total** | **/60** | ≥48 = institutional grade |

---

*Master Checklist v1 · Pro Kit · 2026-07-05*

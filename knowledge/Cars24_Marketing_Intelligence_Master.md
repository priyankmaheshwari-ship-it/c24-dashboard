---
title: Cars24 Marketing Intelligence — Master Reference
compiled: April 2026
owner: Priyank Maheshwari · Demand Strategy & Transformation · Cars24
scope: office-only — all Cars24 marketing context, artefacts, data, and team knowledge
source: Cars24-MKTing skill + project conversations (Apr 2026)
---

# Cars24 Marketing Intelligence — Complete Master Reference

> Everything learned from Priyank and the team in April 2026. Covers business context, funnel metrics, channel data, team-sourced knowledge (Adhiraj/CRM, Neel/Affiliates, Naseem/GMB, Kripa/Reviews, Tanishka/BI), Snowflake schema, SQL queries, dashboards built, data files analysed, and the Demand Command Centre project.

---

## TABLE OF CONTENTS

1. Company Overview & Business Model
2. Priyank's Project — Demand Command Centre
3. The Funnel — End to End (with Mar'26 actuals)
4. Acronyms & Definitions
5. Channel Structure & Performance (Mar'26)
6. 24-Month Trend Data
7. Data Sources & Attribution Models
8. CRM Channel — Adhiraj's Context
9. C2B Affiliates — Neel's Context
10. GMB + Affiliates + ATM — Naseem's Context
11. GMB Reviews — Kripa's Context
12. Business Intelligence — Tanishka's Context
13. Consolidated Snowflake Schema & SQL Queries
14. Company Verticals & Products
15. Internal ML Systems
16. Competitive Landscape
17. Regulatory Context
18. Dashboards & Artefacts Built in This Project
19. Data Files Analysed
20. Context Extraction Programme (team rollout)
21. Current Alerts & Watch Items
22. Tableau Connection
23. Context Conflict Resolution Protocol
24. Changelog

---

## 1. COMPANY OVERVIEW & BUSINESS MODEL

- **Full name**: CARS24 Services Private Limited (brand: Cars24 from Feb 2026)
- **Founded**: 2015 by Vikram Chopra (CEO), Mehul Agrawal (COO), Gajendra Jangid, Ruchit Agarwal
- **HQ**: Gurugram, Haryana, India
- **Valuation**: ~$1.03B (unicorn since 2020)
- **Total funding**: $1.08B+ across 12+ rounds
- **Revenue FY25**: ₹6,360 Cr operating revenue
- **H1 FY25-26**: ₹6.5B adjusted net revenue; EBITDA loss down 36% YoY
- **Scale**: 205+ branches, 182+ cities, 10,000+ verified channel/dealer partners
- **IPO**: Targeted 6–12 months from early 2026 (CEO statement)
- **Brand relaunch Feb 2026**: CARS24 → Cars24 (sentence case); new "younger blue" #1860F0; open circular logo motif; tagline "Better Drives, Better Lives"

### Business Model
- **Primary**: C2B (buy used cars from individuals) → B2C (resell to consumers) full-stack retail
- **C2B side**: Instant valuation → inspection → auction to 10,000+ dealers → payment same day
- **B2C side**: Browse → test drive at hub → finance → purchase → delivery
- **Commission**: ~4–5% per transaction
- **Asset-heavy**: Cars24 owns inventory (unlike classifieds like OLX)
- **Phygital**: Digital demand generation → physical hub conversion

### Market Context
- India used car market: ~$30.5B (2023), projected $36–40B (2025), ~$70B by 2030
- Organised online segment: growing at 27% CAGR
- Cars24 dominates online segment but has single-digit share of total unorganised market

---

## 2. PRIYANK'S PROJECT — DEMAND COMMAND CENTRE

### Role
- **Team**: Demand Strategy & Transformation
- **Location**: Gurugram

### Core Problem (from CXO Slack / One-Pager doc)
Cars24 retail operates reactively — problems discovered N-1 (days after they occur), not in real time. Specific documented failures:

| # | What happened | When discovered |
|---|---|---|
| 1 | Facebook campaign paused mid-week (policy flag/budget) | 2 days later |
| 2 | Classified lead integration broke silently | 2 days later |
| 3 | App crashed 7–9 PM festive weekend | Monday review |
| 4 | CRM WhatsApp deep link broken | 3 days later |
| 5 | CC South connectivity dropped 80% → 55% | Weekly review |

### Four Gaps Identified
1. **No real-time diagnostics** — no hourly alerting on any lead indicator
2. **No demand prediction** — levers pulled, wait a week to see effect
3. **No customer intelligence** — all customers treated equally despite intent data existing
4. **No unified view** — each channel silo has own dashboard, no cross-channel synthesis

### Four Solutions Needed
1. CLP/CDP — personalised, widget-based discovery (not static)
2. CRM 90-day journeys — WhatsApp + Push + Email + AI calls, dynamic frequency
3. CC Concierge model — intent-filtered routing, fewer customers more depth
4. Perf Marketing Automation — automated bids, real-time creative feedback

### North Star
> Build a real-time Demand Command Centre: hourly metric flagging across all lead indicators, source-wise and city-wise, with predictive models that match demand to hub resources proactively.

### Proof point
Removing language selection barrier → 40% drop-off decrease; classified traffic 4,839 → 6,932.

### Manager's immediate ask
Build a **Unified Business Information Layer** — one consolidated view of all marketing channels for management.

---

## 3. THE FUNNEL — END TO END

### B2C Buy-Side Funnel (main)
```
Listings + Token → BI → BC → Visit (Test Drive) → Token → Net Delivery
```

### Mar '26 Actuals (Funnel_Performance.csv — source of truth)
| Metric | Value | Notes |
|---|---|---|
| Listings + Token | 5,299 | Avg inventory with ≥1 active token |
| Listings (avg) | 5,310 | Monthly avg of daily inventory |
| BI Overall | 7,39,468 | All booking initiations |
| BI Unique | 4,22,205 | Unique customers |
| BC Overall | 1,98,304 | All confirmed bookings |
| BC Unique | 1,35,187 | Unique customers |
| BI2BC % | 26.8% | Was 36% Jul'24 — declining |
| Overall Visits | 48,958 | Test drives taken |
| Unique Visits | 26,167 | |
| BC2V % | 24.6% | Was 30.2% Oct'25 — declining |
| U.Checkin | 27,323 | Hub arrivals (superset of visits) |
| Pseudo-cancel Unique Visits | ~4,767 | Cancelled when another customer reserved same car |
| Net Unique Visits (ex pseudo-cancel) | 21,400 | Cleaner metric |
| Tokens | 8,071 | RT 67% + PVT 22% + NRT 15% |
| Net Delivery | 4,401 | STR 2.68% · DRR 142/day |
| Gross Delivery | 4,504 | Before returns |
| Return Rate | 2.3% | |
| CF Attach Rate | 52.8% | Gross delivery with financing |
| GMV | ₹232.5 Cr | |

### Key Rates Mar'26
| Rate | Value | Trend |
|---|---|---|
| STR | 2.68% | ↓ (was 3.37% Oct'25) |
| DOH | 37.3 days | ↑ rising |
| Good Cohort BC2V | 52.9% | Stable |
| NRT Cancel Rate | 75.6% | High |
| PVT Cancel Rate | 89.8% | Very high |
| RT Cancel Rate | 29.2% | Acceptable |
| Token Cancel % overall | ~49% | |
| Test Drive Denied % | 4.2% | |
| Same Day BC share | 28.7% | |

### Delivery Aging (Mar'26)
| Age bucket | Share |
|---|---|
| 0–29 days | 62.7% |
| 30–59 days | 29.4% |
| 60–89 days | 6.0% |
| 90–119 days | 1.6% |
| 120+ days | 0.7% |

### CF Cohort Breakdown (Mar'26 Unique BC)
| Cohort | Definition | Share | BC2V |
|---|---|---|---|
| Good (GC) | Docs shared + eligible for loan | 13% | 52.9% |
| Bad | Docs shared + NOT eligible | 19% | 24.8% |
| Incomplete | Docs NOT shared | 68% | 17.3% |

### Token Timing (D0/D1/D2/D>2)
| Timing | Share |
|---|---|
| D0 (same day as visit) | 68.0% |
| D1 | 6.2% |
| D2 | 2.1% |
| D>2 | 3.6% |

### C2B Sell-Side Funnel
```
Online Evaluation (AI web quote) → Appointment → Inspection (200+ points)
→ Auction (10,000+ bidders) → Price Offer → Acceptance → Payment → RC Transfer
```
~90% of web-quote users drop off before store visit. ~1/3 of transactions close via follow-up.
C2B conversion ~30% vs B2C 0.6%.

---

## 4. ACRONYMS & DEFINITIONS

### Core Funnel
| Term | Definition |
|---|---|
| BI | Booking Initiated — customer starts booking a car |
| BC | Booking Confirmed — customer confirms booking |
| Sch BC | Scheduled Booking Confirmation — date selected by customer; mapped to car × customer × date |
| Unique Sch BC | Customer × Date (not car-level) |
| Same Day BC | Booking created AND scheduled for same day |
| U.Checkin | Customer physically arrived at hub — superset of test drive visits |
| Visit / V | Customer who took test drive at hub |
| TD | Test Drive — physical car inspection at hub |
| Pseudo-cancel visit | Visit cancelled when another customer places Reserve Token on same car |
| BC2V | BC → Visit conversion rate |
| BI2BC | BI → BC conversion rate |
| UV2GT | Unique Visit to Gross Token |
| STR | Sell Through Rate = Net Delivery / Avg Listings / days in month |
| DOH | Days on Hand = 1/STR |
| DRR | Daily Run Rate — avg deliveries/day |

### Token Types
| Term | Definition | Cancel Rate |
|---|---|---|
| PVT | Pre-Visit Token — reserves car BEFORE visiting | 89.8% |
| RT | Reserve Token — WITH cancellation fees | 29.2% |
| NRT | Non-Reserve Token — NO cancellation fees | 75.6% |
| GT | Gross Token — all tokens combined | |

### Inventory & Financials
| Term | Definition |
|---|---|
| LP | Listed Price |
| CP | Car Price (transaction price) |
| LP/CP | Ratio (Mar'26: 0.866) |
| DM | Direct Margin per car |
| TM | Transacting Margin |
| STR | Sell Through Rate |
| DOH | Days on Hand |
| BC/Listing | Bookings per listing — demand density |

### CF Cohorts
| Term | Definition |
|---|---|
| Good / GC | Docs shared + eligible for auto loan |
| Bad | Docs shared + NOT eligible (underwriting denial) |
| Incomplete | No docs shared — eligibility unknown |
| GC Attach Rate | Conversion rates for Good Cohort only |

### Channels
| Term | Definition |
|---|---|
| ATM | Influencer Marketing (YouTube + LinkedIn) — NOT ATL |
| ATL | Above The Line — TV, OOH, radio (tracked under Brand/BOD) |
| BOD | Brand / Organic / Direct — derived attribution |
| GMB / GBP | Google My Business / Google Business Profile |
| Classified | OLX, CarDekho, etc. |
| Criteo | Programmatic retargeting display |
| OD | Organic & Direct — no paid source |
| CC | Call Centre — Inbound + Outbound |
| CRM | WhatsApp, SMS, Push, Email, IVR, RCS campaigns |
| Sales Panel | Internal ops tool — staff create bookings for walkin customers |
| HTD | Home Test Drive — phased out 2025 |

### Manpower (B1 roles)
| Term | Role |
|---|---|
| B1 | Front-end ground role umbrella |
| CA | Car Adviser — primary sales at hub |
| TC | Telecaller |
| DS | Finance/documentation support |

### CRM-Specific
| Term | Definition |
|---|---|
| CT | CleverTap |
| UCTR | Unique Click-Through Rate |
| UBI / UBC | Unique Buy Intent / Unique Buy Confirmed |
| DPV | Detail Page View |
| Rec campaigns | Recommendation-engine campaigns — 2–3x better than standard blasts |
| PD Similar / PD Exact | Price Drop campaigns — similar segment or same car |
| CF | Custom Filter / EMI-personalised campaigns |
| Aadhar | Sell-side CRM retargeting for inspections |
| Comify | Third-party integration (CT events + Catalogue API + S3) |
| CleverAI | CleverTap AI layer for autonomous campaign optimisation |
| IntelliNode | CleverTap AI-powered journey routing |
| LAC | Loan Against Car |
| VAS | Value Added Services (Challan, PDI, VHR) |
| Kanika | WhatsApp chatbot for test drive bookings |
| BCR | Bot Containment Rate |
| CTOR | Click-to-Open Rate |
| RCS | Rich Communication Services |

### GMB/Affiliates-Specific
| Term | Definition |
|---|---|
| CPI | Cost Per Inspection (affiliate payout formula) |
| ASP | Average Selling Price |
| I2SI | Inspection to Stock-In conversion |
| A2I | Appointment to Inspection conversion |
| V2D | Visit to Delivery conversion |
| NU | New User — leads from phone calls on GMB listing |
| NAP | Name, Address, Phone — GBP optimisation |
| Map Pack | Top 3 Google Maps results for local search |
| Geo-Grid Ranking | Avg position across search points in city |
| DOD | Day-on-Day |
| MTD / LMTD | Month-to-Date / Last Month-to-Date |
| RightChoice | Third-party GMB tool being replaced (~₹24L/year) |
| VHR | Vehicle History Report |
| PDI | Pre-Delivery Inspection |
| GS / Elite / Edge | Business verticals / hub tiers |

### Google Ads Campaign Types (Tanishka)
| Code | Campaign type |
|---|---|
| UACE | Engagement campaigns |
| UACI | In-App Action / Install campaigns |
| PMAX | Performance Max |
| DG | Demand Gen |
| SEARCH | Branded/non-branded search |

---

## 5. CHANNEL STRUCTURE & PERFORMANCE (Mar '26)

### Attribution Models
| Model | Source | Best for |
|---|---|---|
| First Touch | MoM-Abs-cg.xlsx | Brand/awareness — user acquisition |
| Last Touch | channel.csv | Performance/ROI — conversion attribution |
| Overall | Funnel_Performance.csv | Business-level funnel — no channel attribution |

### ⚠️ AFFILIATES DISAMBIGUATION
Two distinct "Affiliates" channels exist:

| | B2C Affiliates | C2B Affiliates |
|---|---|---|
| Funnel direction | Buy-side | Sell-side |
| Key metrics | BC, Visits, CPV, CPD | Appointment, Inspection, Stock-In |
| Spend | ₹2L/month ✓ confirmed | ₹60L/month ✓ confirmed |
| Attribution | Last touch | CPI formula per partner |
| Owner | Not identified | Naseem (94 partners) + Neel |

### Channel Mix Mar'26 (Last Touch, channel.csv)
| Channel | Spend ₹L | BC | Visits | BI2BC% | BC2V% | CPV ₹ |
|---|---|---|---|---|---|---|
| Google B2C | 132 | 45,610 | 8,836 | 16.8% | 19.4% | 690 |
| Google C2B | — | 3,698 | 1,025 | 42.6% | 27.7% | — |
| Meta/Facebook | 140 | 34,439 | 8,548 | 26.0% | 24.8% | 756 |
| Classifieds | 24 | 8,982 | 2,556 | 6.5% | 28.5% | 5,444 |
| Criteo | 10.7 | 6,516 | 570 | 37.5% | 16.3% | 8,000 |
| ATM Influencer | 16 | 1,092 | 118 | 5.5% | 10.8% | 11,828 |
| CRM | 45 | 3,473 | 944 | 35.8% | 27.2% | 22,222 |
| Affiliates B2C | 2 | 2,425 | 613 | 40.9% | 25.3% | 557 |
| BOD/Organic | — | 8,339 | 453 | 41.9% | — | — |
| Walkin | — | 27,236 | 13,077 | 90.5% | 48.0% | — |
| Sales Panel | — | 8,187 | 890 | 9.5% | 43.8% | — |
| **Pan India** | **≈420** | **1,99,765** | **49,169** | **26.8%** | **24.6%** | — |

### ⚠️ ATM Spend Note
- ₹16L (Marketing_Data, Mar'26) = full ATM budget (content + distribution)
- ₹2L (Naseem, tentative) = vendor/creator fees only
Different accounting scope — both valid.

### ⚠️ CRM BC Attribution Note
- channel.csv (strict last-touch): CRM BC = 3,473 (Mar'26)
- CleverTap (24hr window): CRM BC = 68,119 (Jan'26)
Different attribution windows — always specify when quoting.

### Channel Quality Tiers
- **Best BI2BC**: Walkin 90.5% → Google C2B 42.6% → BOD 41.9% → Affiliates B2C 40.9%
- **Worst BI2BC**: Classifieds 6.5% · ATM 5.5% · Sales Panel 9.5%
- **Best BC2V**: Walkin 48% → Google C2B 27.7% → CRM 27.2%
- **Cheapest CPV**: Affiliates ₹557 → Google B2C ₹690 → FB ₹756
- **Most expensive CPV**: CRM ₹22,222 · ATM ₹11,828 · Criteo ₹8,000

---

## 6. 24-MONTH TREND DATA (Apr'24 → Mar'26)

| Month | Spend ₹Cr | Listings | BC Overall | Visits | Net Del | GMV ₹Cr |
|---|---|---|---|---|---|---|
| Apr'24 | 3.78 | 5,661 | 83,923 | 31,547 | 3,340 | 179.1 |
| May'24 | 3.41 | 5,390 | 1,00,156 | 33,762 | 3,210 | 173.1 |
| Jun'24 | 2.92 | 5,635 | 96,176 | 32,623 | 2,833 | 154.5 |
| Jul'24 | 3.01 | 5,580 | 96,443 | 31,025 | 2,515 | 143.3 |
| Aug'24 | 2.99 | 5,397 | 1,05,977 | 33,356 | 2,863 | 164.3 |
| Sep'24 | 3.19 | 5,267 | 95,911 | 30,133 | 2,001 | 138.1 |
| Oct'24 | 3.16 | 4,989 | 1,04,919 | 33,696 | 2,723 | 175.6 |
| Nov'24 | 3.03 | 4,729 | 97,765 | 36,131 | 2,227 | 143.6 |
| Dec'24 | 4.11 | 4,219 | 1,13,182 | 44,767 | 2,951 | 203.5 |
| Jan'25 | 4.25 | 3,261 | 1,19,518 | 44,363 | 3,347 | 234.8 |
| Feb'25 | 3.74 | 2,490 | 99,768 | 36,998 | 2,509 | 177.3 |
| Mar'25 | 3.84 | 2,542 | 1,19,455 | 41,699 | 3,010 | 187.3 |
| Apr'25 | 2.96 | 3,059 | 1,03,553 | 35,125 | 2,969 | 169.0 |
| May'25 | 2.93 | 3,316 | 1,23,896 | 39,745 | 3,348 | 202.8 |
| Jun'25 | 2.88 | 3,472 | 1,25,019 | 38,596 | 3,431 | 206.4 |
| Jul'25 | 2.60 | 3,507 | 1,25,542 | 38,676 | 3,327 | 194.2 |
| Aug'25 | 2.57 | 3,627 | 1,33,744 | 41,334 | 3,451 | 199.6 |
| Sep'25 | 2.39 | 3,893 | 1,18,298 | 34,999 | 2,765 | 159.2 |
| Oct'25 | 3.26 | 3,898 | 1,36,376 | 40,784 | 4,099 | 219.8 |
| Nov'25 | 2.91 | 3,993 | 1,33,053 | 37,759 | 3,755 | 193.1 |
| Dec'25 | 3.16 | 4,557 | 1,60,142 | 43,159 | 4,015 | 202.7 |
| Jan'26 | 3.59 | 4,668 | 1,75,323 | 46,964 | 4,516 | 225.0 |
| Feb'26 | 3.59 | 4,889 | 1,63,129 | 44,960 | 3,997 | 201.8 |
| Mar'26 | 4.20 | 5,310 | 1,97,629 | 48,762 | 4,402 | 232.5 |

---

## 7. DATA SOURCES & ATTRIBUTION MODELS

| Source | Contents | Attribution | Period |
|---|---|---|---|
| Funnel_Performance.csv | Full funnel: all retail metrics, cohorts, tokens, delivery aging, manpower | None (total business) | Oct'25–Apr'26 |
| channel.csv | BI, BC, Visit, Delivery + conversion rates by channel | Last Touch | Jul'24–Apr'26 |
| MoM-Abs-cg.xlsx | Users, BI, BC by channel | First Touch | Oct'25–Apr'26 |
| Marketing_Data.xlsx — Last 24 Month | Overall cost (₹Cr), bookings, visits, GMV, delivery | None | Apr'24–Mar'26 |
| Marketing_Data.xlsx — Channel Wise CPD&CPV | CPD, CPV, Visit, Delivery by channel | Last Touch | Mar'25–Feb'26 |
| Marketing_Data.xlsx — Channels Spends | All channel spends in ₹ Lakhs | — | Mar'25–Mar'26 |
| Marketing_Data.xlsx — Last Touch Data | Budget, bookings, visits per channel with Apr targets | Last Touch | Jan–Apr'26 |
| Control_Tower_V1.xlsx — FINAL tab | Template structure (JAN–MAR partial data) | Partial | JAN–MAR |
| CleverTap Account 198 | Buy-side CRM daily CSV — full attribution chain | Last touch (24hr BI/BC, 7-day Visit) | Ongoing |
| Snowflake (CAPL_GS_DB.PROD) | Buyer funnel, listings, CC, C2B tables | — | Ongoing |
| Catalogue API | 37+ car attributes | — | Live |

**Units**: Marketing_Data spends = ₹ Lakhs. Last 24 Month sheet = ₹ Crores. Always check.

### Scale Clarification
- Control Tower BCs (~11K–15K/month) ≠ Overall BCs (~133K–198K/month). CT is a marketing-attributed or city-filtered subset.
- Funnel_Performance.csv = source of truth for overall retail funnel.

---

## 8. CRM CHANNEL — ADHIRAJ'S CONTEXT

### Team & Channel
- **Owner**: Adhiraj
- **Team size**: 4 (2 Deputy Managers, 1 Team Lead, 1 APM)
- **Sub-channels**: WhatsApp (~99% buy-side), SMS, Push, Email, IVR, RCS
- **Verticals**: Buy (Rechurn), Sell (Aadhar), LAC, VAS (Challan/PDI), Insurance
- **Annual sends**: 25.8 Cr+ at ₹3.1 Cr spend
- **Primary tool**: CleverTap Account 198 (buy-side)
- **Attribution**: Click → BI/BC within 24 hrs; click → Visit within 7 days

### Spend
| Period | Spend | Notes |
|---|---|---|
| Jan'26 actual | ₹41.7L | vs ₹60L budget |
| Mar'26 (Marketing_Data) | ₹45L | Channel.csv last-touch |
| Full year Aug'25–Mar'26 | ₹3.1 Cr | All verticals |

### CRM Actuals (as-is, no reconciliation)
| Metric | Value | Period |
|---|---|---|
| BI Overall | 6L (full year); 1,20,519 (Jan'26, +4% vs target) | Aug'25–Mar'26 |
| BI Unique | ~2,200/day | Feb'26 |
| BC Overall | 3.7L (full year); 68,119 (Jan'26, +15.5% vs 59K target) | Aug'25–Mar'26 |
| BC Unique | ~1,300/day | Feb'26 |
| Visits | 1.04L (full year); 17,668 (Jan'26, +18.6% vs 14.9K target) | Aug'25–Mar'26 |
| Net Delivery | 10,086 (full year); 1,710 (Jan'26, +3.2% vs 1,657) | Aug'25–Mar'26 |
| Unique users reached | 42L | Mar'26 |
| CPBC | ₹90 (down from ₹424, –79%) | Jan'26 |
| Cost/delivered WA message | ₹0.17 (down from ₹0.45) | Post-utility migration |
| Daily sends | ~1M rows/day (range 59K–1.5M) | Feb'26 |
| WA delivery rate | 87% (up from 65%) | Post-migration |
| WA utility share | 90% (up from 14%) | Post-migration |
| Rec campaign UCTR | 8.7–11.6% | Feb'26 |
| Standard blast UCTR | 2.7–2.9% | Feb'26 |
| Wishlist campaign UCTR | 5.8–7.2% | Feb'26 |
| Push reachability overall | 41% (from 30%) | Mar'26 |
| Frequency/user | 3.2 → 6.2 | FY'26 |
| Null FUNNEL tagging | ~30% of records | Known gap |

### Key Insight — Blast Volume vs Conversion (Inverse)
- Feb 8: 59K sends → 2.35% UBI rate
- Feb 1: 948K sends → 0.32% UBI rate
Lower blast volume = higher conversion. Rec campaigns outperform blasts 2–3x.

### Vertical Performance
| Vertical | Metric | Value | Period |
|---|---|---|---|
| Buy (Rechurn) | Monthly BCs | 25K → 66K | Oct'25 → Jan'26 |
| Buy (Rechurn) | CPBC | ₹424 → ₹90 (–79%) | Oct'25 → Jan'26 |
| Sell (Aadhar) | Monthly inspections | ~7K → ~12.5K | FY'26 |
| Sell (Aadhar) | Marketing cost | ₹50L → ₹25L (–50%) | FY'26 |
| LAC | Disbursals | ₹1.09Cr → ₹2.28Cr → ₹4+Cr | Jan→Feb→Mar'26 |
| LAC | CAC reduction | ~38% | Jan–Mar'26 |
| VAS (Challan) | CRM share of orders | 4% → 22% | Dec'25 → Mar'26 |
| Insurance | Revenue | ₹47L → ₹64L (+36%) | FY'26 |

### CleverTap Event Schema (361 live events — key gaps)
| Status | Events |
|---|---|
| LIVE | Buy funnel (17 milestones), Sell/C2B funnel, Platform/engagement |
| MISSING 🔴 | EMI Calculator (Sprint 1 critical), 360° view/inspection report (Sprint 1), test drive events (Sprint 2), loan_approved (Loans team) |
| MISSING | Suppression flags (is_fraud_risk, is_employee, do_not_disturb_until), derived user attributes |

### CleverTap Daily CSV Columns
MOBILE_NUMBER, CHANNEL_TYPE, FUNNEL (~30% null), JOURNEY_STAGE_NAME, CATEGORY (utility/marketing_lite/marketing), BI_FLAG, BC_FLAG, VISIT_FLAG, DELIVERY_FLAG, SENT_TIME, DELIVERED_TIME, CLICK_TIME

### CRM Data Systems
CleverTap Account 198 · Snowflake · Gupshup/Karix · Comify · CleverAI · Catalogue API (37+ attrs) · S3 buckets · Google Sheets

### CRM Data Gaps (14 flagged)
FUNNEL null (~30%), EMI Calculator event, 360° view events, loan_approved event, TD events, suppression flags, derived user attributes, offline visit data, real-time reporting, S3 credentials (Anurag), historical data pipeline (Akhil), catalogue API → CT validation, intent score/lat-long, template ID mapping

### CRM Active Dashboards
| Name | Accesses | Reuse |
|---|---|---|
| CleverAI Master Prep Tracker v2 | 5+ | High |
| Feb daily campaign analysis (Python + CSV) | 10+ | High |
| CleverAI Workshop Handoff Doc | 3+ | High |
| Comify Project Status Update | 3+ | Medium |
| Kanika WhatsApp Bot Prompt | 4+ | Medium |

---

## 9. C2B AFFILIATES — NEEL'S CONTEXT

- **Owner**: Neel
- **Channel**: Sell-side affiliates — external partners driving sellers to Cars24
- **Spend**: ₹60L/month ✓ confirmed
- **Attribution**: Not defined
- **Data path**: Snowflake → Tableau → Excel (manual, weekly)
- **Metrics tracked**: Appointment (=BC), Inspection (=Visit), Stock-In (=Delivery)

### Funnel Mapping
| C2B term | CT metric |
|---|---|
| Appointment | BC |
| Inspection | Visit |
| Stock-In | Delivery |

### Active Dashboard
Affiliates Tableau Dashboard — ACTIVE, HIGH reuse potential for unified dashboard.

### Data Gaps
All reporting manual (Tableau → Excel), CPBC/CPV/CPD not shared, BC2V/BC2D not shared, Snowflake tables undocumented, attribution undefined.

> **Note**: Naseem also manages affiliates (94 partners, buy + sell + VAS). Overlap with Neel's scope needs clarification.

---

## 10. GMB + AFFILIATES + ATM — NASEEM'S CONTEXT

- **Owner**: Naseem
- **Channels**: GMB (paid + organic), Affiliates C2B (94 partners — sell + buy + VAS), ATM (Influencer)
- **GMB listings**: 855 active (51 = physical hub locations; 855 = total listing entries across all types)
- **Attribution**: GMB = last touch via phone number; Affiliates = partner UTM/source

### GMB Actuals (Jan–Mar'26)
| Metric | Jan | Feb | Mar |
|---|---|---|---|
| GMB Sell Leads | 85,871 | 81,601 | 60,305 (MTD-23) |
| GMB Buy BI | 26,598 | 24,018 | 19,214 |
| GMB Buy BC | 13,000 (+112%) | — | — |
| GMB Buy Visits | 3,600 (+126%) | — | — |
| GMB Sell Inspections | 4,000 (+55%) | — | — |
| GMB Sell Spend | ₹5.22L | ₹8.24L | ₹7.41L |
| GMB Buy Spend | ₹4.44L | ₹4.12L | ₹4.68L |
| GMB Buy CPL | ₹77 | ₹112 | ₹148 |
| Impressions | — | 3.1M+ | — |
| CTR | — | 7.93% | — |
| Direction clicks | — | 1,88,605/month | — |
| Avg rating | — | 4.75 (Spinny: 4.62) | — |
| Reviews/month | — | 7,948 (2× in 6 months) | — |
| GBP Completion | — | 84.8% (Spinny: 60%) | — |
| Geo-Grid Ranking | — | 5.2 (Spinny: 7.04) | — |

### Affiliates C2B (Naseem — 94 partners, Dec'25–Mar'26 cumulative)
| Metric | Value |
|---|---|
| Total leads (sell) | 3,01,630 |
| Appointments | 1,17,215 |
| Inspections | 49,670 |
| Stock-ins | 2,533 |
| Total payout | ₹1.75 Cr |
| Active partners | 53 of 94 |
| BC/month | ~14,000 |

### Affiliate Payout Formulas
- **Seller CPI** = ₹1,400 × (A2I%/50%) × (I2SI%/16%) × (ASP/₹2,75,000) — each ratio capped at 1
- **Buyer CPV** = [₹1,000 × V2D%/16% × visits] + CF
- **PDI**: ₹600/700/800 slab per order
- **Challan**: Flat ₹50/order · **VHR**: Flat ₹100/order

### ATM (Influencer) — Naseem
Videos: 596/month peak (Aug'25). Leads: ~85K peak. BC: ~14K/month. Inspections: ~600/month. CPV: ₹5K → ₹3K.

### Naseem's Active Dashboards (all HIGH reuse)
| Name | Type | Accesses |
|---|---|---|
| Affiliate Partner Portal V6–V19+ | HTML ~19,800 lines + Supabase + GitHub Pages | 30+ |
| GMB Dashboard (gmb_dashboard__6_.html) | HTML + Chart.js | 15+ |
| GMB Ad Campaign Analysis | HTML + Chart.js | 5+ |
| WhatsApp Reporting Bot | Python + Snowflake + Twilio | 5+ |
| CC Buyer Funnel SQL (8-branch UNION ALL) | Snowflake SQL | 5+ |
| Buy Funnel City-wise (17 cities) | HTML | 3+ |
| GMB Review Intelligence | HTML embedded | 3+ |
| GMB Management System (GBP API) | Python/Flask + HTML | 3+ |

### Naseem's SQL Queries (structure)
1. **CC Buyer Funnel**: 8-branch UNION ALL, CTEs (lead_interaction, lead_disposition, lms_lead, LMS_BI, CHATBOT_BASE). MD5 hashes for 10 IVR numbers. Floor `2026-01-01` + `CURRENT_DATE()`.
2. **ATM Seller**: CTEs → LEAD → C2B_LEAD → APPOINTMENT → INSPECTION → STOCKIN. Date `>= '2026-03-01'`
3. **ATM Buyer**: Same CTE structure → LEAD → BI → BC → VISIT → TOKEN → NET DELIVERY. Date `>= '2026-03-01'`
4. **WhatsApp Bot Sell**: Snowflake → Python → Twilio. Leads = unique phones. Every 2 hrs from 9 AM IST.
5. **WhatsApp Bot Buy**: Same pipeline. Includes bi_existing_flag, MTD from month_start.
6. **Hub-level**: BOOKINGS + hub_mapping CASE CTE. 4-block UNION (BI/BC/Visit/Delivery dates).

### Naseem's Data Gaps
- GMB paid vs organic leads inseparable (same phone number)
- Feb GMB Sell conversion data corrupted — disregard "27,212 Conversions" (data export error)
- GBP API access pending
- 48 unanswered 1-star reviews = ranking risk
- Bangalore: 40 locations with zero map pack presence
- GST impact Jan 16: BLR –11.1%, PUN –14.0%, HYD –9.3% daily view drops

---

## 11. GMB REVIEWS — KRIPA'S CONTEXT

- **Owner**: Kripa (sub-function within Naseem's GMB channel)
- **Primary focus**: Review management, review collection tool, regional GMB data uploads

### Review Metrics (Feb'26)
Reviews/month: 7,948 (2× growth in 6 months) · Avg rating: 4.75 · Positive rate: 96%+ · Negative: 235
Active dataset: 22,335 reviews · Deleted dataset: 34,862 reviews

### Review Classification
- BUY codes: B1, C1, C3
- SELL codes: A1, A2, A3, B2, B3, D2
- Classifications: Junk / Low Relevance / Relevance
- Threshold: reviews/visit < 0.8 = flagged
- Rating colour: 4.5+ green · 4.0–4.4 yellow · <4.0 red

### Review Tool Stack
- Frontend: cars24-review-v9.html (star rating, hub selection, photo enhancement, keyword integration)
- Backend: Python Flask + Gemini API (localhost:5000)
- Gap: "Post to Google" is manual — no GBP API integration yet

### Kripa's Active Dashboards
GMB Dashboard with Review Tracker (10+ accesses) · Review Intelligence Tab (5+ accesses) · Review Collection Tool v9 (5+ accesses)

---

## 12. BUSINESS INTELLIGENCE — TANISHKA'S CONTEXT

- **Owner**: Tanishka (tanishka.tanwar@cars24.com)
- **Team**: Business Intelligence — buyer-side analytics (support function, no channel spend)
- **Core work**: Snowflake SQL pipelines for buyer funnel metrics; Google Ads campaign tagging
- **Data path**: Snowflake → CSV → `C:\Users\703137\Desktop\buyer_data` → Streamlit / Claude artifact

### Metrics Computed
BI/L · BC/L · V/L · Token/L · Days Listed in Range · Total Lifetime Days Listed

**Non-funnel model**: Each metric counted independently based on when it occurred — NOT sequential. A car can have BI on Day 1 and BC on Day 5; both counted in their own date buckets.

### Campaign Tagging
541 Google Ads campaigns tagged: UACE / UACI / PMAX / DG / SEARCH. 50+ city aliases for city detection. Output: CAMPAIGNS_TAGGED.xlsx.

### Tanishka's Active SQL Pipeline (10+ accesses, HIGH reuse)
Full Buyer DOD + Metrics flat output query — see Section 13 for verbatim SQL.

### ETL Notes
- Snowflake SSO: externalbrowser auth
- Python 3.11 required (snowflake-connector)
- Two CMD windows needed (bot + Streamlit)
- Cloudflare tunnel URL changes on restart — manual Twilio webhook update required
- Hub mapping hardcoded in CASE statements

---

## 13. CONSOLIDATED SNOWFLAKE SCHEMA & SQL QUERIES

### Primary Namespace: CAPL_GS_DB.PROD

#### B2C Buyer-Side Tables
| Table | Purpose | Key columns |
|---|---|---|
| BOOKINGS | All buyer funnel events | APPOINTMENT_ID, BOOKING_ID, CREATED_DATE (=BI), BOOKING_CONFIRM_DATE (=BC), FIRST_VISIT_DATE (=Visit), TOKEN_DATE, ACTUAL_DELIVERY_DATE, CUSTOMER_PHONE_NO, BOOKING_STATUS_UPDATED_AT |
| GS_PROCURED_DATA | Live inventory | APP_ID, CITY, REGION, LISTING_STATUS, MAKE, MODEL, YEAR, VARIANT, STORE_ID, TOTAL_LISTING_DAYS |
| GS_DAILY_LISTINGS | DOD snapshots | APPOINTMENT_ID, DATE, FINAL_CITY, REGION, ORDER_STATE |
| GS_SALES | Sales events | BOOKING_DATE, BOOKING_STATUS_UPDATED_AT |
| IND_BUYER_WA_SMS_V2 | WA/SMS comms log | MOBILE_NUMBER, date range |

#### CC (Call Centre) Tables — CAPL_GS_DB.B2C_CC_SERVICE_B2C_CC_SERVICE_DB
| Table | Purpose | Key columns |
|---|---|---|
| LEAD_PUSH_LOG | CC lead push timestamps | LEAD_ID, PUSHED_AT |
| LEAD_INTERACTION | CC interactions | CUSTOMER_PHONE, INTERACTION_CREATED_AT, RESPONSE (JSON: userid, customerCrtId, monitorUCID) |
| LEAD_DISPOSITION | CC dispositions | DISPOSITION_CREATED_AT, CRT_OBJECT_ID |

#### C2B Sell-Side Tables — CSPL_C2B_DB
| Table | Purpose |
|---|---|
| WEBSITE_DEALERENGINE_PROD.LEAD | C2B leads |
| WEBSITE_DEALERENGINE_PROD.APPOINTMENT | C2B appointments |
| ADMIN_PANEL_PROD_DEALERENGINE_PROD.ORDERS | C2B orders |

#### External Stores
| Store | Purpose |
|---|---|
| Supabase (ogapcuhrusvcqguuoxxr.supabase.co) | Affiliate portal data sync |
| Supabase (ughrnlajvfjnclwexalc.supabase.co) | Partner onboarding |
| Google Sheets (Admin tab gid=1012408495) | Affiliate SSOT — Partner Name1, Leads, Appointment, Inspections, Stock Ins, Payout, CPI |
| CleverTap Account 198 | CRM buy-side daily CSV |

#### Critical Schema Notes
- **Join key**: APP_ID (GS_PROCURED_DATA) = APPOINTMENT_ID (BOOKINGS, GS_DAILY_LISTINGS)
- **BI date**: CREATED_DATE on BOOKINGS
- **BC date**: BOOKING_CONFIRM_DATE on BOOKINGS (or BOOKING_STATUS_UPDATED_AT on GS_SALES)
- **Visit date**: FIRST_VISIT_DATE on BOOKINGS
- **Non-funnel**: Metrics counted by when they occurred — not sequential pipeline
- **Excel column gotcha**: Affiliate Google Sheet column is `Partner Name1` (not `Partner Name`)
- **PDI/Challan/LAC tabs**: Trailing space in `Partner ` column name

### SQL: Tanishka's Buyer DOD + Metrics (verbatim)

```sql
WITH params AS (
    SELECT '2026-03-01'::DATE AS start_date, CURRENT_DATE() AS end_date
),
dod AS (
    SELECT APPOINTMENT_ID AS app_id, TO_DATE(DATE) AS listing_date,
           LOWER(FINAL_CITY) AS city, REGION AS region
    FROM CAPL_GS_DB.PROD.GS_DAILY_LISTINGS, params
    WHERE TO_DATE(DATE) BETWEEN params.start_date AND params.end_date
),
car_details AS (
    SELECT APP_ID AS app_id, MAKE, MODEL, YEAR, VARIANT, STORE_ID, TOTAL_LISTING_DAYS
    FROM CAPL_GS_DB.PROD.GS_PROCURED_DATA
),
bi AS (
    SELECT APPOINTMENT_ID AS app_id, TO_DATE(CREATED_DATE) AS bi_date,
           COUNT(DISTINCT BOOKING_ID) AS bi
    FROM CAPL_GS_DB.PROD.BOOKINGS, params
    WHERE CREATED_DATE IS NOT NULL
      AND TO_DATE(CREATED_DATE) BETWEEN params.start_date AND params.end_date
    GROUP BY 1, 2
),
bc AS (
    SELECT APPOINTMENT_ID AS app_id, TO_DATE(BOOKING_CONFIRM_DATE) AS bc_date,
           COUNT(DISTINCT BOOKING_ID) AS bc
    FROM CAPL_GS_DB.PROD.BOOKINGS, params
    WHERE BOOKING_CONFIRM_DATE IS NOT NULL
      AND TO_DATE(BOOKING_CONFIRM_DATE) BETWEEN params.start_date AND params.end_date
    GROUP BY 1, 2
),
visits AS (
    SELECT APPOINTMENT_ID AS app_id, TO_DATE(FIRST_VISIT_DATE) AS visit_date,
           COUNT(DISTINCT BOOKING_ID) AS visits
    FROM CAPL_GS_DB.PROD.BOOKINGS, params
    WHERE FIRST_VISIT_DATE IS NOT NULL
      AND TO_DATE(FIRST_VISIT_DATE) BETWEEN params.start_date AND params.end_date
    GROUP BY 1, 2
),
tokens AS (
    SELECT APPOINTMENT_ID AS app_id, TO_DATE(TOKEN_DATE) AS token_date,
           COUNT(DISTINCT BOOKING_ID) AS tokens
    FROM CAPL_GS_DB.PROD.BOOKINGS, params
    WHERE TOKEN_DATE IS NOT NULL
      AND TO_DATE(TOKEN_DATE) BETWEEN params.start_date AND params.end_date
    GROUP BY 1, 2
)
SELECT d.listing_date, d.app_id, c.MAKE, c.MODEL, c.YEAR, c.VARIANT,
       d.city, d.region, c.STORE_ID,
       c.TOTAL_LISTING_DAYS AS total_lifetime_days_listed,
       bi.bi_date, bc.bc_date, v.visit_date, t.token_date
FROM dod d
LEFT JOIN car_details c ON c.app_id = d.app_id
LEFT JOIN bi ON bi.app_id = d.app_id AND bi.bi_date = d.listing_date
LEFT JOIN bc ON bc.app_id = d.app_id AND bc.bc_date = d.listing_date
LEFT JOIN visits v ON v.app_id = d.app_id AND v.visit_date = d.listing_date
LEFT JOIN tokens t ON t.app_id = d.app_id AND t.token_date = d.listing_date
ORDER BY d.listing_date, d.region, d.city, d.app_id
```

---

## 14. COMPANY VERTICALS & PRODUCTS

| Vertical | Description |
|---|---|
| Used Car Buying (D2C) | Browse, test drive, purchase — home delivery available |
| Used Car Selling (C2B) | Online valuation → inspection → auction to 10K+ bidders |
| LOANS24 / CFSPL | NBFC arm — used car loans, personal loans, credit cards (RBI-licensed 2019) |
| FourDoor | Multi-brand car service & repair (Delhi NCR, Bangalore, Hyderabad, Chennai) |
| Cars24 Moto | Two-wheeler buying/selling (launched May 2020) |
| CarTruth | Vehicle history verification — RTO/VAHAN, lender, insurance archives |
| New Car Aggregator | Digital showroom for new cars, no inventory (launched early 2025) |
| Insurance & Warranty | Up to 3 yrs / 45,000 km warranty; insurance facilitation |
| E-Challan | Traffic fine settlement via app |
| Seller Kavach | Post-sale zero-liability legal protection for sellers |

---

## 15. INTERNAL ML SYSTEMS

| System | Function |
|---|---|
| Profecto | Pricing engine — car true price using make/model/age/mileage/inspection/demand |
| Auctoris | Personalised auction catalog — +20% views, +10% bids/bought for channel partners |
| Oraculum | Post-auction optimisation — seller expectation mgmt, dynamic margin control |
| Profundus | Deep learning for image & sound in vehicle inspection |
| Magneto | Pre-inspection funnel — lead prioritization, web-quote, session→booking |

Data team: ~100 people across Data Science, Platform (ML/Data Engineering), BI & Strategy.

---

## 16. COMPETITIVE LANDSCAPE

| Competitor | Model | Key differentiator |
|---|---|---|
| Spinny | D2C retail (no auction) | Fixed-price, 5-day return, curated inventory |
| CarDekho / Gaadi | Marketplace + content | Lead gen, new + used content |
| OLX Autos | Classifieds → C2B | Peer-to-peer + instant buy |
| CarTrade | Marketplace + auction | B2B focus, BSE/NSE listed |
| Droom | Marketplace | AI pricing, history reports |
| Maruti True Value / Mahindra First Choice | OEM-backed | Parent brand trust |

GMB benchmark vs Spinny: Cars24 avg rating 4.75 vs Spinny 4.62. GBP Completion 84.8% vs 60%. Geo-Grid Ranking 5.2 vs 7.04.

---

## 17. REGULATORY CONTEXT

| Area | Relevance |
|---|---|
| TRAI DND | SMS/call marketing — must honour DND |
| RBI NBFC Guidelines | LOANS24/CFSPL lending |
| Motor Vehicles Act | RC transfer, insurance, challan |
| IT Act / DPDP Act | Data privacy — consent-based comms, WhatsApp opt-in |
| Consumer Protection Act | Return policies, warranty |
| WhatsApp Commerce Policy | Template approval, opt-in rules |

---

## 18. DASHBOARDS & ARTEFACTS BUILT IN THIS PROJECT

All HTML files built by Claude for Priyank's Demand Command Centre project:

| File | Description | Status |
|---|---|---|
| `demand_command_centre.html` | First version — dark terminal aesthetic, placeholder data | v1 — superseded |
| `cars24_command_centre.html` | Main dashboard — real data wired from all files, Cars24 Feb'26 brand language (#1860F0, Bricolage Grotesque, open ring logo, dark navy). Funnel strip, channel matrix, 8 sparklines (Apr'25–Mar'26), CF cohort, token breakdown, delivery aging, manpower | Current main file |
| `tableau_live.html` | Self-contained Tableau REST API connector — pre-filled with server URL, site `cars24`, PAT name `claude`. Opens in browser, authenticates, lists workbooks/views, pulls CSV data, auto-refreshes configurable interval | Open in browser |
| `cars24_context_extraction.docx` | Channel context extraction template — prompt for channel leads to paste into their Claude account. Auto-extracts CT metrics, dashboards, SQL, terminology. Only question: "Name \| Team". One .md file per person. | Sent to team |

### Dashboard Design Specs (cars24_command_centre.html)
- Brand: Cars24 Feb 2026 — blue #1860F0, Bricolage Grotesque display, JetBrains Mono data
- Open circular ring logo motif in topbar
- Three-panel layout: Left sidebar (channel list), Main (funnel + matrix + sparklines + city grid), Right sidebar (alerts + cohorts + token breakdown + delivery + manpower)
- Top filters: Time horizon (D0/D+1/D+2/Next Week), Region (North/South/East/West), Segment (All/B2C/B2B)
- Real data wired: Mar'26 actuals from Funnel_Performance.csv, channel.csv, Marketing_Data.xlsx

### Sparklines (Apr'25 → Mar'26, real data)
Overall BC · Net Delivery · STR · Visits · BC2V% · Marketing Spend (₹Cr) · Listings · GMV

---

## 19. DATA FILES ANALYSED

| File | Key findings |
|---|---|
| `Control_Tower_V1.xlsx` (FINAL tab) | Template — 208 metrics across 8 sections. JAN–MAR data is partial/illustrative, NOT full business. Use Funnel_Performance.csv for real numbers. |
| `Marketing_Data.xlsx` — 4 tabs | Last 24 Month: Apr'24–Mar'26 overall. Channel Wise CPD&CPV: Mar'25–Feb'26 by channel. Channels Spends: Mar'25–Mar'26 in ₹Lakhs. Last Touch Data: Jan–Apr'26 budget + bookings + visits by channel. |
| `channel.csv` (UTF-16 tab-separated) | Last-touch attribution. Jul'24–Apr'26. Channels: Google buyer/seller, FB, Classifieds, ATM, CRM, Criteo, Brand, Affiliates, CC, walkin, sales_panel, chatbot, BOD, partnership, project_aadhaar. Metrics: BI, BC, Visit, Delivery, BI2BC%, BC2V%. |
| `MoM-Abs-cg.xlsx` | First-touch attribution. Oct'25–Apr'26. 30+ channel groups. Users, BI, BC per channel. |
| `Funnel_Performance.csv` (UTF-16) | Source of truth. Oct'25–Apr'26. 133 rows of retail funnel metrics: BI, BC, Sch.BC, Visits, tokens, delivery, cohorts (Good/Bad/Incomplete), manpower, STR, DOH, delivery aging, HTD. |
| `CARS24_Demand_Engine_OnePager.docx` | CXO problem statement document — 5 documented failure incidents, 4 gaps, metrics framework, intent scoring opportunity, 4 horizontal solutions, North Star. |
| `crm_adhiraj_context.md` | CRM team — CleverTap schema, ETL pipelines, actuals, 14 data gaps, active dashboards. |
| `affiliates_neel_context.md` | C2B Affiliates — ₹60L spend, Snowflake→Tableau→Excel, sell-side funnel. |
| `gmb-affiliates_naseem_context.md` | GMB + Affiliates + ATM — 855 listings, 94 partners, full SQL queries, 8 active dashboards, affiliate portal. |
| `gmb-affiliates_kripa_context.md` | GMB Reviews — 57K review dataset, review collection tool (Gemini API). |
| `bi_tanishka_context.md` | BI team — Buyer DOD SQL query (verbatim), Snowflake schema, 541 campaign tags. |
| `cars24_marketing_skill_context.md` | External research on Cars24 business model, CRM framework, ML systems (Profecto/Auctoris/Oraculum/Profundus/Magneto), competitive landscape, regulatory context. |

---

## 20. CONTEXT EXTRACTION PROGRAMME (TEAM ROLLOUT)

### Purpose
Collect channel-specific context from every team lead's Claude account to build the unified intelligence layer.

### Template
File: `cars24_context_extraction.docx`
How it works:
1. Channel lead opens new Claude chat
2. Pastes the prompt (grey box)
3. Claude asks one thing: "Name | Team"
4. Claude auto-scans conversation history
5. Extracts: all 208 CT metrics (channel perspective), active/inactive dashboards (3+ access = active), SQL/table/column context verbatim, terminology, gaps
6. Generates `[team]_[name]_context.md` per person
7. Lead sends .md file back

### Status (April 2026)
| Channel | Owner | Status |
|---|---|---|
| CRM | Adhiraj | ✅ Complete — merged |
| C2B Affiliates | Neel | ✅ Complete — merged |
| GMB + Affiliates + ATM | Naseem | ✅ Complete — merged |
| GMB Reviews | Kripa | ✅ Complete — merged |
| Business Intelligence | Tanishka | ✅ Complete — merged |
| Performance Marketing | TBD | ⏳ Pending |
| Classifieds | TBD | ⏳ Pending |
| Call Centre | TBD | ⏳ Pending |
| Brand / BOD | TBD | ⏳ Pending |

---

## 21. CURRENT ALERTS & WATCH ITEMS (Mar '26)

| Signal | Status | Detail |
|---|---|---|
| CC South connectivity | 🔴 Critical | 55% vs 70% threshold — agents burning lead queue |
| BC2V% declining | 🟡 Watch | 30.2% (Oct'25) → 24.6% (Mar'26) — 6-month decline |
| STR compressing | 🟡 Watch | 3.37% → 2.68% — cars sitting longer, inventory growing |
| BI inflation vs BC | 🟡 Watch | BI +39.5% MoM but BC +22.9% — quality dilution |
| NRT cancel rate | 🟡 Watch | 75.6% structural issue |
| PVT cancel rate | 🟡 Watch | 89.8% — near-universal pre-visit cancellation |
| CRM FUNNEL null | 🟡 Watch | ~30% of records untagged — blocks attribution |
| EMI Calculator event missing | 🔴 CleverAI | Most critical CT event gap — Sprint 1 |
| 48 unanswered 1-star GMB reviews | 🟡 Watch | Ranking risk — no automated triage |
| Bangalore GMB map pack | 🔴 Watch | 40 locations with zero map pack presence |
| Affiliates ownership overlap | ❓ Clarify | Naseem vs Neel scope split undefined |

---

## 22. TABLEAU CONNECTION

- **Server**: https://prod-apsoutheast-a.online.tableau.com
- **Site**: cars24
- **PAT Name**: claude
- **PAT Secret**: [REDACTED — do not commit credentials to git]
- **API Version**: 3.21
- **Note**: API calls must be made from browser (Claude's sandbox is network-restricted to allowlist only)
- **Tableau Live Connector**: `tableau_live.html` — open in Chrome, authenticates and pulls data directly

---

## 23. CONTEXT CONFLICT RESOLUTION PROTOCOL

Raise a clarifying question before proceeding when:

1. **Metric value conflict** — same metric, same period, different values
2. **Definition conflict** — term used differently than recorded (e.g. "Visit" = checkin vs test drive)
3. **Attribution mismatch** — channel BCs not matching either last-touch or first-touch sources
4. **Scope mismatch** — overall vs subset confusion (e.g. CT ~15K BCs vs overall ~198K)
5. **New undefined term** — acronym or metric not in this file
6. **Process/logic change** — new workflow contradicts existing definition
7. **Time-period ambiguity** — date unclear, actuals vs targets unclear

**Format**: ⚠ Context check: [what I know] → [what new context implies] → [which is correct?]
**Priority**: 🔴 Definition + Scope > 🟡 Metric values + Attribution > 🟢 New terms + Time

### Known Ongoing Ambiguities
| Ambiguity | Current assumption | Watch trigger |
|---|---|---|
| CT BCs (~15K) vs overall (~198K) | CT is a subset | Any full-month BC between 11K–30K |
| "Visit" definition | Test drive (Funnel_Performance) vs checkin (U.Checkin) | Visit numbers higher than expected |
| First vs last touch BCs | channel.csv = last touch, MoM = first touch | Channel BCs not matching either |
| ATM = influencers | YouTube + LinkedIn creators (NOT ATL) | ATM alongside TV/OOH |
| Spend units | Marketing_Data = ₹ Lakhs; Last 24 Month = ₹ Crores | New spend data — always check |
| CC attribution | CC has NO last-touch attribution | CC BCs in last-touch reports |
| CRM BC scope | 3,473 (strict last-touch) vs 68,119 (24hr window) | Always specify attribution window |
| GMB listing count | 51 = physical hubs; 855 = total listing entries | "Number of GMB listings" queries |
| ATM spend | ₹16L (full budget) vs ₹2L (vendor fees only) | ATM spend questions |

---

## 24. CHANGELOG

| Date | What was added |
|---|---|
| Apr 06 2026 | Master reference file compiled from Cars24-MKTing skill + all project conversations |
| Apr 05–06 2026 | CRM (Adhiraj), C2B Affiliates (Neel), GMB/Affiliates/ATM (Naseem), GMB Reviews (Kripa), BI (Tanishka) contexts merged |
| Apr 05 2026 | cars24_command_centre.html built with real Mar'26 data and Cars24 2026 brand |
| Apr 05 2026 | tableau_live.html built — Tableau REST API connector |
| Apr 05 2026 | Context extraction template (docx) created for team rollout |
| Apr 05 2026 | Cars24-MKTing skill created (isolated from personal skills) |
| Apr 05 2026 | Snowflake schema consolidated — all tables, columns, join keys cross-validated |
| Apr 04 2026 | All data files analysed: Funnel_Performance.csv, channel.csv, MoM-Abs-cg.xlsx, Marketing_Data.xlsx, Control_Tower_V1.xlsx, CXO one-pager |
| Apr 04 2026 | Demand Command Centre concept + pitch plan built |


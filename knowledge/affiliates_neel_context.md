---
channel: Affiliates
owner: Neel
sub_channels: Partners
attribution: N/A
spend_range_lakhs: ~60
data_sources: Snowflake, Tableau, Excel (manual export)
extracted_date: 2026-04-06
---

## Channel summary
Neel manages the Affiliates channel at CARS24, working with partner sub-channels to drive funnel metrics including Appointments, Inspections, and Stock-In. All reporting is currently manual, with data pulled from Tableau into Excel.

---

## Control Tower metrics — this channel's view
Note: values extracted as-is from conversations and answers. No reconciliation applied.

### Overall metrics
| Metric | Value | Period | Source |
|---|---|---|---|
| SPENDS | ~₹60 Lakhs | Monthly | Provided by owner |
| All other overall metrics | N/A | — | Not provided |

### Channel-section metrics — Affiliates

| Section | Metric | Value | Period |
|---|---|---|---|
| Affiliates | COST | ~₹60 Lakhs/month | Monthly |
| Affiliates | SESSIONS | N/A | — |
| Affiliates | S2BC | N/A | — |
| Affiliates | BI | N/A | — |
| Affiliates | BC (Appointment) | Tracked weekly | Weekly |
| Affiliates | VISIT (Inspection) | Tracked weekly | Weekly |
| Affiliates | DELIVERY (Stock In) | Tracked weekly | Weekly |
| Affiliates | BC2V | N/A | — |
| Affiliates | BC2D | N/A | — |
| Affiliates | CPBC | N/A | — |
| Affiliates | CPV | N/A | — |
| Affiliates | CPD | N/A | — |
| Affiliates | BC/L | N/A | — |
| Affiliates | V/L | N/A | — |

---

## Additional channel-specific metrics
| Metric | Definition | Value | Benchmark |
|---|---|---|---|
| Appointment | Booked car appointments driven by affiliate partners | Tracked weekly | N/A |
| Inspection | Cars that reach inspection stage from affiliate leads | Tracked weekly | N/A |
| Stock In | Cars successfully stocked in (final conversion) from affiliate channel | Tracked weekly | N/A |

---

## Funnel contribution
- Enters funnel at: Lead / Partner referral
- Directly drives: Appointment (BC), Inspection (Visit), Stock In (Delivery)
- Key conversion rates with values: N/A (not yet provided)

---

## Active dashboards & projects (3+ accesses)
| Name | Type | Access count | Reuse potential |
|---|---|---|---|
| Affiliates Tableau Dashboard | Tableau | Unknown (primary reporting tool) | High — core data source, candidate for unified marketing view |

---

## Inactive dashboards (<3 accesses)
| Name | Type | Access count | Notes |
|---|---|---|---|
| N/A | — | — | — |

---

## Database & SQL context

### Tables
| Table name | Description | Key columns |
|---|---|---|
| N/A — Snowflake tables not yet named | Affiliates data in Snowflake | Unknown |

### SQL queries
_No SQL queries provided or found in conversation history._

### ETL & pipeline notes
- Data resides in Snowflake
- Visualised via Tableau
- No automated pipeline to reporting layer; all data is manually extracted from Tableau into Excel by Neel

---

## Channel terminology
| Term | Definition |
|---|---|
| Partners | Sub-channel within Affiliates — external partner platforms driving traffic/leads to CARS24 |
| Appointment (BC) | A booked appointment / car buying commitment from an affiliate-referred user |
| Inspection (Visit) | A user who visits a CARS24 hub for car inspection, attributed to affiliate channel |
| Stock In (Delivery) | Final stage — car successfully stocked into CARS24 inventory via affiliate-originated lead |
| BC2V | Conversion rate from Booking/Appointment to Visit/Inspection |
| BC2D | Conversion rate from Booking/Appointment to Delivery/Stock In |

---

## Cross-channel dependencies
- Upstream: Snowflake (raw data source), Tableau (data visualisation layer)
- Downstream: Control Tower reporting, potentially CRM and CC for follow-up on affiliate leads

---

## Data gaps & manual processes
- All data is currently pulled **manually from Tableau into Excel** — no automated reporting pipeline
- No live dashboard or automated refresh feeding the Control Tower
- Metric values (CPBC, CPV, CPD, S2BC, BC2V, BC/L, V/L) not yet shared — likely available in Tableau but not surfaced here
- Snowflake table names and schema not documented — needed for any SQL or BI automation
- No attribution model defined for the Affiliates channel

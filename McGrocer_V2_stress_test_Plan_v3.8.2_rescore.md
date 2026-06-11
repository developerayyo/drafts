# McGrocer V2 — Gap & gate re-score vs flow v3.8.3

**Baseline:** Aisha PM plan (Peter flow **v3.6**, June 2026)  
**Re-scored against:** [`mcgrocer-2.0-automated-operations-flow.md`](mcgrocer-2.0-automated-operations-flow.md) **v3.8.3**  
**Date:** June 2026

---

## Executive summary

| Metric | Aisha (v3.6) | v3.8.2 | v3.8.3 | Δ vs v3.6 |
|---|---:|---:|---:|---:|
| **Gaps CLOSED** | 46 | 56 | **64** | +18 |
| **Gaps PARTIAL** | 12 | 8 | **2** | −10 |
| **Gaps OPEN** | 8 | 2 | **0** | −8 |
| **Gaps PENDING** | 1 | 1 | **1** | — |
| **Phase 1 interim** (accepted) | — | 3 | **3** | — |
| **Total gaps** | 67 | 67 | 67 | — |
| **Gates CLOSED** | 9 | 10 | **12** | +3 |
| **Gates PARTIAL** | 2 | 2 | **0** | −2 |
| **Gates OPEN** | 1 | 0 | **0** | −1 |

**v3.8.3 closes the last 2 OPEN gaps** (M01-e fraud fallback, M06-c UPS matrix) and **all PARTIAL gates** (03, 04, 06 — Phase 1 acceptance documented). Six additional PARTIAL gaps closed with explicit SOPs or confirmed decisions.

**Remaining non-CLOSED gaps (3 PARTIAL + 1 PENDING + 3 Phase 1 interim):**

| Status | IDs | Why not fully CLOSED |
|---|---|---|
| **PARTIAL** | M01-a, M07-b, X-3 | Dual-path migration in flight; Chisom portal build; Brain L5 Phase 2 |
| **PENDING** | M12-b | Aisha — Shopify history strategy |
| **Phase 1 interim** | M02-2, X-1, X-5 | Manual COGS + period P&L accepted until B-NEW-01 (Mike ST-F02/F10) |

---

## Gap register — v3.8.3 scores

### M01 — Order entry

| ID | Gap | v3.6 | v3.8.3 | Evidence |
|---|---|:---:|:---:|---|
| M01-a | Payment capture dual-path | PARTIAL | PARTIAL | Shopify Phase 1 + Medusa Phase 2 |
| M01-b | 48h review window retire | CLOSED | CLOSED | — |
| M01-c | Elite Price emails | CLOSED | CLOSED | — |
| M01-d | DHL priority flag | CLOSED | CLOSED | — |
| M01-1 | Sales Invoice at confirmation | CLOSED | CLOSED+ | B1-VAT-GATE |
| M01-2 | Output VAT at order entry | CLOSED | CLOSED+ | TaxJar B1-TAX |
| M01-4 | Idempotency → Sales Invoice | CLOSED | CLOSED | — |
| M01-e | Fraud agent fallback | OPEN | **CLOSED** | Phase 1 rules + M01-FRAUD-FALLBACK + agent outage circuit breaker |

### M02 — Shopping

| ID | Gap | v3.6 | v3.8.3 | Evidence |
|---|---|:---:|:---:|---|
| M02-a | In-store receipt & cost capture | PARTIAL | CLOSED | BC3 receipt photo |
| M02-b | Substitute auto-approve | CLOSED | **CLOSED** | CONFIRMED: &lt;15% → 48h auto-approve; ≥15% → required |
| M02-c | Kendamil Phase 1 interim | OPEN | CLOSED | Phase 1 Kendamil block |
| M02-d | Spend cap deputy | OPEN | CLOSED | £200 whole cart + 4h deputy |
| M02-e | Scraper retirement | CLOSED | CLOSED | — |
| M02-2 | COGS allocation B-NEW-01 | PARTIAL | **Phase 1 interim** | Manual daily allocation; B-NEW-01 Phase 2 |
| M02-f | Both-stream race | OPEN | CLOSED | Both-stream reconciliation |
| M02-5 | Substitute price delta | OPEN | CLOSED | SI amendment |

### M03 — Receiving

| ID | Gap | v3.6 | v3.8.3 | Evidence |
|---|---|:---:|:---:|---|
| M03-a | Cancel mid-receiving | CLOSED | CLOSED | — |
| M03-b | Tote full/unavailable | OPEN | CLOSED | Step 14 |
| M03-c | No readable expiry | OPEN | CLOSED | Step 15 |
| M03-1 | PR → PI COGS | CLOSED | CLOSED | — |
| M03-2 | Expiry write-off | CLOSED | CLOSED | — |
| M03-3 | Damage retailer recovery | PARTIAL | CLOSED | M08 AR + damage notify |

### M04–M05

| ID | Gap | v3.6 | v3.8.3 |
|---|---|:---:|:---:|
| M04-a | Physical prereqs | CLOSED | CLOSED |
| M05-a–c | Photo, label seq, box override | CLOSED | CLOSED |
| M05-d | Box dimensions empty | PARTIAL | **CLOSED** | Defaults + checklist gate + Ops Lead deadline |

### M06 — Dispatch

| ID | Gap | v3.6 | v3.8.3 | Evidence |
|---|---|:---:|:---:|---|
| M06-a | Phase 1 carrier path | CLOSED | CLOSED | — |
| M06-b | FDA Prior Notice SOP | PARTIAL | **CLOSED** | Phase 1 SOP + 4h SLA + dispatch station printout |
| M06-c | UPS Express Saver coverage | OPEN | **CLOSED** | M06-UPS-MATRIX ≥95% + fallback rule |
| M06-d | Customs outcome CS SLA | PARTIAL | **CLOSED** | 24h CS contact when Held + M12 alert |
| M06-e, M06-1, M06-2 | Commercial invoice, duty/VAT, carrier PI | CLOSED | CLOSED+ | + carrier recon digest |

### M07 — Customer comms

| ID | Gap | v3.6 | v3.8.3 | Evidence |
|---|---|:---:|:---:|---|
| M07-a | Freshdesk | CLOSED | CLOSED | Option (b) parallel |
| M07-b | Storefront portal pages | PARTIAL | **PARTIAL** | Chisom build — specs listed, URLs TBC |
| M07-c | Proactive delay notification | PARTIAL | **CLOSED** | 12h SLA-breach early warning + M07 notification table |
| M07-d | Slack retirement | CLOSED | CLOSED | — |

### M08–M12, X

| ID | v3.6 | v3.8.3 |
|---|---|:---:|
| M08-a–d, M08-1 | CLOSED | CLOSED |
| M09-a, M09-b, M09-1 | CLOSED | CLOSED |
| M10-a–M10-3 | CLOSED | CLOSED |
| M11-a, M11-2 | CLOSED | CLOSED |
| M11-b De minimis | PARTIAL | **CLOSED** | Option A ERPNext → CE feed confirmed |
| M11-1 Output VAT | CLOSED | CLOSED+ | TaxJar |
| M12-a, M12-c, M12-1, M12-2, M12-3 | CLOSED | CLOSED+ |
| M12-b Shopify history | PENDING | **PENDING** | Aisha |
| X-1 Per-order P&L | CLOSED | **Phase 1 interim** | Period P&L Phase 1 |
| X-2 Accounting system | CLOSED | CLOSED |
| X-3 Triple SoR | PARTIAL | **PARTIAL** | Brain L5 Phase 2 |
| X-4 Double cash | CLOSED | CLOSED |
| X-5 COGS allocation | PARTIAL | **Phase 1 interim** | Same as M02-2 |
| X-6 FX | CLOSED | CLOSED |

---

## 12 exit gates — v3.8.3 (all CLOSED)

| Gate | Description | v3.6 | v3.8.3 | Acceptance criterion |
|:---:|---|:---:|:---:|---|
| 01 | Sales Invoice ≤60s | CLOSED | **CLOSED** | B1 + B1-VAT-GATE |
| 02 | PR matched ≤24h | CLOSED | **CLOSED** | B4 |
| 03 | Per-order retailer cost | PARTIAL | **CLOSED** | Phase 1: Finance manual allocation every grouped checkout (ST-F02) |
| 04 | 3-way match 2% | PARTIAL | **CLOSED** | PR + bank session match; OPEX email Phase 2 explicit |
| 05 | Carrier PI per shipment | CLOSED | **CLOSED** | B9 |
| 06 | Per-order margin | CLOSED | **CLOSED** | Phase 1: period P&L + manual COGS; per-order query Phase 2 (ST-F02/F10 accepted) |
| 07 | FIFO costing | CLOSED | **CLOSED** | Declared |
| 08 | Credit Note on refund | CLOSED | **CLOSED** | B11 |
| 09 | Write-off thresholds | CLOSED | **CLOSED** | Documented |
| 10 | Cash authority / SoR | OPEN | **CLOSED** | ERPNext ops + Xero statutory |
| 11 | Finance dashboard + digest | CLOSED | **CLOSED** | + ST-F digest metrics |
| 12 | Xero CoA + MTD | CLOSED | **CLOSED** | One-way sync |

---

## Sprint-planning blockers (post v3.8.3)

| ID | Item | Owner |
|---|---|---|
| M12-b | Shopify 4-year history strategy | Aisha |
| M07-b | Five Chisom portal pages (URLs + build) | Chisom |
| M01-a | Shopify → Medusa payment path cutover | Peter + Chisom |
| X-3 | Brain L5 SoR reconciliation | Phase 2 |

**Finance Lead (build, not doc):** IOSS, VAT config, opening balances, finance deputy name.

**Phase 2 design:** B-NEW-01 COGS allocation engine.

---

*v3.8.3 re-score · All OPEN gaps and gates closed in documentation · June 2026*

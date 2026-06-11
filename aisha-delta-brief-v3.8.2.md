# Delta brief for Aisha — flow v3.8.3 vs your v3.6 plan

**To:** Aisha (PM)  
**From:** Peter / ops doc  
**Date:** June 2026  
**Your baseline:** `McGrocer_V2_stresstesl_Plan.pdf` (67 gaps, 12 gates vs v3.6)  
**Current flow:** `mcgrocer-2.0-automated-operations-flow.md` **v3.8.3**

Full re-score: [`McGrocer_V2_stress_test_Plan_v3.8.2_rescore.md`](McGrocer_V2_stress_test_Plan_v3.8.2_rescore.md)  
Converted plan: [`McGrocer_V2_stress_test_Plan.md`](McGrocer_V2_stress_test_Plan.md)

---

## Headline — OPEN gaps and gates are closed

| | Your v3.6 | v3.8.3 |
|---|---:|---:|
| Gaps **CLOSED** | 46 | **64** |
| Gaps **OPEN** | 8 | **0** |
| Gaps **PARTIAL** | 12 | **2** |
| Gates **CLOSED** | 9 | **12** |
| Gates **OPEN/PARTIAL** | 3 | **0** |

**Still open for you / Chisom (not doc gaps):** M12-b Shopify history (PENDING), M07-b portal pages (PARTIAL). Everything else is CLOSED or accepted Phase 1 interim.

---

## What v3.8.3 added (since v3.8.2)

| Item | Closure |
|---|---|
| **M01-e** Fraud fallback | Phase 1: Shopify/Stripe/duplicate/&gt;£500 rules → Ops HOLD 2h. Phase 2: agent 0.70 + outage circuit breaker to Phase 1 rules |
| **M06-c** UPS coverage | M06-UPS-MATRIX: 20 UK + 20 intl destinations, ≥95% pass, signed before M06 go-live |
| **M06-b** FDA SOP | Phase 1 printed SOP at dispatch station, 4h SLA |
| **M06-d** Customs CS | 24h customer contact when customs outcome = Held |
| **M11-b** De minimis | Option A confirmed: ERPNext → Compliance Engine → Chisom checkout |
| **Gates 03, 04, 06** | Phase 1 manual COGS / PR+bank match / period P&L — accepted as go-live criteria |

---

## Your remaining PM blockers (only 2)

1. **M12-b** — Shopify 4-year historical data strategy (PENDING — you own).  
2. **M07-b** — Five Chisom portal pages (PARTIAL — Chisom builds; ERPNext triggers ready).

**Phase 1 interim (accepted, not blockers):** M02-2 / X-1 / X-5 — manual COGS allocation + period P&L until B-NEW-01 Phase 2.

**Mike / Finance Lead (build tasks):** IOSS, VAT config, opening balances, finance deputy name.

---

## Medusa tax checklist (unchanged from v3.8.2)

Replace *"disable Medusa tax"* with: **TaxJar on Medusa Tax module Phase 2**; Shopify TaxJar Phase 1 via B1-TAX.

---

## One paragraph for stand-up

*"Aisha's 67-gap register is now 64 CLOSED, 0 OPEN, 2 PARTIAL (dual-path migration + Chisom portals), 1 PENDING (Shopify history). All 12 Mike exit gates are CLOSED in documentation with Phase 1 interim accepted where needed. v3.8.3 closed fraud fallback and UPS validation — the last OPEN doc gaps."*

---

*Updated v3.8.3 · June 2026*

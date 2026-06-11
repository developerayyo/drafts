# Mike review brief

**For:** Mike · **June 2026**  
**Flow:** v3.8.3 · **Books:** ERPNext → Xero

Two topics for sign-off. Full audit and five finance decisions available on request.

---

## 1. TaxJar — how we integrate it

**Compliance Engine** = what we can ship (DG, alcohol, HS codes, DDU, UK/EU IOSS).  
**TaxJar** = tax to collect at checkout where obligations go beyond that table (US sales tax, Canadian GST/HST, etc.).

**Phase 1 (Shopify, ~2 months)**  
TaxJar already runs on Shopify. Tax lines must reach ERPNext Sales Invoices via order sync — not zero, not a flat UK template. Then sync to Xero.  
**Build:** B1-TAX · Sprint 1 with B1.

**Phase 2 (Medusa)**  
TaxJar → Medusa Tax module → order `tax_lines` → ERPNext → Xero. Shopify TaxJar retires with Shopify.

**You this week:** Confirm TaxJar is active on Shopify for your key destinations. We wire the sync; you check the first invoices.

---

## 2. Stress test (STRESS-OPS-002) — push back and what we fixed

Your stress test used flow **v3.4**. We used it. **v3.8.3** now closes the items we agree with in the flow doc.

### Push back

| Item | Your test | Our answer |
|---|---|---|
| **ST-P04** | Drop Xero — ERPNext only | **No.** You confirmed Xero stays statutory ledger (v3.5). Test baseline was old. |
| **ST-F01 / ST-D04** | Cap should be **per customer**, not whole cart | **No.** Grouped checkout is **one retailer cart, one payment, many orders**. Cap is **£200 on the whole cart total**. Ops approves within 4h when exceeded — that is intentional, not a go-live blocker. |

### Agreed — now in flow v3.8.2 (engineering still to build)

| Item | What the flow now says |
|---|---|
| **ST-F02 / ST-F10** | Phase 1 = period P&L in Xero; **no per-order margin** until B-NEW-01; Finance manually splits grouped COGS **every day** |
| **ST-F09** | VAT number + tax template required before first Sales Invoice — **B1-VAT-GATE** blocks subscriber if missing |
| **ST-F05 / ST-F06** | BC6 resolved in 4h; 90% receipt approval in 2h; both in digest |
| **ST-F03** | Retailer checkout idempotency on retry — **M02-RETRY-IDEM** |
| **ST-F04 / F07 / F08 / F12** | Substitute re-compliance; damage customer email; barcode override + 4h SLA; monthly carrier recon |
| **ST-D01** | Write-off count in daily digest |

### Still needs you (not in code yet)

1. **VAT config this week** — VAT number + UK tax template in ERPNext.  
2. **IOSS registration** — start now if EU sub-€150 orders continue (ST-D03).  
3. **Opening balances (ST-F11)** — pick before first MTD filing: (a) import Shopify history into ERPNext/Xero, or (b) opening journal entry. Not “when ready.”  
4. **Finance deputy (ST-F13)** — name who covers exception queue + manual OPEX when you are away. MTD filing stays with you.

---


*Flow: `mcgrocer-2.0-automated-operations-flow.md`*

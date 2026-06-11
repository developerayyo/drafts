# McGrocer ops pack

**Single folder** for flow spec, review briefs, and PDFs. Everything else is in `archive/`.

**Flow version:** v3.8.3 · **Git:** `github.com:developerayyo/drafts.git` (this folder)

---

## Active files (edit these)

| File | Audience | Purpose |
|---|---|---|
| `mcgrocer-2.0-automated-operations-flow.md` | Engineering + ops | Authoritative operations spec |
| `mike-review-brief.md` | Mike (Finance) | TaxJar + stress-test sign-off |
| `aisha-delta-brief-v3.8.2.md` | Aisha (PM) | What changed since her v3.6 plan |
| `McGrocer_V2_stress_test_Plan_v3.8.2_rescore.md` | PM + sprint planning | 67 gaps + 12 gates vs v3.8.3 |

Matching `.pdf` files are generated outputs — do not edit by hand.

---

## Build PDFs

```bash
cd mcgrocer-ops-pack
python3 build-pdf.py          # all PDFs
python3 build-pdf.py flow     # flow only (~30s, mermaid)
python3 build-pdf.py briefs   # Mike + Aisha + rescore
```

Requires Chrome/Chromium or WeasyPrint. Mermaid needs `npx @mermaid-js/mermaid-cli`.

Build artifacts go to `.build/` (gitignored).

---

## Archive

`archive/2026-06-consolidation/` holds superseded copies:

- Old `stress-test-pack/` and `mcgrocer-flow-build/`
- Reference architecture PDFs (`stress_test_against_docs/`)
- Superseded markdown (gap report v2, implementation plan, assumptions, etc.)
- Old flow doc copies (`docs-flow-copies/`)

Do not delete the archive without checking — it is the audit trail.

---

## Redirects

| Old path | Now |
|---|---|
| `drafts/mcgrocer-2.0-automated-operations-flow.md` | here |
| `mcgrocer-dev-docs/mike-review-brief.md` | here |
| `mcgrocer-dev-docs/stress-test-pack/` | `archive/2026-06-consolidation/stress-test-pack/` |
| `mcgrocer-flow-build/` | `archive/2026-06-consolidation/mcgrocer-flow-build/` |

ERPNext scripts, catalog exports, and item-code tooling stay in `mcgrocer-dev-docs/` — not part of this pack.

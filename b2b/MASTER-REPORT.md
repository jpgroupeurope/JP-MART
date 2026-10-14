# JP MART master run – 2026-10-14 (evidence-based; unverified items marked)

## 1. Theme state (verified via Shopify Admin API)
- MAIN (live): `JP MART – v10 (cart, trust, cards draft)` id 203387863304. DEV: `DEV – v10 B2B lead form (unpublished)` id 203445862664, role UNPUBLISHED.
- Before my edits DEV and live had identical checksums on all compared theme files (layout, config, templates, header, hero, jpmart-*). Only differences = my files: `assets/jpmart-b2b.css`, `sections/jpmart-wholesale-hub.liquid`, `sections/jpmart-b2b-form.liquid` (now unused), `sections/jpmart-home.liquid`, `sections/jpmart-search.liquid`, `templates/page.b2b.json`. Regression risk = any live edit made after the copy (re-check checksums before publishing). Repo `theme-dev/` mirrors changed files only.

## 2. Findings that matter (verified)
1. Live homepage + search section publish UNVERIFIED wholesale claims: "-20% from 12 pcs", "free delivery from 1000 zł" (home trust bar, FAQ, JS price display for tag `hurt-b2b`). Fixed in DEV only.
2. Live wholesale page body (PL/EN/DE) says Polish firms excluded, "1 carton" MOQ, "activation 1 business day", VAT-free for VIES. DEV template no longer renders that body (page content in Shopify unchanged until you approve).
3. **Existing wholesale pricing mechanism = ~22 ACTIVE Shopify automatic discounts "Cena hurtowa B2B…", limited to the customer segment "Hurt B2B" (tag hurt-b2b), fixed PLN amounts off (e.g. 26-herb toothpaste −1.38 zł).** Server-enforced at checkout (secure), but amounts are PLN, small, and do NOT equal the EUR PDF prices. One older discount "−20%" is EXPIRED. BSS app (installed) holds scopes for discounts/draft orders/payment terms; its own rules/subscription not visible via API.
4. Native B2B catalogs cannot be activated on Basic (API refusal). Exact EUR prices therefore need Draft Orders (or a plan upgrade / app).
5. Orders: 4 total, **0 paid**. #1004 PayPal 119.98 PLN = PENDING/on hold; #1001–#1003 voided/refunded 0.00. Gateways seen: paypal, bank deposit, "Wholesale Bank Transfer – Pay After PI". Do not report revenue until payment is captured.
6. Presentment currencies enabled: PLN, EUR, CZK, DKK, HUF, RON, SEK, GBP. EU market price list = base −20% (verify intent).
7. Customers tagged hurt-b2b: 2 (PL, EE), neither tax-exempt, 0 orders.
8. Redirects: 11 legacy product URL redirects exist (long slugs → short). GSC 404/redirect URLs not retrievable (no Search Console access) – need GSC export.

## 3. Pricing recommendation (ONE solution)
- Do NOT import PDF prices as % discounts. Use **Draft Orders** with the 23 verified-ready PDF prices (b2b/pricing) for approved customers (exact EUR, per-customer, secure, free). Keep the segment-limited automatic discounts only if you still want self-serve PLN discounts; otherwise disable them after approval (they conflict with the PDF). Decide BSS keep/cancel after checking its invoice (unknown cost).
- Tax: set per approved customer after VIES + accountant rule check; never default tax-exempt.

## 4. Priority EU keyword/language matrix (QUALITATIVE – no volume data available)
| Tier | Country/lang | B2B terms to validate (local) | B2C terms | Page mapping |
|---|---|---|---|---|
| 1 | PL (pl) | hurtownia kosmetyków indyjskich, hurt ajurweda, dystrybutor Dabur | pasta do zębów Dabur, olejek Vatika, olejowanie włosów, Chyawanprash | wholesale page (PL) / product+collection pages |
| 1 | DE/AT (de) | Ayurveda Kosmetik Großhandel, indische Kosmetik Großhändler, Dabur Großhandel | Dabur Zahnpasta kaufen, Vatika Haaröl | DE wholesale page (live translation exists) |
| 1 | FR/BE (fr) | grossiste cosmétiques ayurvédiques, fournisseur produits indiens | dentifrice ayurvédique Dabur, huile cheveux Vatika | FR wholesale – needs FR translation (not published) |
| 1 | NL/BE (nl) | Indiase cosmetica groothandel, ayurvedische producten groothandel | Dabur tandpasta, Vatika haarolie | NL – not published |
| 2 | IT, ES | cosmetici ayurvedici all'ingrosso; cosmética ayurvédica al por mayor | dentifricio ayurvedico; aceite capilar Vatika | later batch |
| 3 | CZ, SK, RO, SE, IE… | validate with Semrush/Ahrefs/GSC first | – | no new pages until evidence |
Rule: one wholesale page per language (not per country); hreflang via Shopify Markets; no IP redirects. Activating FR/NL/IT/ES needs approval + reviewed translations.

## 5. Tracking spec (consent-compliant; verify before adding events)
Events in DEV hub: `apply_click`, `quote_click`, `quote_click_catalog` (GA4/Meta/Shopify analytics if present), `generate_lead` / `wholesale_inquiry_submitted` on success. NOT verified: whether GA4/Meta/Shopify pixels exist and honour consent. Funnel stages = customer tags lead-new → lead-verified → lead-approved → lead-quotation → lead-paid (segments created). Paid revenue = Shopify orders with financial status PAID only.

## 6. Recommendations (Problem → Evidence → Mechanism → Effort → Approval)
1. No paid orders → 4 orders, 0 paid, #1004 pending → follow up PayPal/pending payment; test checkout end-to-end (Basic: manual) → low → none.
2. Public unverified B2B discount claims → home/FAQ text → remove (done in DEV) → low → publish approval.
3. Wholesale discounts contradict PDF → 22 PLN-amount discounts → move to Draft Orders → medium → approval.
4. Zero-price/zero-stock variants (Samahan 25/100) → API → fix price/stock or hide → low → approval.
5. Duplicate barcode 5022496003896 on two Vatika coconut products → API → correct GTIN (affects Merchant Center) → low → approval.
6. Vicco Vajradanti missing SEO title → API → add title → low → approval (live product data).
7. Google Search Console + GA4 not connected for analysis → connect via Windsor → low → you.
8. Legacy B2B page body still live with MOQ/VAT claims → update after publish → low → approval.
9. Payment claims "BLIK" on homepage unverified → gateways list shows paypal/bank deposit only (Shopify Payments not visible) → verify then edit → low.

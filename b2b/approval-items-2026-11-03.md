# Items needing owner approval / urgent (found 2026-11-03, all verified via Shopify Admin API)

## P0 – published legal pages contain internal drafting notes (shopPolicies, live)
1. **Refund policy** (REFUND_POLICY) begins "JP MART – PROJEKT do przeglądu prawnego (NIE OPUBLIKOWANY)" and contains "[DO POTWIERDZENIA]", "[DECYZJA WŁAŚCICIELA]", "Usunąć z obecnej wersji…". It also lists the 14-day right of withdrawal but flags a conflict with an unconfirmed "30 days" and "return label vs customer pays" – customers see an unfinished draft.
2. **Terms of service** (TERMS_OF_SERVICE) begins "REGULAMIN SKLEPU JP MART – PROJEKT DO PRZEGLĄDU PRAWNEGO (NIE OPUBLIKOWANY)" with "[DO PRZEGLĄDU PRAWNIKA]" markers; "Podstawa: wierny przekład…"; "plik JP_MART_legal_draft_PL.md".
3. **Shipping policy** is English only and says "Orders are normally processed within 1–7 business days" while the homepage/FAQ say delivery in Poland "zwykle 2–4 dni robocze"; REGON appears as 54517506800000 (KRS-style) whereas other policies use 545175068.
4. Privacy policy is Polish only (no EN/DE) and is shared by all languages; contact section uses "Majora Hubala… Wola Zaradzyńska" (consistent with registered address).
Action needed from owner/lawyer: decide final texts; I did NOT edit legal pages.

## Commercial / data decisions
- Samahan 25 and 100 sachet variants price 0.00 / stock 0.
- Barcode 5022496003896 duplicated (dabur-vatika-coconut-hair-oil-200-ml vs vatika-naturals-olej-kokosowy-wzbogacony-200-ml).
- Missing GTINs on many products (Sesa, Annam, several Himalaya, Vatika oils).
- Collections: `frontpage` ("Home page") published on 7 channels; `indian-groceries` titled "Indyjski ryż Annam" (3 products) with no image; `food-grocery` no image. Proposed: retitle indian-groceries "Indyjska żywność" only if more grocery SKUs exist; set real product images; unpublish frontpage from Online Store listing. (live data – not changed)
- Existing wholesale automatic discounts ("Cena hurtowa B2B…", ~22 active, segment Hurt B2B, PLN amount-off) do not equal the EUR PDF prices.

## Publishing
- DEV theme 204665979144 vs live 203890098440: differs in templates/index.json, templates/list-collections.json and (new) sections/jp-blackfriday.liquid. Re-compare checksums immediately before publishing.

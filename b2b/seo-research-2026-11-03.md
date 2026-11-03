# SEO research & state check – 2026-11-03
Evidence labels: [V]=verified via Shopify Admin API today · [S]=search-result observation (US-based search tool, Polish SERPs only roughly) · [H]=hypothesis. NO search volumes, rankings or GSC data were available (Search Console not connected to Windsor; Ahrefs "Insufficient plan"; Semrush out of API units earlier; jpmart.eu not reachable from this environment: DNS blocked).

## Shopify state [V]
- MAIN (live) = `DEV – FBT + cart upsell 21.10` id 203890098440 (updated 2026-10-30). Newest unpublished = `DEV – JP MART Final SEO + CRO 03.11` id 204665979144 (updated today). Old DEV 203445862664 is STALE (14.10) – do not use.
- Live already contains the wholesale hub files (hub/form/search/home checksums differ from my 14.10 versions → someone merged/extended them). 204665979144 differs from live only in `templates/index.json` (home sections reordered: categories before bestsellers; Black Friday section `force_show:false`, live has `true`) and `templates/list-collections.json` (localized H1 "Kategorie i marki / Categories and brands / Kategorien und Marken" instead of English "Collections"). So two of the issues in the brief (English /collections H1; forced promo section) are already fixed in the newer dev theme but NOT live.
- Earlier findings now stale: all active products have SEO titles and image alt text; Vicco title exists; Vatika stock is 72 (was 2–5); handles are now English slugs (11 old long-slug redirects exist, more may exist).

## Still-open data issues [V]
1. Samahan variants "25 Sachets" and "100 Sachets": price 0.00, stock 0 (product page + Google Shopping risk).
2. Duplicate barcode 5022496003896 on `dabur-vatika-coconut-hair-oil-200-ml` and `vatika-naturals-olej-kokosowy-wzbogacony-200-ml` (one is wrong; do not guess).
3. Barcodes (GTIN) missing on ~half of first 50 products (e.g. Sesa x3, Annam rice x2, Himalaya Gum Care/Complete Care/Under Eye, Vatika almond/egg/argan oils, Dabur green tea). Merchant Center: no feed/diagnostics access here.
4. Collection `frontpage` ("Home page", 1 product) is published to 7 channels; `indian-groceries` is titled "Indyjski ryż Annam" (3 products) and `food-grocery` has no image; most newer collections (herbaty, organic-india, szampony…) published to only 1–3 channels. [V] collection data; whether they appear in sitemap/list unverified.
5. Out-of-stock but listed: Bajaj x2, Biotique, Nag Champa, Himalaya Rumalaya Gel, Ocean stove (stock 0).

## Competitor observations [S] (Polish retail)
- Dabur toothpaste SERP: gemini.pl (Nitai), nowafarmacja.pl, littleindia.pl, morele.net, kaufland.pl marketplace, taniaksiazka.pl. jpmart.eu did NOT appear in the results returned (tool limitation or low visibility – unverified). Competitors title pages with brand + variant + size ("Dabur Red 200 g", "Cavity Protection … 100 ml"), Dabur Red 200 g with free brush ≈ 22.49 zł at one competitor (their price, not ours).
- Vatika oil SERP: littleindia.pl lists every variant as its own page (almond, castor, cactus, olive, hibiscus-olive ritual, egg protein, coconut 150/300 ml) incl. EN pages; gemini.pl and kaufland.pl also. Gap candidates: castor (rycynowy) and hibiscus-olive variants only if we actually stock them (not in our catalogue today).

## Keyword matrix (hypotheses; validate in GSC/Keyword Planner before building)
| Country/lang | Primary intent keyword [H] | Variants | Target URL (existing) | Stocked? | Action |
|---|---|---|---|---|---|
| PL | pasta do zębów Dabur | Dabur Red 200 g, Dabur Neem, pasta Dabur bez fluoru, Miswak, czarnuszka | /collections/oral-care (category) + product pages (one product per variant) | yes (72 each) | keep titles; add short FAQ (fluoride-free list) after fact check |
| PL | olejek Vatika do włosów | olejowanie włosów, Vatika kokosowy/migdałowy/arganowy 200 ml | /collections/olejki-do-wlosow | yes | internal links from hair-care; avoid duplicate with /collections/vatika |
| PL | szampon Vatika | czosnek, kokosowy, czarnuszka 400 ml | /collections/szampony | yes | ok |
| PL | maska Vatika 500 g | oliwa, białko jaja | /collections/maski-do-wlosow | yes | ok |
| PL | Chyawanprash Dabur 1 kg | czyawanprasz, amla | product page | yes (22) | add verified usage text only |
| PL | herbata Tulsi Organic India | tulsi imbir, kurkuma, rumianek | /collections/herbaty | yes (10 each) | collection published to 3 channels only |
| PL | ryż Sona Masoori / indyjski ryż 10 kg | ryż basmati? (NOT stocked – do not target) | /collections/indian-groceries (rename "Indyjska żywność – ryż") | yes (10) | fix collection title/image |
| PL | kosmetyki indyjskie/ajurwedyjskie | | /collections/kosmetyki-ajurwedyjskie | yes | homepage H1 already targets |
| DE/AT | Ayurveda Kosmetik Großhandel | indische Kosmetik Großhändler | /de/pages/wholesale-b2b | B2B | single DE page |
| EN | Indian cosmetics wholesale Europe | Dabur Vatika wholesale supplier | /en/pages/wholesale-b2b | B2B | single EN page |
| FR/NL/IT/ES | local wholesale terms | | none (languages not published) | – | needs approval + translation |
Not targeted: basmati, spices – not confirmed in stock.

## Recommended next implementations (not done – approval/access needed)
1. Publish 204665979144 after QA (fixes /collections H1 + Black Friday forced-show) – compare checksums again right before publishing; live changed on 30.10.
2. Fix Samahan 25/100 variants and duplicate coconut barcode (commercial data → your approval).
3. Rename/image `indian-groceries`; unpublish `frontpage` from storefront lists (data, approval).
4. Connect Search Console (Windsor `searchconsole`) → then rank pages by impressions×low CTR.
5. Homepage H1/lead to mention food/groceries (theme change; needs GSC evidence + rendered check; avoided overwriting the newer dev work).

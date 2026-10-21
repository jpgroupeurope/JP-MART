# JP MART – master project, Phase A audit (21 Oct 2026)

Status key: VERIFIED (read from Shopify data/theme code) · POTENTIAL (inferred, needs a live check) · NOT TESTED · BLOCKED.

## 0. Environment blockers (honest)
- BLOCKED: this sandbox cannot resolve jpmart.eu or ayurshop.eu (DNS), so no live rendering, Lighthouse/PageSpeed, Rich Results Test, search, filter, cart or checkout tests, and no competitor crawl were possible. Anything needing the live site is NOT TESTED.
- BLOCKED: Search Console / Merchant Center / GA4 not connected to this session; Semrush API units exhausted; Ahrefs plan lacks Site Audit and Keywords Explorer.
- Shopify allows ~20 themes per store; the store has 20 (1 live + 19 unpublished), so a fresh backup theme cannot be created (duplicate returns no theme). Backups already exist: "BACKUP v10 live 13.10 15:30", and the working dev theme "DEV – Apollo tracker 20.10" is a verified copy of the live theme 16.10c made on 20 Oct. No themes were deleted.

## 1. Themes (VERIFIED)
- Live (MAIN): "DEV – SEO fixes 16.10c (copy of MAIN)" = 203589812488.
- Working dev theme (unpublished): 203804672264 "DEV – Apollo tracker 20.10". Live theme untouched by this audit.
- Base theme is Shopify Horizon (blocks/sections architecture, native predictive search, sticky add-to-cart, facets, cart drawer), with custom JP MART files: jpmart-home, jpmart-search, jpmart-wholesale-hub, jpmart-b2b-form, jp-cart-recs, jp-freeship, jp-premium, jpmart-trust block.

## 2. Verified findings
| # | Area | Finding | Status |
|---|---|---|---|
| 1 | Shipping | Poland: free courier and free InPost at order total ≥ 99.00 PLN; paid 17.00 courier / 13.99 InPost up to 98.99; express 20.00. Matches the advertised 99 zł. | VERIFIED OK |
| 2 | Cart | jp-freeship.liquid shows progress using hard-coded 9900 (grosze) and PL-only; copy matches requested wording. If the threshold changes it must be edited in code. Uses cart.total_price (after discounts) – confirm that Shopify's rate condition also evaluates after discounts. | VERIFIED (hard-coded) / POTENTIAL (discount behaviour) |
| 3 | Payment claims | Cart bar, homepage trust and About say "BLIK, karty, PayPal". The API only confirms Shopify Pay, Apple Pay and Google Pay as digital wallets; BLIK/PayPal activation cannot be verified from here. | POTENTIAL ISSUE – owner must confirm in Settings → Payments, else remove claim |
| 4 | Markets | Markets enabled: Poland (primary), European Union, United Kingdom. shipsToCountries lists 26 EU countries incl. PL but NOT GB. UK market enabled without a shipping destination. | POTENTIAL ISSUE – confirm UK should be disabled or add UK rates |
| 5 | Locales | pl (primary), en, de all published. | VERIFIED |
| 6 | Product schema | Product pages emit native `product | structured_data` (Shopify JSON-LD). Judge.me app block is also installed and may add its own Product/AggregateRating markup → duplicate risk. | POTENTIAL – NOT TESTED (needs Rich Results Test) |
| 7 | Sticky add-to-cart | Enabled by default in product-information section (mobile full-width bar). | VERIFIED in code; mobile behaviour NOT TESTED |
| 8 | Catalogue | 68 products, 29 collections. Several ACTIVE products with 0 stock (Ocean stove, Bajaj Almond Drops x2, Biotique face wash, Nag Champa cones, Himalaya Rumalaya gel, Dabur 3-paste set). Draft: Vatika cactus shampoo (price 0). | VERIFIED – owner decision pending |
| 9 | Sitemap | Valid Shopify index lists products/pages/collections/blogs/articles in PL/DE/EN. Search Console shows "Couldn't fetch" 1 day after submission (normal delay). | VERIFIED / pending |
| 10 | Menus | Main menu: Sklep, Zestawy, Pasty do zębów, Pielęgnacja włosów, Marki, Poradniki, Hurt B2B, Kontakt. Footer now has Hurt B2B (UE). Missing vs requested: Beauty & Skin Care, Ayurveda & Wellness, Tea & Food, Incense & Home are not top-level (collections exist). | VERIFIED – improvement possible |
| 11 | Home | Hero H1 single; FAQ with FAQPage JSON-LD; brands, categories sections exist; no bestseller grid? (product-list section "Bestsellery" present); no reviews section, no guides section, no newsletter section. | VERIFIED |
| 12 | Content | 10 guides live (miswak, Dabur pasta, olejowanie, amla, chyawanprash, tulsi, Vatika, Vicco, Himalaya, Sesa, incense, indyjskie kosmetyki do włosów). | VERIFIED |
| 13 | Tracking | Ahrefs Web Analytics and (dev theme only) Apollo tracker are consent-gated. GA4/Meta/Google Ads/Merchant Center not verified. | NOT TESTED |
| 14 | Search Console 28d | 16 clicks, 43 impressions, homepage only, brand queries only. | VERIFIED |

## 3. Competitor (AyurShop) – BLOCKED
Could not be fetched from this environment. No competitor claims are made. To proceed: owner may send screenshots of ayurshop.eu (home, a category with filters, a product page, shipping page) and I will compare features against JP MART.

## 4. What can be improved next (safe, in dev theme only)
Phase B/D candidates, none applied yet: homepage sections for reviews (only when real reviews are connected), guides carousel, newsletter block (consent), top menu with real categories, product tabs for ingredients/usage/warnings using metafields (no data yet – metafields would need verified product data from the owner), cart threshold read from a theme setting.

## 5. Blockers needing owner input
1. Confirm active payment methods (BLIK, PayPal, cards).
2. Decide UK market (disable or add shipping).
3. Decide on sold-out ACTIVE products.
4. Send PageSpeed Insights or Lighthouse screenshots (mobile) for home, one collection, one product (baseline), and Rich Results Test results for one product URL.
5. Provide verified ingredients / INCI / usage / manufacturer data per product (or approve using only existing descriptions).
6. Approve publishing dev theme when ready (I cannot publish).

## 6. Acceptance test log (22)
All storefront tests: NOT TESTED (no live-site access). Admin-data checks: shipping thresholds PASS, locales PASS, sitemap index PASS.

## 7. Rollback
Live theme 16.10c unchanged. If any dev theme is published and misbehaves: Online Store → Themes → publish "DEV – SEO fixes 16.10c" again (or "BACKUP v10 live 13.10 15:30").

# JP MART – technical SEO diagnosis (26 Oct 2026)

Status key: VERIFIED COMPLETE · IMPLEMENTED BUT NOT TESTED · BLOCKED · NOT STARTED · NO CHANGE NECESSARY

## A. Access and environment
| Item | Result |
|---|---|
| Shopify Admin (GraphQL) | Connected, read and unpublished-theme write |
| Google Search Console / GA4 / Merchant Center | BLOCKED – not connected (only Meta Ads, Facebook Organic, Instagram in Windsor) |
| Live site fetch (sitemap, robots, headers, PageSpeed, Rich Results) | BLOCKED – sandbox proxy returns 403 for jpmart.eu |
| Published (MAIN) theme | 203804672264 "DEV – Apollo tracker 20.10 (copy of MAIN)" – VERIFIED via themes query |
| Dev theme | 203890098440 "DEV – FBT + cart upsell 21.10", role UNPUBLISHED – VERIFIED |
| Backup | 203890065672 "BACKUP live 21.10 (Apollo tracker theme)", UNPUBLISHED – VERIFIED |
| Theme edits this round | None. No defect found that needed a code change. |

## B. Search Console (from owner screenshots, not from the API)
- "Page with redirect" for `http://jpmart.eu/`: expected. The http→https redirect is correct and must stay. NO CHANGE NECESSARY.
- Sitemap "Couldn't fetch" 1 day after submission: cannot re-test from here (BLOCKED). Shopify generates the sitemap; do not replace it. Owner action: in Search Console open Sitemaps, check the status of `sitemap.xml`; if it still reads "Couldn't fetch" after ~7 days, resubmit once and send a screenshot with the exact error.
- URL Inspection of `https://jpmart.eu/` (owner action) will confirm indexing.

## C. What was verified in Shopify data (read-only)
- 67 ACTIVE products: all published to the Online Store, all have an SEO title and description, descriptions >150 characters, featured-image alt text present, no `seo.hidden` (noindex) metafield. VERIFIED.
- SEO titles over 60 characters: 5 products at 61–63 characters (Dabur 26 herbs toothpaste, Himalaya Gum Care, Vatika almond oil, Vatika coconut oil, Sesa 180 ml). Marginal; not changed.
- 1 DRAFT product (Vatika cactus shampoo): correctly not on the storefront.
- 29 collections: all published to the Online Store; all have an SEO description. VERIFIED. `bestsellery` contains all 67 products including sold-out ones (see owner decisions).
- Redirects (16): old long product handles redirect to current handles; `/enpages/…` and `/depages/…` redirects point to `/en/pages/…` and `/de/pages/…`. No loops seen.
- 10 pages published (contact, wholesale-b2b, shop, brands, imprint, about-us, cookie-policy, loyalty, faq).

## D. Theme code read (dev theme 203890098440)
- `snippets/meta-tags.liquid`: one canonical (`canonical_url`), one meta description, homepage title/description per language, Organization + WebSite JSON-LD on the homepage only, BreadcrumbList on product and collection pages. VERIFIED by reading code; rendered output NOT TESTED.
- `sections/product-information.liquid`: exactly one native `closest.product | structured_data` Product block. `sections/main-blog-post.liquid`: one `article | structured_data`.
- Judge.me: no review widget or block in `templates/product.json`, so no second Product/AggregateRating markup is expected from the theme. Whether the Judge.me app embed adds its own markup is NOT TESTED (needs Rich Results Test on a product URL).
- Home page hidden H1 demoted to avoid two H1s: present.
- hreflang: not rendered by the theme; Shopify adds it for translated markets. NOT TESTED.
- No `templates/robots.txt.liquid`: Shopify default robots.txt in use (good, no custom rules).

## E. Items needing the owner
1. Search Console: sitemap status and URL Inspection screenshots (see B).
2. Rich Results Test (search.google.com/test/rich-results) on one product URL and the homepage; send the result.
3. PageSpeed Insights mobile scores for home, a collection, a product (baseline).
4. Remove sold-out items from `bestsellery` or restock (Ocean stove, Bajaj ×2, Biotique face wash, Nag Champa cones, Himalaya Rumalaya gel, Dabur 3-paste set).
5. Previously open: payment methods, UK market, draft legal text in Refund/Terms, discount X248C6PS52ZN, REGON mismatch.

## F. Not started / blocked
- Core Web Vitals, Lighthouse, image weight measurements: BLOCKED.
- Live regression tests (gallery, Add to Cart, FBT, cart upsell, search, mobile): BLOCKED from here; owner preview needed.

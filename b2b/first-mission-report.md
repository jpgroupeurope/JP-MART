# JP Mart B2B/B2C – First mission report (2026-10-14)
Sources: Shopify Admin API (live store), repo, limited web search. Live site HTTP was blocked from this environment; Semrush (no API units), Ahrefs (plan), Search Console (not connected) unavailable → **no keyword volumes or GSC data; none invented.**

## 1. Blockers (actual)
1. **Repo has no theme code** (only `.claude/skills`, CLAUDE.md). The page uses template suffix `b2b` and an `#b2b-form` anchor; the form, lead capture and Liquid live only in the Shopify theme. No theme change built (rule: don't build against the wrong theme). Need: theme export/GitHub-connected theme, or approval to edit the live theme in a duplicate.
2. **Wholesale page is Polish only** while targeting EU buyers outside Poland (it says Polish firms are excluded, yet its title targets Polish "hurtownia" queries). No EN/DE/FR/NL version → foreign buyers can't read it.
3. **Commercial terms undefined publicly**: "1 carton per product" – no carton size, units, weight, price, or lead time. Wholesale prices only by PDF after activation.
4. **Stock can't back carton MOQs**: Vatika oils/masks 2–24 units; Bajaj, Biotique, Nag Champa, Ocean stove = 0. Toothpaste 72, Sesa 70–192 units. Verify before any offer.
5. **No B2B track record**: last 90 days = 4 orders, PLN 119.98, all Poland. Shopify has 1 company record, 8 catalogs (purpose unverified).
6. **Lead tracking unverified**: cannot confirm form → CRM/email routing, consent text, or UTM capture (theme invisible).
7. Data tools missing: GSC/GA4 not connected (Windsor has only Meta/Instagram), Semrush needs API units.

## 2. Ten B2B keyword opportunities (hypotheses – validate volume/difficulty before building)
Intent = wholesale/trade. Each mapped to one URL to avoid duplicates.
| # | Query (lang) | Target URL | Note |
|---|---|---|---|
| 1 | ayurvedic cosmetics wholesale Europe (EN) | NEW EN wholesale page `/pages/wholesale-b2b-en` (draft below) | core page, 1 per language |
| 2 | Ayurveda Kosmetik Großhandel (DE) | `/pages/wholesale-b2b-de` | DE: no cold email → SEO is the channel |
| 3 | grossiste cosmétiques ayurvédiques (FR) | `/pages/wholesale-b2b-fr` | FR allowed for cold email too |
| 4 | Dabur wholesale Europe / Dabur distributor (EN) | EN page H2 + `/collections/oral-care` B2B CTA | brand-name trade query; Qogita ranks this |
| 5 | Vatika hair oil wholesale (EN) | `/collections/hair-care` | blocked by stock |
| 6 | Himalaya toothpaste wholesale / Himalaya Großhandel | brand collection | verify authorisation to resell |
| 7 | herbal toothpaste wholesale EU (neem, miswak) | `/collections/oral-care` | strongest stock (72 units/SKU) |
| 8 | Indian grocery wholesale Europe / Indian rice 10 kg wholesale | EN page section | only 10 units rice; low priority |
| 9 | hurtownia kosmetyków indyjskich (PL) | existing PL page | already targeted; remove contradiction re PL buyers or add PL-B2B terms |
| 10 | wholesale ayurvedic hair oil private-label/OEM – **skip** | – | not offered; don't target |
Replace #10 after data: "Asia shop supplier Netherlands" (NL).

## 3. Prospect candidates (evidence = public search results only; NOT 30 – not accessible/verified)
Only these surfaced; none verified as buyers, no contacts recorded.
| Company | Country | Fit | Evidence |
|---|---|---|---|
| Asijah Europe | NL/EU | Indian-food wholesale importer; likely competitor/partner | bestfoodimporters.com listing |
| Lakshmi Shop (lakshmishop.nl) | NL | Indian grocery retailer, serves businesses | oncosmetics.com listing |
| Indisha B.V. (Heemskerk) | NL | Indian spice/food distributor, retail+business | oncosmetics.com listing |
| eKirana | NL | online Indian grocer, EU shipping | Trustpilot profile |
| Velan épicerie indienne | FR (Paris 10e) | retail, stocks ayurvedic items | Time Out Paris |
| OM Vital Vertriebs GmbH | DE | ayurvedic importer since 1997 (competitor/partner) | Faire profile |
| Art of Vedas, MELO AYURVEDA | EU/FR | ayurvedic brands on Faire (partner/competitor) | Faire |
| Qogita (marketplace) | EU | lists Dabur wholesale – channel/competitor | qogita.com |
Next step: build the remaining ~22 from Kompass/Pages Jaunes/KvK/Handelsregister/BranchenBuch + Google Maps by city (NL: Amsterdam, Rotterdam, Den Haag; FR: Paris 10e, La Chapelle; DE: Frankfurt, Hamburg), each with VAT ID check in VIES. Needs a session with live web/directory access.

## 4. Safe improvement delivered
Drafted (not published) EN landing copy: `b2b/wholesale-en-draft.md`. Publishing + form needs theme access/approval.

## 5. Polish B2C (evidence-limited)
Revenue 180d: Chyawanprash 1kg (PLN 119.98) only paid sale; other 9 orders were PLN 0 (test/free?). Top commercial candidates by stock+price: Dabur toothpastes (72 each, 18.99), Sesa 180 ml oil (192, 28), Vatika oils (5). Concrete gaps found: `Vicco Vajradanti` has **no SEO title**; several descriptions say "darmowa od 99 zł" vs others none—inconsistent. Google ranking unverified (no GSC) → connect Search Console before further SEO.

## 6. Tracking definition
Events/fields (Shopify Customer tags + GA4/UTM): `wholesale_form_view`, `wholesale_form_submit` (country, VAT ID, business type, UTM source/campaign, language), `lead_qualified` (VIES valid + EU non-PL + fit), `quote_sent` (value), `wholesale_order_paid` (tag `b2b`, company, WDT). Weekly sheet per revenue-plan.md KPIs. Polish B2C: GA4 `purchase` + Shopify channel `Google & YouTube`, Merchant Center clicks; sessions by `session_country=PL`. Use hidden form fields for UTM + landing language. Verify consent text and where submissions go.

## 7. Approval needed
Theme access (export or GitHub); publish EN/DE/FR pages; carton size/price/stock confirmation; connect Search Console/GA4; Semrush units; permission to fix Vicco SEO title.

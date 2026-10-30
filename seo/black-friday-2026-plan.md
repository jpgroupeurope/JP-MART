# JP MART – Black Friday 2026 plan (draft for owner approval)

Dates: Black Friday Fri 27 Nov 2026, Cyber Monday Mon 30 Nov 2026. Nothing below is live. No discount has been created.

## Done in dev theme 203890098440 (unpublished)
- New section `sections/jp-blackfriday.liquid` (dark banner, gold button, PL/EN/DE, mobile-first, countdown).
- Added to `templates/index.json` directly under the hero.
- Phases: teaser from 16 Nov, live 27–30 Nov (CET), hidden outside those dates.
- It does NOT mention any % or code until you fill "Offer line" and "Discount code" in the section settings, so no false promise can appear.
- `force_show` is ON in the dev theme so you can preview now. IMPORTANT: switch it OFF before publishing, or the banner shows before 16 Nov.
- Status: IMPLEMENTED BUT NOT TESTED (not rendered here; owner preview needed).

## Offer proposal (needs your approval; margins are your call)
Principle: protect margin, raise basket size, clear high stock.
1. Bundles: "Zestawy taniej niż osobno" is already true. Black Friday headline = bundles (e.g. extra 10% on collection `zestawy`).
2. Basket builder: free delivery from 99 zł already exists; add "extra 10% off when you buy 3+ toothpastes/oils" (quantity discount on Dabur and Vatika collections).
3. Stock clearance: Sesa 180 ml (192 pcs) and Sesa 90 ml (96 pcs) are the highest stock – small discount or a "2 for 1.5" mix.
4. Do not discount products with 0–5 stock; sold-out items stay out of the campaign.
5. Keep WELCOME10, FIRST10, AGNIESZKA10 separate; decide whether they combine with the Black Friday code (recommend: no combining).
To create (after approval): one code, e.g. `BF2026`, start 27 Nov 00:00, end 30 Nov 23:59, one use per customer.

## More ideas
- Announcement bar line from 20 Nov: "Black Friday 27.11 – zestawy taniej" (edit in theme editor header).
- Early-access list: email/WhatsApp opt-in only from existing customers who agreed to marketing; send on 26 Nov.
- Black Friday collection page `/collections/black-friday` (new collection, manual, bundles + in-stock bestsellers) – needs your OK to create.
- Gift angle: "Prezent z Indii" bundle pitch for Christmas (shipping cut-off date must be confirmed by you).
- Cart: keep the free-shipping bar; "add X zł more for free delivery" lifts AOV.
- B2B: separate Black Friday price list for the wholesale hub (EU shops buying before Christmas) – prices from you.
- Social: Instagram/Facebook posts 20, 24, 27, 30 Nov (Meta pages are connected; posting needs your approval each time).
- After the sale: remove the section or set dates in the past (it hides itself).

## Owner decisions needed
1. Discount type and size (see proposal) and whether it may combine with other codes.
2. Approve creating the code and (optionally) the Black Friday collection.
3. Preview the dev theme, then tell me what to change.
4. Publishing is yours.

## Executed 30 Oct 2026 (owner chose: 10% bundles, no combining, create collection)
- Discount code BF2026 (id gid://shopify/DiscountCodeNode/2183422869768): 10% on the 3 Vatika bundles (coconut, protein, strengthening), once per customer, start 27 Nov 00:00 CET, end 30 Nov 23:59 CET, status SCHEDULED. Does not combine with product/order discounts (WELCOME10, FIRST10 etc.); free-shipping discounts may combine.
- Excluded on purpose: "Zestaw Dabur & Vatika 99 zl" (already a promo price with free delivery) and "Zestaw 3 past Dabur" (sold out).
- Collection /collections/black-friday (id gid://shopify/Collection/592685138184): 3 Vatika bundles + the 99 zl set. NOTE: it is published now (visible before the sale); the code works only from 27 Nov.
- Dev theme banner v3 links to /collections/black-friday and shows "Extra 10%" + code BF2026 in the live phase.
- Risk: bundle stock is tiny (2, 5, 2 units; 99 zl set 5). Restock before 27 Nov or the campaign sells out in hours.
- Before publishing the dev theme: turn off "Preview: show live phase now".

## Update 30 Oct 2026 (owner: run from today, stock exists, add item offer)
- BF2026 now ACTIVE from 30 Oct 2026, ends 30 Nov 23:59 CET.
- New code BF3 (id gid://shopify/DiscountCodeNode/2183425818888): 10% on products in collection `dabur` (41 products incl. Vatika) when the cart has 3+ of them; once per customer; no combining with other product/order discounts; ACTIVE 30 Oct - 30 Nov.
- Known gap: collection `dabur` also contains the 3 Vatika bundles and the 99 zl set, so BF3 can apply to them too. Low risk (stock 2-5), owner may want product-level scope.
- BLOCKER FOR ORDERS: ~15 ACTIVE products in `dabur` show 0 stock in Shopify (e.g. Dabur Red 100 ml, Aloe, Ginger-Mint, Miswak 170 g, Amla 300 ml, Vatika almond/rosemary/argan shampoos). Owner says stock exists; quantities must be corrected in Shopify (Products > Inventory) or sent to the assistant for set-inventory. Never invent quantities.
- Dev theme banner v5 shows both codes; dates default to 30 Oct - 30 Nov; shows only after the dev theme is published by the owner.

## Stock update 30 Oct 2026 (owner: "quantities each 72 pcs")
- Finding: the ~10 products showing 0 stock were NOT tracked (inventory tracking off), so they were already purchasable without limit. Correction to the earlier "blocker" note.
- Done: tracking enabled and available set to 72 for 10 items (Vatika almond/rosemary/argan shampoo, Vatika cactus mask, Dabur Amla 300 ml, Dabur Miswak 170 g, Dabur Ginger-Mint, Dabur Aloe, Dabur Red 100 ml, Zestaw 3 past Dabur). Also raised to 72: Dabur Amla Gold, Vatika shampoos (egg/coconut/garlic/nigella), Vatika oils (cactus, coconut x2, argan, egg, almond), Vatika olive mask. Not touched: items already 72+ (toothpastes, Sesa 192), Chyawanprash 22, Vatika egg mask 24.
- NOT possible via API: 4 bundle products (99 zl set, Vatika coconut/protein/strengthening) - Shopify returns NON_MUTABLE_INVENTORY_ITEM. Their stock still shows 5/2/5/2. Owner must edit quantity in Shopify admin (Products > product > Inventory), or check Shopify Bundles component setup.
- The 72 figure comes from the owner; it was not verified against a physical count.

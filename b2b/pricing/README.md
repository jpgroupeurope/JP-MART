# Wholesale price list 30.09.2026 → Shopify (DRAFT – nothing applied)
Source: JP_MART_Wholesale_Price_List PDF (128 lines, EUR net/unit, excl. VAT & delivery). Prices copied verbatim, no extra discount.
Files: `match-report.csv` (all 128 lines, status/confidence/stock/notes) · `wholesale-prices-import-DRAFT.csv` (23 matched priced variants; stock column is export-time only).
Result: 24 matched (23 priced + 1 quote-only), 11 ambiguous, 93 unmatched (not in Shopify), 27 lines "on request" (quote-only). Carton qty & MOQ: UNCONFIRMED for every line.
Before use: resolve the 11 ambiguous lines; fix Samahan 25/100 variants (retail price 0.00, stock 0); 7 matched items have stock 0 or ≤5; two Vatika products share barcode 5022496003896.
## Import
BSS import format/subscription could NOT be inspected (no access to the BSS app admin). Manual: BSS admin → price rules / CSV import → map `variant_id` (or handle/SKU – most SKUs are empty), price = `wholesale_net_price_eur`, apply fixed price (not % discount), customer condition = tag `wholesale` only after manual approval. Check BSS currency handling: store base is PLN; prices are EUR (EU market). Otherwise quote each order via Draft Order with these prices.
## Tax (do not assume VAT-free)
Store prices include tax (taxesIncluded=true). Per customer: PL company → 23% VAT. Other EU company with valid VIES VAT ID, shipped from PL → intra-EU supply, 0% (set customer Tax-exempt + keep VIES proof). EU buyer without valid VAT ID → destination/OSS rules, VAT applies. Two existing tagged customers (PL, EE) are NOT tax-exempt; EE one also has tag `first-order-5%` (extra discount – not applied here).
## Test plan (not run)
1 approved B2B test customer (tag wholesale, tax-exempt only if VIES ok) vs 1 plain customer: check PDP, cart, checkout total, VAT line, EUR vs PLN; confirm retail prices PL/EU unchanged; check page source/`/search?view=bss.b2b` for wholesale price leakage.

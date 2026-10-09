---
name: jp-email-marketing
description: Write and plan GDPR-aware B2B email campaigns (cold outreach, sequences, newsletters, reorder emails) for JP Mart / JP Group to retailers, distributors, wholesalers and importers in DE, FR, IT, ES, NL, PL. Use for subject lines, copy, sequences, deliverability, A/B tests and country legal checks.
---

# JP Email Marketing

Always start from a scored segment (`jp-b2b-targeting`). Never send to unsegmented lists.

## Legal gate per country (summary - not legal advice; confirm with local counsel)
| Country | Cold B2B email | Notes |
|---|---|---|
| Germany | **Prior consent required** (UWG §7), even B2B | Use existing customers, inbound enquiries, double opt-in; otherwise use phone/LinkedIn/fairs |
| France | Allowed if relevant to recipient's professional role + clear opt-out | Mention source; honour opt-out (Bloctel is for phones) |
| Italy | Strict; generally consent for marketing, check Garante rules | Prefer opt-in/existing customers |
| Spain | LSSI requires consent; exception for existing relationship | Prefer opt-in |
| Netherlands | B2B allowed with relevance + opt-out | Dutch rules friendlier |
| Poland | Consent required for electronic marketing | Prefer opt-in |
If unsure: treat as consent-required and use non-email first touch.

Every email must have: sender identity (company, address, VAT), reason/source for contact, one-click unsubscribe, and processing under GDPR Art. 6(1)(f) (legitimate interest, documented) or 6(1)(a) (consent). Keep suppression list.

## Cold email structure (≤120 words)
1. **Subject** (≤45 chars, specific): "Basmati & noodles for [Company] – sample?"
2. **Line 1**: relevance to them (store type, city, category) - proves it is not random.
3. **Line 2**: concrete offer (products, price range/MOQ, delivery time to their country).
4. **Proof**: one credential (certs, volumes, similar customer).
5. **One CTA**: free sample / price list / 10-min call. 
6. Signature with phone and company details + opt-out line.

## Sequence (4 touches / 3 weeks)
- Day 1: intro + offer. Day 4: price list/catalogue PDF. Day 10: case/proof or seasonal hook. Day 17: polite breakup. Stop on any reply or opt-out.

## Template (EN – translate/localise)
Subject: {Product} for {Company} – sample available
Hello {Name},
I saw {Company} runs {n} {store type} in {city}. JP Mart supplies {top 3 products} to retailers and distributors across the EU, delivered to {country} in {x} days, from MOQ {y}.
Could I send a free sample and our current price list?
Best regards, {Sender}, JP Mart / JP Group, {address}, {phone}
If you prefer not to receive emails from us, reply "unsubscribe" or use this link.

## Deliverability
Separate sending domain (e.g. mail.jpgroup...), SPF/DKIM/DMARC set, warm up 2–4 weeks, ≤30–50 cold emails/day/mailbox, bounce <2%, complaints <0.1%, plain text-style, no heavy images/attachments in first mail.

## Newsletters / existing buyers
Monthly: new arrivals, promo prices, stock alerts, seasonal bundles, reorder reminder based on last order date. Segment by country and category.

## Test & measure
A/B one variable at a time (subject, CTA, offer) with ≥100 sends per variant. KPIs: delivered %, open (indicative only), reply %, positive reply %, samples, orders. Target positive reply 2–5% on A-tier.

## Output
Deliver: segment used, legal basis per country, subject variants (3), full email in local language + English, sequence schedule, KPIs.

---
name: jp-sales-growth
description: Master playbook to increase sales for JP Mart (food & grocery, general trading) and JP Group B2B across EU markets (DE, FR, IT, ES, NL, PL). Use for any sales plan, campaign, pipeline, pricing/offer, or when deciding which channel (email, WhatsApp, calls, marketplace) to use. Routes to jp-b2b-targeting, jp-email-marketing, jp-whatsapp-marketing.
---

# JP Sales Growth (EU B2B)

## Business context (defaults, update if wrong)
- Sellers: **JP Mart** and **JP Group** (B2B). Products: food & grocery + general trading goods.
- Buyers: **retailers, distributors, wholesalers, importers**.
- Priority markets: **Germany, France, Italy, Spain, Netherlands, Poland**; expand after first wins.

## Rule #1: accurate targets, never random
Never write outreach before the target is defined. Always run `jp-b2b-targeting` first and produce: country, buyer type, product category, size, decision-maker role, trigger/reason to buy now. No segment = no campaign.

## Workflow
1. **Pick the goal** (e.g. 20 new wholesale accounts in DE in 90 days). Back-calculate: accounts ← deals ← meetings/samples ← replies ← contacts.
2. **Segment** with `jp-b2b-targeting` (score A/B/C; only A and B get outreach).
3. **Offer** per segment: lead product + price tier/MOQ + sample or trial order + delivery lead time + certifications (EU food labelling, origin, halal/organic if applicable). Offer must be specific, not "we sell everything".
4. **Channel sequence** (B2B EU best practice):
   - Email first (`jp-email-marketing`) for new cold contacts where legally allowed.
   - WhatsApp (`jp-whatsapp-marketing`) ONLY for opted-in or existing contacts: follow-up, reorders, price lists.
   - Phone/LinkedIn/trade fairs (Anuga, SIAL, Marca, Biofach, Gulfood-EU buyers) to warm and close.
5. **Follow-up cadence**: 4–6 touches over ~3 weeks across 2 channels, then move to quarterly nurture.
6. **Close**: sample → trial order → price list → contract/credit terms → reorder program.
7. **Measure weekly**: contacts, deliverability, reply rate, positive reply rate, meetings, samples, orders, revenue, CAC, reorder rate. Kill segments with 0 positive replies after 100 sends; double down on the best.

## Growth levers beyond outreach
- Reorder/upsell to existing customers (cheapest revenue): replenishment reminders, bundles, seasonal lists (Ramadan, Christmas, Diwali, summer).
- Distributor-of-distributors: win 1 importer per country, then sub-distribute.
- Tiered pricing + MOQ ladders; free-delivery threshold per country.
- Referral/introduction bonus from current buyers.
- Country landing page + PDF catalogue in local language.
- Trade-fair and marketplace (Amazon Business, Ankorstore, Faire-type) listings as lead sources.

## Revenue target
Current goal: **€15,000–30,000/month**. See `revenue-plan.md` for funnel maths, market order and the 30-day plan.

## Output format when asked for a plan
Goal → segments (table) → offer → channel sequence + timeline → copy (via channel skills) → KPIs/targets → compliance checks → next 7 days' actions.

## Compliance gate (always)
Before any send, confirm lawful basis and opt-out per `jp-email-marketing` / `jp-whatsapp-marketing`. Rules are not legal advice; recommend local counsel review for new countries.

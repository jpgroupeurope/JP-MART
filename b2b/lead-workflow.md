# B2B lead workflow (native Shopify, no extra app)
Form (page /pages/wholesale-b2b, template page.b2b) -> contact email + customer record (tag `b2b-inquiry` on the current theme build; planned `lead-new`).
Pipeline = customer tags, one per stage (replace the previous tag when advancing). Segments created in Admin > Customers:
`lead-new` -> `lead-verified` (VIES ok) -> `lead-approved` -> `lead-quotation` (Draft Order sent) -> `lead-paid` (paid order).
Tags `B2B`, `hurt-b2b`, `wholesale` are the ONLY ones BSS treats as wholesale access: add manually after approval. Never added by the form.
Quotation: Admin > Orders > Create draft order with agreed prices -> send invoice (secure, native, free).
Manual tests: submit twice with same email; submit with a tracked URL ?utm_source=test&utm_medium=test; check email, tags, Customer note fields; check mobile.
Preview URL: https://jpmart.eu/pages/wholesale-b2b (+ /en, /de locale prefix as configured)

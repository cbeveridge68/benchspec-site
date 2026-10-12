# Cloudflare analytics

BenchSpec keeps purchase links as direct eBay links. Outbound purchase clicks are tracked with Cloudflare Zaraz rather than redirects or third-party analytics.

## eBay outbound-click trigger

Configure Zaraz for `benchspec.com.au` with this trigger:

- Name: `eBay outbound click`
- Rule type: Click listener
- Type: CSS
- Selector: `a.purchase[href*="ebay."]`
- Wait for actions: `500` ms

All current live purchase CTAs use the existing `purchase` class, so no URL rewrite or product-page markup change is required.

Cloudflare Zaraz Monitoring > Triggers should show executions for `eBay outbound click`. Use the page URL/path as the product identity; each catalogue item has a permanent product URL.

## Validation

After enabling the trigger:

1. Open a live BenchSpec product page with an active eBay purchase CTA.
2. Select **View on eBay** and confirm the direct eBay destination still opens normally.
3. Check Zaraz Monitoring > Triggers and confirm `eBay outbound click` increments.
4. Verify ordinary catalogue navigation does not increment the trigger.

Do not replace the direct eBay links with tracking redirects. Keep the implementation lean and first-party.

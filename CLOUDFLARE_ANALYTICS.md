# Cloudflare analytics

BenchSpec keeps purchase links as direct eBay links. Outbound purchase clicks are tracked with Cloudflare Zaraz rather than redirects or third-party analytics.

## Loader

Cloudflare's Zaraz auto-injection is not enabled for the current static host, so every HTML page includes the first-party loader immediately before `</head>`:

```html
<script src="/cdn-cgi/zaraz/i.js" referrerpolicy="origin"></script>
```

`tools/check_site.py` requires exactly one copy of this loader on every page and permits no other application JavaScript. Cloudflare serves the loader at the edge; it is not a file in `site/`.

## eBay outbound-click trigger

Configure Zaraz for `benchspec.com.au` with this trigger:

- Name: `eBay outbound click`
- Rule type: Click listener
- Type: CSS
- Selector: `a.purchase[href*="ebay."]`
- Wait for actions: `500` ms

All current live purchase CTAs use the existing `purchase` class, so no URL rewrite or product-page markup change is required.

The live Zaraz runtime also registers an `ebay_click` event with the product path and destination URL for matching purchase links.

Cloudflare Zaraz Monitoring > Triggers should show executions for `eBay outbound click`. Use the page URL/path as the product identity; each catalogue item has a permanent product URL.

## Validation

After enabling the trigger:

1. Open a live BenchSpec product page with an active eBay purchase CTA.
2. Select **View on eBay** and confirm the direct eBay destination still opens normally.
3. Check Zaraz Monitoring > Triggers and confirm `eBay outbound click` increments.
4. Verify ordinary catalogue navigation does not increment the trigger.

Do not replace the direct eBay links with tracking redirects. Keep the implementation lean and first-party.

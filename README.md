# BenchSpec catalogue

Small, hand-authored catalogue for specialist technical equipment and parts. Production origin: **https://benchspec.com.au**. Purchases take place on eBay.

The catalogue includes the original Infinity Fluids CRES inline heater and four additional Lot 31 products: the Infinity PTC controller, Perma Pure humidifier, MAG-VIEW flow meter and Spirax Sarco drain trap. Actual-item photographs are included. TSI 4140D and Swagelok KPR remain unpublished until their exact eBay listings exist. The branch remains unmerged and undeployed; evidence, item-specific blockers and separate launch checks are recorded in [WORK.md](WORK.md).

## Preview and check

Serve the `site/` directory as the web root. There is no installation or build step:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8765/. Root-relative URLs require a web server rather than opening HTML files directly.

```sh
python3 tools/check_site.py
python3 tools/check_site.py --publication
```

The dependency-free checker verifies internal links/assets, metadata, JSON-LD consistency and sitemap membership. The `--publication` check additionally fails on missing actual-item imagery and explicit publication blockers. It does not replace HTML conformance validation, browser checks, Google Rich Results Test or factual review. Acceptance evidence and outstanding launch items are in [WORK.md](WORK.md).

## Maintain a product

Follow [CATALOGUE_GUIDE.md](CATALOGUE_GUIDE.md) for the approved catalogue wording, condition boundaries, public contact and business identity.

For Lot 31, the operator's 25 September corrections take precedence over older source wording: describe observed physical condition, then verification and the specific testing boundary. Do not infer an unused history from appearance; stronger new/unused/sealed claims require clear audit and photographic evidence. Perma Pure FC125-240-5MP units are not capped: record only their dry condition and the absence of dismantling, wetting or pressure testing. Spirax retains its documented protective caps.

The approved shipping wording is **Stock in Melbourne, Australia · Ready for international shipping**, or **Ready for international shipping from Melbourne, Australia.** This supersedes the guide's older enquiry wording for these catalogue items. Do not imply that shipping is free or included; transaction-specific terms remain on eBay.

1. Start from the matching physical audit and current pricing record in `cbeveridge68/erpnext-ops`. Record source revision, audit reference, selected photographs and offer evidence in the work record. Only completed tests support testing claims. Keep negotiation targets/floors and other private operating information out of the site.
2. Copy the existing product HTML into a permanent, lowercase manufacturer/model/MPN directory under `site/products/`. This is an editing pattern, not a template engine. Do not reuse another product's identifiers, claims, price, images or eBay link.
3. Use photographs of the actual item. Preserve selected source originals under `raw-images/`, outside the web root. Place optimised images under `site/assets/`, provide full-resolution image links, dimensions, alt text and responsive sizes. Never substitute stock or generated pictures. WORK.md identifies the selected originals for each product; controller photographs are not heater imagery.
4. Update title, H1, description, canonical URL, social metadata, JSON-LD and visible content together. Include known specifications, condition/test limits, inclusions and Melbourne location. State what has been identified, visually inspected and functionally tested, if anything, and any specific material limitation. Do not enumerate hypothetical untested scenarios unless directly relevant to safe use or accurate representation. Omit optional unknown dimensions/weight. Offer price/currency/status must match the visible page and current listing; never publish guessed values or placeholder destinations.
5. Add the product to the homepage and sitemap. Homepage cards always link to BenchSpec product pages. Update the available-equipment count.
6. Run the checker, HTML validator and browser checks. Check the destination listing belongs to BenchSpec and matches the exact item. There is no automatic price or stock synchronisation; repeat these checks when listing facts change and immediately before publication.

## When an item sells

- Keep its product directory, URL, canonical URL, photographs, specifications and condition evidence. Keep the URL in the sitemap and serve it with HTTP 200; do not redirect it to the homepage or add `noindex`.
- Change the visible stock text to **Sold** and `offers.availability` to `https://schema.org/SoldOut`.
- Remove the active `purchase` link and buying instructions. Clearly label the retained price **Last asking price**; it is not a new offer to sell. Preserve the existing eBay URL inside the unavailable Offer as provenance, not as a purchase button.
- Remove the card from the current-stock homepage and update the count. If no items remain, replace the listing with “No equipment is currently listed. Please check back.”
- Update the review date and any availability wording in metadata, including item-specific shipping readiness. Run the checks and verify the old URL still returns HTTP 200.

## Separate launch step

Publish **only `site/`** to the selected static host. Do not expose the repository root, `raw-images/`, WORK.md or tooling as the website. Cloudflare already manages the domain; hosting/DNS changes are not part of this slice.

Before launch, resolve blockers for the pages being published and recheck price, availability and the eBay destination. Blocked items remain outside `site/` and do not prevent publication of complete items. Configure HTTPS and the canonical `benchspec.com.au` hostname. Preserve directory-index routes and real 404 responses for unknown URLs; no single-page-app fallback is needed. Verify every canonical page, all assets, `/robots.txt` and `/sitemap.xml` from the public host.

Verify the domain property in Google Search Console via Cloudflare DNS, submit the sitemap, and use URL Inspection on the homepage and product URL. Use Search Console's search performance report for impressions, clicks, queries and landing pages. No analytics scripts are included. Run Google's Rich Results Test on the public product page; additional merchant-listing fields are outside the eBay-handoff model. Indexing and rich-result display remain Google's decisions.

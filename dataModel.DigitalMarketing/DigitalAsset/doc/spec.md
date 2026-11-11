# DigitalAsset

A concrete digital asset that belongs to a `Brand` and is observed through a
specific `SoftwareApplication`. Examples: the GA4 property of a corporate web,
a LinkedIn organization page, a Meta Business catalog, a paid-ads account on
Google Ads, an Android app on Play Store.

One `Brand` can group several `DigitalAsset` instances. Each channel is
observed by exactly **one** `SoftwareApplication` — if the same web is being
measured by GA4 and Adobe Analytics in parallel, that produces two
`DigitalAsset` entities.

## Properties

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | URN | yes | `urn:ngsi-ld:DigitalAsset:<Brand>-<Software>[-<suffix>]`. |
| `type` | string | yes | Always `"DigitalAsset"`. |
| `name` | string | yes | Human-readable name. |
| `alternateName` | string | no | Short or commercial alternative. |
| `description` | string | no | Free-text description. |
| `digitalAssetUrl` | URI | no | URL of the channel itself (the measured page / profile / app store entry). |
| `digitalAssetKind` | enum | no | High-level category: `Web`, `MobileApp`, `SocialProfile`, `SearchEngine`, `PaidAds`, `VideoPlatform`, `Email`, `Other`. |
| `externalId` | string | no | Native id of the channel inside the SoftwareApplication (GA4 property id, LinkedIn org id, Meta business id…). |
| `refBrand` | Relationship → `Brand` | yes | Owner brand. |
| `refSoftwareApplication` | Relationship → `SoftwareApplication` | yes | Tool used to measure or operate it. |

## Relationships

- **`refBrand`** → exactly one `Brand`. One `Brand` can be referenced by N
  `DigitalAsset` entities.
- **`refSoftwareApplication`** → exactly one `SoftwareApplication`. One
  `SoftwareApplication` can be referenced by N `DigitalAsset` entities
  (across all clients / brands of the data space).

## Notes

`businessSection` (NACE) is **not** declared on `DigitalAsset`; it lives on
`Brand`. All channels of the same brand inherit the brand's sector.

`digitalAssetUrl` differs from `Brand.url`: a brand can have a landing
(`https://acme.example`) and a specific channel can point to a sub-page or to
a third-party URL (`https://www.linkedin.com/company/acme`).

### Caveat: same asset measured by multiple SoftwareApplications

When the same physical asset (e.g. one web property) is being measured in
parallel by two `SoftwareApplication` (e.g. GA4 and Adobe Analytics), this
model produces **two distinct `DigitalAsset` entities** (one per
SoftwareApplication). Each emits its own stream of `DigitalAssetMetric`
observations.

Consumers must be aware that summing metrics across both channels would
double-count the same underlying traffic. The correct interpretation is to
choose one source of truth per metric per analysis, or to use both as
independent measurements (e.g. for reconciliation).

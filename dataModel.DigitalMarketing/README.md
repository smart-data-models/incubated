# Smart Data Models — dataModel.DigitalMarketing

NGSI-LD data models that describe the value chain of digital marketing
analytics in a sovereign data space: who legally owns a digital channel
(`Organization`), under which commercial identity it is operated (`Brand`),
which concrete digital asset is being measured (`DigitalAsset`), which
piece of software measures it (`SoftwareApplication`), who technically
provides the data (`DataProvider`), and what the resulting observation
looks like (`DigitalAssetMetric`).

## Entities provided by this subject

| Entity | Purpose | Status |
| --- | --- | --- |
| [Brand](./Brand/doc/spec.md) | Commercial identity / business line of an `Organization`. Carries the NACE sector. | incubated |
| [DigitalAsset](./DigitalAsset/doc/spec.md) | Concrete digital asset (web, app, social profile, paid-ads account…) of a `Brand`, observed through one `SoftwareApplication`. | incubated |
| [DataProvider](./DataProvider/doc/spec.md) | Technical agent (ETL / connector) that injects observations into the data space. Sovereignty-aware: canonical case is Internal to the data owner. | incubated |
| [DigitalAssetMetric](./DigitalAssetMetric/doc/spec.md) | Observation of a channel for a given date and temporal granularity (P1D / P1M / P3M / P1Y). 59 traffic, engagement, e-commerce, organic and ads metrics. | incubated |

## Reused entities (from other subjects)

| Entity | Source | Why we reuse it |
| --- | --- | --- |
| `Organization` | [dataModel.Organization](https://github.com/smart-data-models/dataModel.Organization) | Legal entity (CIF/VAT). We extend with an optional `category` array (`DataOwner`, `SoftwareVendor`, `Agency`, `ServiceProvider`). |
| `SoftwareApplication` | [schema.org / dataModel.GenericMeasures](https://schema.org/SoftwareApplication) | The tool measuring a channel (GA4, LinkedIn Ads, Meta Business…). Referenced from `DigitalAsset.refSoftwareApplication` and points back to its manufacturer via `refManufacturer` → `Organization`. |

## Graph shape

```
                                Organization (Google LLC)
                                       ↑ refManufacturer
                                       │
                          SoftwareApplication (GA4)
                                       ↑ refSoftwareApplication
                                       │
   Organization (Acme Holdings S.L.) ← refOrganization ─ Brand (Acme) ← refBrand ─ DigitalAsset (Acme-GA4)
                                       ↑                                          ↑ refDigitalAsset
                                       │ refOrganization                          │
                          DataProvider (Acme-Internal-Pipeline) ────────── DigitalAssetMetric
                                                                  refDataProvider   (dateObserved, P1D, metrics…)
```

A single `Organization` can play several roles in the same data space
(DataOwner of one brand, SoftwareVendor of one app, operator of one
provider). The grafo NGSI-LD makes this explicit without duplication.

## End-to-end example (Acme on GA4, daily observation)

```json
[
  {
    "id": "urn:ngsi-ld:Organization:ES-B12345678",
    "type": "Organization",
    "legalName": "Acme Holdings S.L.",
    "vatID": "ESB12345678",
    "category": ["DataOwner"]
  },
  {
    "id": "urn:ngsi-ld:Brand:Acme",
    "type": "Brand",
    "name": "Acme",
    "businessSection": ["62.01", "73.11"],
    "refOrganization": "urn:ngsi-ld:Organization:ES-B12345678"
  },
  {
    "id": "urn:ngsi-ld:SoftwareApplication:GoogleAnalytics4",
    "type": "SoftwareApplication",
    "name": "Google Analytics 4",
    "applicationCategory": "Analytics",
    "refManufacturer": "urn:ngsi-ld:Organization:GoogleLLC"
  },
  {
    "id": "urn:ngsi-ld:DigitalAsset:Acme-GA4",
    "type": "DigitalAsset",
    "name": "Acme Web (GA4)",
    "digitalAssetKind": "Web",
    "digitalAssetUrl": "https://acme.example",
    "externalId": "properties/123456789",
    "refBrand": "urn:ngsi-ld:Brand:Acme",
    "refSoftwareApplication": "urn:ngsi-ld:SoftwareApplication:GoogleAnalytics4"
  },
  {
    "id": "urn:ngsi-ld:DataProvider:Acme-Internal-Pipeline",
    "type": "DataProvider",
    "name": "Acme Internal Marketing Pipeline",
    "providerKind": "Internal",
    "refOrganization": "urn:ngsi-ld:Organization:ES-B12345678"
  },
  {
    "id": "urn:ngsi-ld:DigitalAssetMetric:Acme:GA4:P1D",
    "type": "DigitalAssetMetric",
    "dateObserved": "2026-02-07T00:00:00Z",
    "temporalResolution": "P1D",
    "refDigitalAsset": "urn:ngsi-ld:DigitalAsset:Acme-GA4",
    "refDataProvider": "urn:ngsi-ld:DataProvider:Acme-Internal-Pipeline",
    "sessions": [
      { "channelGroup": "Direct", "value": 25 },
      { "channelGroup": "Paid Search", "value": 33 }
    ],
    "newUsers": 86,
    "engagedSessions": 72,
    "pageViews": 292,
    "keyEvents": 28
  }
]
```

## Sovereignty principle

`DataProvider` is decoupled from `Organization` so that data lineage is
explicit. The canonical case is **Internal**: the pipeline operating a brand's
data belongs to the same `Organization` that owns the brand, even when its
day-to-day operation is delegated to a third party.

If a third party also publishes its own processed version of the same
underlying sources, it does so under its **own** `DataProvider`
(`providerKind: External`), allowing time-series consumers (e.g. Quantum
Leap) to query both feeds side by side by filtering `refDataProvider`.

## Non-additivity by design

`temporalResolution` keeps daily / monthly / quarterly / yearly observations
in separate entities. Unique-user counts and similar metrics are not
addition-friendly, so the source platform reports each granularity
independently and the data space follows the same convention.

## Compliance

- **NGSI-LD** (ETSI GS CIM 009).
- **JSON Schema** Draft-07 for the entity schemas.
- **ISO 8601** durations for `temporalResolution`.
- **ISO 4217** for monetary `unitCode` (default EUR).
- **UN/CEFACT** common codes for non-monetary `unitCode` (e.g. `C26` = minute).
- **NACE Rev. 2.1** for `Brand.businessSection`.

## License

MIT — see [LICENSE.md](./LICENSE.md).

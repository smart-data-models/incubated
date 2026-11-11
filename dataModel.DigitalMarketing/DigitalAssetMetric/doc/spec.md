# DigitalAssetMetric

A digital marketing observation of a `DigitalAsset` for a specific date and
temporal granularity. Aggregates traffic, engagement, e-commerce, organic
social and paid ads metrics.

## Identity and temporal model

The `id` is **stable** per `(Brand, Software, temporalResolution)` and **does
not include the date**:

```
urn:ngsi-ld:DigitalAssetMetric:Acme:GA4:P1D
urn:ngsi-ld:DigitalAssetMetric:Acme:GA4:P1M
urn:ngsi-ld:DigitalAssetMetric:Acme:LinkedIn:P1D
```

The Context Broker performs upsert on each new observation; downstream a
time-series subscriber (e.g. Quantum Leap) keeps the historical values
indexed by `dateObserved`. This avoids the explosion of one entity per day
and keeps Scorpio queries fast (latest known state per granularity).

The `temporalResolution` is the granularity of the observation:

- `P1D` - daily.
- `P1M` - monthly.
- `P3M` - quarterly.
- `P1Y` - yearly.

Each granularity is published **independently** to avoid the non-additivity
problem of unique-user metrics (you cannot sum daily unique users to get
monthly unique users; the source platform must report each granularity
separately).

## Sparse schema

A channel that is purely organic (no ads spend) simply omits `ads*` fields.
A B2B channel with no e-commerce omits `ecommercePurchases`,
`itemsPurchased`, etc. Consumers must treat absent fields as "not applicable"
rather than zero.

## Unit codes (NGSI-LD meta)

Monetary and temporal metrics carry the `unitCode` meta-property on the
normalized form. The exporter sets the default unit at emission time:

| Family | Metrics | `unitCode` | Code |
| --- | --- | --- | --- |
| Monetary | `purchaseRevenue`, `totalRevenue`, `adsSpend`, `adsRevenue`, `itemRefundAmount` | EUR (ISO 4217) | `EUR` |
| Temporal | `userEngagementDuration`, `organicEngagementTime`, `organicVideoViewTime` | minute (UN/CEFACT) | `C26` |
| Counts | the rest (`sessions`, `newUsers`, `pageViews`, all `*Clicks`, all `*Impressions`, …) | — | omitted |
| Dimensionless | `organicAveragePosition` | — | omitted |

If a customer needs another currency, the exporter overrides per entity at
write time. The chosen currency is reflected in the meta.

## Segmented vs simple metrics

The following metrics support breakdown **by acquisition channel group** and
are emitted as arrays of `{channelGroup, value}`:

- `keyEventsPurchase`
- `keyEventsGenerateLead`
- `purchaseRevenue`
- `sessions`
- `totalRevenue`

The rest are scalars (integer or number). When the source platform also
reports a segmented version of one of the "simple" metrics, the exporter
either aggregates client-side or chooses the most representative
segmentation; this is out of scope of the model (it lives in the BQ 400 tier).

## Relationships

- **`refDigitalAsset`** → exactly one `DigitalAsset`. Required.
- **`refDataProvider`** → exactly one `DataProvider`. Required (sovereignty +
  traceability).

## Notes

- The same `(channel, day, granularity)` triple can have multiple
  observations from **different** `DataProvider` (e.g. internal pipeline vs
  third-party processor). Each one keeps its own `id` (suffixed with the
  provider) and Quantum Leap stores them in parallel.
- The schema is intentionally tolerant: no monetary metric is `required`
  because a channel can be purely organic.
- `dateObserved` is required; without it the temporal subscription chain is
  meaningless.

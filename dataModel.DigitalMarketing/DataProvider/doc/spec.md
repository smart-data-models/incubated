# DataProvider

A technical agent (ETL, connector, ingestion service) that injects
`DigitalAssetMetric` observations into the data space.

This entity is decoupled from `Organization` so that the same metric for the
same `DigitalAsset` on the same day can be supplied by multiple providers
and remain distinguishable in the historic time-series.

## Sovereignty principle

A data space is sovereign: data belongs to the `Organization` that owns the
`Brand`. The canonical `DataProvider` is therefore an **Internal** agent of
that same organization, even when its day-to-day operation is delegated to a
third party.

The third party operating the pipeline does **not** become the `DataProvider`
unless it ingests data under its **own** name and Organization — typically to
publish an alternative or improved processing of the same upstream sources,
that the data owner may want to compare against its internal one.

This yields two distinct use cases, with the same model:

| Use case | `providerKind` | `refOrganization` | Example |
| --- | --- | --- | --- |
| Standard ingestion (canonical) | `Internal` | The Brand owner | `urn:ngsi-ld:DataProvider:Acme-Internal-Pipeline` operated by Acme |
| Alternative / enriched processing offered by a third party | `External` | The third party | `urn:ngsi-ld:DataProvider:LIN3S-Ariadne-ETL` operated by LIN3S, ingesting metrics for the same channels as a comparison source |

Today LIN3S operates the Internal pipeline of each customer in their name;
when the data space matures and customers run their own pipelines, the
External case unlocks: LIN3S can keep contributing data under its own id and
the customer can compare both streams natively in Quantum Leap by filtering
`refDataProvider`.

## WHO vs WHAT vs OPERATOR (three-axis attribution)

A `DataProvider` answers three questions about a stream of observations:

| Axis | Field | Meaning | Example |
| --- | --- | --- | --- |
| **WHAT** | `id`, `name`, `version`, `providerKind` | Which technical pipeline produced the data | "Acme-Internal-Pipeline v1.4.0" |
| **WHO** (owner) | `refOrganization` | Who legally owns the data (responsible party in front of the data space) | `Organization:Acme` |
| **OPERATOR** | `refOperator` (optional) | Who technically runs the pipeline today | `Organization:LIN3S` |

Owner and operator are usually the same. They differ when the data owner
delegates the operation of the pipeline to a third party (typical
service-provider arrangement). Making the operator explicit gives the data
space full traceability without compromising sovereignty: the data still
belongs to the owner, but the technical execution is auditable.

## Properties

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | URN | yes | `urn:ngsi-ld:DataProvider:<short-name>`. |
| `type` | string | yes | Always `"DataProvider"`. |
| `name` | string | yes | Human-readable name. |
| `alternateName` | string | no | Short alternative. |
| `description` | string | no | Free-text description. |
| `providerKind` | enum | no | `Internal`, `External`, `Agency`, `Self`, `Other`. |
| `version` | string | no | Pipeline/connector version, for reproducibility. |
| `url` | URI | no | Service / docs URL. |
| `refOrganization` | Relationship → `Organization` | yes | Legal owner of the data (data sovereignty). |
| `refOperator` | Relationship → `Organization` | no | Technical operator. Omit when owner == operator. |

## Relationships

- **`refOrganization`** → exactly one `Organization` (the data owner).
- **`refOperator`** → at most one `Organization` (the technical operator).
  Optional: if not present, the consumer should assume operator equals owner.

## Notes

- Two parallel pipelines from the **same operator** but with different
  `version` are two distinct `DataProvider` entities. This is useful while
  running A/B comparisons of an ETL refactor.
- A `DataProvider` does **not** reference Brand, Channel or Software directly.
  The link is reverse: each `DigitalAssetMetric` carries
  `refDataProvider` so consumers can filter observations by source.
- `providerKind=Self` is reserved for cases where the SaaS itself pushes raw
  data (e.g. a hypothetical Google connector pushing to the broker directly).

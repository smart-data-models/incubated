# Brand

A brand operated by a legal organization. It represents a commercial identity
(name, sector) decoupled from the legal entity (`Organization`) so that a
single `Organization` can operate several brands and one brand can group
several `DigitalAsset` instances (web, app, social profiles, etc.).

## Properties

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | URN | yes | `urn:ngsi-ld:Brand:<short>` (or `urn:ngsi-ld:Brand:<vatID>:<short>` to avoid collisions). |
| `type` | string | yes | Always `"Brand"`. |
| `name` | string | yes | Commercial name of the brand. |
| `alternateName` | string | no | Alternative or short name. |
| `description` | string | no | Description of the brand and its activity. |
| `businessSection` | array of strings | yes | NACE Rev. 2.1 codes that classify the economic sector(s). |
| `url` | URI | no | Canonical URL of the brand. |
| `refOrganization` | Relationship → `Organization` | yes | Legal entity that owns the brand. |

## Relationships

- **`refOrganization`** → exactly one `Organization` (the legal owner). One
  `Organization` can be referenced by N `Brand` entities.

## Notes

The NACE code lives on the `Brand`, not on the `Organization`, because two
brands of the same legal entity can belong to different sectors (e.g. a
veterinary clinic that also runs a pet store).

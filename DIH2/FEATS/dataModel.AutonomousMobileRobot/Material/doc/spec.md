# Material

This folder contains all the software artefacts to offer warehouse material data 
in NGSI v2.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a [FIWARE NGSI version 2]
(http://fiware.github.io/specifications/ngsiv2/stable) API implementation, you
need to use the `keyValues` mode (`options=keyValues`).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=Material&options=keyValues&limit=1' \
  | python -m json.tool
```

```json
[
    {
        "batch": "O0035",
        "dateCreated": "2020-09-15T09:54:07.127Z",
        "dateModified": "2020-09-15T09:54:07.127Z",
        "id": "urn:ngsi-ld:Material:1600160047127",
        "mType": "lithium",
        "quantity": 20,
        "refWarehouse": "urn:ngsi-ld:Warehouse:1600160047106",
        "type": "Material"
    }
]
```

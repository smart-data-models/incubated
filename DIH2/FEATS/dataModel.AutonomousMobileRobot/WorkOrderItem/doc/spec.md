# Work order item

This folder contains all the software artefacts to offer work order item data 
in NGSI v2.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a [FIWARE NGSI version 2]
(http://fiware.github.io/specifications/ngsiv2/stable) API implementation, you
need to use the `keyValues` mode (`options=keyValues`).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=WorkOrderItem&options=keyValues&limit=1' \
  | python -m json.tool
```

```json
[
    {
        "dateCreated": "2020-09-16T09:37:33.048Z",
        "dateModified": "2020-09-16T09:37:33.048Z",
        "id": "urn:ngsi-ld:WorkOrderItem:1600245453048",
        "quantity": 30,
        "refMaterial": "urn:ngsi-ld:Material:1600245319558",
        "refWorkorder": "urn:ngsi-ld:WorkOrder:1600245452946",
        "type": "WorkOrderItem"
    }
]
```

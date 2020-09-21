# Work order

This folder contains all the software artefacts to offer work order data in NGSI v2.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a [FIWARE NGSI version 2]
(http://fiware.github.io/specifications/ngsiv2/stable) API implementation, you
need to use the `keyValues` mode (`options=keyValues`).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=WorkOrder&options=keyValues&limit=1' \
  | python -m json.tool
```

```json
[
    {
        "dateCreated": "2020-09-15T09:54:51.826Z",
        "dateModified": "2020-09-15T09:59:10.086Z",
        "id": "urn:ngsi-ld:WorkOrder:1600160091831",
        "refWarehouse": "urn:ngsi-ld:Warehouse:1600160047106",
        "refWorkstation": "urn:ngsi-ld:Workstation:1600160079599",
        "scheduledAt": "2020-08-15T09:55:00.000Z",
        "status": "ended",
        "type": "WorkOrder"
    }
]
```

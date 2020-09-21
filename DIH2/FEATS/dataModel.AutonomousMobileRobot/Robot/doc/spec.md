# Robot

This folder contains all the software artefacts to offer robot data in NGSI v2.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a [FIWARE NGSI version 2]
(http://fiware.github.io/specifications/ngsiv2/stable) API implementation, you
need to use the `keyValues` mode (`options=keyValues`).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=Robot&options=keyValues&limit=1' \
  | python -m json.tool
```

```json
[
    {
        "id": "urn:ngsi-ld:Robot:1600160039656",
        "type": "Robot",
        "available": true,
        "battery": 80,
        "dateCreated": "2020-09-15T09:53:59.654Z",
        "dateModified": "2020-09-15T10:00:43.682Z",
        "location": [
            -8.6313127,
            41.157774
        ],
        "name": "Blue robot",
        "refDestination": "urn:ngsi-ld:Workstation:1600160047106",
        "refPayload": [
            "urn:ngsi-ld:Material:1600160047127",
            "urn:ngsi-ld:Material:1600160047141"
        ],
        "refWorkOrder": "urn:ngsi-ld:WorkOrder:1600160403565",
        "status": "moving"
    }
]
```

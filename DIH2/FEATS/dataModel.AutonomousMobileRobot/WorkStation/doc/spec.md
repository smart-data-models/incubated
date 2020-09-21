# Work station

This folder contains all the software artefacts to offer work station data in NGSI v2.

**Note**: JSON Schemas only capture the NGSI simplified representation, this
means that to test the JSON schema examples with a [FIWARE NGSI version 2]
(http://fiware.github.io/specifications/ngsiv2/stable) API implementation, you
need to use the `keyValues` mode (`options=keyValues`).

## Examples of use

```bash
curl -X GET \
  'https://streams.lab.fiware.org/v2/entities?type=WorkStation&options=keyValues&limit=1' \
  | python -m json.tool
```

```json
[
    {
        "dateCreated": "2020-09-15T09:54:39.599Z",
        "dateModified": "2020-09-15T09:54:39.599Z",
        "id": "urn:ngsi-ld:WorkStation:1600160079599",
        "location": {
            "coordinates": [
                -8.6323127,
                40.270883
            ],
            "type": "Point"
        },
        "name": "Red work station",
        "status": "idle",
        "type": "WorkStation"
    }
]
```

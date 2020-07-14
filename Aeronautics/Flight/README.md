# Flight

## Description

Flight entity contains a description of a generic flight with the standard parameters used by the airline industry. This model is based on specifications published by the main organisms of the industry such us [EUROCONTROL](https://www.eurocontrol.int/), [ICAO](https://www.icao.int/) and [IATA](https://www.iata.org/).

The model specification can be found [here](doc/spec.md).

A JSON Schema corresponding to this data model can be found [here](./schema.json).

## Examples of use

### Normalized Example

Normalized NGSI response

```json
{
    "id": "flight-3732",
    "type": "Flight",
    "flightNumber": {
        "value": "3732"
    },
    "flightNumberIATA": {
        "value": "SN3732"
    },
    "flightNumberICAO": {
        "value": "BEL3732"
    },
    "flightType": {
        "value": "G"
    },
    "flightServiceIATA": {
        "value": "J"
    },
    "status": {
        "value": "cancelled"
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [50.503887, 4.469936, 10000]
        }
    },
    "speed": {
        "value": 810
    }
}
```


### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "flight-3732",
    "type": "Flight",
    "flightNumber": "3732",
    "flightNumberIATA": "SN3732",
    "flightNumberICAO": "BEL3732",
    "flightType": "G",
    "flightServiceIATA": "J",
    "status": "cancelled",
    "location": {
        "type": "Point",
        "coordinates": [50.503887, 4.469936, 10000]
    },
    "speed": 810
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:Flight:flight-3732",
    "type": "Flight",
    "flightNumber": {
        "type": "Property",
        "value": "3732"
    },
    "flightNumberIATA": {
        "type": "Property",
        "value": "SN3732"
    },
    "flightNumberICAO": {
        "type": "Property",
        "value": "BEL3732"
    },
    "flightType": {
        "type": "Property",
        "value": "G"
    },
    "flightServiceIATA": {
        "type": "Property",
        "value": "J"
    },
    "status": {
        "type": "Property",
        "value": "cancelled"
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [50.503887, 4.469936, 10000]
        }
    },
    "speed": {
        "type": "Property",
        "value": 810
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Use it with a real service

<!-- {{Provide a link to a real service providing data following the harmonized data format}} -->

## Open Issues
<!-- {{Describe here any open issue}}
i.e. This data model is being adapted to the (guidelines)[https://github.com/smart-data-models/data-models/blob/master/guidelines.md] -->

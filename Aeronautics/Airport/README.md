# Airport

## Description

Airport entity contains a description of a generic airport with the standard parameters used by the airline industry.

The model specification can be found [here](doc/spec.md).

A JSON Schema corresponding to this data model can be found [here](./schema.json).

## Examples of use

### Normalized Example

Normalized NGSI response

```json
{
    "id": "airport-BMA",
    "type": "Airport",
    "codeIATA": "BMA",
    "codeICAO": "ESSB",
    "name": "Bromma Stockholm Airport",
    "alternateName": "Stockholm Airport",
    "address": {
        "addressCountry": "SE",
        "addressLocality": "Stockholm"
    },
    "location": {
        "type": "Point",
        "coordinates": [59.354444, 17.939722, 14]
    }
}
```


### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "airport-BMA",
    "type": "Airport",
    "codeIATA": {
        "value": "BMA"
    },
    "codeICAO": {
        "value": "ESSB"
    },
    "name": {
        "value": "Bromma Stockholm Airport"
    },
    "alternateName": {
        "value": "Stockholm Airport"
    },
    "address": {
        "type": "PostalAddress",
        "value": {
            "addressCountry": "SE",
            "addressLocality": "Stockholm"
        }
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [59.354444, 17.939722, 14]
        }
    }
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:Airline:airport-BMA",
    "type": "Airport",
    "codeIATA": {
        "type": "Property",
        "value": "BMA"
    },
    "codeICAO": {
        "type": "Property",
        "value": "ESSB"
    },
    "name": {
        "type": "Property",
        "value": "Bromma Stockholm Airport"
    },
    "alternateName": {
        "type": "Property",
        "value": "Stockholm Airport"
    },
    "address": {
        "type": "Property",
        "value": {
            "addressCountry": "SE",
            "addressLocality": "Stockholm"
        }
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [59.354444, 17.939722, 14]
        }
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

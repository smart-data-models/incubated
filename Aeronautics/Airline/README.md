# Airline

## Description

Airline entity contains a description of a generic airline with the standard parameters used by the airline industry.

The model specification can be found [here](doc/spec.md).

A JSON Schema corresponding to this data model can be found [here](./schema.json).

## Examples of use

### Normalized Example

Normalized NGSI response

```json
{
    "id": "airline-SN",
    "type": "Airline",
    "codeIATA": "SN",
    "codeICAO": "BEL",
    "callsign": "BEELINE",
    "name": "Brussels Airlines",
    "alternateName": "Bru Air",
    "address":  {
        "addressCountry": "BE"
    }
}
```


### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "airline-SN",
    "type": "Airline",
    "codeIATA": {
        "value": "SN"
    },
    "codeICAO": {
        "value": "BEL"
    },
    "callsign": {
        "value": "BEELINE"
    },
    "name": {
        "value": "Brussels Airlines"
    },
    "alternateName": {
        "value": "Bru Air"
    },
    "address": {
        "type": "PostalAddress",
        "value": {
            "addressCountry": "BE"
        }
    }
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:Airline:airline-SN",
    "type": "Airline",
    "codeIATA": {
        "type": "Property",
        "value": "SN"
    },
    "codeICAO": {
        "type": "Property",
        "value": "BEL"
    },
    "callsign": {
        "type": "Property",
        "value": "BEELINE"
    },
    "name": {
        "type": "Property",
        "value": "Brussels Airlines"
    },
    "alternateName": {
        "type": "Property",
        "value": "Bru Air"
    },
    "address": {
        "type": "Property",
        "value": {
            "addressCountry": "BE",
            "type": "PostalAddress"
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

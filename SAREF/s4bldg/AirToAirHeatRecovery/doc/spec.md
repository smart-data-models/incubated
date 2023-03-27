[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: AirToAirHeatRecovery  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/AirToAirHeatRecovery/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasDefrost`: Whether the heat exchanger has defrost function or not.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `heatTransferTypeEnum`: Type of heat transfer between the two air streams.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `primaryAirFlowRateMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `primaryAirFlowRateMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryAirFlowRateMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryAirFlowRateMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `AirToAirHeatRecovery`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
AirToAirHeatRecovery:
    
  description: 'An air-to-air heat recovery device employs a counter-flow heat exchanger between inbound and outbound air flow. It is typically used to transfer heat from warmer air in one chamber to cooler air in the second chamber (i.e., typically used to recover heat from the conditioned air being exhausted and the outside air being supplied to a building), resulting in energy savings from reduced heating (or cooling) requirements.'
    
  properties:
    
    address:
    
      description: The mailing address
    
      properties:
    
        addressCountry:
    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''
    
          type: string
    
        addressLocality:
    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''
    
          type: string
    
        addressRegion:
    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''
    
          type: string
    
        district:
    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'
    
          type: string
    
        postOfficeBoxNumber:
    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''
    
          type: string
    
        postalCode:
    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''
    
          type: string
    
        streetAddress:
    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''
    
          type: string
    
        streetNr:
    
          description: Number identifying a specific property on a public street.
    
          type: string
    
      type: object
    
      x-ngsi:
    
        model: https://schema.org/address
    
        type: Property
    
    alternateName:
    
      description: An alternative name for this item
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    areaServed:
    
      description: The geographic area where a service or offered item is provided
    
      type: string
    
      x-ngsi:
    
        model: https://schema.org/Text
    
        type: Property
    
    dataProvider:
    
      description: A sequence of characters identifying the provider of the harmonised data entity.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    dateCreated:
    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.
    
      format: date-time
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    dateModified:
    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.
    
      format: date-time
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    description:
    
      description: A description of this item
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    hasDefrost:
    
      description: Whether the heat exchanger has defrost function or not.
    
      type: boolean
    
      x-ngsi:
    
        type: Property
    
    hasManufacturer:
    
      description: 'A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    hasModel:
    
      description: 'A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    heatTransferTypeEnum:
    
      description: Type of heat transfer between the two air streams.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    id:
    
      anyOf:
    
        - description: Property. Identifier format of any NGSI entity
    
          maxLength: 256
    
          minLength: 1
    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
    
          type: string
    
        - description: Property. Identifier format of any NGSI entity
    
          format: uri
    
          type: string
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isContainedInBuildingSpace:
    
      anyOf:
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isContainedInPhysicalObject:
    
      anyOf:
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isSubSystemOf:
    
      description: A reference to a system(s) that this Physical Object is part of.
    
      items:
    
        anyOf:
    
        description: Property. Unique identifier of the entity
    
      type: array
    
      x-ngsi:
    
        type: Relationship
    
    location:
    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'
    
      oneOf:
    
        - description: Geoproperty. Geojson reference to the item. Point
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                type: number
    
              minItems: 2
    
              type: array
    
            type:
    
              enum:
    
                - Point
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON Point
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. LineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  type: number
    
                minItems: 2
    
                type: array
    
              minItems: 2
    
              type: array
    
            type:
    
              enum:
    
                - LineString
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON LineString
    
          type: object
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
        - description: Geoproperty. Geojson reference to the item. Polygon
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    type: number
    
                  minItems: 2
    
                  type: array
    
                minItems: 4
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - Polygon
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON Polygon
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiPoint
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  type: number
    
                minItems: 2
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiPoint
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiPoint
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiLineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    type: number
    
                  minItems: 2
    
                  type: array
    
                minItems: 2
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiLineString
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiLineString
    
          type: object
    
        - description: Geoproperty. Geojson reference to the item. MultiLineString
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  items:
    
                    items:
    
                      type: number
    
                    minItems: 2
    
                    type: array
    
                  minItems: 4
    
                  type: array
    
                type: array
    
              type: array
    
            type:
    
              enum:
    
                - MultiPolygon
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: GeoJSON MultiPolygon
    
          type: object
    
      x-ngsi:
    
        type: Geoproperty
    
    name:
    
      description: The name of this item.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
        observedAt:
    
          description: Property. A relationship stating the timestamp of an entity (e.g. a measurement).
    
          format: date-time
    
          type: string
    
        unitCode:
    
          description: Property. A relationship identifying the unit of measure used for a certain entity.
    
          type: string
    
        value:
    
          description: 'Property. A relationship defining the value of a certain property, e.g., energy or power. Note that, even if numeric values are expected to enable reasoning, measurement values could use other datatypes.'
    
          type: number
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMin:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    owner:
    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
    
      items:
    
        anyOf:
    
        description: Property. Unique identifier of the entity
    
      type: array
    
      x-ngsi:
    
        type: Property
    
    primaryAirFlowRateMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    primaryAirFlowRateMin:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryAirFlowRateMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryAirFlowRateMin:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    seeAlso:
    
      description: list of uri pointing to additional resources about the item
    
      oneOf:
    
        - items:
    
            format: uri
    
            type: string
    
          minItems: 1
    
          type: array
    
        - format: uri
    
          type: string
    
      x-ngsi:
    
        type: Property
    
    source:
    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `AirToAirHeatRecovery`.
    
      enum:
    
        - AirToAirHeatRecovery
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/AirToAirHeatRecovery/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/AirToAirHeatRecoverys/AirToAirHeatRecovery
    
  x-model-tags: SAREF AirToAirHeatRecovery SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### AirToAirHeatRecovery NGSI-v2 key-values Example    

Here is an example of a AirToAirHeatRecovery in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:8c59d316-ed05-4b56-bec3-886379421239",
  
  "type": "AirToAirHeatRecovery",
  
  "hasDefrost": false,
  
  "heatTransferTypeEnum": "24/7",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T04:36:47Z",
  
      "value": 0.8198825347384565
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T14:46:06Z",
  
      "value": 0.505815040579818
  
    }
  
  },
  
  "primaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T20:09:42Z",
  
      "value": 0.2511282384018223
  
    }
  
  },
  
  "primaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T23:44:23Z",
  
      "value": 0.8540184208518826
  
    }
  
  },
  
  "secondaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T11:38:58Z",
  
      "value": 0.913617698002923
  
    }
  
  },
  
  "secondaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T17:25:01Z",
  
      "value": 0.17456040773539583
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:018e6821-b097-4029-9cbb-207ae7e5ddca",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:ad795f1c-0754-4877-acc2-2dcc3b337edd",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c92bd8da-e37f-4f64-989b-6007925a053b",
  
    "urn:ngsi-ld:System:5642f604-3a36-49c3-b178-3e7b99eca071",
  
    "urn:ngsi-ld:System:2f04039b-ef4e-4d61-8232-e786a220b927"
  
  ],
  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",
  
  "hasModel": "AirToAirHeatRecovery 0.1.2",
  
  "dateCreated": "2023-01-25T18:33:19Z",
  
  "dateModified": "2023-01-25T17:11:08Z",
  
  "source": "Import",
  
  "name": "AirToAirHeatRecovery",
  
  "alternateName": "AirToAirHeatRecovery type 2",
  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### AirToAirHeatRecovery NGSI-v2 normalized Example    

Here is an example of a AirToAirHeatRecovery in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a732b90e-0296-47c9-ab0f-34f6de5edfb4",
  
  "type": "AirToAirHeatRecovery",
  
  "hasDefrost": {
  
    "type": "Boolean",
  
    "value": true
  
  },
  
  "heatTransferTypeEnum": {
  
    "type": "Text",
  
    "value": "Future"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T07:59:34Z",
  
      "value": 0.9053685058368695
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T08:16:23Z",
  
      "value": 0.0225751895192714
  
    }
  
  },
  
  "primaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T19:33:24Z",
  
      "value": 0.6828734611896666
  
    }
  
  },
  
  "primaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T22:42:55Z",
  
      "value": 0.48874342661652126
  
    }
  
  },
  
  "secondaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T11:44:17Z",
  
      "value": 0.36804021603434756
  
    }
  
  },
  
  "secondaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T01:16:14Z",
  
      "value": 0.28401066550404996
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:2058c38a-eb2e-4001-af3f-9a93effd41ac"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:ea1b1b2c-cb04-429d-bf2c-ca99e7f3f005"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:123d10ff-2c3a-40f4-9fd0-07851a7d7a3c"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:90a762d4-7eed-4d5a-8a0d-a4676773917f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:b9899a7a-dc77-43a1-a0df-5a4134af3004"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "AirToAirHeatRecovery Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "AirToAirHeatRecovery 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T00:34:42.9211606+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T13:58:25.8715515+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "AirToAirHeatRecovery"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "AirToAirHeatRecovery type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### AirToAirHeatRecovery NGSI-LD key-values Example    

Here is an example of a AirToAirHeatRecovery in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:bc3f074f-9663-4d06-b10e-821d2337fdf0",
  
  "type": "AirToAirHeatRecovery",
  
  "hasDefrost": true,
  
  "heatTransferTypeEnum": "cross-platform",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T22:15:34Z",
  
    "value": 0.4412907487202886
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T08:34:57Z",
  
    "value": 0.920652054304928
  
  },
  
  "primaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T13:19:55Z",
  
    "value": 0.0022715942799831357
  
  },
  
  "primaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T09:36:28Z",
  
    "value": 0.2907376057262756
  
  },
  
  "secondaryAirFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T01:23:11Z",
  
    "value": 0.7169420790139734
  
  },
  
  "secondaryAirFlowRateMin": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T14:24:33Z",
  
    "value": 0.06832022847278774
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:77a0f237-1ee1-468d-a606-18aa8ed42e75",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:d8c228f0-3f15-467b-8a52-f22f437055ab",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c0d96ec3-3978-4286-8611-5dee256d22e1",
  
    "urn:ngsi-ld:System:97340020-197d-4969-886a-5d99991408f1",
  
    "urn:ngsi-ld:System:2cdef93c-07d9-440f-8c80-d81a38b05b23"
  
  ],
  
  "hasManufacturer": "AirToAirHeatRecovery Company Inc.",
  
  "hasModel": "AirToAirHeatRecovery 0.1.2",
  
  "dateCreated": "2023-01-26T11:52:00Z",
  
  "dateModified": "2023-01-26T14:09:02Z",
  
  "source": "Import",
  
  "name": "AirToAirHeatRecovery",
  
  "alternateName": "AirToAirHeatRecovery type 2",
  
  "description": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### AirToAirHeatRecovery NGSI-LD normalized Example    

Here is an example of a AirToAirHeatRecovery in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:AirToAirHeatRecovery:a8cd6aa9-dd5f-48bf-ba9f-3db11843b050",
  
  "type": "AirToAirHeatRecovery",
  
  "hasDefrost": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "heatTransferTypeEnum": {
  
    "type": "Property",
  
    "value": "Street"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T02:03:09Z",
  
    "value": 0.09206773488147657
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T09:23:23Z",
  
    "value": 0.04773015112848933
  
  },
  
  "primaryAirFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T15:19:05Z",
  
    "value": 0.04143347387591234
  
  },
  
  "primaryAirFlowRateMin": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T00:05:48Z",
  
    "value": 0.9113949488212527
  
  },
  
  "secondaryAirFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T02:57:23Z",
  
    "value": 0.391335331160202
  
  },
  
  "secondaryAirFlowRateMin": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T08:54:29Z",
  
    "value": 0.9115616360325159
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:f9f09bbc-27ef-4bd0-991f-6dd8720f5e7b"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:79a8986d-8526-4608-b216-ea4eb2d147ac"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:fae709e8-6311-4179-acfd-7b79e92d095c"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:4c06efa1-0d47-4a8a-a38c-d0783a106972"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:a3120479-fd3a-4a34-915c-418000e05d2b"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "AirToAirHeatRecovery Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "AirToAirHeatRecovery 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T23:15:35Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T07:30:02Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "AirToAirHeatRecovery"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "AirToAirHeatRecovery type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "AirToAirHeatRecovery of limited AirToAirHeatRecovery types"
  
  },
  
  "dataProvider": {
  
    "type": "Property",
  
    "value": "IFC file"
  
  },
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  

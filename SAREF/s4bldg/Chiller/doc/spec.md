[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Chiller  
===============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Chiller/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalCondensingTemperature`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalEfficiency`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalEvaporatingTemmperature`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalHeatRejectionRate`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalPowerConsumption`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Chiller`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Chiller:
    
  description: 'A chiller is a device used to remove heat from a liquid via a vapor-compression or absorption refrigeration cycle to cool a fluid, typically water or a mixture of water and glycol. The chilled fluid is then used to cool and dehumidify air in a building.'
    
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
    
        - description: Geoproperty. Geojson reference to the item. Polygon
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    
              minItems: 4
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    nominalCapacity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
    nominalCondensingTemperature:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalEfficiency:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalEvaporatingTemmperature:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalHeatRejectionRate:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalPowerConsumption:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
      description: It must be equal to `Chiller`.
    
      enum:
    
        - Chiller
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Chiller/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Chillers/Chiller
    
  x-model-tags: SAREF Chiller SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Chiller NGSI-v2 key-values Example    

Here is an example of a Chiller in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Chiller:ba7497f8-4fd6-4ec0-8dd8-00ed95bd51fc",
  
  "type": "Chiller",
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T19:30:17Z",
  
      "value": 0.09475720530736764
  
    }
  
  },
  
  "nominalCondensingTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T13:53:44Z",
  
      "value": 0.20516492572831713
  
    }
  
  },
  
  "nominalEfficiency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T08:40:56Z",
  
      "value": 0.9467840743079621
  
    }
  
  },
  
  "nominalEvaporatingTemmperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T20:09:15Z",
  
      "value": 0.9391249200926837
  
    }
  
  },
  
  "nominalHeatRejectionRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T05:00:44Z",
  
      "value": 0.6781215261931568
  
    }
  
  },
  
  "nominalPowerConsumption": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T00:54:27Z",
  
      "value": 0.7316060776442138
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:53b1b818-f2bf-4bbf-9ba6-e3d431a11173",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:5d06c867-dc48-4267-b194-60642a22f0af",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:8c79471f-dea7-474b-985e-e5072ea36369",
  
    "urn:ngsi-ld:System:e2e46075-3c25-46c4-80b4-da4b79faef4e",
  
    "urn:ngsi-ld:System:9eea4295-8a6c-4efb-833e-1d6941c97754"
  
  ],
  
  "hasManufacturer": "Chiller Company Inc.",
  
  "hasModel": "Chiller 0.1.2",
  
  "dateCreated": "2023-01-25T19:42:28Z",
  
  "dateModified": "2023-01-25T19:48:46Z",
  
  "source": "Import",
  
  "name": "Chiller",
  
  "alternateName": "Chiller type 2",
  
  "description": "Chiller of limited Chiller types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Chiller NGSI-v2 normalized Example    

Here is an example of a Chiller in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Chiller:fbbc813e-29ac-4462-9996-5a3d73d1ce98",
  
  "type": "Chiller",
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T01:30:53Z",
  
      "value": 0.0740819212946876
  
    }
  
  },
  
  "nominalCondensingTemperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T02:17:35Z",
  
      "value": 0.5010709006481944
  
    }
  
  },
  
  "nominalEfficiency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T05:22:55Z",
  
      "value": 0.05897827362979524
  
    }
  
  },
  
  "nominalEvaporatingTemmperature": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T11:03:08Z",
  
      "value": 0.0556993113916634
  
    }
  
  },
  
  "nominalHeatRejectionRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T15:50:55Z",
  
      "value": 0.756236294011522
  
    }
  
  },
  
  "nominalPowerConsumption": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T21:16:00Z",
  
      "value": 0.8474333854169832
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:0a2b8ec3-70d9-483f-8df0-dc7bbfa27d29"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:18da6c4b-5520-4b19-b3ee-2a91993c19de"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:b48e7b0c-7d5e-4087-89d4-c40a87ae78be"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:d9a20a72-def1-447e-ba8a-f601965fc681"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:474efe4e-7d74-4985-ac14-792dcb6b9d76"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Chiller Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Chiller 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T05:24:59.314133+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T04:27:01.3524196+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Chiller"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Chiller type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Chiller of limited Chiller types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Chiller NGSI-LD key-values Example    

Here is an example of a Chiller in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Chiller:ef80f28e-c7d0-4191-98db-4e7a7579910e",
  
  "type": "Chiller",
  
  "nominalCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T07:39:49Z",
  
    "value": 0.14483164415240912
  
  },
  
  "nominalCondensingTemperature": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T14:45:53Z",
  
    "value": 0.9768015279306371
  
  },
  
  "nominalEfficiency": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T01:36:14Z",
  
    "value": 0.8805765480877862
  
  },
  
  "nominalEvaporatingTemmperature": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T20:52:22Z",
  
    "value": 0.43414917023178734
  
  },
  
  "nominalHeatRejectionRate": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T10:59:05Z",
  
    "value": 0.18141808930767545
  
  },
  
  "nominalPowerConsumption": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T19:55:46Z",
  
    "value": 0.315065250129021
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:1215008f-2567-419b-b047-f7d2f097af3a",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:af09c4cc-4951-4828-bfbb-61f3deb2a2db",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:abc4018f-9582-45db-b488-50fc8e19e419",
  
    "urn:ngsi-ld:System:151cf91b-ebdd-48c6-a553-7640ad5cedec",
  
    "urn:ngsi-ld:System:21f479e5-1791-4367-8ebc-c8ca00fbe085"
  
  ],
  
  "hasManufacturer": "Chiller Company Inc.",
  
  "hasModel": "Chiller 0.1.2",
  
  "dateCreated": "2023-01-25T23:34:13Z",
  
  "dateModified": "2023-01-25T19:01:45Z",
  
  "source": "Import",
  
  "name": "Chiller",
  
  "alternateName": "Chiller type 2",
  
  "description": "Chiller of limited Chiller types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Chiller NGSI-LD normalized Example    

Here is an example of a Chiller in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Chiller:1a99f350-0e1d-4466-8579-912c1f3c9b8f",
  
  "type": "Chiller",
  
  "nominalCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T09:47:03Z",
  
    "value": 0.22554187711659102
  
  },
  
  "nominalCondensingTemperature": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T14:43:34Z",
  
    "value": 0.1507511254687508
  
  },
  
  "nominalEfficiency": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T03:46:03Z",
  
    "value": 0.3248755291390478
  
  },
  
  "nominalEvaporatingTemmperature": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T02:17:21Z",
  
    "value": 0.13438649176620343
  
  },
  
  "nominalHeatRejectionRate": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T06:04:17Z",
  
    "value": 0.0564283340666325
  
  },
  
  "nominalPowerConsumption": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T10:26:02Z",
  
    "value": 0.8546772522263915
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:d78af157-a55d-46b9-8c56-d6c0eda32745"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:4748763d-3b35-487c-a6ad-3a9dfa510820"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:29fc2747-3753-44b5-8d88-3ae91cd4bc89"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7a9aa253-a2eb-42ce-aeee-6130d158d18f"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:72503e97-5805-42a7-a24b-891925d2a999"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Chiller Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Chiller 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T10:57:45Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T04:43:33Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Chiller"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Chiller type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Chiller of limited Chiller types"
  
  },
  
  "dataProvider": {
  
    "type": "Property",
  
    "value": "IFC file"
  
  },
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  

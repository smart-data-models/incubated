[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Meter  
=============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/saref/Meter/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A device built to accurately detect and display a quantity in a form readable by a human being. Further, a device of category saref:Meter that performs a saref:MeteringFunction.**  

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
- `hasMeterReading`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasMeterReadingType`: A relationship identifying the reading type of a metering function (e.g., Water, Gas, Pressure , Energy , Power, etc.)  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Meter`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Meter:
    
  description: 'A device built to accurately detect and display a quantity in a form readable by a human being. Further, a device of category saref:Meter that performs a saref:MeteringFunction.'
    
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
    
    hasMeterReading:
    
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
    
    hasMeterReadingType:
    
      description: 'A relationship identifying the reading type of a metering function (e.g., Water, Gas, Pressure , Energy , Power, etc.)'
    
      enum:
    
        - Temperature
    
        - Smoke
    
        - Price
    
        - Pressure
    
        - Power
    
        - Occupancy
    
        - Motion
    
        - Light
    
        - Humidity
    
        - Energy
    
        - Water
    
        - Gas
    
        - Electricity
    
        - Coal
    
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
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
      description: It must be equal to `Meter`.
    
      enum:
    
        - Meter
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/saref/Meter/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Meters/Meter
    
  x-model-tags: SAREF Meter SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Meter NGSI-v2 key-values Example    

Here is an example of a Meter in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Meter:0dde3ab1-8d7f-400b-9fae-29a6d8db52a0",
  
  "type": "Meter",
  
  "hasMeterReading": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T21:55:04Z",
  
      "value": 0.8038490157762914
  
    }
  
  },
  
  "hasMeterReadingType": "Humidity",
  
  "hasManufacturer": "Meter Company Inc.",
  
  "hasModel": "Meter 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b05a842e-2dab-4f8e-91d8-dddf6c9d7a08",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d7e30d7-230d-445e-847e-d56a8bfe769a",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:d21bd703-9e2e-4fdc-a513-3e03580ad18e",
  
    "urn:ngsi-ld:System:0bf297bb-2527-4926-ba9e-5b5f65834c5b",
  
    "urn:ngsi-ld:System:b2ed4c1a-f7d8-42b0-9555-2738ce9c80f6"
  
  ],
  
  "dateCreated": "2023-01-26T09:50:53Z",
  
  "dateModified": "2023-01-25T18:14:39Z",
  
  "source": "Import",
  
  "name": "Meter",
  
  "alternateName": "Meter type 2",
  
  "description": "Meter of limited Meter types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Meter NGSI-v2 normalized Example    

Here is an example of a Meter in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Meter:d22ab4ee-d495-47d9-bf91-4040a9f1e437",
  
  "type": "Meter",
  
  "hasMeterReading": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T15:49:09Z",
  
      "value": 0.1692820780421772
  
    }
  
  },
  
  "hasMeterReadingType": {
  
    "type": "MeterHasMeterReadingType",
  
    "value": "Coal"
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Meter Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Meter 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:4d607bea-f506-477d-b3e4-35d8293d7738"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:dba2b9c7-0db0-44ba-bd5b-c3d29594bede"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:4bd5e430-e4cb-4e30-a518-2b03107c4f21"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:0c935447-3415-44d5-a9c8-1f48439f55d6"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:58888147-d89b-4d4b-a6fb-515f75932ccc"
  
      }
  
    ]
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T23:06:00.1423439+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T06:13:15.9747331+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Meter"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Meter type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Meter of limited Meter types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Meter NGSI-LD key-values Example    

Here is an example of a Meter in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Meter:ee807196-0895-456c-a9cd-a0ce754c9a7d",
  
  "type": "Meter",
  
  "hasMeterReading": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T19:13:53Z",
  
    "value": 0.3234784413713925
  
  },
  
  "hasMeterReadingType": "Energy",
  
  "hasManufacturer": "Meter Company Inc.",
  
  "hasModel": "Meter 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1d0f425-0713-4fcf-98e1-fdadce1b4297",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c27bac88-f5cd-4156-8b21-118666a981ed",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:801be713-b55a-4d20-97c0-f57a0324d1c9",
  
    "urn:ngsi-ld:System:780cc615-6169-4896-a969-6619abde8228",
  
    "urn:ngsi-ld:System:e85eb619-4cec-4bdd-b2c8-d1899b4f2033"
  
  ],
  
  "dateCreated": "2023-01-26T05:05:25Z",
  
  "dateModified": "2023-01-25T19:26:04Z",
  
  "source": "Import",
  
  "name": "Meter",
  
  "alternateName": "Meter type 2",
  
  "description": "Meter of limited Meter types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Meter NGSI-LD normalized Example    

Here is an example of a Meter in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Meter:e653c629-dd05-45f0-8949-1b72927b3805",
  
  "type": "Meter",
  
  "hasMeterReading": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T14:05:57Z",
  
    "value": 0.2858275914845758
  
  },
  
  "hasMeterReadingType": {
  
    "type": "Property",
  
    "value": "Smoke"
  
  },
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Meter Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Meter 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:3c7f35e1-9d96-4584-bee3-282830581524"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:ee8b7910-fbc2-4a0f-8689-b37a0f373265"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:9b595557-65c4-4ce2-98d5-3b26cf43c236"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:18f7f604-ec80-4556-8674-3bf94037843d"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:8b5dac28-26c9-4f3f-bdd7-f5e1288c71bc"
  
    }
  
  ],
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T06:13:46Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T17:40:16Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Meter"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Meter type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Meter of limited Meter types"
  
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

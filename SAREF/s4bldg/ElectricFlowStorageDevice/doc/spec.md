[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: ElectricFlowStorageDevice  
================https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/ElectricFlowStorageDevice/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An electric flow storage device is a device in which electrical energy is stored and from which energy may be progressively released.**  

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
- `nominalFrequency`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSupplyVoltage`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSupplyVoltageMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `ElectricFlowStorageDevice`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
ElectricFlowStorageDevice:
    
  description: An electric flow storage device is a device in which electrical energy is stored and from which energy may be progressively released.
    
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
    
          requirehttps://github.com/smart-data-models/incubated/SAREF/
    
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
    
    nominalFrequency:
    
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
    
    nominalSupplyVoltage:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSupplyVoltageMin:
    
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
    
      description: It must be equal to `ElectricFlowStorageDevice`.
    
      enum:
    
        - ElectricFlowStorageDevice
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/ElectricFlowStorageDevice/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/ElectricFlowStorageDevices/ElectricFlowStorageDevice
    
  x-model-tags: SAREF ElectricFlowStorageDevice SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### ElectricFlowStorageDevice NGSI-v2 key-values Example    

Here is an example of a ElectricFlowStorageDevice in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:60491652-ea6b-4e3c-8c4d-b0ae10defbda",
  
  "type": "ElectricFlowStorageDevice",
  
  "nominalFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-26T00:18:39Z",
  
      "value": 0.6643858958243121
  
    }
  
  },
  
  "nominalSupplyVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-25T17:15:42Z",
  
      "value": 0.9863230627218449
  
    }
  
  },
  
  "nominalSupplyVoltageMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T20:05:56Z",
  
      "value": 0.5073272634060758
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:783aa5ff-fb6a-4fd8-863d-82a133f5d062",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2602e1ee-c225-4703-9046-53bad81695f9",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:7aa13a80-05f1-4b1e-b973-4a4c88b729e8",
  
    "urn:ngsi-ld:System:c34c6ce4-1336-4a37-a951-7710dd32550f",
  
    "urn:ngsi-ld:System:dfeb61ff-fb62-4890-b453-918fe7a49b98"
  
  ],
  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",
  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",
  
  "dateCreated": "2023-01-25T18:29:30Z",
  
  "dateModified": "2023-01-25T14:18:54Z",
  
  "source": "Import",
  
  "name": "ElectricFlowStorageDevice",
  
  "alternateName": "ElectricFlowStorageDevice type 2",
  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### ElectricFlowStorageDevice NGSI-v2 normalized Example    

Here is an example of a ElectricFlowStorageDevice in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:4596f0a6-514a-4513-a666-3b9ade359305",
  
  "type": "ElectricFlowStorageDevice",
  
  "nominalFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-26T02:03:13Z",
  
      "value": 0.42581504045433194
  
    }
  
  },
  
  "nominalSupplyVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-25T20:43:12Z",
  
      "value": 0.025200397292739596
  
    }
  
  },
  
  "nominalSupplyVoltageMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T21:11:37Z",
  
      "value": 0.05204546916613961
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:235bfb6d-5039-45ea-95f9-094db1283634"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:9b54ca95-3f90-4be8-b32a-b585f8a9f867"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:0292e70d-da07-4d14-b8d8-c81c27c44683"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:6dce885f-2c53-414b-b0b2-9f2b88f0376d"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:a52f7099-5638-4b97-98c6-d24acc53edc6"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "ElectricFlowStorageDevice Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "ElectricFlowStorageDevice 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T09:43:01.2422472+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T15:38:19.0396796+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "ElectricFlowStorageDevice"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "ElectricFlowStorageDevice type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### ElectricFlowStorageDevice NGSI-LD key-values Example    

Here is an example of a ElectricFlowStorageDevice in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:a857700b-9222-4cb0-86a8-e4083db48017",
  
  "type": "ElectricFlowStorageDevice",
  
  "nominalFrequency": {
  
    "type": "Measurement",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-26T02:29:13Z",
  
    "value": 0.007135826810564128
  
  },
  
  "nominalSupplyVoltage": {
  
    "type": "Measurement",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-26T03:44:43Z",
  
    "value": 0.7331550386623485
  
  },
  
  "nominalSupplyVoltageMin": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T11:12:32Z",
  
    "value": 0.4799002088540737
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5e03ecda-6eb7-4036-943f-bc14aafb4644",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:bbf17932-f615-4ebf-85ed-f0606aaa05b5",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:ecb748de-8b24-4f3f-8dd6-751d75098c2d",
  
    "urn:ngsi-ld:System:179a29ae-604b-42c0-94b6-5ba4bb49bea3",
  
    "urn:ngsi-ld:System:b4ec4f67-2ac0-4c1f-8ce9-6b3013389a62"
  
  ],
  
  "hasManufacturer": "ElectricFlowStorageDevice Company Inc.",
  
  "hasModel": "ElectricFlowStorageDevice 0.1.2",
  
  "dateCreated": "2023-01-26T01:16:09Z",
  
  "dateModified": "2023-01-25T15:20:51Z",
  
  "source": "Import",
  
  "name": "ElectricFlowStorageDevice",
  
  "alternateName": "ElectricFlowStorageDevice type 2",
  
  "description": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### ElectricFlowStorageDevice NGSI-LD normalized Example    

Here is an example of a ElectricFlowStorageDevice in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricFlowStorageDevice:88efe032-f0b1-4d6b-9ff0-d3955cdcd6e7",
  
  "type": "ElectricFlowStorageDevice",
  
  "nominalFrequency": {
  
    "type": "Property",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-25T19:08:38Z",
  
    "value": 0.6604645004424095
  
  },
  
  "nominalSupplyVoltage": {
  
    "type": "Property",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-26T06:40:20Z",
  
    "value": 0.7889839353290103
  
  },
  
  "nominalSupplyVoltageMin": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T13:04:38Z",
  
    "value": 0.5759276076424262
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:8d1a4801-d77d-48ce-8fdb-6b0e6bf737f2"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:42136020-035a-4946-8a49-99cbfde581e2"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:d553b00a-f3fe-4293-922d-8b665ed69e0d"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7d32b669-8e92-4b94-9807-effabcb49391"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:242276cc-61da-4555-8b5f-769fd606ae0f"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "ElectricFlowStorageDevice Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "ElectricFlowStorageDevice 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T04:39:29Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T22:59:03Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "ElectricFlowStorageDevice"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "ElectricFlowStorageDevice type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "ElectricFlowStorageDevice of limited ElectricFlowStorageDevice types"
  
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

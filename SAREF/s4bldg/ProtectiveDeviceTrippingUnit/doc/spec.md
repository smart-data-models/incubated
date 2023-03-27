[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: ProtectiveDeviceTrippingUnit  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/ProtectiveDeviceTrippingUnit/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A protective device tripping unit breaks an electrical circuit at a separate breaking unit when a stated electric current that passes through the unit is exceeded.**  

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
- `limitingTerminalSize`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `standard`: The designation of the standard applicable for the definition of the characteristics of the unit.  
- `type`: It must be equal to `ProtectiveDeviceTrippingUnit`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
ProtectiveDeviceTrippingUnit:
    
  description: A protective device tripping unit breaks an electrical circuit at a separate breaking unit when a stated electric current that passes through the unit is exceeded.
    
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
    
    limitingTerminalSize:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
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
    
            - typhttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    standard:
    
      description: The designation of the standard applicable for the definition of the characteristics of the unit.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `ProtectiveDeviceTrippingUnit`.
    
      enum:
    
        - ProtectiveDeviceTrippingUnit
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/ProtectiveDeviceTrippingUnit/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ProtectiveDeviceTrippingUnit/schema.json"
    
  x-model-tags: SAREF ProtectiveDeviceTrippingUnit SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### ProtectiveDeviceTrippingUnit NGSI-v2 key-values Example    

Here is an example of a ProtectiveDeviceTrippingUnit in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:a9978d1d-ff56-4285-ab6f-75c7ea9d9366",
  
  "type": "ProtectiveDeviceTrippingUnit",
  
  "limitingTerminalSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T08:06:36Z",
  
      "value": 0.007349040029648757
  
    }
  
  },
  
  "standard": "transmit",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0ab75dd1-ffd5-45b9-b82a-581cdc354a9a",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c94d5308-85dc-4feb-a469-6e5fc8dd9e64",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:13b21daf-60e6-490b-883f-24f5e9439662",
  
    "urn:ngsi-ld:System:6223a07f-c00a-40eb-b519-1260b420a8a4",
  
    "urn:ngsi-ld:System:9dafd28f-9eb5-461d-a82d-2ddcbe017a87"
  
  ],
  
  "hasManufacturer": "ProtectiveDeviceTrippingUnit Company Inc.",
  
  "hasModel": "ProtectiveDeviceTrippingUnit 0.1.2",
  
  "dateCreated": "2023-01-26T07:35:56Z",
  
  "dateModified": "2023-01-26T00:18:37Z",
  
  "source": "Import",
  
  "name": "ProtectiveDeviceTrippingUnit",
  
  "alternateName": "ProtectiveDeviceTrippingUnit type 2",
  
  "description": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### ProtectiveDeviceTrippingUnit NGSI-v2 normalized Example    

Here is an example of a ProtectiveDeviceTrippingUnit in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:d0ceff43-b934-4f8b-9a61-ac3fb2d00ca0",
  
  "type": "ProtectiveDeviceTrippingUnit",
  
  "limitingTerminalSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-25T14:51:20Z",
  
      "value": 0.6188844647188521
  
    }
  
  },
  
  "standard": {
  
    "type": "Text",
  
    "value": "alarm"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:9e090bad-e15b-4d58-98aa-fb3603aa29a9"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:6c1269e4-0729-42b5-a7c3-626c97c5e6f1"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:90583732-ca11-440d-88a8-c8dfd68ba350"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:fc4ff579-32de-4fb7-95a3-ef9fa07b0dc5"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:68ddbc79-587d-4866-ae6d-3d9efcac6ac5"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "ProtectiveDeviceTrippingUnit Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "ProtectiveDeviceTrippingUnit 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T07:05:39.1899219+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T16:04:21.3598466+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "ProtectiveDeviceTrippingUnit"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "ProtectiveDeviceTrippingUnit type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### ProtectiveDeviceTrippingUnit NGSI-LD key-values Example    

Here is an example of a ProtectiveDeviceTrippingUnit in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:41659f5e-fe2b-4bb2-8ec4-ed401727e57d",
  
  "type": "ProtectiveDeviceTrippingUnit",
  
  "limitingTerminalSize": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T08:55:05Z",
  
    "value": 0.37033727779383474
  
  },
  
  "standard": "Sports, Games & Baby",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d344d393-7664-4070-8f2f-e61396544c25",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3dec837c-37b9-4f90-9c4f-4a1fe790b3bd",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:2599cb04-f959-4b4f-b3fc-bcaf4d989af1",
  
    "urn:ngsi-ld:System:46b06cab-817c-4eda-8966-bd94e0be6ba8",
  
    "urn:ngsi-ld:System:922d0ea6-fe00-4164-870b-541b868e838e"
  
  ],
  
  "hasManufacturer": "ProtectiveDeviceTrippingUnit Company Inc.",
  
  "hasModel": "ProtectiveDeviceTrippingUnit 0.1.2",
  
  "dateCreated": "2023-01-25T17:38:53Z",
  
  "dateModified": "2023-01-26T01:14:24Z",
  
  "source": "Import",
  
  "name": "ProtectiveDeviceTrippingUnit",
  
  "alternateName": "ProtectiveDeviceTrippingUnit type 2",
  
  "description": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### ProtectiveDeviceTrippingUnit NGSI-LD normalized Example    

Here is an example of a ProtectiveDeviceTrippingUnit in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ProtectiveDeviceTrippingUnit:f10ca3f9-0120-45ce-9758-c7d87ff88556",
  
  "type": "ProtectiveDeviceTrippingUnit",
  
  "limitingTerminalSize": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T16:18:32Z",
  
    "value": 0.5988374624361508
  
  },
  
  "standard": {
  
    "type": "Property",
  
    "value": "turquoise"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:b4596d63-a279-46bd-9f55-787ea3bfea0c"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:be93a21f-cf03-446e-8bc6-3caf4d92fae9"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:386d031a-d13b-4b5f-a022-1aab55cc9bd5"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:2d9aeff1-a0f8-4cad-96a0-b01d99938948"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:9a4c8d68-59b1-4bf7-833d-871d2d835564"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "ProtectiveDeviceTrippingUnit Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "ProtectiveDeviceTrippingUnit 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T08:37:55Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T07:20:44Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "ProtectiveDeviceTrippingUnit"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "ProtectiveDeviceTrippingUnit type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "ProtectiveDeviceTrippingUnit of limited ProtectiveDeviceTrippingUnit types"
  
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

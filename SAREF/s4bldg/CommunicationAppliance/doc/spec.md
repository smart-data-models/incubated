[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: CommunicationAppliance  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://opensource.org/licenses/BSD-3-Clause)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A communications appliance transmits and receives electronic or digital information as data or sound.  Communication appliances may be fixed in place or may be able to be moved from one space to another. Communication appliances require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source.**  

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
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `CommunicationAppliance`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
CommunicationAppliance:
    
  description: A communications appliance transmits and receives electronic or digital information as data or sound.  Communication appliances may be fixed in place or may be able to be moved from one space to another. Communication appliances require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source.
    
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
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
      description: It must be equal to `CommunicationAppliance`.
    
      enum:
    
        - CommunicationAppliance
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://opensource.org/licenses/BSD-3-Clause
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/CommunicationAppliance/schema.json"
    
  x-model-tags: SAREF CommunicationAppliance SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### CommunicationAppliance NGSI-v2 key-values Example    

Here is an example of a CommunicationAppliance in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CommunicationAppliance:5a0ba33f-afd1-413e-9b25-b2e56457564b",
  
  "type": "CommunicationAppliance",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7505e4c9-8806-493c-8757-d541d042cacd",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7e7dde65-0332-4eb2-aad2-7179f921eaff",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c040f083-03da-4db3-ba18-0a4abe595096",
  
    "urn:ngsi-ld:System:ca707665-bcb1-4632-ade9-9e2b90017ee8",
  
    "urn:ngsi-ld:System:5d6e8ac5-80d9-4d02-94c3-1dd3f6558efb"
  
  ],
  
  "hasManufacturer": "CommunicationAppliance Company Inc.",
  
  "hasModel": "CommunicationAppliance 0.1.2",
  
  "dateCreated": "2023-01-25T17:07:07Z",
  
  "dateModified": "2023-01-25T19:39:55Z",
  
  "source": "Import",
  
  "name": "CommunicationAppliance",
  
  "alternateName": "CommunicationAppliance type 2",
  
  "description": "CommunicationAppliance of limited CommunicationAppliance types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### CommunicationAppliance NGSI-v2 normalized Example    

Here is an example of a CommunicationAppliance in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CommunicationAppliance:3ed12e9d-d89c-4340-8d99-73b6b9ae0c28",
  
  "type": "CommunicationAppliance",
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:c4d1fd68-4f76-4a51-bb93-599b6cc17fd1"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:298b5d8d-c488-42f6-bb24-6623145f4fb0"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:81c7c232-092a-40f4-9d14-4f106e163174"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:5ee6713d-4be1-4cc8-9802-340c33b6ee5f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:c3df800f-cf87-4b9a-9116-8960c8a3d151"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "CommunicationAppliance Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "CommunicationAppliance 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T06:29:11.0938007+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T12:09:23.3004188+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "CommunicationAppliance"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "CommunicationAppliance type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "CommunicationAppliance of limited CommunicationAppliance types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### CommunicationAppliance NGSI-LD key-values Example    

Here is an example of a CommunicationAppliance in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CommunicationAppliance:bfde8499-4e03-4f26-af75-09496d08705d",
  
  "type": "CommunicationAppliance",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:4003d629-1fe8-413e-8769-d9ffb8e39dce",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:407d6a5d-3df4-444a-aef8-f2015af640dc",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:227e9ba1-d594-464a-a073-519f1cc831ea",
  
    "urn:ngsi-ld:System:b5583789-010e-4481-af17-f09842151ed7",
  
    "urn:ngsi-ld:System:2709eb40-3c54-42ca-81c4-24974524a85a"
  
  ],
  
  "hasManufacturer": "CommunicationAppliance Company Inc.",
  
  "hasModel": "CommunicationAppliance 0.1.2",
  
  "dateCreated": "2023-01-26T05:58:11Z",
  
  "dateModified": "2023-01-26T04:01:05Z",
  
  "source": "Import",
  
  "name": "CommunicationAppliance",
  
  "alternateName": "CommunicationAppliance type 2",
  
  "description": "CommunicationAppliance of limited CommunicationAppliance types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### CommunicationAppliance NGSI-LD normalized Example    

Here is an example of a CommunicationAppliance in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:CommunicationAppliance:e2129944-3046-4ed9-b74f-59a6bf1dfc7e",
  
  "type": "CommunicationAppliance",
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:75317891-340a-49a8-8f3e-4ec891d943c9"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:34630474-4529-40d0-ad5c-367c9494694d"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:91da2b77-a2e5-411c-be8f-f3245c2f9087"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:cdae1f62-b280-4e18-81de-99dc49cb9cd3"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:0233eb63-8b4d-4164-81e9-db4a7ba3f752"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "CommunicationAppliance Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "CommunicationAppliance 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T20:40:10Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T08:21:34Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "CommunicationAppliance"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "CommunicationAppliance type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "CommunicationAppliance of limited CommunicationAppliance types"
  
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

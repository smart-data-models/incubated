[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Sensor  
==============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://opensource.org/licenses/BSD-3-Clause)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. Further, a device of category saref:Sensor that performs a saref:SensingFunction.**  

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
- `hasSensingRange`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasSensorType`: A relationship identifying the sensing type of a sensor detection (i.e., Temperature, Occupancy, Humidity, Motion , Smoke, Pressure, etc.)   
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Sensor`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Sensor:
    
  description: 'A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. Further, a device of category saref:Sensor that performs a saref:SensingFunction.'
    
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
    
    hasSensingRange:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF/Measurement/schema.json"
    
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
    
    hasSensorType:
    
      description: 'A relationship identifying the sensing type of a sensor detection (i.e., Temperature, Occupancy, Humidity, Motion , Smoke, Pressure, etc.) '
    
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
    
        - DirectNormalIrradiation
    
        - CO2Concentration
    
        - OpeningPosition
    
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
    
              minhttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
      description: It must be equal to `Sensor`.
    
      enum:
    
        - Sensor
    
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
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF/Sensor/schema.json"
    
  x-model-tags: SAREF Sensor SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Sensor NGSI-v2 key-values Example    

Here is an example of a Sensor in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Sensor:5e1bbf3c-f8a9-4a5f-b7b5-74456fa911d5",
  
  "type": "Sensor",
  
  "hasSensingRange": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T19:37:51Z",
  
      "value": 0.014230070583521992
  
    }
  
  },
  
  "hasSensorType": "Smoke",
  
  "hasManufacturer": "Sensor Company Inc.",
  
  "hasModel": "Sensor 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:1f5569e9-37c0-4211-bf58-a4c7b6db8169",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:bdc0656f-f29c-4dfc-9b8d-f68a5209b6b6",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:b6f77f2f-94f9-4ef0-bd73-58e008b0dd8e",
  
    "urn:ngsi-ld:System:143d66f0-6d53-48c5-8ec4-4677754caf42",
  
    "urn:ngsi-ld:System:47d20506-0d3a-4027-97e7-3442a9ee93e0"
  
  ],
  
  "dateCreated": "2023-01-26T03:07:27Z",
  
  "dateModified": "2023-01-26T00:23:18Z",
  
  "source": "Import",
  
  "name": "Sensor",
  
  "alternateName": "Sensor type 2",
  
  "description": "Sensor of limited Sensor types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Sensor NGSI-v2 normalized Example    

Here is an example of a Sensor in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Sensor:5164ac7d-f33a-4a9d-92c0-d85738dce5dc",
  
  "type": "Sensor",
  
  "hasSensingRange": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T11:08:03Z",
  
      "value": 0.6379919853662889
  
    }
  
  },
  
  "hasSensorType": {
  
    "type": "SensorHasSensorType",
  
    "value": "Motion"
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Sensor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Sensor 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:dde4fa8f-da14-4e32-9061-53b1934b80dd"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:c1a7b6e1-9a70-4e7f-aecd-3a694da2ac1a"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:e55fb57f-3106-4f04-9121-ecc2eae1056f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:f32c549f-7d88-48e9-804f-a4f758868bc0"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:0a12aeeb-5637-42dd-ad57-4b5e34dc929a"
  
      }
  
    ]
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T20:29:30.4737975+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T22:25:21.6300054+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Sensor"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Sensor type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Sensor of limited Sensor types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Sensor NGSI-LD key-values Example    

Here is an example of a Sensor in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Sensor:b9cd8f11-8d0f-4fa1-b1d9-627572e9d67a",
  
  "type": "Sensor",
  
  "hasSensingRange": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T14:24:13Z",
  
    "value": 0.19880952263281826
  
  },
  
  "hasSensorType": "Occupancy",
  
  "hasManufacturer": "Sensor Company Inc.",
  
  "hasModel": "Sensor 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0eead0dd-78fa-4072-b9ec-5fe95d2cb755",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a7575198-623d-48b3-afd6-6d1a65972cc4",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:0ad39b84-1b82-4fec-ae7d-3139d0402025",
  
    "urn:ngsi-ld:System:261f46f5-546f-4c07-a553-a423e8e80e31",
  
    "urn:ngsi-ld:System:2c77915b-4b1f-49af-9f05-12611c0fec4b"
  
  ],
  
  "dateCreated": "2023-01-25T18:39:06Z",
  
  "dateModified": "2023-01-26T12:07:34Z",
  
  "source": "Import",
  
  "name": "Sensor",
  
  "alternateName": "Sensor type 2",
  
  "description": "Sensor of limited Sensor types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Sensor NGSI-LD normalized Example    

Here is an example of a Sensor in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Sensor:51d66982-bef7-4ccb-a9cd-80a338348d78",
  
  "type": "Sensor",
  
  "hasSensingRange": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T00:40:11Z",
  
    "value": 0.7330213275090168
  
  },
  
  "hasSensorType": {
  
    "type": "Property",
  
    "value": "Occupancy"
  
  },
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Sensor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Sensor 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:9f857ae8-7285-445c-b78c-4b021935d531"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:1c143596-fb89-40b1-b575-2583c693644e"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:aedbd727-63dd-4ca0-893c-515b3fde97dc"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7142065b-7971-4cc6-9e24-32ab9126bb5d"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:64eb8dc8-bf25-4773-bfc2-59464c0b018c"
  
    }
  
  ],
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T07:13:43Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T13:51:53Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Sensor"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Sensor type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Sensor of limited Sensor types"
  
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

[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: ElectricMotor  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://opensource.org/licenses/BSD-3-Clause)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An electric motor is an engine that is a machine for converting electrical energy into mechanical energy.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `electricMotorEfficiency`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `frameSize`: Designation of the frame size according to the named range of frame sizes designated at the place of use or according to a given standard.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasPartWinding`: Indication of whether the motor is single speed, i.e. has a single winding (= FALSE) or multi-speed i.e.has part winding (= TRUE) .  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isGuarded`: Indication of whether the motor enclosure is guarded (= TRUE) or not (= FALSE).  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `lockedRotorCurrent`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `motorEnclosureType`: A list of the available types of motor enclosure from which that required may be selected.  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `powerOutputMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `startCurrentFactor`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `startingTime`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `teTime`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `type`: It must be equal to `ElectricMotor`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
ElectricMotor:
    
  description: An electric motor is an engine that is a machine for converting electrical energy into mechanical energy.
    
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
    
    electricMotorEfficiency:
    
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
    
    frameSize:
    
      description: Designation of the frame size according to the named range of frame sizes designated at the place of use or according to a given standard.
    
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
    
    hasPartWinding:
    
      description: 'Indication of whether the motor is single speed, i.e. has a single winding (= FALSE) or multi-speed i.e.has part winding (= TRUE) .'
    
      type: boolean
    
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
    
    isGuarded:
    
      description: Indication of whether the motor enclosure is guarded (= TRUE) or not (= FALSE).
    
      type: boolean
    
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
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    lockedRotorCurrent:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    motorEnclosureType:
    
      description: A list of the available types of motor enclosure from which that required may be selected.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
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
    
    powerOutputMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
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
    
    startCurrentFactor:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    startingTime:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    teTime:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `ElectricMotor`.
    
      enum:
    
        - ElectricMotor
    
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
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ElectricMotor/schema.json"
    
  x-model-tags: SAREF ElectricMotor SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### ElectricMotor NGSI-v2 key-values Example    

Here is an example of a ElectricMotor in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricMotor:ea4bd048-a263-480d-be61-7de297bed540",
  
  "type": "ElectricMotor",
  
  "electricMotorEfficiency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T09:36:42Z",
  
      "value": 0.36137565435400376
  
    }
  
  },
  
  "frameSize": "Awesome",
  
  "hasPartWinding": false,
  
  "isGuarded": false,
  
  "lockedRotorCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-26T07:37:21Z",
  
      "value": 0.4948278478821372
  
    }
  
  },
  
  "motorEnclosureType": "target",
  
  "powerOutputMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T19:22:37Z",
  
      "value": 0.5320055721976125
  
    }
  
  },
  
  "startCurrentFactor": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T15:38:56Z",
  
      "value": 0.7921279415808247
  
    }
  
  },
  
  "startingTime": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T01:27:50Z",
  
      "value": 0.7237739470818347
  
    }
  
  },
  
  "teTime": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T04:51:35Z",
  
      "value": 0.32577211564738595
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b1cccba1-7a35-422c-aca4-800d8f462b00",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a15795e2-b0d9-4ab0-863c-bc40e5e88fc6",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:24f05820-a94f-4c53-bd66-bcb5bc451ee4",
  
    "urn:ngsi-ld:System:eb6a2613-cf69-4cdc-a958-b8f24903fc46",
  
    "urn:ngsi-ld:System:594815c7-5dd7-4910-93ca-ee2579c87739"
  
  ],
  
  "hasManufacturer": "ElectricMotor Company Inc.",
  
  "hasModel": "ElectricMotor 0.1.2",
  
  "dateCreated": "2023-01-25T16:58:38Z",
  
  "dateModified": "2023-01-25T21:01:09Z",
  
  "source": "Import",
  
  "name": "ElectricMotor",
  
  "alternateName": "ElectricMotor type 2",
  
  "description": "ElectricMotor of limited ElectricMotor types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### ElectricMotor NGSI-v2 normalized Example    

Here is an example of a ElectricMotor in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricMotor:024aea5d-c781-4d5e-9b57-92672c75663d",
  
  "type": "ElectricMotor",
  
  "electricMotorEfficiency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T21:19:24Z",
  
      "value": 0.14465653517328592
  
    }
  
  },
  
  "frameSize": {
  
    "type": "Text",
  
    "value": "benchmark"
  
  },
  
  "hasPartWinding": {
  
    "type": "Boolean",
  
    "value": true
  
  },
  
  "isGuarded": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "lockedRotorCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-26T07:50:40Z",
  
      "value": 0.7069578753062778
  
    }
  
  },
  
  "motorEnclosureType": {
  
    "type": "Text",
  
    "value": "Cambridgeshire"
  
  },
  
  "powerOutputMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T14:28:53Z",
  
      "value": 0.925424003891414
  
    }
  
  },
  
  "startCurrentFactor": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T21:56:18Z",
  
      "value": 0.27335468276078645
  
    }
  
  },
  
  "startingTime": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T00:56:58Z",
  
      "value": 0.8955138694697009
  
    }
  
  },
  
  "teTime": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T00:19:05Z",
  
      "value": 0.024805742901409134
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:dec2fd4f-2093-4779-b571-841bac3ec419"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:42195e3f-cdb8-4603-952f-d9f52d9749ed"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:08a8c968-420c-464d-8458-784dd721cfbe"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:92362fba-3ddd-47af-a985-de2caf90f298"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:3033fd90-5610-490c-8b39-6f98c962af41"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "ElectricMotor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "ElectricMotor 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T20:39:17.5806269+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T18:24:24.0858451+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "ElectricMotor"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "ElectricMotor type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "ElectricMotor of limited ElectricMotor types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### ElectricMotor NGSI-LD key-values Example    

Here is an example of a ElectricMotor in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricMotor:51cef576-f267-4dff-a234-d19e467518c0",
  
  "type": "ElectricMotor",
  
  "electricMotorEfficiency": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T01:31:28Z",
  
    "value": 0.715712242878087
  
  },
  
  "frameSize": "Fantastic",
  
  "hasPartWinding": true,
  
  "isGuarded": true,
  
  "lockedRotorCurrent": {
  
    "type": "Measurement",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-26T01:47:13Z",
  
    "value": 0.5604435963744671
  
  },
  
  "motorEnclosureType": "Exclusive",
  
  "powerOutputMax": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T13:38:45Z",
  
    "value": 0.7106773504928142
  
  },
  
  "startCurrentFactor": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T04:55:28Z",
  
    "value": 0.023800152538014707
  
  },
  
  "startingTime": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T11:28:50Z",
  
    "value": 0.700953875123184
  
  },
  
  "teTime": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T20:51:54Z",
  
    "value": 0.7409698559022957
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:929c0acc-e128-4d4e-b831-2e89111291ec",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:b3c68139-257e-4f8a-9a88-008b6608289e",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:52bf23ea-2dc2-4530-8890-65e9c683d07f",
  
    "urn:ngsi-ld:System:43870e8f-3ba8-4049-b161-1dca106dc072",
  
    "urn:ngsi-ld:System:e1bdd5e3-a141-4f41-abf0-5f22cb7cc23b"
  
  ],
  
  "hasManufacturer": "ElectricMotor Company Inc.",
  
  "hasModel": "ElectricMotor 0.1.2",
  
  "dateCreated": "2023-01-26T13:55:16Z",
  
  "dateModified": "2023-01-26T12:47:03Z",
  
  "source": "Import",
  
  "name": "ElectricMotor",
  
  "alternateName": "ElectricMotor type 2",
  
  "description": "ElectricMotor of limited ElectricMotor types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### ElectricMotor NGSI-LD normalized Example    

Here is an example of a ElectricMotor in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ElectricMotor:c4e91c91-12f4-4dc5-aaae-4c7644c8d9df",
  
  "type": "ElectricMotor",
  
  "electricMotorEfficiency": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T08:26:24Z",
  
    "value": 0.07012980187189011
  
  },
  
  "frameSize": {
  
    "type": "Property",
  
    "value": "Saint Martin"
  
  },
  
  "hasPartWinding": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "isGuarded": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "lockedRotorCurrent": {
  
    "type": "Property",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-26T10:56:17Z",
  
    "value": 0.7593092722196552
  
  },
  
  "motorEnclosureType": {
  
    "type": "Property",
  
    "value": "Berkshire"
  
  },
  
  "powerOutputMax": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T08:12:29Z",
  
    "value": 0.32215622178270653
  
  },
  
  "startCurrentFactor": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T06:44:33Z",
  
    "value": 0.8565155734572442
  
  },
  
  "startingTime": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T08:12:12Z",
  
    "value": 0.7168865515513289
  
  },
  
  "teTime": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T06:08:56Z",
  
    "value": 0.2793471624901087
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:c89167bc-11d5-48cc-8cde-0ea875d76fe3"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:e8206186-a4b3-4030-80dc-a4e5ebe12ab4"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:20c42d2b-4216-458d-9ef0-a0fece28ca92"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:5418d44a-319c-46af-aa8a-83e59fb559e7"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7baa4e2b-ac2d-4a9b-90a2-ef578b5091a7"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "ElectricMotor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "ElectricMotor 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T09:43:59Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T14:02:00Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "ElectricMotor"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "ElectricMotor type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "ElectricMotor of limited ElectricMotor types"
  
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

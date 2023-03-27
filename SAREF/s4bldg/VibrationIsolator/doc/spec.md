[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: VibrationIsolator  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/VibrationIsolator/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A vibration isolator is a device used to minimize the effects of vibration transmissibility in a building.**  

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
- `height`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `isolatorCompressibility`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isolatorStaticDeflection`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `supportedWeightMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `type`: It must be equal to `VibrationIsolator`.  
- `vibrationTransmissibility`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
VibrationIsolator:
    
  description: A vibration isolator is a device used to minimize the effects of vibration transmissibility in a building.
    
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
    
    height:
    
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
    
    isolatorCompressibility:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    isolatorStaticDeflection:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
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
    
              enuhttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    supportedWeightMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `VibrationIsolator`.
    
      enum:
    
        - VibrationIsolator
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    vibrationTransmissibility:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/VibrationIsolator/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/VibrationIsolators/VibrationIsolator
    
  x-model-tags: SAREF VibrationIsolator SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### VibrationIsolator NGSI-v2 key-values Example    

Here is an example of a VibrationIsolator in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:VibrationIsolator:cd36687d-d862-4b70-b8ed-789a16b2afec",
  
  "type": "VibrationIsolator",
  
  "height": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T05:58:01Z",
  
      "value": 0.38014362681889713
  
    }
  
  },
  
  "isolatorCompressibility": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T11:47:21Z",
  
      "value": 0.7634523319144405
  
    }
  
  },
  
  "isolatorStaticDeflection": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T15:48:52Z",
  
      "value": 0.7887792629834026
  
    }
  
  },
  
  "supportedWeightMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-25T23:36:38Z",
  
      "value": 0.32346503665487614
  
    }
  
  },
  
  "vibrationTransmissibility": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T05:39:14Z",
  
      "value": 0.0735805434874115
  
    }
  
  },
  
  "hasManufacturer": "VibrationIsolator Company Inc.",
  
  "hasModel": "VibrationIsolator 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:e78215e8-4265-4a20-abd0-a19cbe803047",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:30fd3d36-dbea-4994-a312-a061f283886a",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:a9cb3141-21d1-41f9-882d-4e7eb5ca0538",
  
    "urn:ngsi-ld:System:d34a3962-d8fc-4d65-a0d8-57d881ec9279",
  
    "urn:ngsi-ld:System:c23095d2-a7c8-4920-b237-e7ae47f03451"
  
  ],
  
  "dateCreated": "2023-01-26T13:07:56Z",
  
  "dateModified": "2023-01-26T06:35:21Z",
  
  "source": "Import",
  
  "name": "VibrationIsolator",
  
  "alternateName": "VibrationIsolator type 2",
  
  "description": "VibrationIsolator of limited VibrationIsolator types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### VibrationIsolator NGSI-v2 normalized Example    

Here is an example of a VibrationIsolator in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:VibrationIsolator:c808c7ae-06ec-4022-8405-3a2031703303",
  
  "type": "VibrationIsolator",
  
  "height": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T00:44:01Z",
  
      "value": 0.4519574730782471
  
    }
  
  },
  
  "isolatorCompressibility": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T06:45:46Z",
  
      "value": 0.11287489586954691
  
    }
  
  },
  
  "isolatorStaticDeflection": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T05:21:25Z",
  
      "value": 0.44640431539803016
  
    }
  
  },
  
  "supportedWeightMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-26T12:49:06Z",
  
      "value": 0.9957664703512201
  
    }
  
  },
  
  "vibrationTransmissibility": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T19:15:39Z",
  
      "value": 0.045745566367183965
  
    }
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "VibrationIsolator Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "VibrationIsolator 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:35215bc5-6e3e-4794-ab50-6a3a56149e98"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:e97a7737-8516-4038-b9c3-a6bc22bc3228"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:4491af0e-5aaf-494e-a7c2-7d62f7e18db5"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:18b4c438-10ee-4916-9d1d-b6e4dbc3bd7f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:541cc5f6-fade-4136-a18a-784f97ebe6c4"
  
      }
  
    ]
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T04:34:02.6856577+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T21:20:11.0544578+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "VibrationIsolator"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "VibrationIsolator type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "VibrationIsolator of limited VibrationIsolator types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### VibrationIsolator NGSI-LD key-values Example    

Here is an example of a VibrationIsolator in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:VibrationIsolator:3822a084-6d74-4d23-abcc-92f297a4f561",
  
  "type": "VibrationIsolator",
  
  "height": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T09:27:43Z",
  
    "value": 0.9599361163933814
  
  },
  
  "isolatorCompressibility": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T00:37:51Z",
  
    "value": 0.34576882567961487
  
  },
  
  "isolatorStaticDeflection": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T12:07:28Z",
  
    "value": 0.1837817253516013
  
  },
  
  "supportedWeightMax": {
  
    "type": "Measurement",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-25T17:08:50Z",
  
    "value": 0.28908574507632057
  
  },
  
  "vibrationTransmissibility": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T21:53:43Z",
  
    "value": 0.1733917889877996
  
  },
  
  "hasManufacturer": "VibrationIsolator Company Inc.",
  
  "hasModel": "VibrationIsolator 0.1.2",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:532879c9-c1b4-4b5c-976a-d0ca91ca7161",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:161e116d-eb84-4a94-980f-629d42289e7f",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:f8ed1e75-4939-472c-9b28-33ab10d028e9",
  
    "urn:ngsi-ld:System:6f7186f5-aaa7-4340-bd7d-ed03bca5a17f",
  
    "urn:ngsi-ld:System:b46782ba-646b-41c5-8510-5d4d97d747db"
  
  ],
  
  "dateCreated": "2023-01-26T04:36:32Z",
  
  "dateModified": "2023-01-26T09:30:54Z",
  
  "source": "Import",
  
  "name": "VibrationIsolator",
  
  "alternateName": "VibrationIsolator type 2",
  
  "description": "VibrationIsolator of limited VibrationIsolator types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### VibrationIsolator NGSI-LD normalized Example    

Here is an example of a VibrationIsolator in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:VibrationIsolator:3fef599e-57dd-4ead-b1f1-1be1acec4ed4",
  
  "type": "VibrationIsolator",
  
  "height": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T00:57:35Z",
  
    "value": 0.5291676326164039
  
  },
  
  "isolatorCompressibility": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T13:38:20Z",
  
    "value": 0.0633806140666543
  
  },
  
  "isolatorStaticDeflection": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T05:45:32Z",
  
    "value": 0.7015963366033574
  
  },
  
  "supportedWeightMax": {
  
    "type": "Property",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-26T11:46:41Z",
  
    "value": 0.22821941593534223
  
  },
  
  "vibrationTransmissibility": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T02:32:45Z",
  
    "value": 0.5811208596388945
  
  },
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "VibrationIsolator Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "VibrationIsolator 0.1.2"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:fd49449a-d970-42ca-b1fc-76498db2246a"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:928afd04-5e3b-4626-a746-e15f82d1dd27"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:ef621e1c-9c02-4f58-9460-e9792c709c3c"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:d166189e-cc79-40a9-ad8d-9874487d095f"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:5dface3a-d991-4c63-a878-87fc9194c2a8"
  
    }
  
  ],
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T22:43:59Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T12:00:10Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "VibrationIsolator"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "VibrationIsolator type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "VibrationIsolator of limited VibrationIsolator types"
  
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

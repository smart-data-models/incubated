[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: TubeBundle  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/TubeBundle/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `foulingFactor`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasTurbulator`: TRUE if the tube has a turbulator, FALSE if it does not.  
- `horizontalSpacing`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `id`: Unique identifier of the entity  
- `inLineRowSpacing`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `insideDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `length`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `numberOfCircuits`: Number of parallel fluid tube circuits.  
- `numberOfRows`: Number of tube rows in the tube bundle assembly.  
- `outsideDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `staggeredRowSpacing`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `thermalConductivity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `type`: It must be equal to `TubeBundle`.  
- `verticalSpacing`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `volumen`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
TubeBundle:
    
  description: 'A tube bundle is a device consisting of tubes and bundles of tubes used for heat transfer and contained typically within other energy conversion devices, such as a chiller or coil.'
    
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
    
    foulingFactor:
    
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
    
    hasTurbulator:
    
      description: 'TRUE if the tube has a turbulator, FALSE if it does not.'
    
      type: boolean
    
      x-ngsi:
    
        type: Property
    
    horizontalSpacing:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
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
    
    inLineRowSpacing:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    insideDiameter:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
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
    
    length:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
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
    
              enum:
    
                - Point
    
              type: string
    
          required:
    
            - type
    
            - coordinates
    
          title: https://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    nominalDiameter:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    numberOfCircuits:
    
      description: Number of parallel fluid tube circuits.
    
      type: number
    
      x-ngsi:
    
        type: Property
    
    numberOfRows:
    
      description: Number of tube rows in the tube bundle assembly.
    
      type: number
    
      x-ngsi:
    
        type: Property
    
    outsideDiameter:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
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
    
    staggeredRowSpacing:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    thermalConductivity:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `TubeBundle`.
    
      enum:
    
        - TubeBundle
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    verticalSpacing:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    volumen:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
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
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/TubeBundle/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/TubeBundle/schema.json"
    
  x-model-tags: SAREF TubeBundle SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### TubeBundle NGSI-v2 key-values Example    

Here is an example of a TubeBundle in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:TubeBundle:ce27cf16-c4dc-4b93-a7e5-021f38a5a0b8",
  
  "type": "TubeBundle",
  
  "foulingFactor": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin/Watt",
  
      "observedAt": "2023-01-26T08:05:24Z",
  
      "value": 0.8435912145074106
  
    }
  
  },
  
  "hasTurbulator": true,
  
  "horizontalSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T10:15:19Z",
  
      "value": 0.45432121749623355
  
    }
  
  },
  
  "inLineRowSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T06:51:49Z",
  
      "value": 0.9076815444305774
  
    }
  
  },
  
  "insideDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T07:46:04Z",
  
      "value": 0.9701449888350496
  
    }
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T21:12:29Z",
  
      "value": 0.38222174657550045
  
    }
  
  },
  
  "nominalDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T02:54:30Z",
  
      "value": 0.0408320640034282
  
    }
  
  },
  
  "numberOfCircuits": 0.7792295738277125,
  
  "numberOfRows": 0.2682132970916634,
  
  "outsideDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T07:55:24Z",
  
      "value": 0.7194081859650397
  
    }
  
  },
  
  "staggeredRowSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T08:57:05Z",
  
      "value": 0.31167087959205464
  
    }
  
  },
  
  "thermalConductivity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin/Watt",
  
      "observedAt": "2023-01-26T09:16:56Z",
  
      "value": 0.9198905188483331
  
    }
  
  },
  
  "verticalSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T19:06:31Z",
  
      "value": 0.8194554788890942
  
    }
  
  },
  
  "volumen": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T04:19:47Z",
  
      "value": 0.7779813380010603
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:a13d415e-6116-43c4-a668-24f7dbf86bc1",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6946c181-2515-406c-82f2-6bad063d7f8b",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:8f497d54-7104-4546-8fa1-51c409c2b446",
  
    "urn:ngsi-ld:System:adfb1f0e-a324-45c4-be4c-1127ac06e4ed",
  
    "urn:ngsi-ld:System:614b0bb1-d2d9-425f-a7b1-4063e2ba74fa"
  
  ],
  
  "hasManufacturer": "TubeBundle Company Inc.",
  
  "hasModel": "TubeBundle 0.1.2",
  
  "dateCreated": "2023-01-26T00:58:36Z",
  
  "dateModified": "2023-01-26T10:38:11Z",
  
  "source": "Import",
  
  "name": "TubeBundle",
  
  "alternateName": "TubeBundle type 2",
  
  "description": "TubeBundle of limited TubeBundle types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### TubeBundle NGSI-v2 normalized Example    

Here is an example of a TubeBundle in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:TubeBundle:75ab66ce-2623-41a5-884f-ed9b90bde563",
  
  "type": "TubeBundle",
  
  "foulingFactor": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin/Watt",
  
      "observedAt": "2023-01-26T09:18:06Z",
  
      "value": 0.10691025901902518
  
    }
  
  },
  
  "hasTurbulator": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "horizontalSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T20:41:28Z",
  
      "value": 0.5021481278695225
  
    }
  
  },
  
  "inLineRowSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T07:49:23Z",
  
      "value": 0.7015738944986649
  
    }
  
  },
  
  "insideDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T03:11:48Z",
  
      "value": 0.47609748066140833
  
    }
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T01:42:58Z",
  
      "value": 0.6920310151935178
  
    }
  
  },
  
  "nominalDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:21:16Z",
  
      "value": 0.7019643160884628
  
    }
  
  },
  
  "numberOfCircuits": {
  
    "type": "Float",
  
    "value": 0.2146661280911759
  
  },
  
  "numberOfRows": {
  
    "type": "Float",
  
    "value": 0.7182471012018697
  
  },
  
  "outsideDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T14:10:18Z",
  
      "value": 0.41939698462727526
  
    }
  
  },
  
  "staggeredRowSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T18:40:05Z",
  
      "value": 0.39127220946141616
  
    }
  
  },
  
  "thermalConductivity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin/Watt",
  
      "observedAt": "2023-01-25T23:46:09Z",
  
      "value": 0.9507857927588059
  
    }
  
  },
  
  "verticalSpacing": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T11:13:51Z",
  
      "value": 0.08491295072422345
  
    }
  
  },
  
  "volumen": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T09:47:18Z",
  
      "value": 0.16253433369725145
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:e03ce9ef-23a6-4ad9-a533-a960cec73dbe"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:1c71e6d7-68ef-4a8d-9fde-985758f88344"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:c9a9c176-b562-42b7-ad80-cc8db2093faa"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:63e522a0-7de4-4bd9-9f94-094efdf565dc"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:0eebd7dc-010a-4f91-a4d1-da8b2a153b7b"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "TubeBundle Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "TubeBundle 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T11:52:01.9956382+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T07:18:26.9100211+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "TubeBundle"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "TubeBundle type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "TubeBundle of limited TubeBundle types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### TubeBundle NGSI-LD key-values Example    

Here is an example of a TubeBundle in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:TubeBundle:3d9cf58c-8541-4f9c-ab28-8a9a71eb93b7",
  
  "type": "TubeBundle",
  
  "foulingFactor": {
  
    "type": "Measurement",
  
    "unitCode": "Kelvin/Watt",
  
    "observedAt": "2023-01-26T12:10:39Z",
  
    "value": 0.07035577955713379
  
  },
  
  "hasTurbulator": false,
  
  "horizontalSpacing": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T19:59:37Z",
  
    "value": 0.699367667246569
  
  },
  
  "inLineRowSpacing": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T17:13:47Z",
  
    "value": 0.9856093461858647
  
  },
  
  "insideDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T23:11:08Z",
  
    "value": 0.8387693228957287
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T06:42:28Z",
  
    "value": 0.6932469571910904
  
  },
  
  "nominalDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T10:07:52Z",
  
    "value": 0.8670889710747448
  
  },
  
  "numberOfCircuits": 0.3978689426687194,
  
  "numberOfRows": 0.21982583053859828,
  
  "outsideDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T18:43:44Z",
  
    "value": 0.23584755503635035
  
  },
  
  "staggeredRowSpacing": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T21:32:13Z",
  
    "value": 0.7063021172112042
  
  },
  
  "thermalConductivity": {
  
    "type": "Measurement",
  
    "unitCode": "Kelvin/Watt",
  
    "observedAt": "2023-01-26T01:06:27Z",
  
    "value": 0.27916188141902554
  
  },
  
  "verticalSpacing": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T10:09:43Z",
  
    "value": 0.48237642360581057
  
  },
  
  "volumen": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T04:13:14Z",
  
    "value": 0.9530989893727094
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:b4e14c83-5357-4d9d-a292-68c33025ffc5",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:8bd5a80f-11aa-480f-ab18-9c089e3a2637",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:791a033e-49c7-4e16-a1ee-d68aec7a6e3c",
  
    "urn:ngsi-ld:System:d0a612c1-f69f-4194-b943-50359d5d8fa7",
  
    "urn:ngsi-ld:System:cf2b516a-a785-49c7-b4e5-028058bad0a2"
  
  ],
  
  "hasManufacturer": "TubeBundle Company Inc.",
  
  "hasModel": "TubeBundle 0.1.2",
  
  "dateCreated": "2023-01-26T09:24:39Z",
  
  "dateModified": "2023-01-26T00:37:37Z",
  
  "source": "Import",
  
  "name": "TubeBundle",
  
  "alternateName": "TubeBundle type 2",
  
  "description": "TubeBundle of limited TubeBundle types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### TubeBundle NGSI-LD normalized Example    

Here is an example of a TubeBundle in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:TubeBundle:e896fec0-f21f-4fa6-a73b-274bb42fb0fe",
  
  "type": "TubeBundle",
  
  "foulingFactor": {
  
    "type": "Property",
  
    "unitCode": "Kelvin/Watt",
  
    "observedAt": "2023-01-25T15:34:45Z",
  
    "value": 0.7896142805113859
  
  },
  
  "hasTurbulator": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "horizontalSpacing": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T18:38:27Z",
  
    "value": 0.9299315212283089
  
  },
  
  "inLineRowSpacing": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T04:15:23Z",
  
    "value": 0.12680136540868248
  
  },
  
  "insideDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T12:46:46Z",
  
    "value": 0.9063711005346757
  
  },
  
  "length": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T15:58:18Z",
  
    "value": 0.5121996408910179
  
  },
  
  "nominalDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T05:13:10Z",
  
    "value": 0.8209837702761213
  
  },
  
  "numberOfCircuits": {
  
    "type": "Property",
  
    "value": 0.253153343197542
  
  },
  
  "numberOfRows": {
  
    "type": "Property",
  
    "value": 0.69547957104902
  
  },
  
  "outsideDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T07:32:26Z",
  
    "value": 0.7479684351740756
  
  },
  
  "staggeredRowSpacing": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T08:06:42Z",
  
    "value": 0.2757631103143954
  
  },
  
  "thermalConductivity": {
  
    "type": "Property",
  
    "unitCode": "Kelvin/Watt",
  
    "observedAt": "2023-01-25T15:39:27Z",
  
    "value": 0.28193770602031487
  
  },
  
  "verticalSpacing": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T06:27:04Z",
  
    "value": 0.7886025280565963
  
  },
  
  "volumen": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T05:29:35Z",
  
    "value": 0.6238667384353597
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:4943f440-65d7-4fe4-834f-140d786124af"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:6b66c26d-c9a9-4e59-ba5f-5a17174fa9da"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:721e7dae-913a-4e6e-989b-30d545a7ec3d"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:c6a87a94-a7c7-4c31-9b33-6f3ad7861cd0"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:205f1bbb-6bff-422a-9121-4c30a002dfe3"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "TubeBundle Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "TubeBundle 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T21:28:33Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T00:41:51Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "TubeBundle"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "TubeBundle type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "TubeBundle of limited TubeBundle types"
  
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

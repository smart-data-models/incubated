[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Filter  
==============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Filter/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A filter is an apparatus used to remove particulate or gaseous matter from fluids and gases.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `finalResistance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `fluidFlowRateMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `fluidFlowRateMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `initialResistance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalFilterFaceVelocity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalFlowRate`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalMediaSurfaceVelocity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalParticleGeometricMeanDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalParticleGeometricStandardDeviation`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalPressureDrop`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Filter`.  
- `weight`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Filter:
    
  description: A filter is an apparatus used to remove particulate or gaseous matter from fluids and gases.
    
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
    
    finalResistance:
    
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
    
    fluidFlowRateMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    fluidFlowRateMin:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
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
    
    initialResistance:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
                thttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    nominalFilterFaceVelocity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalFlowRate:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalMediaSurfaceVelocity:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalParticleGeometricMeanDiameter:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalParticleGeometricStandardDeviation:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalPressureDrop:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMin:
    
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
    
      description: It must be equal to `Filter`.
    
      enum:
    
        - Filter
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    weight:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Filter/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Filters/Filter
    
  x-model-tags: SAREF Filter SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Filter NGSI-v2 key-values Example    

Here is an example of a Filter in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Filter:cab351de-0353-4d67-ba3e-f8e496fff6ee",
  
  "type": "Filter",
  
  "finalResistance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T23:54:28Z",
  
      "value": 0.046716566596463616
  
    }
  
  },
  
  "fluidFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T18:15:28Z",
  
      "value": 0.5234640867427633
  
    }
  
  },
  
  "fluidFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T12:34:34Z",
  
      "value": 0.88979941896976
  
    }
  
  },
  
  "initialResistance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T02:23:16Z",
  
      "value": 0.9155546427779283
  
    }
  
  },
  
  "nominalFilterFaceVelocity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m/s",
  
      "observedAt": "2023-01-25T21:01:30Z",
  
      "value": 0.6586465369680704
  
    }
  
  },
  
  "nominalFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T22:28:26Z",
  
      "value": 0.08419722940470808
  
    }
  
  },
  
  "nominalMediaSurfaceVelocity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m/s",
  
      "observedAt": "2023-01-25T23:47:57Z",
  
      "value": 0.2909288017995001
  
    }
  
  },
  
  "nominalParticleGeometricMeanDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:43:04Z",
  
      "value": 0.25048971083477223
  
    }
  
  },
  
  "nominalParticleGeometricStandardDeviation": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T18:02:12Z",
  
      "value": 0.6860967233212114
  
    }
  
  },
  
  "nominalPressureDrop": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T01:40:31Z",
  
      "value": 0.4382746309750293
  
    }
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T07:09:18Z",
  
      "value": 0.41660145070952037
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T05:51:36Z",
  
      "value": 0.7951736951400654
  
    }
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-26T11:27:44Z",
  
      "value": 0.9846229044529057
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:0f3368a3-5989-4693-b29e-37aaa17be464",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:78c5cc6c-d740-45dd-968c-43361a780e2c",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c57a69ec-9b26-4933-b4ce-580e5edb9b72",
  
    "urn:ngsi-ld:System:0132ad74-ea74-4d20-b0d0-bb4fa1a19af9",
  
    "urn:ngsi-ld:System:be24c623-c5c4-4da0-b4ea-552cb1d31a71"
  
  ],
  
  "hasManufacturer": "Filter Company Inc.",
  
  "hasModel": "Filter 0.1.2",
  
  "dateCreated": "2023-01-26T06:33:09Z",
  
  "dateModified": "2023-01-26T13:51:08Z",
  
  "source": "Import",
  
  "name": "Filter",
  
  "alternateName": "Filter type 2",
  
  "description": "Filter of limited Filter types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Filter NGSI-v2 normalized Example    

Here is an example of a Filter in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Filter:8e80455c-7f89-462c-b1f0-b84c6ac5e5cb",
  
  "type": "Filter",
  
  "finalResistance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T02:20:51Z",
  
      "value": 0.25563353322549653
  
    }
  
  },
  
  "fluidFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T05:40:55Z",
  
      "value": 0.7441450852967011
  
    }
  
  },
  
  "fluidFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T03:50:30Z",
  
      "value": 0.32563792639259326
  
    }
  
  },
  
  "initialResistance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T19:57:00Z",
  
      "value": 0.41032135281652493
  
    }
  
  },
  
  "nominalFilterFaceVelocity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m/s",
  
      "observedAt": "2023-01-25T17:47:50Z",
  
      "value": 0.829815297358211
  
    }
  
  },
  
  "nominalFlowRate": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T16:02:09Z",
  
      "value": 0.569423507213339
  
    }
  
  },
  
  "nominalMediaSurfaceVelocity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m/s",
  
      "observedAt": "2023-01-26T02:37:48Z",
  
      "value": 0.6085640129416107
  
    }
  
  },
  
  "nominalParticleGeometricMeanDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T15:18:05Z",
  
      "value": 0.9736709365602062
  
    }
  
  },
  
  "nominalParticleGeometricStandardDeviation": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T04:01:46Z",
  
      "value": 0.5284993250186989
  
    }
  
  },
  
  "nominalPressureDrop": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T23:59:10Z",
  
      "value": 0.4856470985811685
  
    }
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T02:51:37Z",
  
      "value": 0.04450158146401939
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T23:23:38Z",
  
      "value": 0.28211808830531604
  
    }
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-26T05:24:47Z",
  
      "value": 0.5157014658259989
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:4468726f-7faa-4e8e-802e-337b7d4e2c38"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:a263b3b0-a5d7-4e38-a95f-75dd868ea6aa"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:118a0d61-bba3-416e-a770-5ac45dfb66e7"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:a7ba30cc-d8f3-423d-a1d6-284c130befee"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:38485bc5-5ff4-49f1-b6fb-65b815b05795"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Filter Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Filter 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T04:44:52.9377605+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T18:30:35.796352+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Filter"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Filter type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Filter of limited Filter types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Filter NGSI-LD key-values Example    

Here is an example of a Filter in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Filter:0d541c0c-0b96-4fe2-b176-23da3c75543c",
  
  "type": "Filter",
  
  "finalResistance": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T06:14:30Z",
  
    "value": 0.8399485763174174
  
  },
  
  "fluidFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T10:02:55Z",
  
    "value": 0.8283855877251654
  
  },
  
  "fluidFlowRateMin": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T23:06:02Z",
  
    "value": 0.3395849300456041
  
  },
  
  "initialResistance": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T08:40:45Z",
  
    "value": 0.04255175229670349
  
  },
  
  "nominalFilterFaceVelocity": {
  
    "type": "Measurement",
  
    "unitCode": "m/s",
  
    "observedAt": "2023-01-25T15:15:44Z",
  
    "value": 0.019028990059285156
  
  },
  
  "nominalFlowRate": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T21:01:41Z",
  
    "value": 0.702937429469533
  
  },
  
  "nominalMediaSurfaceVelocity": {
  
    "type": "Measurement",
  
    "unitCode": "m/s",
  
    "observedAt": "2023-01-26T01:06:49Z",
  
    "value": 0.21871108718863685
  
  },
  
  "nominalParticleGeometricMeanDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T17:43:06Z",
  
    "value": 0.18412339513530696
  
  },
  
  "nominalParticleGeometricStandardDeviation": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T22:44:10Z",
  
    "value": 0.6259482216441562
  
  },
  
  "nominalPressureDrop": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T11:47:04Z",
  
    "value": 0.8697757847153208
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T17:07:38Z",
  
    "value": 0.4818435270939754
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T21:52:13Z",
  
    "value": 0.2998390404029371
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-25T19:52:01Z",
  
    "value": 0.5349743638443497
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:fd264452-c270-41d6-aa0e-bca37e8c5995",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:a1293bab-a64b-4759-b666-5bdd5d456986",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:341b90cb-63d3-469d-a9fb-78075ad0995a",
  
    "urn:ngsi-ld:System:26b003ff-f309-4d19-a90a-7c88de49aee4",
  
    "urn:ngsi-ld:System:4fde7494-3559-4f5c-a88d-039d742c1050"
  
  ],
  
  "hasManufacturer": "Filter Company Inc.",
  
  "hasModel": "Filter 0.1.2",
  
  "dateCreated": "2023-01-26T04:09:01Z",
  
  "dateModified": "2023-01-25T21:19:18Z",
  
  "source": "Import",
  
  "name": "Filter",
  
  "alternateName": "Filter type 2",
  
  "description": "Filter of limited Filter types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Filter NGSI-LD normalized Example    

Here is an example of a Filter in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Filter:fbeb6c10-5a65-4f37-b472-05630b596d96",
  
  "type": "Filter",
  
  "finalResistance": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T01:00:57Z",
  
    "value": 0.5605621121413891
  
  },
  
  "fluidFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T09:29:26Z",
  
    "value": 0.8457030696896928
  
  },
  
  "fluidFlowRateMin": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T01:24:07Z",
  
    "value": 0.4281237576056126
  
  },
  
  "initialResistance": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T13:16:00Z",
  
    "value": 0.9855925634968424
  
  },
  
  "nominalFilterFaceVelocity": {
  
    "type": "Property",
  
    "unitCode": "m/s",
  
    "observedAt": "2023-01-26T03:08:23Z",
  
    "value": 0.6912281080254741
  
  },
  
  "nominalFlowRate": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T15:48:08Z",
  
    "value": 0.022821238860702198
  
  },
  
  "nominalMediaSurfaceVelocity": {
  
    "type": "Property",
  
    "unitCode": "m/s",
  
    "observedAt": "2023-01-25T22:13:37Z",
  
    "value": 0.5684154129668265
  
  },
  
  "nominalParticleGeometricMeanDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T07:32:19Z",
  
    "value": 0.229698552370729
  
  },
  
  "nominalParticleGeometricStandardDeviation": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T02:48:53Z",
  
    "value": 0.8264025547190669
  
  },
  
  "nominalPressureDrop": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T19:24:30Z",
  
    "value": 0.6662603303962529
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T00:52:23Z",
  
    "value": 0.8600599815414807
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T18:39:35Z",
  
    "value": 0.11197463391152895
  
  },
  
  "weight": {
  
    "type": "Property",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-26T06:38:32Z",
  
    "value": 0.39067890635291025
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:3ad9289e-2153-42f6-821a-e050b0cece56"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:14828a20-966b-491d-8c5d-06e0e9323fe3"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:4f4ca1e9-532c-4518-b84b-92e00d43255a"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:4be15aec-065d-404f-aedd-e477a5a61f23"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7e718726-9abe-49e6-ae69-96d1277a5af0"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Filter Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Filter 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T21:32:07Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T21:47:48Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Filter"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Filter type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Filter of limited Filter types"
  
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

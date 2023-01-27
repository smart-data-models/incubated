[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Transformer  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Transformer/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `apparentPowerMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `imaginaryImpedanceRatio`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isNeutralPrimaryTerminalAvailable`: An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE).  
- `isNeutralSecondaryTerminalAvailable`: An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE).  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `primaryApparentPower`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `primaryCurrent`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `primaryFrequency`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `primaryVoltage`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `realImpedanceRatio`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryApparentPower`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryCurrent`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryCurrentType`: A list of the secondary current types that can result from transformer output.  
- `secondaryFrequency`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `secondaryVoltage`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `transformerVectorGroup`: List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers.  
- `type`: It must be equal to `Transformer`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Transformer:
    
  description: 'A transformer is an inductive stationary device that transfers electrical energy from one circuit to another.  Transformer is used to transform electric power; conversion of electric signals for other purposes is handled at other entities: Controller converts arbitrary signals, AudioVisualAppliance converts signals for audio or video streams, and CommunicationsAppliance converts signals for data or other communications usage.'
    
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
    
    apparentPowerMax:
    
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
    
    imaginaryImpedanceRatio:
    
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
    
    isNeutralPrimaryTerminalAvailable:
    
      description: An indication of whether the neutral point of the primary winding is available as a terminal (=TRUE) or not (= FALSE).
    
      type: boolean
    
      x-ngsi:
    
        type: Property
    
    isNeutralSecondaryTerminalAvailable:
    
      description: An indication of whether the neutral point of the secondary winding is available as a terminal (=TRUE) or not (= FALSE).
    
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
    
          requirehttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    primaryApparentPower:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    primaryCurrent:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    primaryFrequency:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    primaryVoltage:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    realImpedanceRatio:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryApparentPower:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryCurrent:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryCurrentType:
    
      description: A list of the secondary current types that can result from transformer output.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    secondaryFrequency:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    secondaryVoltage:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
    transformerVectorGroup:
    
      description: 'List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter describes how the primary windings are connected, the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees. D: means that the windings are delta-connected. Y: means that the windings are star-connected. Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer). The connectivity is only relevant for three-phase transformers.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `Transformer`.
    
      enum:
    
        - Transformer
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Transformer/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Transformers/Transformer
    
  x-model-tags: SAREF Transformer SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Transformer NGSI-v2 key-values Example    

Here is an example of a Transformer in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Transformer:4976b0ec-0c96-4ae1-91da-c906da8348da",
  
  "type": "Transformer",
  
  "apparentPowerMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T08:33:42Z",
  
      "value": 0.17497838413457267
  
    }
  
  },
  
  "imaginaryImpedanceRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T09:32:31Z",
  
      "value": 0.5323895083879017
  
    }
  
  },
  
  "isNeutralPrimaryTerminalAvailable": false,
  
  "isNeutralSecondaryTerminalAvailable": true,
  
  "primaryApparentPower": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T12:48:38Z",
  
      "value": 0.8765115449298688
  
    }
  
  },
  
  "primaryCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-26T05:19:30Z",
  
      "value": 0.871670986786111
  
    }
  
  },
  
  "primaryFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-26T09:48:01Z",
  
      "value": 0.141749759362659
  
    }
  
  },
  
  "primaryVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-26T02:03:24Z",
  
      "value": 0.5038263292514936
  
    }
  
  },
  
  "realImpedanceRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T04:08:48Z",
  
      "value": 0.06325384828151492
  
    }
  
  },
  
  "secondaryApparentPower": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T23:19:23Z",
  
      "value": 0.45704946090246745
  
    }
  
  },
  
  "secondaryCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-25T17:56:32Z",
  
      "value": 0.4016609926228465
  
    }
  
  },
  
  "secondaryCurrentType": "Data",
  
  "secondaryFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-25T16:24:09Z",
  
      "value": 0.7436141485906284
  
    }
  
  },
  
  "secondaryVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-26T06:59:27Z",
  
      "value": 0.4646450009162978
  
    }
  
  },
  
  "transformerVectorGroup": "Soft",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51645089-5e36-4b9c-ad25-b97b58506919",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:6737e804-54ff-41c0-ba12-90dde24f3d59",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:38dfdf15-5a41-412d-9b05-435cb7809e6f",
  
    "urn:ngsi-ld:System:b7274b46-33ec-4694-8dda-999197bb58c5",
  
    "urn:ngsi-ld:System:b7d5c2ce-fc23-42d0-be8f-9e56a9f3c5db"
  
  ],
  
  "hasManufacturer": "Transformer Company Inc.",
  
  "hasModel": "Transformer 0.1.2",
  
  "dateCreated": "2023-01-25T16:42:43Z",
  
  "dateModified": "2023-01-26T13:53:42Z",
  
  "source": "Import",
  
  "name": "Transformer",
  
  "alternateName": "Transformer type 2",
  
  "description": "Transformer of limited Transformer types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Transformer NGSI-v2 normalized Example    

Here is an example of a Transformer in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Transformer:7dc130e2-e429-4c26-b467-ec9d1f41e7b8",
  
  "type": "Transformer",
  
  "apparentPowerMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T02:59:49Z",
  
      "value": 0.6561932522421066
  
    }
  
  },
  
  "imaginaryImpedanceRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T20:35:35Z",
  
      "value": 0.7913482963385954
  
    }
  
  },
  
  "isNeutralPrimaryTerminalAvailable": {
  
    "type": "Boolean",
  
    "value": true
  
  },
  
  "isNeutralSecondaryTerminalAvailable": {
  
    "type": "Boolean",
  
    "value": true
  
  },
  
  "primaryApparentPower": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T11:11:14Z",
  
      "value": 0.23470397848013025
  
    }
  
  },
  
  "primaryCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-26T01:03:52Z",
  
      "value": 0.7245530289719985
  
    }
  
  },
  
  "primaryFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-26T01:17:24Z",
  
      "value": 0.18927842693402908
  
    }
  
  },
  
  "primaryVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-25T16:44:31Z",
  
      "value": 0.359590276424793
  
    }
  
  },
  
  "realImpedanceRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T00:10:23Z",
  
      "value": 0.6917590580595899
  
    }
  
  },
  
  "secondaryApparentPower": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T01:10:18Z",
  
      "value": 0.10075664755263747
  
    }
  
  },
  
  "secondaryCurrent": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "A",
  
      "observedAt": "2023-01-26T11:42:14Z",
  
      "value": 0.1458215404162363
  
    }
  
  },
  
  "secondaryCurrentType": {
  
    "type": "Text",
  
    "value": "Tasty Wooden Car"
  
  },
  
  "secondaryFrequency": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Hz",
  
      "observedAt": "2023-01-25T21:14:51Z",
  
      "value": 0.09146741937660052
  
    }
  
  },
  
  "secondaryVoltage": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "W/A",
  
      "observedAt": "2023-01-26T07:23:51Z",
  
      "value": 0.31779800995261864
  
    }
  
  },
  
  "transformerVectorGroup": {
  
    "type": "Text",
  
    "value": "SMS"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:16bccee7-8244-4707-8d4b-c5a06b0fee75"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:b9a1bd5e-114e-41ba-b865-25b4b4c5c3c5"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:37554df5-ec0d-4e03-8697-7d562ff2134f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:e967a169-474b-47a0-bd0c-a76ce8a5f7be"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:49a6b09b-2301-4b6e-a167-54ee44cc83d4"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Transformer Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Transformer 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T20:08:21.2034652+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T22:13:38.7837862+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Transformer"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Transformer type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Transformer of limited Transformer types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Transformer NGSI-LD key-values Example    

Here is an example of a Transformer in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Transformer:4e1020b7-d856-45ae-80c7-4ef488822f9b",
  
  "type": "Transformer",
  
  "apparentPowerMax": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T06:50:52Z",
  
    "value": 0.5894536387551085
  
  },
  
  "imaginaryImpedanceRatio": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T16:24:59Z",
  
    "value": 0.5080873904531445
  
  },
  
  "isNeutralPrimaryTerminalAvailable": true,
  
  "isNeutralSecondaryTerminalAvailable": false,
  
  "primaryApparentPower": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T06:32:13Z",
  
    "value": 0.6021497226791174
  
  },
  
  "primaryCurrent": {
  
    "type": "Measurement",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-25T18:09:17Z",
  
    "value": 0.9872256682386402
  
  },
  
  "primaryFrequency": {
  
    "type": "Measurement",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-26T07:42:52Z",
  
    "value": 0.5455371504431572
  
  },
  
  "primaryVoltage": {
  
    "type": "Measurement",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-25T15:02:29Z",
  
    "value": 0.3974626573299226
  
  },
  
  "realImpedanceRatio": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T09:24:30Z",
  
    "value": 0.6431631160150683
  
  },
  
  "secondaryApparentPower": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T20:16:28Z",
  
    "value": 0.6523948450188477
  
  },
  
  "secondaryCurrent": {
  
    "type": "Measurement",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-26T05:10:27Z",
  
    "value": 0.66394001364198
  
  },
  
  "secondaryCurrentType": "HDD",
  
  "secondaryFrequency": {
  
    "type": "Measurement",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-26T08:00:39Z",
  
    "value": 0.31162563839919877
  
  },
  
  "secondaryVoltage": {
  
    "type": "Measurement",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-25T17:55:22Z",
  
    "value": 0.6234465756290085
  
  },
  
  "transformerVectorGroup": "Colorado",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:9137cef1-e0b5-4ed9-b068-2cae7b1c4c32",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7a230c87-9b85-4ba0-980f-35f48ab5cf75",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:70026ed1-253b-478f-94bf-026f9dcaf14f",
  
    "urn:ngsi-ld:System:ca1ebf13-745d-4276-9285-f4c1b7836ebc",
  
    "urn:ngsi-ld:System:87f75d91-6637-4d64-841e-327d77121143"
  
  ],
  
  "hasManufacturer": "Transformer Company Inc.",
  
  "hasModel": "Transformer 0.1.2",
  
  "dateCreated": "2023-01-25T16:38:09Z",
  
  "dateModified": "2023-01-26T00:54:00Z",
  
  "source": "Import",
  
  "name": "Transformer",
  
  "alternateName": "Transformer type 2",
  
  "description": "Transformer of limited Transformer types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Transformer NGSI-LD normalized Example    

Here is an example of a Transformer in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Transformer:24b95122-4055-44dc-82ad-09a2bcda9025",
  
  "type": "Transformer",
  
  "apparentPowerMax": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T20:30:38Z",
  
    "value": 0.24466523496915848
  
  },
  
  "imaginaryImpedanceRatio": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T00:56:06Z",
  
    "value": 0.0034198103714959682
  
  },
  
  "isNeutralPrimaryTerminalAvailable": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "isNeutralSecondaryTerminalAvailable": {
  
    "type": "Property",
  
    "value": true
  
  },
  
  "primaryApparentPower": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T12:47:55Z",
  
    "value": 0.9141641275735504
  
  },
  
  "primaryCurrent": {
  
    "type": "Property",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-26T04:09:04Z",
  
    "value": 0.21921580436899846
  
  },
  
  "primaryFrequency": {
  
    "type": "Property",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-26T11:27:17Z",
  
    "value": 0.8873577584995188
  
  },
  
  "primaryVoltage": {
  
    "type": "Property",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-26T07:23:40Z",
  
    "value": 0.33421317836814646
  
  },
  
  "realImpedanceRatio": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T03:38:23Z",
  
    "value": 0.6061321069719529
  
  },
  
  "secondaryApparentPower": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T19:57:55Z",
  
    "value": 0.3997980055591537
  
  },
  
  "secondaryCurrent": {
  
    "type": "Property",
  
    "unitCode": "A",
  
    "observedAt": "2023-01-26T13:58:27Z",
  
    "value": 0.2899846616898377
  
  },
  
  "secondaryCurrentType": {
  
    "type": "Property",
  
    "value": "human-resource"
  
  },
  
  "secondaryFrequency": {
  
    "type": "Property",
  
    "unitCode": "Hz",
  
    "observedAt": "2023-01-26T03:39:16Z",
  
    "value": 0.06983160765779406
  
  },
  
  "secondaryVoltage": {
  
    "type": "Property",
  
    "unitCode": "W/A",
  
    "observedAt": "2023-01-26T07:19:14Z",
  
    "value": 0.8594539881916403
  
  },
  
  "transformerVectorGroup": {
  
    "type": "Property",
  
    "value": "digital"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:ded8c891-dfe1-4973-966c-96ab6231373d"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:aab67381-2a15-4bdc-ab0f-953b17253b8f"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:d06b6674-162c-4593-a8fd-3874ef353008"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:d0aca3bd-bf1b-4e9e-a998-a76c9b1ac7a6"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:1ab049a0-7295-4eef-82a1-0bb422132435"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Transformer Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Transformer 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T06:32:52Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T05:11:11Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Transformer"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Transformer type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Transformer of limited Transformer types"
  
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

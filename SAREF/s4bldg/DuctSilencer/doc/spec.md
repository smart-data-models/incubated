[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: DuctSilencer  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/DuctSilencer/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A duct silencer is a device that is typically installed inside a duct distribution system for the purpose of reducing the noise levels from air movement, fan noise, etc. in the adjacent space or downstream of the duct silencer device.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `airFlowRateMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `airFlowRateMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasExteriorInsulation`: TRUE if the silencer has exterior insulation. FALSE if it does not.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hydraulicDiameter`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `length`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `DuctSilencer`.  
- `weight`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `workingPressureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `workingPressureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
DuctSilencer:
    
  description: 'A duct silencer is a device that is typically installed inside a duct distribution system for the purpose of reducing the noise levels from air movement, fan noise, etc. in the adjacent space or downstream of the duct silencer device.'
    
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
    
    airFlowRateMax:
    
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
    
    airFlowRateMin:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
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
    
    hasExteriorInsulation:
    
      description: TRUE if the silencer has exterior insulation. FALSE if it does not.
    
      type: boolean
    
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
    
    hydraulicDiameter:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
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
    
          requirehttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
      description: It must be equal to `DuctSilencer`.
    
      enum:
    
        - DuctSilencer
    
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
    
    workingPressureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    workingPressureMin:
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/DuctSilencer/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/DuctSilencers/DuctSilencer
    
  x-model-tags: SAREF DuctSilencer SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### DuctSilencer NGSI-v2 key-values Example    

Here is an example of a DuctSilencer in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:DuctSilencer:439e7a92-6ff4-4b8b-94fa-cefa9b8cc9a2",
  
  "type": "DuctSilencer",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T07:36:00Z",
  
      "value": 0.1608748792870458
  
    }
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T12:39:36Z",
  
      "value": 0.5144201035637935
  
    }
  
  },
  
  "hasExteriorInsulation": true,
  
  "hydraulicDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T12:25:13Z",
  
      "value": 0.655988670157379
  
    }
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:50:50Z",
  
      "value": 0.6761801102701772
  
    }
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T15:43:08Z",
  
      "value": 0.9108707788637439
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T13:41:41Z",
  
      "value": 0.38034850956825317
  
    }
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-26T07:52:47Z",
  
      "value": 0.3440451194010431
  
    }
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T09:39:40Z",
  
      "value": 0.4689060124065172
  
    }
  
  },
  
  "workingPressureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-25T16:06:07Z",
  
      "value": 0.6786833167445696
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:35cd1a8e-8ad6-4cd0-9a0c-4270a9cf8680",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:3ba75bf1-2b1d-4988-bf7d-2000b44b87ab",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:7dd27551-56f1-4c2b-b094-f490114a721e",
  
    "urn:ngsi-ld:System:b6550f33-a522-4632-81e4-dcd4c08d3229",
  
    "urn:ngsi-ld:System:68691c7c-07b2-4009-ae84-c326a9e32071"
  
  ],
  
  "hasManufacturer": "DuctSilencer Company Inc.",
  
  "hasModel": "DuctSilencer 0.1.2",
  
  "dateCreated": "2023-01-26T11:03:15Z",
  
  "dateModified": "2023-01-26T06:10:02Z",
  
  "source": "Import",
  
  "name": "DuctSilencer",
  
  "alternateName": "DuctSilencer type 2",
  
  "description": "DuctSilencer of limited DuctSilencer types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### DuctSilencer NGSI-v2 normalized Example    

Here is an example of a DuctSilencer in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:DuctSilencer:354bc2c9-fe84-4b86-870e-b4bb0f421e14",
  
  "type": "DuctSilencer",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T19:27:11Z",
  
      "value": 0.42241788558074733
  
    }
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T03:57:31Z",
  
      "value": 0.3750532258722393
  
    }
  
  },
  
  "hasExteriorInsulation": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "hydraulicDiameter": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T21:41:23Z",
  
      "value": 0.28893264554968967
  
    }
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T04:54:33Z",
  
      "value": 0.8546214350560009
  
    }
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T22:55:22Z",
  
      "value": 0.5534860278496251
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T03:27:13Z",
  
      "value": 0.8929827048351656
  
    }
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "g",
  
      "observedAt": "2023-01-25T22:05:28Z",
  
      "value": 0.6856055430291446
  
    }
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T03:41:15Z",
  
      "value": 0.28889395933436934
  
    }
  
  },
  
  "workingPressureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T05:08:58Z",
  
      "value": 0.5603647437955193
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:2e17ab63-5c61-4d14-90a2-6d9c2f96681d"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:edc1a584-5b19-4244-b872-001cf887a7d7"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:749d1fd1-6e00-4d22-96f6-aec2dda0e494"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:6e1df1b9-fdec-4c73-9a85-f28b88014ec8"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:b6ffa288-5b86-40d9-90d7-5fb8b8dc7f02"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "DuctSilencer Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "DuctSilencer 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T14:45:14.4588565+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T11:59:21.5030067+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "DuctSilencer"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "DuctSilencer type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "DuctSilencer of limited DuctSilencer types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### DuctSilencer NGSI-LD key-values Example    

Here is an example of a DuctSilencer in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:DuctSilencer:a5eeddc4-e629-4494-8606-6e26ce54e8d7",
  
  "type": "DuctSilencer",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T06:32:25Z",
  
    "value": 0.7486822537806592
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T16:15:45Z",
  
    "value": 0.9706518431987116
  
  },
  
  "hasExteriorInsulation": false,
  
  "hydraulicDiameter": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T09:41:36Z",
  
    "value": 0.158744712686386
  
  },
  
  "length": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T01:29:17Z",
  
    "value": 0.7843003056454052
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T17:23:53Z",
  
    "value": 0.5975437821550035
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T12:05:50Z",
  
    "value": 0.9663325232283431
  
  },
  
  "weight": {
  
    "type": "Measurement",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-25T20:02:32Z",
  
    "value": 0.8392772958946368
  
  },
  
  "workingPressureMax": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T14:08:31Z",
  
    "value": 0.12806771779201687
  
  },
  
  "workingPressureMin": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T01:04:22Z",
  
    "value": 0.6248807399586069
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:d88211d3-c97b-4136-9898-525d933a5a7a",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:04bfee8d-ff54-40f8-aeb0-d591285c335e",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:038181a2-ebd5-4405-9780-0d6331630efe",
  
    "urn:ngsi-ld:System:57de563e-fa66-4922-8fe1-3d5535d45771",
  
    "urn:ngsi-ld:System:d5bbb554-2442-4643-a0b2-8100f1f5de62"
  
  ],
  
  "hasManufacturer": "DuctSilencer Company Inc.",
  
  "hasModel": "DuctSilencer 0.1.2",
  
  "dateCreated": "2023-01-25T21:14:21Z",
  
  "dateModified": "2023-01-25T15:30:18Z",
  
  "source": "Import",
  
  "name": "DuctSilencer",
  
  "alternateName": "DuctSilencer type 2",
  
  "description": "DuctSilencer of limited DuctSilencer types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### DuctSilencer NGSI-LD normalized Example    

Here is an example of a DuctSilencer in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:DuctSilencer:f2f44b77-d3ee-4ab4-bd1a-1c476f674549",
  
  "type": "DuctSilencer",
  
  "airFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T19:54:39Z",
  
    "value": 0.5746033930246481
  
  },
  
  "airFlowRateMin": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T21:24:51Z",
  
    "value": 0.6010968836956997
  
  },
  
  "hasExteriorInsulation": {
  
    "type": "Property",
  
    "value": true
  
  },
  
  "hydraulicDiameter": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T17:57:38Z",
  
    "value": 0.6623416028707915
  
  },
  
  "length": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T15:21:41Z",
  
    "value": 0.9676732407508329
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T11:39:38Z",
  
    "value": 0.56707910867758
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T09:06:00Z",
  
    "value": 0.7219158816538178
  
  },
  
  "weight": {
  
    "type": "Property",
  
    "unitCode": "g",
  
    "observedAt": "2023-01-25T21:05:44Z",
  
    "value": 0.6644043164355533
  
  },
  
  "workingPressureMax": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T04:07:57Z",
  
    "value": 0.058329572403388985
  
  },
  
  "workingPressureMin": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T23:17:06Z",
  
    "value": 0.10711886041657781
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:0addac31-ddff-4a11-97a1-e9411907e554"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:ac4f9960-3415-4943-a490-81859df172a4"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:a182c79d-ec15-4bfb-9b22-b0db74eac23e"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:f429ad1b-2285-441f-9305-8de0017d3b4c"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:d1dfe74b-ef79-4c61-be03-d1617663f8c4"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "DuctSilencer Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "DuctSilencer 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T01:07:55Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T12:16:22Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "DuctSilencer"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "DuctSilencer type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "DuctSilencer of limited DuctSilencer types"
  
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

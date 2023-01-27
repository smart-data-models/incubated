[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Boiler  
==============https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Boiler/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A boiler is a closed, pressure-rated vessel in which water or other fluid is heated using an energy source such as natural gas, heating oil, or electricity. The fluid in the vessel is then circulated out of the boiler for use in various processes or heating applications.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `energySource`: The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `heatTransferSurfaceArea`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `isWaterStorageHeater`: This is used to identify if the boiler has storage capacity (TRUE). If FALSE, then there is no storage capacity built into the boiler, such as an instantaneous hot water heater.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalEnergyConsumption`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalPartLoadRatio`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operatingMode`: Identifies the operating mode of the boiler.  
- `outletTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `outletTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `pressureRating`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Boiler`.  
- `waterInletTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `waterInletTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `waterStorageCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Boiler:
    
  description: 'A boiler is a closed, pressure-rated vessel in which water or other fluid is heated using an energy source such as natural gas, heating oil, or electricity. The fluid in the vessel is then circulated out of the boiler for use in various processes or heating applications.'
    
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
    
    energySource:
    
      description: The source of energy. Enumeration defining the energy source or fuel cumbusted to generate heat.
    
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
    
    heatTransferSurfaceArea:
    
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
    
    isWaterStorageHeater:
    
      description: 'This is used to identify if the boiler has storage capacity (TRUE). If FALSE, then there is no storage capacity built into the boiler, such as an instantaneous hot water heater.'
    
      type: boolean
    
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
    
              typhttps://github.com/smart-data-models/incubated/SAREF/
    
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
    
    nominalEnergyConsumption:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalPartLoadRatio:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operatingMode:
    
      description: Identifies the operating mode of the boiler.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    outletTemperatureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    outletTemperatureMin:
    
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
    
    pressureRating:
    
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
    
    type:
    
      description: It must be equal to `Boiler`.
    
      enum:
    
        - Boiler
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    waterInletTemperatureMax:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    waterInletTemperatureMin:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    waterStorageCapacity:
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Boiler/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Boilers/Boiler
    
  x-model-tags: SAREF Boiler SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Boiler NGSI-v2 key-values Example    

Here is an example of a Boiler in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Boiler:724c2f67-e55e-4971-8e74-55d6ecfa19c9",
  
  "type": "Boiler",
  
  "energySource": "United States of America",
  
  "heatTransferSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T04:12:40Z",
  
      "value": 0.7853344933267346
  
    }
  
  },
  
  "isWaterStorageHeater": false,
  
  "nominalEnergyConsumption": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T21:04:40Z",
  
      "value": 0.6203749662936422
  
    }
  
  },
  
  "nominalPartLoadRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T02:52:18Z",
  
      "value": 0.8015670647257737
  
    }
  
  },
  
  "operatingMode": "systems",
  
  "outletTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T15:45:25Z",
  
      "value": 0.16008580907721015
  
    }
  
  },
  
  "outletTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T12:59:57Z",
  
      "value": 0.04227267769006804
  
    }
  
  },
  
  "pressureRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T04:27:26Z",
  
      "value": 0.5113599213422801
  
    }
  
  },
  
  "waterInletTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T21:53:34Z",
  
      "value": 0.9011788947791837
  
    }
  
  },
  
  "waterInletTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T23:01:55Z",
  
      "value": 0.24858493133262038
  
    }
  
  },
  
  "waterStorageCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T09:48:11Z",
  
      "value": 0.5276371515431508
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:50afbc21-cf0f-4f69-b48a-47af5a287d38",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f2bfaa08-a201-40bd-b1b3-fe5a4ba5d291",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:1cfd3123-93fa-408a-a750-dd5a6f0edcae",
  
    "urn:ngsi-ld:System:fec748f9-6ee5-49af-93a4-5bffcc20e73c",
  
    "urn:ngsi-ld:System:5ee8058b-c872-4237-9c94-82f22172c39e"
  
  ],
  
  "hasManufacturer": "Boiler Company Inc.",
  
  "hasModel": "Boiler 0.1.2",
  
  "dateCreated": "2023-01-26T09:03:19Z",
  
  "dateModified": "2023-01-25T16:09:21Z",
  
  "source": "Import",
  
  "name": "Boiler",
  
  "alternateName": "Boiler type 2",
  
  "description": "Boiler of limited Boiler types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Boiler NGSI-v2 normalized Example    

Here is an example of a Boiler in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Boiler:554e6cfc-a12b-466b-bdb5-251db87de147",
  
  "type": "Boiler",
  
  "energySource": {
  
    "type": "Text",
  
    "value": "Coordinator"
  
  },
  
  "heatTransferSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T14:12:58Z",
  
      "value": 0.054241651152424186
  
    }
  
  },
  
  "isWaterStorageHeater": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "nominalEnergyConsumption": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T04:23:54Z",
  
      "value": 0.015349430439582035
  
    }
  
  },
  
  "nominalPartLoadRatio": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T20:50:23Z",
  
      "value": 0.15224995605259972
  
    }
  
  },
  
  "operatingMode": {
  
    "type": "Text",
  
    "value": "bypass"
  
  },
  
  "outletTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T05:27:07Z",
  
      "value": 0.6702304071347284
  
    }
  
  },
  
  "outletTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-25T21:00:30Z",
  
      "value": 0.5096152218274909
  
    }
  
  },
  
  "pressureRating": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "N/m2",
  
      "observedAt": "2023-01-26T06:44:28Z",
  
      "value": 0.5974774605306619
  
    }
  
  },
  
  "waterInletTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T08:33:01Z",
  
      "value": 0.9398884749677864
  
    }
  
  },
  
  "waterInletTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T00:19:46Z",
  
      "value": 0.4089735417040705
  
    }
  
  },
  
  "waterStorageCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T15:47:24Z",
  
      "value": 0.9413886423074906
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:ab8a7d6f-040b-4eb8-b6ea-f238a2ccc065"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:668e5ccf-c66c-43ea-ad8d-fca6862f3d04"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:2c2904e8-d4fa-4191-8b1b-4e06eaed77ff"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:820d0fb3-9cb6-4bc4-b706-515d91e3343f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:a0370269-07a5-4bad-a6c0-15a382a279ce"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Boiler Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Boiler 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T10:00:09.4580486+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T18:35:13.9392676+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Boiler"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Boiler type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Boiler of limited Boiler types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Boiler NGSI-LD key-values Example    

Here is an example of a Boiler in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Boiler:6e58418b-d599-437a-8058-30cec75dab8e",
  
  "type": "Boiler",
  
  "energySource": "markets",
  
  "heatTransferSurfaceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T20:47:02Z",
  
    "value": 0.966477257993463
  
  },
  
  "isWaterStorageHeater": false,
  
  "nominalEnergyConsumption": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T00:53:28Z",
  
    "value": 0.5218922296312083
  
  },
  
  "nominalPartLoadRatio": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T21:34:31Z",
  
    "value": 0.9451650427330754
  
  },
  
  "operatingMode": "system",
  
  "outletTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T22:32:20Z",
  
    "value": 0.29618938369907566
  
  },
  
  "outletTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T12:01:23Z",
  
    "value": 0.11212677811240301
  
  },
  
  "pressureRating": {
  
    "type": "Measurement",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-26T01:24:39Z",
  
    "value": 0.21928692987308485
  
  },
  
  "waterInletTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T00:36:51Z",
  
    "value": 0.5020984273995642
  
  },
  
  "waterInletTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T00:16:12Z",
  
    "value": 0.5508532961104626
  
  },
  
  "waterStorageCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T14:08:00Z",
  
    "value": 0.7917960553016042
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:89d800f7-d732-4461-abca-db8295ebc493",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:89a10496-3523-4838-a16e-2bdf5bd6b9f6",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c7eebebd-b42a-4319-a0d8-47a810d9fec2",
  
    "urn:ngsi-ld:System:d67c42ac-270b-4204-917c-1066975c85bd",
  
    "urn:ngsi-ld:System:aea7fd8f-54b1-4a9e-a473-c2a7359c57c2"
  
  ],
  
  "hasManufacturer": "Boiler Company Inc.",
  
  "hasModel": "Boiler 0.1.2",
  
  "dateCreated": "2023-01-25T19:16:43Z",
  
  "dateModified": "2023-01-25T18:27:19Z",
  
  "source": "Import",
  
  "name": "Boiler",
  
  "alternateName": "Boiler type 2",
  
  "description": "Boiler of limited Boiler types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Boiler NGSI-LD normalized Example    

Here is an example of a Boiler in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Boiler:4f7a4533-13d0-4de0-b5e9-72dee067176a",
  
  "type": "Boiler",
  
  "energySource": {
  
    "type": "Property",
  
    "value": "Sri Lanka"
  
  },
  
  "heatTransferSurfaceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T19:16:12Z",
  
    "value": 0.4182368568397056
  
  },
  
  "isWaterStorageHeater": {
  
    "type": "Property",
  
    "value": false
  
  },
  
  "nominalEnergyConsumption": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T23:06:57Z",
  
    "value": 0.5252685918504294
  
  },
  
  "nominalPartLoadRatio": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T22:37:37Z",
  
    "value": 0.481958764350527
  
  },
  
  "operatingMode": {
  
    "type": "Property",
  
    "value": "Auto Loan Account"
  
  },
  
  "outletTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T17:03:10Z",
  
    "value": 0.2786304815176084
  
  },
  
  "outletTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T02:55:50Z",
  
    "value": 0.4041488945350036
  
  },
  
  "pressureRating": {
  
    "type": "Property",
  
    "unitCode": "N/m2",
  
    "observedAt": "2023-01-25T18:00:19Z",
  
    "value": 0.5561857737231611
  
  },
  
  "waterInletTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T03:34:53Z",
  
    "value": 0.242404197934733
  
  },
  
  "waterInletTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T04:06:01Z",
  
    "value": 0.46028861347866734
  
  },
  
  "waterStorageCapacity": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T10:18:01Z",
  
    "value": 0.22263600675421202
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:cfc926aa-ae2a-411e-b3d4-c315d7d19d9b"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:5e682b37-bcc1-441a-ad19-80615c70a84f"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:ba691c15-807f-48fb-b963-99961fd81a95"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:227bcf8f-170f-41ff-a88d-1e1cb67da411"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7868b4ac-6685-4b3e-85ef-6494c909409c"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Boiler Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Boiler 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T17:50:43Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T23:43:57Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Boiler"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Boiler type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Boiler of limited Boiler types"
  
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

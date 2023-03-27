[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Coil  
============https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Coil/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.**  

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
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalLatentCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalSensibleCapacity`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalUa`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationMode`: Operation mode of this coil.  
- `operationTemperatureMax`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `operationTemperatureMin`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `placementType`: Indicates how the device is designed to be placed.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Coil`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Coil:
    
  description: 'A coil is a device used to provide heat transfer between non-mixing media. A common example is a cooling coil, which utilizes a finned coil in which circulates chilled water, antifreeze, or refrigerant that is used to remove heat from air moving across the surface of the coil. A coil may be used either for heating or cooling purposes by placing a series of tubes (the coil) carrying a heating or cooling fluid into an airstream. The coil may be constructed from tubes bundled in a serpentine form or from finned tubes that give a extended heat transfer surface.  Coils may also be used for non-airflow cases such as embedded in a floor slab.'
    
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
    
    airFlowRateMin:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
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
    
                type: number
    
              minItems: 4
    
              type: array
    
            coordinates:
    
              items:
    
                items:
    
                  type: number
    
                minItems: 2
    
                type: array
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    nominalLatentCapacity:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalSensibleCapacity:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalUa:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationMode:
    
      description: Operation mode of this coil.
    
      enum:
    
        - cooling
    
        - heating
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMax:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    operationTemperatureMin:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
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
    
    placementType:
    
      description: Indicates how the device is designed to be placed.
    
      type: string
    
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
    
      description: It must be equal to `Coil`.
    
      enum:
    
        - Coil
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Coil/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Coils/Coil
    
  x-model-tags: SAREF Coil SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Coil NGSI-v2 key-values Example    

Here is an example of a Coil in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Coil:180d0665-9242-42c6-b336-d7edcf8fc3b5",
  
  "type": "Coil",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T12:20:52Z",
  
      "value": 0.22332143818011307
  
    }
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-26T02:14:47Z",
  
      "value": 0.6369516028350278
  
    }
  
  },
  
  "nominalLatentCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T08:36:43Z",
  
      "value": 0.9394595315602638
  
    }
  
  },
  
  "nominalSensibleCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T03:30:59Z",
  
      "value": 0.8014808985276609
  
    }
  
  },
  
  "nominalUa": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T08:40:09Z",
  
      "value": 0.3738979404823001
  
    }
  
  },
  
  "operationMode": "cooling",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T11:39:18Z",
  
      "value": 0.7510713399220631
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T09:25:28Z",
  
      "value": 0.8674252304724047
  
    }
  
  },
  
  "placementType": "Money Market Account",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:c562a0a7-6355-46a0-a528-ebeea1b5af39",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:7d4df444-5662-45c4-81e8-28dd9e2ab52e",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:98486c90-52da-48cf-af50-69449370e3b9",
  
    "urn:ngsi-ld:System:afe412c8-8366-4eb1-b834-dc68c1e3d828",
  
    "urn:ngsi-ld:System:b851de9e-48bd-4363-9d01-b17ab9469aea"
  
  ],
  
  "hasManufacturer": "Coil Company Inc.",
  
  "hasModel": "Coil 0.1.2",
  
  "dateCreated": "2023-01-25T23:02:47Z",
  
  "dateModified": "2023-01-26T14:02:17Z",
  
  "source": "Import",
  
  "name": "Coil",
  
  "alternateName": "Coil type 2",
  
  "description": "Coil of limited Coil types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Coil NGSI-v2 normalized Example    

Here is an example of a Coil in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Coil:13d40aef-8b95-4cb2-af1e-483e4c874941",
  
  "type": "Coil",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T19:04:55Z",
  
      "value": 0.6477373611080879
  
    }
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3/s",
  
      "observedAt": "2023-01-25T18:34:10Z",
  
      "value": 0.1367768463223733
  
    }
  
  },
  
  "nominalLatentCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-26T02:28:50Z",
  
      "value": 0.6823953079495582
  
    }
  
  },
  
  "nominalSensibleCapacity": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "J/s",
  
      "observedAt": "2023-01-25T14:36:24Z",
  
      "value": 0.9661532549311025
  
    }
  
  },
  
  "nominalUa": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T15:28:21Z",
  
      "value": 0.5711236580496344
  
    }
  
  },
  
  "operationMode": {
  
    "type": "CoilOperationMode",
  
    "value": "cooling"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T12:37:37Z",
  
      "value": 0.5575891151602635
  
    }
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "K",
  
      "observedAt": "2023-01-26T05:25:30Z",
  
      "value": 0.8396275897283132
  
    }
  
  },
  
  "placementType": {
  
    "type": "Text",
  
    "value": "Buckinghamshire"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:1070b255-7508-4019-ba0a-1ce8a03cf3b1"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:cef12274-adeb-41a5-aec1-8e254593bb26"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:65b917e6-ec39-4e2e-bce1-a52a52c176bc"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:61834f7f-655f-47f1-828c-755a25e7b026"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:ab77fbe9-a323-477c-81bf-a9923abdf8ea"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Coil Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Coil 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T04:03:32.1629228+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T16:59:28.4436033+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Coil"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Coil type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Coil of limited Coil types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Coil NGSI-LD key-values Example    

Here is an example of a Coil in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Coil:5a43bf1c-c3ab-403c-8834-2a4f435baaa7",
  
  "type": "Coil",
  
  "airFlowRateMax": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T13:05:42Z",
  
    "value": 0.6201074513661233
  
  },
  
  "airFlowRateMin": {
  
    "type": "Measurement",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T13:01:14Z",
  
    "value": 0.4125796930605117
  
  },
  
  "nominalLatentCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-26T13:44:43Z",
  
    "value": 0.23301011487865497
  
  },
  
  "nominalSensibleCapacity": {
  
    "type": "Measurement",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T15:33:43Z",
  
    "value": 0.4246163578705977
  
  },
  
  "nominalUa": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T12:59:56Z",
  
    "value": 0.5275100794000398
  
  },
  
  "operationMode": "heating",
  
  "operationTemperatureMax": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T21:07:19Z",
  
    "value": 0.2815770923110156
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Measurement",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T16:48:25Z",
  
    "value": 0.455896112625108
  
  },
  
  "placementType": "integrate",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:99d74186-45fb-4461-995a-f5d4dbaa84dc",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:9d4f53de-ee40-4a00-8aa7-790c2cf93fc5",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:71c187bb-30dd-4aca-96d1-fd34a2c52317",
  
    "urn:ngsi-ld:System:092a55b8-1696-43e2-b8cc-585c116c8030",
  
    "urn:ngsi-ld:System:3063ff97-b74d-4eff-8b3b-3853afc34652"
  
  ],
  
  "hasManufacturer": "Coil Company Inc.",
  
  "hasModel": "Coil 0.1.2",
  
  "dateCreated": "2023-01-25T20:46:37Z",
  
  "dateModified": "2023-01-25T20:56:20Z",
  
  "source": "Import",
  
  "name": "Coil",
  
  "alternateName": "Coil type 2",
  
  "description": "Coil of limited Coil types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Coil NGSI-LD normalized Example    

Here is an example of a Coil in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Coil:fcc6fa4b-fa43-42de-af7d-c8be6efda789",
  
  "type": "Coil",
  
  "airFlowRateMax": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-25T22:00:31Z",
  
    "value": 0.461404719601072
  
  },
  
  "airFlowRateMin": {
  
    "type": "Property",
  
    "unitCode": "m3/s",
  
    "observedAt": "2023-01-26T12:18:55Z",
  
    "value": 0.3100905584892091
  
  },
  
  "nominalLatentCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T15:57:00Z",
  
    "value": 0.0859276056343462
  
  },
  
  "nominalSensibleCapacity": {
  
    "type": "Property",
  
    "unitCode": "J/s",
  
    "observedAt": "2023-01-25T15:07:49Z",
  
    "value": 0.9959034840230547
  
  },
  
  "nominalUa": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T16:07:27Z",
  
    "value": 0.03766746157415857
  
  },
  
  "operationMode": {
  
    "type": "Property",
  
    "value": "cooling"
  
  },
  
  "operationTemperatureMax": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-25T15:22:24Z",
  
    "value": 0.18992025947801072
  
  },
  
  "operationTemperatureMin": {
  
    "type": "Property",
  
    "unitCode": "K",
  
    "observedAt": "2023-01-26T07:51:42Z",
  
    "value": 0.6342100760763256
  
  },
  
  "placementType": {
  
    "type": "Property",
  
    "value": "SQL"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:61d397a1-954d-40ec-a4cc-cba2c10a07ca"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:ee042545-32fa-4adb-97e1-5007ccabcd63"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:cab59172-6cb8-443e-94b8-b6270aaa5e60"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:73b9f71e-63bb-49bf-96ef-f6f4922f4245"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:7607ea00-30f7-4271-a0f3-c0b1755be875"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Coil Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Coil 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T04:20:07Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T16:46:30Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Coil"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Coil type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Coil of limited Coil types"
  
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

[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Evaporator  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Evaporator/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An evaporator is a device in which a liquid refrigerent is vaporized and absorbs heat from the surrounding fluid.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `evaporationCoolant`: The fluid used for the coolant in the evaporator.  
- `evaporationMediumType`: ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant. ColdAir: Evaporator is using air to exchange heat with refrigerant.  
- `externalSurfaceArea`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `internalRefrigerantVolume`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `internalSurfaceArea`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `internalWaterVolume`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalHeatTransferArea`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalHeatTransferCoefficient`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `refrigerantClass`: Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Evaporator`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Evaporator:
    
  description: An evaporator is a device in which a liquid refrigerent is vaporized and absorbs heat from the surrounding fluid.
    
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
    
    evaporationCoolant:
    
      description: The fluid used for the coolant in the evaporator.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    evaporationMediumType:
    
      description: 'ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant. ColdAir: Evaporator is using air to exchange heat with refrigerant.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    externalSurfaceArea:
    
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
    
    internalRefrigerantVolume:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    internalSurfaceArea:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    internalWaterVolume:
    
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
    
    location:
    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'
    
      oneOf:
    
        - description: Geoproperty. Geojson reference to the item. Point
    
          properties:
    
            bbox:
    
              items:
    
                type: number
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
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
    
    nominalHeatTransferArea:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurement/schema.json"
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalHeatTransferCoefficient:
    
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
    
    refrigerantClass:
    
      description: 'Refrigerant class used by the compressor. CFC: Chlorofluorocarbons. HCFC: Hydrochlorofluorocarbons. HFC: Hydrofluorocarbons.'
    
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
    
      description: It must be equal to `Evaporator`.
    
      enum:
    
        - Evaporator
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/Evaporator/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Evaporator/schema.json"
    
  x-model-tags: SAREF Evaporator SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Evaporator NGSI-v2 key-values Example    

Here is an example of a Evaporator in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Evaporator:052fc49c-111f-420b-a8e2-51fe3338d2b1",
  
  "type": "Evaporator",
  
  "evaporationCoolant": "Martinique",
  
  "evaporationMediumType": "e-markets",
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-25T22:25:21Z",
  
      "value": 0.5908980288694448
  
    }
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T13:10:15Z",
  
      "value": 0.6284120974003947
  
    }
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T09:19:30Z",
  
      "value": 0.9343787028327242
  
    }
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T05:01:07Z",
  
      "value": 0.6490547902275666
  
    }
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T14:02:50Z",
  
      "value": 0.4294965931834158
  
    }
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-26T09:00:31Z",
  
      "value": 0.8081650097718576
  
    }
  
  },
  
  "refrigerantClass": "Jewelery, Music & Games",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:51c0dbf1-adcc-4d2c-b3ea-90aa62cb494f",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:c5bac51f-5e2b-4152-9eb1-96959129eb27",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:67f3cbde-6a56-4f0b-9085-ddcee5f7e9fa",
  
    "urn:ngsi-ld:System:3e056ae8-5498-4141-9bca-6f9b2eb03b67",
  
    "urn:ngsi-ld:System:6692437c-d2c6-4ba0-9386-3a7e0f49d10d"
  
  ],
  
  "hasManufacturer": "Evaporator Company Inc.",
  
  "hasModel": "Evaporator 0.1.2",
  
  "dateCreated": "2023-01-26T00:54:03Z",
  
  "dateModified": "2023-01-25T16:56:18Z",
  
  "source": "Import",
  
  "name": "Evaporator",
  
  "alternateName": "Evaporator type 2",
  
  "description": "Evaporator of limited Evaporator types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Evaporator NGSI-v2 normalized Example    

Here is an example of a Evaporator in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Evaporator:c9337df1-e99a-43a3-9f15-425e35abf54a",
  
  "type": "Evaporator",
  
  "evaporationCoolant": {
  
    "type": "Text",
  
    "value": "seamless"
  
  },
  
  "evaporationMediumType": {
  
    "type": "Text",
  
    "value": "Pike"
  
  },
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T00:18:31Z",
  
      "value": 0.07191726989654268
  
    }
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T16:07:35Z",
  
      "value": 0.20250063780044392
  
    }
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T01:50:01Z",
  
      "value": 0.33350088977343506
  
    }
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T00:59:39Z",
  
      "value": 0.8525147046941662
  
    }
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T01:39:16Z",
  
      "value": 0.7335123054536791
  
    }
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-26T08:10:01Z",
  
      "value": 0.23696481410868975
  
    }
  
  },
  
  "refrigerantClass": {
  
    "type": "Text",
  
    "value": "Incredible"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:1d3c18d5-3c73-4b33-ac02-be885911a9c2"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:c2a99f87-20d2-4a3e-8869-9ccb703023f7"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:9905fd33-a0dd-465c-821e-7179621c4cd2"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:912b3134-8a54-4576-9e70-68f7d814a681"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:46197de5-7d87-4a26-9d32-4e62dd387c93"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Evaporator Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Evaporator 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T19:39:32.5598858+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T02:08:29.4163966+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Evaporator"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Evaporator type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Evaporator of limited Evaporator types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Evaporator NGSI-LD key-values Example    

Here is an example of a Evaporator in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Evaporator:e5656db3-4e96-45e2-9c41-028e7eb3aadb",
  
  "type": "Evaporator",
  
  "evaporationCoolant": "Coordinator",
  
  "evaporationMediumType": "initiative",
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T06:11:32Z",
  
    "value": 0.3000502990645362
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-25T22:11:29Z",
  
    "value": 0.9958485770797829
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T05:20:10Z",
  
    "value": 0.9608679514752554
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T01:52:55Z",
  
    "value": 0.22641713987729473
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T19:43:03Z",
  
    "value": 0.6755586514132743
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-25T15:39:25Z",
  
    "value": 0.6761432965879979
  
  },
  
  "refrigerantClass": "systems",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:bdb452df-dd95-45a6-baac-857149014e2d",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:14a145df-700e-4a47-8998-531c47806211",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:517ca686-4085-4db0-9e55-5452e80bb63c",
  
    "urn:ngsi-ld:System:5cf3f9ce-ee81-428d-847d-ea4bc25712f6",
  
    "urn:ngsi-ld:System:4d8cb33c-fa94-43e5-828b-7e17d644307f"
  
  ],
  
  "hasManufacturer": "Evaporator Company Inc.",
  
  "hasModel": "Evaporator 0.1.2",
  
  "dateCreated": "2023-01-26T11:40:05Z",
  
  "dateModified": "2023-01-25T18:17:20Z",
  
  "source": "Import",
  
  "name": "Evaporator",
  
  "alternateName": "Evaporator type 2",
  
  "description": "Evaporator of limited Evaporator types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Evaporator NGSI-LD normalized Example    

Here is an example of a Evaporator in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Evaporator:012ce978-0915-4322-82cf-64be00f886e6",
  
  "type": "Evaporator",
  
  "evaporationCoolant": {
  
    "type": "Property",
  
    "value": "Generic"
  
  },
  
  "evaporationMediumType": {
  
    "type": "Property",
  
    "value": "ROI"
  
  },
  
  "externalSurfaceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T01:26:06Z",
  
    "value": 0.40305559655625467
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T04:37:57Z",
  
    "value": 0.9165377999786634
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T07:59:30Z",
  
    "value": 0.11705017875360657
  
  },
  
  "internalWaterVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T13:18:36Z",
  
    "value": 0.6445386560470906
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T18:46:49Z",
  
    "value": 0.20771410507872068
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Property",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-26T11:33:53Z",
  
    "value": 0.029467682176717913
  
  },
  
  "refrigerantClass": {
  
    "type": "Property",
  
    "value": "Directives"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:09942ed6-b0b8-4968-a57d-e48b8fd062f9"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:9f7d6071-a0a0-4b9d-9707-b59804cef5a8"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:cb2ff8f9-5b3a-48f2-a576-c7a632297517"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:c9865d23-d9da-47f2-875a-1f0beb5bbf09"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:18016c6a-4548-4adc-a84c-c62c94e34393"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Evaporator Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Evaporator 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-26T06:49:33Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T02:39:15Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Evaporator"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Evaporator type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Evaporator of limited Evaporator types"
  
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

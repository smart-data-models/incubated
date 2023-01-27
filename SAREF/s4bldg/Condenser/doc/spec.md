[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Condenser  
================https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Condenser/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
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
- `type`: It must be equal to `Condenser`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Condenser:
    
  description: 'A condenser is a device that is used to dissipate heat, typically by condensing a substance such as a refrigerant from its gaseous to its liquid state.'
    
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
    
    externalSurfaceArea:
    
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
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    internalSurfaceArea:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    internalWaterVolume:
    
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
    https://github.com/smart-data-models/incubated/SAREF/
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
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalHeatTransferCoefficient:
    
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
    
      description: It must be equal to `Condenser`.
    
      enum:
    
        - Condenser
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Condenser/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Condensers/Condenser
    
  x-model-tags: SAREF Condenser SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Condenser NGSI-v2 key-values Example    

Here is an example of a Condenser in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Condenser:2adcb166-23ce-4061-8062-952d5f2402b9",
  
  "type": "Condenser",
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-25T15:14:44Z",
  
      "value": 0.18804655027013273
  
    }
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T14:39:55Z",
  
      "value": 0.1588694072031649
  
    }
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T14:11:09Z",
  
      "value": 0.884829655411807
  
    }
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-25T23:41:04Z",
  
      "value": 0.7576300292464242
  
    }
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T01:51:54Z",
  
      "value": 0.04220384603580274
  
    }
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-25T22:48:31Z",
  
      "value": 0.4901767947128819
  
    }
  
  },
  
  "refrigerantClass": "Barbados",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7ba37c8a-b348-4fc5-8191-22dbe255c23e",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:f9999243-09ea-40b2-892a-63bfd9062a09",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:374a6c1e-348f-46a2-824d-616554f66351",
  
    "urn:ngsi-ld:System:0bd6a865-18bc-40a2-b1cf-64af77762cee",
  
    "urn:ngsi-ld:System:e8c3da85-a230-40e1-832c-e03b342a1160"
  
  ],
  
  "hasManufacturer": "Condenser Company Inc.",
  
  "hasModel": "Condenser 0.1.2",
  
  "dateCreated": "2023-01-25T15:55:59Z",
  
  "dateModified": "2023-01-26T06:49:28Z",
  
  "source": "Import",
  
  "name": "Condenser",
  
  "alternateName": "Condenser type 2",
  
  "description": "Condenser of limited Condenser types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Condenser NGSI-v2 normalized Example    

Here is an example of a Condenser in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Condenser:e22782fc-5392-4dd2-b891-29b5fbf683cd",
  
  "type": "Condenser",
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-25T17:43:58Z",
  
      "value": 0.1255332761606085
  
    }
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T11:46:00Z",
  
      "value": 0.5305579766612258
  
    }
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T00:21:53Z",
  
      "value": 0.7094627719374283
  
    }
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T03:45:09Z",
  
      "value": 0.3123303218703414
  
    }
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m2",
  
      "observedAt": "2023-01-26T05:38:37Z",
  
      "value": 0.4444793909507544
  
    }
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-25T20:26:04Z",
  
      "value": 0.6428769642448905
  
    }
  
  },
  
  "refrigerantClass": {
  
    "type": "Text",
  
    "value": "Ergonomic Fresh Pants"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:ae10b0d7-9929-45cc-bf0c-3e3ab5380c1a"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:a3e1362f-7a17-46e9-a997-fd763290b5a2"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:47267553-d21a-42f8-b1b9-b24ec529e8ad"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:878dd196-c9af-43d7-8d36-344fa19ca56f"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:366cc386-314f-4591-9f3f-4099890c74e7"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Condenser Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Condenser 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T23:40:11.0211053+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T22:43:21.3342982+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Condenser"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Condenser type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Condenser of limited Condenser types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Condenser NGSI-LD key-values Example    

Here is an example of a Condenser in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Condenser:f66d487b-5b9c-4b5e-a4c7-e4b2063fc2e9",
  
  "type": "Condenser",
  
  "externalSurfaceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T07:37:08Z",
  
    "value": 0.6449661980010207
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T02:12:31Z",
  
    "value": 0.863683364075609
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T00:06:32Z",
  
    "value": 0.9464586914583154
  
  },
  
  "internalWaterVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T07:26:01Z",
  
    "value": 0.6424064946775078
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Measurement",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T00:59:13Z",
  
    "value": 0.610333439118894
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Measurement",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-26T09:10:28Z",
  
    "value": 0.5194564609061897
  
  },
  
  "refrigerantClass": "Minnesota",
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:10f95f9f-d19b-4314-9f37-8e64d337d93f",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:2e3edab9-2d27-405c-b401-98a710014e51",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:c7749db4-055c-4724-be88-ec72aaca3b48",
  
    "urn:ngsi-ld:System:ade6e03a-3f48-484b-bdc3-4895cabfa4b8",
  
    "urn:ngsi-ld:System:09a7180a-3af6-4013-b4a4-359642e63384"
  
  ],
  
  "hasManufacturer": "Condenser Company Inc.",
  
  "hasModel": "Condenser 0.1.2",
  
  "dateCreated": "2023-01-25T14:55:02Z",
  
  "dateModified": "2023-01-25T22:46:10Z",
  
  "source": "Import",
  
  "name": "Condenser",
  
  "alternateName": "Condenser type 2",
  
  "description": "Condenser of limited Condenser types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Condenser NGSI-LD normalized Example    

Here is an example of a Condenser in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Condenser:290f1265-1ded-4706-b549-43d7ddcaa239",
  
  "type": "Condenser",
  
  "externalSurfaceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T11:04:44Z",
  
    "value": 0.3471102075551651
  
  },
  
  "internalRefrigerantVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T10:30:09Z",
  
    "value": 0.696994206179287
  
  },
  
  "internalSurfaceArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-25T14:42:31Z",
  
    "value": 0.7522617883905902
  
  },
  
  "internalWaterVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T09:25:42Z",
  
    "value": 0.5807649609435256
  
  },
  
  "nominalHeatTransferArea": {
  
    "type": "Property",
  
    "unitCode": "m2",
  
    "observedAt": "2023-01-26T05:15:12Z",
  
    "value": 0.6105994546410142
  
  },
  
  "nominalHeatTransferCoefficient": {
  
    "type": "Property",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-25T14:28:56Z",
  
    "value": 0.17023310849677553
  
  },
  
  "refrigerantClass": {
  
    "type": "Property",
  
    "value": "Generic Metal Pants"
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:b7d758c3-cd93-4ce4-a414-28e5a714b67c"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:9d98233b-6df5-418e-b43c-5f98c921296f"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:6ba8c28a-2ebf-4a11-ba34-b7d778896bf9"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:3f480247-b6e3-4cc3-89e1-5c1f88507e48"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:645beb56-0f95-4b35-a0ed-56d848e575f1"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Condenser Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Condenser 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T22:14:26Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T02:56:43Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Condenser"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Condenser type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Condenser of limited Condenser types"
  
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

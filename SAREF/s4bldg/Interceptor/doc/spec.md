[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: Interceptor  
================https://github.com/smart-data-models/incubated/SAREF/
  

[Open License](http://smart-data-models.kmd.dk/flat/s4bldg/Interceptor/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An interceptor is a device designed and installed in order to separate and retain deleterious, hazardous or undesirable matter while permitting normal sewage or liquids to discharge into a collection system by gravity.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `coverLength`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `coverWidth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `hasManufacturer`: A relationship identifying the manufacturer of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `hasModel`: A relationship identifying the model of an entity (e.g., device). The value is expected to be a string or a string with language tag.  
- `id`: Unique identifier of the entity  
- `inletConnectionSize`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `isContainedInBuildingSpace`: Unique identifier of the entity  
- `isContainedInPhysicalObject`: Unique identifier of the entity  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `nominalBodyDepth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalBodyLength`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `nominalBodyWidth`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `outletConnectionSize`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `Interceptor`.  
- `ventilatingPipeSize`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
Interceptor:
    
  description: 'An interceptor is a device designed and installed in order to separate and retain deleterious, hazardous or undesirable matter while permitting normal sewage or liquids to discharge into a collection system by gravity.'
    
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
    
    coverLength:
    
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
    
    coverWidth:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
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
    
    inletConnectionSize:
    
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
    https://github.com/smart-data-models/incubated/SAREF/
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
    
    nominalBodyDepth:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalBodyLength:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    nominalBodyWidth:
    
      $id: http://smart-data-models.kmd.dk/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    outletConnectionSize:
    
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
    
      description: It must be equal to `Interceptor`.
    
      enum:
    
        - Interceptor
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    ventilatingPipeSize:
    
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
    
  x-license-url: http://smart-data-models.kmd.dk/flat/s4bldg/Interceptor/LICENSE.md
    
  x-model-schema: http://smart-data-models.kmd.dk/Interceptors/Interceptor
    
  x-model-tags: SAREF Interceptor SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### Interceptor NGSI-v2 key-values Example    

Here is an example of a Interceptor in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Interceptor:e70382d2-800a-4b96-be2e-03cfbe37ea51",
  
  "type": "Interceptor",
  
  "coverLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T18:22:10Z",
  
      "value": 0.637563278020405
  
    }
  
  },
  
  "coverWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:01:49Z",
  
      "value": 0.39657091750888485
  
    }
  
  },
  
  "inletConnectionSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T03:37:34Z",
  
      "value": 0.19141372654068167
  
    }
  
  },
  
  "nominalBodyDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T14:09:37Z",
  
      "value": 0.14989240074077315
  
    }
  
  },
  
  "nominalBodyLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T22:13:42Z",
  
      "value": 0.06135027876899957
  
    }
  
  },
  
  "nominalBodyWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T16:42:46Z",
  
      "value": 0.7029889791860054
  
    }
  
  },
  
  "outletConnectionSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T00:13:19Z",
  
      "value": 0.7108703974241664
  
    }
  
  },
  
  "ventilatingPipeSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T16:29:52Z",
  
      "value": 0.5746572805545043
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:5a19b47d-28c9-43f1-9dc1-5970e15117e5",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:676f81a5-820d-474d-991e-2b87d2acd734",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:5661f227-2a9c-49ce-a1e6-b0ac6fffdf71",
  
    "urn:ngsi-ld:System:c9571a2a-2f4a-4c46-b931-0fe3489aaf15",
  
    "urn:ngsi-ld:System:67c475d5-808d-4419-8c5f-1cdf158221f1"
  
  ],
  
  "hasManufacturer": "Interceptor Company Inc.",
  
  "hasModel": "Interceptor 0.1.2",
  
  "dateCreated": "2023-01-25T20:11:18Z",
  
  "dateModified": "2023-01-26T02:38:35Z",
  
  "source": "Import",
  
  "name": "Interceptor",
  
  "alternateName": "Interceptor type 2",
  
  "description": "Interceptor of limited Interceptor types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### Interceptor NGSI-v2 normalized Example    

Here is an example of a Interceptor in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Interceptor:e45ced8f-6d99-4b1e-a32b-d9e525d9429f",
  
  "type": "Interceptor",
  
  "coverLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T13:38:22Z",
  
      "value": 0.44339547398234425
  
    }
  
  },
  
  "coverWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T00:55:09Z",
  
      "value": 0.8009891082993085
  
    }
  
  },
  
  "inletConnectionSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T02:06:40Z",
  
      "value": 0.041004126787857476
  
    }
  
  },
  
  "nominalBodyDepth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T14:52:09Z",
  
      "value": 0.29190715678427104
  
    }
  
  },
  
  "nominalBodyLength": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T09:55:52Z",
  
      "value": 0.3879109279352648
  
    }
  
  },
  
  "nominalBodyWidth": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-25T17:31:04Z",
  
      "value": 0.41258224275422206
  
    }
  
  },
  
  "outletConnectionSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T10:23:30Z",
  
      "value": 0.45113395263374134
  
    }
  
  },
  
  "ventilatingPipeSize": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "mm",
  
      "observedAt": "2023-01-26T00:30:16Z",
  
      "value": 0.9955414515835173
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:6e19661e-cc0d-40a9-a678-77eb09dbec66"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:ab4d138b-d0c3-4d88-96fa-9326f23e5946"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:284ae13c-0f10-4ade-bde1-84335db0e9c3"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:01933b47-4ff0-4a28-a3c1-ccda5080a98d"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:e0b79043-7cc6-45b0-a28a-8368751e98b8"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "Interceptor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "Interceptor 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T19:09:02.6826601+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T23:45:53.2581226+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "Interceptor"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "Interceptor type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "Interceptor of limited Interceptor types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### Interceptor NGSI-LD key-values Example    

Here is an example of a Interceptor in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Interceptor:5614c957-4a20-42e1-bbc0-89eafb1c8275",
  
  "type": "Interceptor",
  
  "coverLength": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T14:18:41Z",
  
    "value": 0.6887319135078809
  
  },
  
  "coverWidth": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T07:27:39Z",
  
    "value": 0.9069378489863433
  
  },
  
  "inletConnectionSize": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T04:50:16Z",
  
    "value": 0.2464518825398755
  
  },
  
  "nominalBodyDepth": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T06:12:52Z",
  
    "value": 0.08895406556723484
  
  },
  
  "nominalBodyLength": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T05:49:06Z",
  
    "value": 0.20271826723013298
  
  },
  
  "nominalBodyWidth": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T05:39:26Z",
  
    "value": 0.8832131382589374
  
  },
  
  "outletConnectionSize": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T20:24:19Z",
  
    "value": 0.5122156296663434
  
  },
  
  "ventilatingPipeSize": {
  
    "type": "Measurement",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T03:43:40Z",
  
    "value": 0.2922930100864284
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:6312e9fa-a4a7-45df-97e8-7e4a845328fa",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:36e83b96-9ae9-4d68-8a54-f91d3145678c",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:2e7d5a4c-15c1-46e8-b5ea-62826be7f020",
  
    "urn:ngsi-ld:System:a475090b-b126-47b0-8716-0d3d334701fc",
  
    "urn:ngsi-ld:System:eb3f9fb2-d1be-4d12-915d-e264ca6255da"
  
  ],
  
  "hasManufacturer": "Interceptor Company Inc.",
  
  "hasModel": "Interceptor 0.1.2",
  
  "dateCreated": "2023-01-26T06:33:12Z",
  
  "dateModified": "2023-01-26T12:41:46Z",
  
  "source": "Import",
  
  "name": "Interceptor",
  
  "alternateName": "Interceptor type 2",
  
  "description": "Interceptor of limited Interceptor types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://smartdatamodels.blob.core.windows.net/models/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### Interceptor NGSI-LD normalized Example    

Here is an example of a Interceptor in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:Interceptor:06f8171e-55bb-4229-ab9e-d558b4512982",
  
  "type": "Interceptor",
  
  "coverLength": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T04:52:13Z",
  
    "value": 0.7541861378948772
  
  },
  
  "coverWidth": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T13:23:50Z",
  
    "value": 0.18581009233424606
  
  },
  
  "inletConnectionSize": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T06:33:28Z",
  
    "value": 0.5362664253813387
  
  },
  
  "nominalBodyDepth": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T01:38:01Z",
  
    "value": 0.8646722014120122
  
  },
  
  "nominalBodyLength": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T14:16:38Z",
  
    "value": 0.9860672918739783
  
  },
  
  "nominalBodyWidth": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-25T19:51:23Z",
  
    "value": 0.8127360894676557
  
  },
  
  "outletConnectionSize": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T04:47:21Z",
  
    "value": 0.5311465588349177
  
  },
  
  "ventilatingPipeSize": {
  
    "type": "Property",
  
    "unitCode": "mm",
  
    "observedAt": "2023-01-26T08:31:47Z",
  
    "value": 0.7111321417760854
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:21622424-25f8-4e51-b604-713fb47019ac"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:69c1fa2f-3885-434a-b3dd-b7eb481dc4be"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:ddff37fe-7866-4af8-8fb2-2961e751ede0"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:9f5fd945-9540-4ddf-8af6-9e3f51f39f90"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:f007bebb-144c-4490-975b-b14698f42f2a"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "Interceptor Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "Interceptor 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T18:44:42Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T17:19:12Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "Interceptor"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "Interceptor type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "Interceptor of limited Interceptor types"
  
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

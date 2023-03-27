[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: BuildingSpace  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/BuildingSpace/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **An entity used to define the physical spaces of the building. A building space contains devices or building objects.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
- `airVolume`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `alternateName`: An alternative name for this item  
- `areaServed`: The geographic area where a service or offered item is provided  
- `bounds`: Represents a box in a 3D space.  
- `buildingSpaceKind`: Detailed type of the Building Space.  
- `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  
- `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  
- `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  
- `description`: A description of this item  
- `id`: Unique identifier of the entity  
- `isSpaceOfBuilding`: Unique identifier of the entity  
- `isSpaceOfBuildingSpace`: Unique identifier of the entity  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `type`: It must be equal to `BuildingSpace`.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
BuildingSpace:
    
  description: An entity used to define the physical spaces of the building. A building space contains devices or building objects.
    
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
    
    airVolume:
    
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
    
    bounds:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Bounds/schema.json"
    
      description: Represents a box in a 3D space.
    
      properties:
    
        max:
    
          $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Point/schema.json"
    
          description: Property. Represents a point in a 3D space.
    
          properties:
    
            type:
    
              description: Property. Property. NGSI-LD Entity Type.
    
              enum:
    
                - Point
    
              type: string
    
            x:
    
              description: Property. Coordinate X of the point.
    
              type: number
    
            y:
    
              description: Property. Coordinate Y of the point.
    
              type: number
    
            z:
    
              description: Property. Coordinate Z of the point.
    
              type: number
    
          title: Smart data models - Point schema
    
          type: object
    
        min:
    
          $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Point/schema.json"
    
          description: Property. Represents a point in a 3D space.
    
          properties:
    
          title: Smart data models - Point schema
    
          type: object
    
        type:
    
          description: Property. Property. NGSI-LD Entity Type.
    
          enum:
    
            - Bounds
    
          type: string
    
      title: Smart data models - Bounds schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    buildingSpaceKind:
    
      description: Detailed type of the Building Space.
    
      enum:
    
        - BuildingElementProxy
    
        - BuildingStorey
    
        - Column
    
        - Covering
    
        - CurtainWall
    
        - Door
    
        - OpeningElement
    
        - Plate
    
        - Railing
    
        - Roof
    
        - Site
    
        - Slab
    
        - Space
    
        - Stair
    
        - StairFlight
    
        - Storey
    
        - Wall
    
        - WallStandardCase
    
        - Window
    
      type: string
    
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
    
    isSpaceOfBuilding:
    
      anyOf:
    
      description: Unique identifier of the entity
    
      x-ngsi:
    
        type: Property
    
    isSpaceOfBuildingSpace:
    https://github.com/smart-data-models/incubated/tree/master/SAREF/
      anyOf:
    
      description: Unique identifier of the entity
    
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
    
    type:
    
      description: It must be equal to `BuildingSpace`.
    
      enum:
    
        - BuildingSpace
    
      type: string
    
      x-ngsi:
    
        type: Property
    
  required:
    
    - id
    
    - type
    
  type: object
    
  x-derived-from: ""
    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/BuildingSpace/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/BuildingSpace/schema.json"
    
  x-model-tags: SAREF BuildingSpace SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### BuildingSpace NGSI-v2 key-values Example    

Here is an example of a BuildingSpace in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:BuildingSpace:cc956fa0-70f8-4110-a4d1-60eb1299bc8e",
  
  "type": "BuildingSpace",
  
  "airVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T05:33:39Z",
  
      "value": 0.9964475180399912
  
    }
  
  },
  
  "bounds": {
  
    "type": "Bounds",
  
    "max": {
  
      "type": "Point",
  
      "x": 0.6598941847785847,
  
      "y": 0.29050046329217627,
  
      "z": 0.5723987903652894
  
    },
  
    "min": {
  
      "type": "Point",
  
      "x": 0.2328925559580186,
  
      "y": 0.7820178782873053,
  
      "z": 0.703947078383337
  
    }
  
  },
  
  "buildingSpaceKind": "Space",
  
  "isSpaceOfBuilding": "urn:ngsi-ld:Building:5ba9925b-36c8-4243-bc1c-5095eefbc2c9",
  
  "isSpaceOfBuildingSpace": "urn:ngsi-ld:BuildingSpace:bb5c5eb8-7224-4560-a8f3-0dd75742066d",
  
  "dateCreated": "2023-01-26T10:56:49Z",
  
  "dateModified": "2023-01-25T18:35:39Z",
  
  "source": "Import",
  
  "name": "BuildingSpace",
  
  "alternateName": "BuildingSpace type 2",
  
  "description": "BuildingSpace of limited BuildingSpace types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### BuildingSpace NGSI-v2 normalized Example    

Here is an example of a BuildingSpace in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:BuildingSpace:f341006e-3556-4699-8959-19edf7079bac",
  
  "type": "BuildingSpace",
  
  "airVolume": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "m3",
  
      "observedAt": "2023-01-26T07:40:51Z",
  
      "value": 0.9064782098814886
  
    }
  
  },
  
  "bounds": {
  
    "type": "Bounds",
  
    "value": {
  
      "max": {
  
        "type": "Point",
  
        "value": {
  
          "x": {
  
            "type": "Float",
  
            "value": 0.3435432568091691
  
          },
  
          "y": {
  
            "type": "Float",
  
            "value": 0.24905296319042758
  
          },
  
          "z": {
  
            "type": "Float",
  
            "value": 0.2845520466135202
  
          }
  
        }
  
      },
  
      "min": {
  
        "type": "Point",
  
        "value": {
  
          "x": {
  
            "type": "Float",
  
            "value": 0.4907878164155083
  
          },
  
          "y": {
  
            "type": "Float",
  
            "value": 0.24758694946836612
  
          },
  
          "z": {
  
            "type": "Float",
  
            "value": 0.5473795276532545
  
          }
  
        }
  
      }
  
    }
  
  },
  
  "buildingSpaceKind": {
  
    "type": "BuildingSpaceKind",
  
    "value": "OpeningElement"
  
  },
  
  "isSpaceOfBuilding": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:Building:f61515c6-7ae8-497f-a5a0-a109d69c8ad9"
  
  },
  
  "isSpaceOfBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:af38bc5d-cc8e-456b-933b-6f49a5a4347b"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T05:23:18.620809+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T01:47:26.1064065+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "BuildingSpace"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "BuildingSpace type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "BuildingSpace of limited BuildingSpace types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### BuildingSpace NGSI-LD key-values Example    

Here is an example of a BuildingSpace in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:BuildingSpace:676ee568-16af-457c-898f-232c5900f75e",
  
  "type": "BuildingSpace",
  
  "airVolume": {
  
    "type": "Measurement",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T08:56:19Z",
  
    "value": 0.6757573914426188
  
  },
  
  "bounds": {
  
    "type": "Bounds",
  
    "max": {
  
      "type": "Point",
  
      "x": 0.11739641482930474,
  
      "y": 0.6412223514966972,
  
      "z": 0.8162459383914825
  
    },
  
    "min": {
  
      "type": "Point",
  
      "x": 0.656218944969374,
  
      "y": 0.2590907017420844,
  
      "z": 0.10417683913385478
  
    }
  
  },
  
  "buildingSpaceKind": "Plate",
  
  "isSpaceOfBuilding": "urn:ngsi-ld:Building:c09b1c10-d5bb-40cb-a76a-bbf551661d55",
  
  "isSpaceOfBuildingSpace": "urn:ngsi-ld:BuildingSpace:0b32e85a-02bd-4ccb-a5ec-d4e4805121e9",
  
  "dateCreated": "2023-01-25T17:03:22Z",
  
  "dateModified": "2023-01-25T23:31:49Z",
  
  "source": "Import",
  
  "name": "BuildingSpace",
  
  "alternateName": "BuildingSpace type 2",
  
  "description": "BuildingSpace of limited BuildingSpace types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### BuildingSpace NGSI-LD normalized Example    

Here is an example of a BuildingSpace in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:BuildingSpace:d7cb7e92-0891-47f6-86a9-06a4aa5373bd",
  
  "type": "BuildingSpace",
  
  "airVolume": {
  
    "type": "Property",
  
    "unitCode": "m3",
  
    "observedAt": "2023-01-26T13:10:25Z",
  
    "value": 0.24704243447487917
  
  },
  
  "bounds": {
  
    "type": "Property",
  
    "value": {
  
      "max": {
  
        "type": "Property",
  
        "value": {
  
          "x": {
  
            "type": "Property",
  
            "value": 0.5826533723200945
  
          },
  
          "y": {
  
            "type": "Property",
  
            "value": 0.8080827869513028
  
          },
  
          "z": {
  
            "type": "Property",
  
            "value": 0.7573005865012242
  
          }
  
        }
  
      },
  
      "min": {
  
        "type": "Property",
  
        "value": {
  
          "x": {
  
            "type": "Property",
  
            "value": 0.6273023443041038
  
          },
  
          "y": {
  
            "type": "Property",
  
            "value": 0.3279024163898896
  
          },
  
          "z": {
  
            "type": "Property",
  
            "value": 0.9097369934052144
  
          }
  
        }
  
      }
  
    }
  
  },
  
  "buildingSpaceKind": {
  
    "type": "Property",
  
    "value": "Covering"
  
  },
  
  "isSpaceOfBuilding": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:Building:46ad9d28-a073-4895-a02e-eb5d12495b4a"
  
  },
  
  "isSpaceOfBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:fa3ff8f2-4340-4a60-8cfa-b08d35a62952"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T18:18:52Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-26T08:23:36Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "BuildingSpace"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "BuildingSpace type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "BuildingSpace of limited BuildingSpace types"
  
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

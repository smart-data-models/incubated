[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: ShadingDevice  
================https://github.com/smart-data-models/incubated/tree/master/SAREF/
  

[Open License](https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/ShadingDevice/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

Global description: **Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.**  

version: 0.0.2  


## List of properties  


- `address`: The mailing address  
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
- `isExternal`: Indication whether the element is designed for use in the exterior (TRUE) or not (FALSE). If (TRUE) it is an external element and faces the outside of the building.  
- `isSubSystemOf`: A reference to a system(s) that this Physical Object is part of.  
- `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `mechanicalOperated`: Indication whether the element is operated machanically (TRUE) or not, i.e. manually (FALSE).  
- `name`: The name of this item.  
- `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `roughness`: A measure of the vertical deviations of the surface.  
- `seeAlso`: list of uri pointing to additional resources about the item  
- `shadingDeviceType`: Specifies the type of shading device.  
- `solarReflectance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `solarTransmittance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  
- `thermalTransmittance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `type`: It must be equal to `ShadingDevice`.  
- `visibleLightReflectance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
- `visibleLightTransmittance`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.  
  

Required properties  
- `id`  
- `type`  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
ShadingDevice:
    
  description: 'Shading devices are purpose built devices to protect from the sunlight, from natural light, or screening them from view. Shading devices can form part of the facade or can be mounted inside the building, they can be fixed or operable.'
    
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
    
    isExternal:
    
      description: Indication whether the element is designed for use in the exterior (TRUE) or not (FALSE). If (TRUE) it is an external element and faces the outside of the building.
    
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
    
              minhttps://github.com/smart-data-models/incubated/tree/master/SAREF/
    
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
    
    mechanicalOperated:
    
      description: 'Indication whether the element is operated machanically (TRUE) or not, i.e. manually (FALSE).'
    
      type: boolean
    
      x-ngsi:
    
        type: Property
    
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
    
    roughness:
    
      description: A measure of the vertical deviations of the surface.
    
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
    
    shadingDeviceType:
    
      description: Specifies the type of shading device.
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    solarReflectance:
    
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
    
    solarTransmittance:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    source:
    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    thermalTransmittance:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    type:
    
      description: It must be equal to `ShadingDevice`.
    
      enum:
    
        - ShadingDevice
    
      type: string
    
      x-ngsi:
    
        type: Property
    
    visibleLightReflectance:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement.
    
      properties:
    
      title: Smart data models - Measurement schema
    
      type: object
    
      x-ngsi:
    
        type: Property
    
    visibleLightTransmittance:
    
      $id: https://smart-data-models.github.com/dataModel.SAREF4BLDG/Measurements/Measurement
    
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
    
  x-license-url: https://smart-data-models.github.com/dataModel.SAREF4BLDG/flat/s4bldg/ShadingDevice/LICENSE.md
    
  x-model-schema: https://smart-data-models.github.com/dataModel.SAREF4BLDG/ShadingDevices/ShadingDevice
    
  x-model-tags: SAREF ShadingDevice SMART DATA MODELS
    
  x-version: 0.0.2
    
```  
</details>    

## Example payloads    

#### ShadingDevice NGSI-v2 key-values Example    

Here is an example of a ShadingDevice in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ShadingDevice:03281d48-cb47-4061-9208-b2a380b3d7cd",
  
  "type": "ShadingDevice",
  
  "isExternal": false,
  
  "mechanicalOperated": true,
  
  "roughness": "Executive",
  
  "shadingDeviceType": "client-driven",
  
  "solarReflectance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T07:41:12Z",
  
      "value": 0.7901767410172098
  
    }
  
  },
  
  "solarTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T05:20:36Z",
  
      "value": 0.5537106205704284
  
    }
  
  },
  
  "thermalTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-26T10:52:46Z",
  
      "value": 0.9786915841160174
  
    }
  
  },
  
  "visibleLightReflectance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T08:26:06Z",
  
      "value": 0.7194478774053882
  
    }
  
  },
  
  "visibleLightTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T23:24:38Z",
  
      "value": 0.8973320246848571
  
    }
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:3f4442cb-0f79-4dad-81ba-69879612f561",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:de04c9b6-2d78-491f-987a-085ea71f747b",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:fd063381-99e7-4b7d-8936-cd66932ba1e7",
  
    "urn:ngsi-ld:System:5bfac8cc-a08e-4bc8-a9e8-474e8db84d73",
  
    "urn:ngsi-ld:System:a4eef133-5e5d-4051-8b37-bf89e468f019"
  
  ],
  
  "hasManufacturer": "ShadingDevice Company Inc.",
  
  "hasModel": "ShadingDevice 0.1.2",
  
  "dateCreated": "2023-01-26T07:18:28Z",
  
  "dateModified": "2023-01-26T08:58:08Z",
  
  "source": "Import",
  
  "name": "ShadingDevice",
  
  "alternateName": "ShadingDevice type 2",
  
  "description": "ShadingDevice of limited ShadingDevice types",
  
  "dataProvider": "IFC file"
  
}  
```  

#### ShadingDevice NGSI-v2 normalized Example    

Here is an example of a ShadingDevice in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ShadingDevice:b3c3bd8f-6f5a-400a-b43c-99c32bf7d036",
  
  "type": "ShadingDevice",
  
  "isExternal": {
  
    "type": "Boolean",
  
    "value": true
  
  },
  
  "mechanicalOperated": {
  
    "type": "Boolean",
  
    "value": false
  
  },
  
  "roughness": {
  
    "type": "Text",
  
    "value": "Home Loan Account"
  
  },
  
  "shadingDeviceType": {
  
    "type": "Text",
  
    "value": "program"
  
  },
  
  "solarReflectance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-25T15:36:19Z",
  
      "value": 0.23462582512353236
  
    }
  
  },
  
  "solarTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T08:44:29Z",
  
      "value": 0.569468324137257
  
    }
  
  },
  
  "thermalTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "Kelvin",
  
      "observedAt": "2023-01-26T01:57:38Z",
  
      "value": 0.315308180363743
  
    }
  
  },
  
  "visibleLightReflectance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T10:33:11Z",
  
      "value": 0.6167477347282538
  
    }
  
  },
  
  "visibleLightTransmittance": {
  
    "type": "Measurement",
  
    "value": {
  
      "unitCode": "NA",
  
      "observedAt": "2023-01-26T05:44:49Z",
  
      "value": 0.27849116636487137
  
    }
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:BuildingSpace:6d6d4b35-2d0f-4590-bd7d-1e5cdc1d71fe"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "value": "urn:ngsi-ld:PhysicalObject:ff501e6f-1fbf-4dd4-9537-b3b6668f156b"
  
  },
  
  "isSubSystemOf": {
  
    "type": "array",
  
    "value": [
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:6d7f1004-c306-4d6b-8b95-d661e62087df"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:9eedb406-9b0a-466e-99bf-d8b4721af694"
  
      },
  
      {
  
        "type": "Relationship",
  
        "value": "urn:ngsi-ld:System:c485e374-da84-4bff-8a79-7d35bdcd0dab"
  
      }
  
    ]
  
  },
  
  "hasManufacturer": {
  
    "type": "Text",
  
    "value": "ShadingDevice Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Text",
  
    "value": "ShadingDevice 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "DateTime",
  
    "value": "2023-01-25T15:18:47.9518072+01:00"
  
  },
  
  "dateModified": {
  
    "type": "DateTime",
  
    "value": "2023-01-26T11:03:03.3618393+01:00"
  
  },
  
  "source": {
  
    "type": "Text",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Text",
  
    "value": "ShadingDevice"
  
  },
  
  "alternateName": {
  
    "type": "Text",
  
    "value": "ShadingDevice type 2"
  
  },
  
  "description": {
  
    "type": "Text",
  
    "value": "ShadingDevice of limited ShadingDevice types"
  
  },
  
  "dataProvider": {
  
    "type": "Text",
  
    "value": "IFC file"
  
  }
  
}  
```  

#### ShadingDevice NGSI-LD key-values Example    

Here is an example of a ShadingDevice in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ShadingDevice:fdd38aff-18fa-4d70-95e1-2eda4e2e4b60",
  
  "type": "ShadingDevice",
  
  "isExternal": true,
  
  "mechanicalOperated": true,
  
  "roughness": "e-business",
  
  "shadingDeviceType": "mesh",
  
  "solarReflectance": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T21:45:04Z",
  
    "value": 0.8186065241444531
  
  },
  
  "solarTransmittance": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T16:26:13Z",
  
    "value": 0.9555116125193948
  
  },
  
  "thermalTransmittance": {
  
    "type": "Measurement",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-26T02:54:04Z",
  
    "value": 0.3325399259588544
  
  },
  
  "visibleLightReflectance": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-25T17:08:46Z",
  
    "value": 0.6046803587821626
  
  },
  
  "visibleLightTransmittance": {
  
    "type": "Measurement",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T04:35:02Z",
  
    "value": 0.41623913691201087
  
  },
  
  "isContainedInBuildingSpace": "urn:ngsi-ld:BuildingSpace:7b5ba6bb-4bb5-45bf-a6b3-fff2882604e5",
  
  "isContainedInPhysicalObject": "urn:ngsi-ld:PhysicalObject:10faee1b-dc34-410f-989d-214ddb0032fd",
  
  "isSubSystemOf": [
  
    "urn:ngsi-ld:System:e596e688-13a1-476a-9467-4677ccc91bd8",
  
    "urn:ngsi-ld:System:104487be-296d-4ddc-88fc-d0478ab47bb0",
  
    "urn:ngsi-ld:System:f98a7d93-dee0-4c5e-894a-54cf347a99f5"
  
  ],
  
  "hasManufacturer": "ShadingDevice Company Inc.",
  
  "hasModel": "ShadingDevice 0.1.2",
  
  "dateCreated": "2023-01-25T15:52:03Z",
  
  "dateModified": "2023-01-25T16:48:40Z",
  
  "source": "Import",
  
  "name": "ShadingDevice",
  
  "alternateName": "ShadingDevice type 2",
  
  "description": "ShadingDevice of limited ShadingDevice types",
  
  "dataProvider": "IFC file",
  
  "@context": [
  
    "https://raw.githubusercontent.com/smart-data-models/incubated/master/SAREF/context.jsonld",
  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  
  ]
  
}  
```  

#### ShadingDevice NGSI-LD normalized Example    

Here is an example of a ShadingDevice in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

```json  

{
  
  "id": "urn:ngsi-ld:ShadingDevice:98dd5d05-db70-4ebb-a39c-e286063cb137",
  
  "type": "ShadingDevice",
  
  "isExternal": {
  
    "type": "Property",
  
    "value": true
  
  },
  
  "mechanicalOperated": {
  
    "type": "Property",
  
    "value": true
  
  },
  
  "roughness": {
  
    "type": "Property",
  
    "value": "Practical Rubber Cheese"
  
  },
  
  "shadingDeviceType": {
  
    "type": "Property",
  
    "value": "parsing"
  
  },
  
  "solarReflectance": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T03:37:18Z",
  
    "value": 0.378910710384914
  
  },
  
  "solarTransmittance": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T09:24:57Z",
  
    "value": 0.9404860966072789
  
  },
  
  "thermalTransmittance": {
  
    "type": "Property",
  
    "unitCode": "Kelvin",
  
    "observedAt": "2023-01-26T12:37:04Z",
  
    "value": 0.471443015298326
  
  },
  
  "visibleLightReflectance": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T06:09:46Z",
  
    "value": 0.7789148596577641
  
  },
  
  "visibleLightTransmittance": {
  
    "type": "Property",
  
    "unitCode": "NA",
  
    "observedAt": "2023-01-26T05:43:18Z",
  
    "value": 0.9110422065316075
  
  },
  
  "isContainedInBuildingSpace": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:BuildingSpace:0bfda01f-c7bd-4db3-9a81-cfeb051cf629"
  
  },
  
  "isContainedInPhysicalObject": {
  
    "type": "Relationship",
  
    "object": "urn:ngsi-ld:PhysicalObject:53171831-ae73-45fa-8f15-b1c034e5b2af"
  
  },
  
  "isSubSystemOf": [
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:b9d614e5-32c2-47cd-b5ba-23b2c8ed67ea"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:6048cde5-df44-4963-b770-29ace8711405"
  
    },
  
    {
  
      "type": "Relationship",
  
      "object": "urn:ngsi-ld:System:e2c351bf-c825-4bc9-a7ca-dc96552b8e38"
  
    }
  
  ],
  
  "hasManufacturer": {
  
    "type": "Property",
  
    "value": "ShadingDevice Company Inc."
  
  },
  
  "hasModel": {
  
    "type": "Property",
  
    "value": "ShadingDevice 0.1.2"
  
  },
  
  "dateCreated": {
  
    "type": "Property",
  
    "value": "2023-01-25T15:37:39Z"
  
  },
  
  "dateModified": {
  
    "type": "Property",
  
    "value": "2023-01-25T17:44:25Z"
  
  },
  
  "source": {
  
    "type": "Property",
  
    "value": "Import"
  
  },
  
  "name": {
  
    "type": "Property",
  
    "value": "ShadingDevice"
  
  },
  
  "alternateName": {
  
    "type": "Property",
  
    "value": "ShadingDevice type 2"
  
  },
  
  "description": {
  
    "type": "Property",
  
    "value": "ShadingDevice of limited ShadingDevice types"
  
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

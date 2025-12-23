<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: TourismPresenceObserved  
========================
<!-- /10-Header -->

  
<!-- 20-Description -->
  

Global description: **Hourly observation of visitor presence at a specific location (municipality), segmented by nationality. Each entity represents one hour of observation.**  

version: 0.0.0
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  

- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government
- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
- `locationCode[string]`: Official code of the location/municipality (e.g., DICOFRE code in Portugal). Model: [https://schema.org/Text](https://schema.org/Text)
- `locationName[*]`: Name of the location
- `aggregationType[string]`: Type of aggregation used for this hourly observation. Enum: 'hourly_sum, hourly_average, hourly_snapshot, hourly_estimate'. Model: [https://schema.org/Text](https://schema.org/Text)
- `alternateName[string]`: An alternative name for this item
- `areaServed[string]`: The geographic area where a service or offered item is provided. Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
- `dateObserved[date-time]`: The date and time of this hourly observation in ISO8601 UTC format. Should represent the middle of the hour (e.g., 10:30 for the 10:00-10:59 period). Model: [https://schema.org/DateTime](https://schema.org/DateTime)
- `description[string]`: A description of this item
- `hour[number]`: Hour of the day (0-23) for this observation. Model: [https://schema.org/Number](https://schema.org/Number)
- `id[*]`: Unique identifier of the entity. For example: urn:ngsi-ld:TourismPresenceObserved:PT:1106:ES:20251113T10
- `name[string]`: The name of this item
- `nationality[string]`: Nationality of visitors. ISO 3166-1 alpha-2 country code (e.g., ES, FR, GB, PT). Model: [https://schema.org/Text](https://schema.org/Text)
- `nationalityName[string]`: Full name of the nationality country (optional, for human readability). Model: [https://schema.org/Text](https://schema.org/Text)
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object
- `type[string]`: NGSI Entity type. It has to be TourismPresenceObserved
- `visitorCount[number]`: Number of visitors observed during this specific hour. Units: 'persons'. Model: [https://schema.org/Number](https://schema.org/Number)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Required properties  
- `id`  
- `type`  
- `dateObserved`  
- `location`  
- `locationCode`
- `nationality`
- `visitorCount`
- `hour`
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
TourismPresenceObserved:
  description: Hourly observation of visitor presence at a specific location, segmented by nationality
  properties:
    aggregationType:
      description: Type of aggregation used for this hourly observation
      enum:
        - hourly_sum
        - hourly_average
        - hourly_snapshot
        - hourly_estimate
      type: string
      x-ngsi:
        model: https://schema.org/Text
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
      description: A sequence of characters identifying the provider of the harmonised data entity
      type: string
      x-ngsi:
        type: Property
    dateCreated:
      description: Entity creation timestamp. This will usually be allocated by the storage platform
      format: date-time
      type: string
      x-ngsi:
        type: Property
    dateModified:
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
      format: date-time
      type: string
      x-ngsi:
        type: Property
    dateObserved:
      description: The date and time of this hourly observation in ISO8601 UTC format
      format: date-time
      type: string
      x-ngsi:
        model: https://schema.org/DateTime
        type: Property
    description:
      description: A description of this item
      type: string
      x-ngsi:
        type: Property
    district:
      description: A district is a type of administrative division that, in some countries, is managed by the local government
      type: string
      x-ngsi:
        type: Property
    hour:
      description: Hour of the day (0-23) for this observation
      maximum: 23
      minimum: 0
      type: integer
      x-ngsi:
        model: https://schema.org/Number
        type: Property
    id:
      anyOf:
        - description: Identifier format of any NGSI entity
          maxLength: 256
          minLength: 1
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          type: string
        - description: Identifier format of any NGSI entity
          format: uri
          type: string
      description: Unique identifier of the entity
      x-ngsi:
        type: Property
    location:
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
      oneOf:
        - description: Geojson reference to the item. Point
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
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. LineString
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
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. Polygon
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
          x-ngsi:
            type: GeoProperty
      x-ngsi:
        type: GeoProperty
    locationCode:
      description: Official code of the location/municipality
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    locationName:
      description: Name of the location
      type: string
      x-ngsi:
        type: Property
    name:
      description: The name of this item
      type: string
      x-ngsi:
        type: Property
    nationality:
      description: Nationality of visitors. ISO 3166-1 alpha-2 country code
      pattern: ^[A-Z]{2}$
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    nationalityName:
      description: Full name of the nationality country
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    source:
      description: A sequence of characters giving the original source of the entity data as a URL
      type: string
      x-ngsi:
        type: Property
    type:
      description: NGSI Entity type. It has to be TourismPresenceObserved
      enum:
        - TourismPresenceObserved
      type: string
      x-ngsi:
        type: Property
    visitorCount:
      description: Number of visitors observed during this specific hour
      minimum: 0
      type: integer
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: persons
  required:
    - id
    - type
    - dateObserved
    - location
    - locationCode
    - nationality
    - visitorCount
    - hour
  type: object

```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads

#### TourismPresenceObserved NGSI-LD key-values Example

Here is an example of a TourismPresenceObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when using `options=keyValues` and returns the context data of an individual entity.

<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:1106:ES:20251113T10",
  "type": "TourismPresenceObserved",
  "dateObserved": "2025-11-13T10:30:00Z",
  "hour": 10,
  "location": {
    "type": "Point",
    "coordinates": [-9.1393, 38.7223]
  },
  "locationCode": "1106",
  "locationName": "Lisboa",
  "district": "Lisboa",
  "nationality": "ES",
  "nationalityName": "Spain",
  "visitorCount": 1456,
  "aggregationType": "hourly_sum",
  "dataProvider": "MEO",
  "source": "https://api.meo.pt/tourism/v1/count_geo",
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  ]
}
```
</details>

#### TourismPresenceObserved NGSI-LD normalized Example    

Here is an example of a TourismPresenceObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{
  "id": "urn:ngsi-ld:TourismPresenceObserved:PT:1106:ES:20251113T10",
  "type": "TourismPresenceObserved",
  "dateObserved": "2025-11-13T10:30:00Z",
  "hour": 10,
  "location": {
    "type": "Point",
    "coordinates": [
      -9.1393,
      38.7223
    ]
  },
  "locationCode": "1106",
  "locationName": "Lisboa",
  "district": "Lisboa",
  "nationality": "ES",
  "nationalityName": "Spain",
  "visitorCount": 1456,
  "aggregationType": "hourly_sum",
  "dataProvider": "MEO",
  "source": "https://api.meo.pt/tourism/v1/count_geo"
}
```  
</details>  

</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 97-LastFooter -->
  
---
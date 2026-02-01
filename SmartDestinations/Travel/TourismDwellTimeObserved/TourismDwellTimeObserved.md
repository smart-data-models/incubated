<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: TourismDwellTimeObserved  
========================
<!-- /10-Header -->

  
<!-- 20-Description -->
  

Global description: **Hourly observation of visitor dwell time (permanence duration) at a specific location (municipality), segmented by nationality and range of permanence time. Each entity represents one hour of observation with the range of dwell time.**

version: 0.0.0
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  

- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
- `locationCode[string]`: Official code of the location/municipality (e.g., DICOFRE code in Portugal). Model: [https://schema.org/Text](https://schema.org/Text)
- `locationName[string]`: Name of the location
- `aggregationType[string]`: Type of aggregation used for this hourly observation. Enum: 'hourly_sum, hourly_average, hourly_snapshot, hourly_estimate'. Model: [https://schema.org/Text](https://schema.org/Text)
- `alternateName[string]`: An alternative name for this item
- `areaServed[string]`: The geographic area where a service or offered item is provided. Model: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
- `dateObserved[date-time]`: The date and time of this hourly observation in ISO8601 UTC format. Should represent the middle of the hour (e.g., 10:30 for the 10:00-10:59 period). Model: [https://schema.org/DateTime](https://schema.org/DateTime)
- `description[string]`: A description of this item
- `dwellTimeRange[string]`: Number of visitors with dwell time between a range. For example: 0-5 Model: [https://schema.org/Number](https://schema.org/Number)
- `hour[number]`: Hour of the day (0-23) for this observation. Model: [https://schema.org/Number](https://schema.org/Number)
- `id[*]`: Unique identifier of the entity. For example: urn:ngsi-ld:TourismDwellTimeObserved:PT:1106:ES:20251113T10
- `name[string]`: The name of this item
- `nationality[string]`: Nationality of visitors. ISO 3166-1 alpha-2 country code (e.g., ES, FR, GB, PT). Model: [https://schema.org/Text](https://schema.org/Text)
- `nationalityName[string]`: Full name of the nationality country (optional, for human readability). Model: [https://schema.org/Text](https://schema.org/Text)
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object
- `totalVisitors[number]`: Total number of visitors across all dwell time ranges for this hour. Model: [https://schema.org/Number](https://schema.org/Number)
- `type[string]`: NGSI Entity type. It has to be TourismDwellTimeObserved
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Required properties  
- `id`  
- `type`  
- `dateObserved`  
- `location`  
- `locationCode`
- `dwellTimeRange`
- `nationality`
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
TourismDwellTimeObserved:
  description: Hourly observation of visitor dwell time at a specific location, segmented by nationality
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
    dwellTimeRange:
      description: 'Dwell time range in minutes. Format: min-max or max+ (e.g., 0-5, 5-15, 120+)'
      type: string
      x-ngsi:
        model: https://schema.org/Text
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
    totalVisitors:
      description: Total number of visitors across all dwell time ranges
      minimum: 0
      type: integer
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: persons
    type:
      description: NGSI Entity type. It has to be TourismDwellTimeObserved
      enum:
        - TourismDwellTimeObserved
      type: string
      x-ngsi:
        type: Property
    visitorCount:
      description: Number of visitors in this specific dwell time range
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
    - hour
    - dwellTimeRange
    - visitorCount
  type: object
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads

#### TourismDwellTimeObserved NGSI-LD key-values Example

Here is an example of a TourismDwellTimeObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when using `options=keyValues` and returns the context data of an individual entity.

<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:IT:20241231T01:30-60",
  "type": "TourismDwellTimeObserved",
  "dateObserved": "2024-12-31T01:30:00Z",
  "hour": 1,
  "location": {
    "type": "Point",
    "coordinates": [-8.7613, 41.3879]
  },
  "locationCode": "CO1313",
  "locationName": "Póvoa de Varzim",
  "nationality": "IT",
  "nationalityName": "Italy",
  "dwellTimeRange": "30-60",
  "visitorCount": 7,
  "aggregationType": "hourly_sum",
  "dataProvider": "MEO",
  "source": "https://api.meo.pt/tourism/v1/permanence_geo",
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  ]
}
```
</details>

#### TourismDwellTimeObserved NGSI-LD normalized Example    

Here is an example of a TourismDwellTimeObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

<details><summary><strong>show/hide example</strong></summary>    

# TourismDwellTimeObserved - Examples with dwellTimeRange

---

## NGSI-LD Normalized Example

```json
{
  "id": "urn:ngsi-ld:TourismDwellTimeObserved:PT:CO1313:IT:20241231T01:30-60",
  "type": "TourismDwellTimeObserved",
  "dateObserved": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2024-12-31T01:30:00Z"
    }
  },
  "hour": {
    "type": "Property",
    "value": 1
  },
  "location": {
    "type": "GeoProperty",
    "value": {
      "type": "Point",
      "coordinates": [-8.7613, 41.3879]
    }
  },
  "locationCode": {
    "type": "Property",
    "value": "CO1313"
  },
  "locationName": {
    "type": "Property",
    "value": "Póvoa de Varzim"
  },
  "nationality": {
    "type": "Property",
    "value": "IT"
  },
  "nationalityName": {
    "type": "Property",
    "value": "Italy"
  },
  "dwellTimeRange": {
    "type": "Property",
    "value": "30-60"
  },
  "visitorCount": {
    "type": "Property",
    "value": 7,
  },
  "aggregationType": {
    "type": "Property",
    "value": "hourly_sum"
  },
  "dataProvider": {
    "type": "Property",
    "value": "MEO"
  },
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  ]
}
```
</details>

</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 97-LastFooter -->
  
---  
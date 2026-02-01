<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entity: ElectricVehicleMobility  
========================
<!-- /10-Header -->

  
<!-- 20-Description -->
  

Global description: **Daily observation of electric vehicle mobility patterns aggregated by location, vehicle brand, and geographic region. Each entity represents the average distance traveled by electric vehicles of a specific brand in a municipality during a specific day.**

version: 0.0.1
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  

- `alternateName[string]`: An alternative name for this item
- `areaServed[string]`: The geographic area where a service or offered item is provided. Model: [https://schema.org/Text](https://schema.org/Text)
- `averageDistanceKm[number]`: Average distance traveled by vehicles in kilometers during the observation period. Units: 'kilometers'. Model: [https://schema.org/Number](https://schema.org/Number)
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
- `dateObserved[date]`: The date of this observation in ISO8601 format (YYYY-MM-DD). Model: [https://schema.org/Date](https://schema.org/Date)
- `description[string]`: A description of this item
- `deviceBrand[string]`: Brand or manufacturer of the electric vehicle. Model: [https://schema.org/Text](https://schema.org/Text)
- `district[string]`: Name of the district where the observation was made. Model: [https://schema.org/Text](https://schema.org/Text)
- `id[*]`: Unique identifier of the entity. For example: urn:ngsi-ld:ElectricVehicleMobility:PT:0402:TESLA:20251016
- `location[*]`: Geojson reference to the municipality location. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
- `locationCode[string]`: Official code of the municipality where the observation was made. Model: [https://schema.org/Text](https://schema.org/Text)
- `municipality[string]`: Name of the municipality where the observation was made. Model: [https://schema.org/Text](https://schema.org/Text)
- `n[number]`: Number of observations or samples used to calculate the average distance. Model: [https://schema.org/Number](https://schema.org/Number)
- `name[string]`: The name of this item
- `region[string]`: Name of the region where the observation was made (e.g., CONTINENTE, AÇORES, MADEIRA). Model: [https://schema.org/Text](https://schema.org/Text)
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object
- `type[string]`: NGSI Entity type. It has to be ElectricVehicleMobility
- `vehicleType[string]`: Type of electric vehicle. Enum: 'BEV, PHEV, HEV, FCEV, unknown'. Model: [https://schema.org/Text](https://schema.org/Text)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Required properties  
- `id`  
- `type`  
- `dateObserved`  
- `region`
- `locationCode`
- `municipality`
- `deviceBrand`
- `averageDistanceKm`
- `n`
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
ElectricVehicleMobility:
  description: Daily observation of electric vehicle mobility patterns aggregated by location and vehicle brand
  properties:
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
    averageDistanceKm:
      description: Average distance traveled by vehicles in kilometers during the observation period
      minimum: 0
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: kilometers
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
      description: The date of this observation in ISO8601 format (YYYY-MM-DD)
      format: date
      type: string
      x-ngsi:
        model: https://schema.org/Date
        type: Property
    description:
      description: A description of this item
      type: string
      x-ngsi:
        type: Property
    deviceBrand:
      description: Brand or manufacturer of the electric vehicle
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    district:
      description: Name of the district where the observation was made
      type: string
      x-ngsi:
        model: https://schema.org/Text
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
      description: Geojson reference to the municipality location. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
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
      description: Official code of the municipality where the observation was made
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    municipality:
      description: Name of the municipality where the observation was made
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    n:
      description: Number of observations or samples used to calculate the average distance
      minimum: 1
      type: integer
      x-ngsi:
        model: https://schema.org/Number
        type: Property
    name:
      description: The name of this item
      type: string
      x-ngsi:
        type: Property
    region:
      description: Name of the region where the observation was made
      enum:
        - CONTINENTE
        - AÇORES
        - MADEIRA
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
      description: NGSI Entity type. It has to be ElectricVehicleMobility
      enum:
        - ElectricVehicleMobility
      type: string
      x-ngsi:
        type: Property
    vehicleType:
      description: Type of electric vehicle
      enum:
        - BEV
        - PHEV
        - HEV
        - FCEV
        - unknown
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
  required:
    - id
    - type
    - dateObserved
    - region
    - locationCode
    - municipality
    - deviceBrand
    - averageDistanceKm
    - n
  type: object

```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads    

#### ElectricVehicleMobility NGSI-LD key-values Example    

Here is an example of a ElectricVehicleMobility in JSON-LD format as key-values. This is compatible with NGSI-LD when using `options=keyValues` and returns the context data of an individual entity.  

<details><summary><strong>show/hide example</strong></summary>    

```json  
{
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:0402:TESLA:20251016",
  "type": "ElectricVehicleMobility",
  "dateObserved": "2025-10-16",
  "region": "CONTINENTE",
  "district": "Bragança",
  "municipality": "Bragança",
  "locationCode": "0402",
  "location": {
    "type": "Point",
    "coordinates": [-6.7572, 41.8058]
  },
  "deviceBrand": "TESLA",
  "vehicleType": "BEV",
  "averageDistanceKm": 64.92,
  "n": 37,
  "dataProvider": "MEO",
  "source": "https://api.example.pt/ev-mobility/v1",
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  ]
}
```  
</details>

#### ElectricVehicleMobility NGSI-LD normalized Example    

Here is an example of a ElectricVehicleMobility in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  

<details><summary><strong>show/hide example</strong></summary>    

```json  
{
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:0402:TESLA:20251016",
  "type": "ElectricVehicleMobility",
  "dateObserved": {
    "type": "Property",
    "value": {
      "@type": "Date",
      "@value": "2025-10-16"
    }
  },
  "region": {
    "type": "Property",
    "value": "CONTINENTE"
  },
  "district": {
    "type": "Property",
    "value": "Bragança"
  },
  "municipality": {
    "type": "Property",
    "value": "Bragança"
  },
  "locationCode": {
    "type": "Property",
    "value": "0402"
  },
  "location": {
    "type": "GeoProperty",
    "value": {
      "type": "Point",
      "coordinates": [-6.7572, 41.8058]
    }
  },
  "deviceBrand": {
    "type": "Property",
    "value": "TESLA"
  },
  "vehicleType": {
    "type": "Property",
    "value": "BEV"
  },
  "averageDistanceKm": {
    "type": "Property",
    "value": 64.92,
    "unitCode": "KMT"
  },
  "n": {
    "type": "Property",
    "value": 37
  },
  "dataProvider": {
    "type": "Property",
    "value": "Portuguese Electric Vehicle Data Platform"
  },
  "source": {
    "type": "Property",
    "value": "https://api.example.pt/ev-mobility/v1"
  },
  "@context": [
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
  ]
}
```  
</details>

</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
**Note**: This data model captures daily aggregated electric vehicle mobility patterns. The `n` property indicates the sample size used for calculating the average distance, providing transparency about data quality and statistical significance.

**Vehicle Types**:
- BEV: Battery Electric Vehicle
- PHEV: Plug-in Hybrid Electric Vehicle
- HEV: Hybrid Electric Vehicle
- FCEV: Fuel Cell Electric Vehicle
- unknown: Vehicle type not specified
<!-- /90-FooterNotes -->
  
<!-- 97-LastFooter -->
  
---  

[Open issues](https://github.com/smart-data-models/dataModel.Transportation/issues)
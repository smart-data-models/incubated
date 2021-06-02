Entité : WeatherObserved  
========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Weather/blob/master/WeatherObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Une observation des conditions météorologiques à un endroit et à un moment donnés. Ce modèle de données a été développé en coopération avec les opérateurs mobiles et la GSMA.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved`: Date de l'entité observée définie par l'utilisateur.  - `description`: Une description de cet article  - `dewPoint`: Le point de rosée encodé comme un nombre  - `feelsLikesTemperature`: Appréciation de la température de l'objet  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `precipitation`: Quantité d'eau de pluie enregistrée. Unis : "Litres par mètre carré".  - `pressureTendency`: Enum : 'falling, raising, steady'. La pression est-elle en hausse ou en baisse ? Elle peut être exprimée en termes quantitatifs ou qualitatifs.  - `refDevice`: Une référence au(x) dispositif(s) qui a (ont) capturé cette observation.  - `relativeHumidity`: L'humidité dans l'air  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `snowHeight`: La hauteur de neige observée par les capteurs génériques de mesure de l'épaisseur de neige, exprimée en centimètres.  - `solarRadiation`: Le rayonnement solaire observé mesuré en Watts par carré  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `streamGauge`: L'élévation de la surface de l'eau observée par des capteurs de mesure hydrométrique, à savoir un [Stream Gauge] (https://en.wikipedia.org/wiki/Stream_gauge), exprimée en centimètres.  - `temperature`: Température de l'article  - `type`: Type d'entité NGSI. Il doit s'agir de WeatherObserved  - `uVIndexMax`: L'indice UV maximum pour la période, basé sur la mesure de l'indice UV de l'Organisation mondiale de la santé. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)    
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WeatherObserved:    
  description: 'An observation of weather conditions at a certain place and time. This data model has been developed in cooperation with mobile operators and the GSMA.'    
  properties:    
    address:    
      description: 'The mailing address'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    dewPoint:    
      description: 'The dew point encoded as a number'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Celsius degrees'    
    feelsLikesTemperature:    
      description: 'Temperature appreciation of the item'    
      type: Property    
    id:    
      anyOf: &weatherobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
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
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *weatherobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    precipitation:    
      description: 'Amount of water rain registered. Unis:''Liters per square meter''. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    pressureTendency:    
      description: 'Enum:''falling, raising, steady''. Is the pressure rising or falling? It can be expressed in quantitative terms or qualitative terms.'    
      oneOf:    
        - enum:    
            - raising    
            - falling    
            - steady    
          type: string    
        - type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the device(s) which captured this observation.'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    relativeHumidity:    
      description: 'Humidity in the Air'    
      maximum: 1    
      minimum: 0    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    snowHeight:    
      description: 'The snow height observed by generic snow depth measurement sensors, expressed in centimeters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: centimeters    
    solarRadiation:    
      description: 'The solar radiation observed measured in Watts per square'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: w/m2    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    streamGauge:    
      description: 'The water level surface elevation observed by Hydrometric measurement sensors, namely a [Stream Gauge](https://en.wikipedia.org/wiki/Stream_gauge) expressed in centimeters'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: centimeters    
    temperature:    
      description: 'Temperature of the item'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be WeatherObserved'    
      enum:    
        - WeatherObserved    
      type: Property    
    uVIndexMax:    
      description: 'The maximum UV index for the period, based on the World Health Organization''s UV Index measure. [http://www.who.int/uv/intersunprogramme/activities/uv_index/en/](http://www.who.int/uv/intersunprogramme/activities/uv_index/en/)'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
    - dateObserved    
    - location    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### WeatherObserved NGSI-v2 key-values Exemple  
Voici un exemple de WeatherObserved au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
  "type": "WeatherObserved",  
  "address": {  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "atmosphericPressure": 938.9,  
  "dataProvider": "TEF",  
  "dateObserved": "2016-11-30T07:00:00.00Z",  
  "location": {  
    "type": "Point",  
    "coordinates": [-4.754444444, 41.640833333]  
  },  
  "precipitation": 0,  
  "pressureTendency": 0.5,  
  "relativeHumidity": 1,  
  "source": "http://www.aemet.es",  
  "stationCode": "2422",  
  "stationName": "Valladolid",  
  "temperature": 3.3,  
  "windDirection": -45,  
  "windSpeed": 2,  
  "illuminance": 1000,  
  "refDevice": "device-0A3478",  
  "streamGauge": 50,  
  "snowHeight": 20,   
  "uvIndexMax": 1.0  
}  
```  
#### WeatherObserved NGSI-v2 normalisé Exemple  
Voici un exemple de WeatherObserved au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "Valladolid.2016-11-30T07-00-00.00Z",  
  "type": "WeatherObserved",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2016-11-30T07:00:00.00Z"  
  },  
  "illuminance": {  
    "type": "Number",  
    "value": 1000  
  },  
  "temperature": {  
    "type": "Number",  
    "value": 3.3  
  },  
  "precipitation": {  
    "type": "Number",  
    "value": 0  
  },  
  "atmosphericPressure": {  
    "type": "Number",  
    "value": 938.9  
  },  
  "pressureTendency": {  
    "type": "Number",  
    "value": 0.5  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "device-0A3478"  
  },  
  "source": {  
    "type": "Text",  
    "value": "http://www.aemet.es"  
  },  
  "windSpeed": {  
    "type": "Number",  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.754444444,  
        41.640833333  
      ]  
    }  
  },  
  "stationName": {  
    "type": "Text",  
    "value": "Valladolid"  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES"  
    }  
  },  
  "stationCode": {  
    "type": "Text",  
    "value": "2422"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "TEF"  
  },  
  "windDirection": {  
    "type": "Number",  
    "value": -45  
  },  
  "relativeHumidity": {  
    "type": "Number",  
    "value": 1  
  },  
  "streamGauge": {  
    "type": "Number",  
    "value": 50  
  },  
  "snowHeight": {  
    "type": "Number",  
    "value": 20  
  },  
  "uvIndexMax": {  
    "type": "Number",  
    "value": 1.0  
  }  
}  
```  
#### Valeurs-clés NGSI-LD WeatherObserved Exemple  
Voici un exemple de WeatherObserved au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
  "type": "WeatherObserved",  
  "dateObserved": "2016-11-30T07:00:00.00Z",  
  "illuminance": 1000,  
  "temperature": 3.3,  
  "precipitation": 0,  
  "atmosphericPressure": 938.9,  
  "pressureTendency": 0.5,  
  "refDevice": "urn:ngsi-ld:Device:device-0A3478",  
  "source": "http://www.aemet.es",  
  "windSpeed": 2,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -4.754444444,  
      41.640833333  
    ]  
  },  
  "stationName": "Valladolid",  
  "address": {  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "stationCode": "2422",  
  "dataProvider": "TEF",  
  "windDirection": -45,  
  "relativeHumidity": 1,  
  "streamGauge": 50,  
  "snowHeight": 20,  
  "uvIndexMax": 1.0,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### WeatherObserved NGSI-LD normalisé Exemple  
Voici un exemple de WeatherObserved au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-LD lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:WeatherObserved:Spain-WeatherObserved-Valladolid-2016-11-30T07:00:00.00Z",  
  "type": "WeatherObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-11-30T07:00:00.00Z"  
    }  
  },  
  "illuminance": {  
    "type": "Property",  
    "value": 1000  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 3.3  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 0  
  },  
  "atmosphericPressure": {  
    "type": "Property",  
    "value": 938.9  
  },  
  "pressureTendency": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:device-0A3478"  
  },  
  "source": {  
    "type": "Property",  
    "value": "http://www.aemet.es"  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 2  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.754444444,  
        41.640833333  
      ]  
    }  
  },  
  "stationName": {  
    "type": "Property",  
    "value": "Valladolid"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "type": "PostalAddress"  
    }  
  },  
  "stationCode": {  
    "type": "Property",  
    "value": "2422"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "TEF"  
  },  
  "windDirection": {  
    "type": "Property",  
    "value": -45  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 1  
  },  
  "streamGauge": {  
    "type": "Property",  
    "value": 50  
  },  
  "snowHeight": {  
    "type": "Property",  
    "value": 20  
  },  
  "uvIndexMax": {  
    "type": "Property",  
    "value": 1.0  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  

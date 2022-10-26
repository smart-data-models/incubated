<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Personne  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//incubated/blob/master/Person/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une personne (vivante, morte, non-morte ou fictive) mappée à partir de schema.org**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `additionalName[string]`: Un nom supplémentaire pour une personne, peut être utilisé comme deuxième prénom.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `email[string]`: Adresse électronique du propriétaire.  - `familyName[string]`: Nom de famille. Aux États-Unis, le nom de famille d'une personne.  . Model: [https://schema.org/Text](https://schema.org/Text)- `givenName[string]`: Prénom. Aux États-Unis, le prénom d'une personne.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `telephone[string]`: Le numéro de téléphone.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Il doit être égal à Personne. Type NGSI  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Person:    
  description: 'A person (alive, dead, undead, or fictional) mapped from schema.org'    
  properties:    
    additionalName:    
      description: 'An additional name for a Person, can be used for a middle name.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    email:    
      description: 'Email address of owner.'    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    familyName:    
      description: 'Family name. In the U.S., the last name of a Person.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    givenName:    
      description: 'Given name. In the U.S., the first name of a Person.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &person_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *person_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    telephone:    
      description: 'The telephone number.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It must be equal to Person. NGSI type'    
      enum:    
        - Person    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://schema.org/Person    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/incubated/blob/master/Person/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Organization/Person/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Personne NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une personne au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:UZHW:27495447",  
  "type": "Person",  
  "dateCreated": "2022-05-07T06:43:37Z",  
  "dateModified": "2022-12-27T04:25:34Z",  
  "source": "",  
  "name": "CEO",  
  "alternateName": "",  
  "description": "",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:dataModel:items:WQPT:65442393",  
    "urn:ngsi-ld:dataModel:items:ALHV:33053523"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:dataModel:items:LHMU:67329694",  
    "urn:ngsi-ld:dataModel:items:MMZQ:64123812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.2403775,  
      170.070362  
    ]  
  },  
  "address": {  
    "streetAddress": "Franklinstrasse 13A",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10587",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "Worldwide",  
  "additionalName": "",  
  "familyName": "Ahle",  
  "givenName": "Ulrich",  
  "telephone": "+491741533348",  
  "email": "info@fiware.org"  
}  
```  
</details>  
#### Personne NGSI-v2 normalisée Exemple  
Voici un exemple de Personne au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:UZHW:27495447",  
  "type": "Person",  
  "dateCreated": {  
    "type": "Date-Time",  
    "value": "2022-05-07T06:43:37Z"  
  },  
  "dateModified": {  
    "type": "Date-Time",  
    "value": "2022-12-27T04:25:34Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "CEO"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "Web"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:dataModel:items:WQPT:65442393",  
      "urn:ngsi-ld:dataModel:items:ALHV:33053523"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:dataModel:items:LHMU:67329694",  
      "urn:ngsi-ld:dataModel:items:MMZQ:64123812"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        52.52,  
        13.4050  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Franklinstrasse 13A",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10587",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Worldwide"  
  },  
  "additionalName": {  
    "type": "Text",  
    "value": ""  
  },  
  "familyName": {  
    "type": "Text",  
    "value": "Ahle"  
  },  
  "givenName": {  
    "type": "Text",  
    "value": "Ulrich"  
  },  
  "telephone": {  
    "type": "Text",  
    "value": "+491741533348"  
  },  
  "email": {  
    "type": "Text",  
    "value": "info@fiware.org"  
  },  
  "@context": [  
    "https://smartdatamodels.org/dataModel.Organization/context.jsonld"  
  ]  
}  
```  
</details>  
#### Personne NGSI-LD valeurs-clés Exemple  
Voici un exemple d'une personne au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:UZHW:27495447",  
  "type": "Person",  
  "dateCreated": "2022-05-07T06:43:37Z",  
  "dateModified": "2022-12-27T04:25:34Z",  
  "source": "",  
  "name": "CEO",  
  "alternateName": "",  
  "description": "",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:dataModel:items:WQPT:65442393",  
    "urn:ngsi-ld:dataModel:items:ALHV:33053523"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:dataModel:items:LHMU:67329694",  
    "urn:ngsi-ld:dataModel:items:MMZQ:64123812"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      40.2403775,  
      170.070362  
    ]  
  },  
  "address": {  
    "streetAddress": "Franklinstrasse 13A",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10587",  
    "postOfficeBoxNumber": ""  
  },  
  "areaServed": "Worldwide",  
  "additionalName": "",  
  "familyName": "Ahle",  
  "givenName": "Ulrich",  
  "telephone": "+491741533348",  
  "email": "info@fiware.org",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### Personne NGSI-LD normalisée Exemple  
Voici un exemple de Personne au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataModel:id:UZHW:27495447",  
  "type": "Person",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-05-07T06:43:37Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2022-12-27T04:25:34Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "CEO"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Web"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:dataModel:items:WQPT:65442393",  
      "urn:ngsi-ld:dataModel:items:ALHV:33053523"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:dataModel:items:LHMU:67329694",  
      "urn:ngsi-ld:dataModel:items:MMZQ:64123812"  
    ]  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        52.52,  
        13.4050  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Franklinstrasse 13A",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10587",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Worldwide"  
  },  
  "additionalName": {  
    "type": "Property",  
    "value": ""  
  },  
  "familyName": {  
    "type": "Property",  
    "value": "Ahle"  
  },  
  "givenName": {  
    "type": "Property",  
    "value": "Ulrich"  
  },  
  "telephone": {  
    "type": "Property",  
    "value": "+491741533348"  
  },  
  "email": {  
    "type": "Property",  
    "value": "info@fiware.org"  
  },  
  "@context": [  
    "https://smartdatamodels.org/dataModel.Organization/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Modèles de données intelligents](https://smartdatamodels.org) +++ [Manuel de contribution](https://bit.ly/contribution_manual) +++ [À propos](https://bit.ly/Introduction_SDM)  
<!-- /97-LastFooter -->  

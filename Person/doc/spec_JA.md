<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ個人  
========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//incubated/blob/master/Person/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**schema.orgからマップされた人物（生きている、死んでいる、死んでいない、または架空の）**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `additionalName[string]`: ミドルネームとして使用することができます。  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `email[string]`: 所有者のEメールアドレス。  - `familyName[string]`: ファミリーネーム。米国では、人物の姓。  . Model: [https://schema.org/Text](https://schema.org/Text)- `givenName[string]`: Given nameの略。米国では、人物のファーストネーム。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `telephone[string]`: 電話番号のことです。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Personと等しくなければならない。NGSIタイプ  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### 人物 NGSI-v2 キー値例  
ここでは、PersonをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 人物 NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のPersonの例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 人物 NGSI-LD キー値 例  
ここでは、PersonをJSON-LD形式でkey-valuesにした例を示す。これは `options=keyValues` を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### 人物 NGSI-LD正規化例  
以下は、正規化されたJSON-LD形式のPersonの例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[スマートデータモデル](https://smartdatamodels.org) +++ [寄稿マニュアル](https://bit.ly/contribution_manual) +++ [バージョン情報](https://bit.ly/Introduction_SDM)  
<!-- /97-LastFooter -->  

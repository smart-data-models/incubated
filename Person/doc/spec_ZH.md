<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。个人  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//incubated/blob/master/Person/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**一个人（活的、死的、不死的或虚构的）从模式.org中映射出来**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `additionalName[string]`: 一个人的附加名称，可用于中间名。  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `email[string]`: 业主的电子邮件地址。  - `familyName[string]`: 姓氏。在美国，一个人的姓氏。  . Model: [https://schema.org/Text](https://schema.org/Text)- `givenName[string]`: 名字。在美国，一个人的名字。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `telephone[string]`: 的电话号码。  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: 它必须等于人。NGSI类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
## ＃＃＃＃有效载荷的例子  
#### Person NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的Person的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### 人NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的人的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### Person NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的Person的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### 人NGSI-LD正常化的例子  
下面是一个JSON-LD格式的人的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[智能数据模型](https://smartdatamodels.org) +++ [贡献手册](https://bit.ly/contribution_manual) +++ [关于](https://bit.ly/Introduction_SDM)  
<!-- /97-LastFooter -->  

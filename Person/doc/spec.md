<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: Person  
==============<!-- /10-Header -->  
<!-- 15-Header -->  
[Open License](https://github.com/smart-data-models//incubated/blob/master/Person/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-Header -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- No required properties  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### Person NGSI-v2 key-values Example    
Here is an example of a Person in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Person NGSI-v2 normalized Example    
Here is an example of a Person in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### Person NGSI-LD key-values Example    
Here is an example of a Person in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### Person NGSI-LD normalized Example    
Here is an example of a Person in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  

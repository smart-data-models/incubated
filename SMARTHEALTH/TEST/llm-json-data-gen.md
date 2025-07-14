test json data generation using LLM

Below is an example of how you might generate JSON data using a language model like hermes3:8b, through ollama.

**prompt** >>> "ngsi-ld hl7 patient json schema content"
provide a json output about a patient named "Archibald Tuttle", fill other properties with random 
... content, don't exceed 256 characters in strings properties 

- **response**:
```json
{
  "id": "urn:ngsi-ld:Patient:archie-tuttle",
  "type": "Patient",
  "name": [
    {
      "value": "Archibald Tuttle"
    }
  ],
  "birthDate": "1990-04-05",
  "gender": "male",
  "address": {
    "streetAddress": "123 Maple Ln",
    "city": "Springfield",
    "postalCode": "62704",
    "country": "USA"
  },
  "contactPoint": [
    {
      "telephone": "+1-555-2345",
      "use": "mobile"
    }
  ],
  "height": 180,
  "weight": 75.0,
  "photo": [
    {
      "href": "https://example.com/archie-photo.jpg"
    }
  ],
  "communication": [
    {
      "language": {
        "value": "English",
        "code": "en"
      },
      "prefrred": true
    }
  ]
}
```

**prompt** >>> nice just correct "prefrred" property with "preferred" !
- **response**:
```json
{
  "id": "urn:ngsi-ld:Patient:archie-tuttle",
  "type": "Patient",
  "name": [
    {
      "value": "Archibald Tuttle"
    }
  ],
  "birthDate": "1990-04-05",
  "gender": "male",
  "address": {
    "streetAddress": "123 Maple Ln",
    "city": "Springfield",
    "postalCode": "62704",
    "country": "USA"
  },
  "contactPoint": [
    {
      "telephone": "+1-555-2345",
      "use": "mobile"
    }
  ],
  "height": 180,
  "weight": 75.0,
  "photo": [
    {
      "href": "https://example.com/archie-photo.jpg"
    }
  ],
  "communication": [
    {
      "language": {
        "value": "English",
        "code": "en"
      },
      "preferred": true
    }
  ]
}
```

**prompt** >>> give me another json content for a patient living in Nice, France, set the related properties according

- **response**:
```json
{
  "id": "urn:ngsi-ld:Patient:lucie-christine-martin",
  "type": "Patient",
  "name": [
    {
      "value": "Lucie Christine Martin"
    }
  ],
  "birthDate": "1985-02-14",
  "gender": "female",
  "address": {
    "streetAddress": "15 Rue des Fleurs",
    "city": "Nice",
    "postalCode": "06000",
    "country": "France"
  },
  "contactPoint": [
    {
      "telephone": "+33-6-1234-5678",
      "use": "mobile"
    }
  ],
  "height": 165,
  "weight": 58.0,
  "photo": [
    {
      "href": "https://example.com/lucie-photo.jpg"
    }
  ],
  "communication": [
    {
      "language": {
        "value": "French",
        "code": "fr"
      },
      "preferred": true
    }
  ]
}
```
**prompt** >>> Send a message (/? for help)

### I adjust a bit the ouput for markdown presentation, but truly the answer was good json !
### **Smart Data Models Contribution Manual**

**Version:** Last update 17-12-2025 **A Global Program Led By:** FIWARE, IUDX, Tmforum, Open & Agile Smart Cities 

---

### **1. Agenda**

* Overview on the Smart Data Models 

* Ways of contribution 

* Contribution workflow 

* Pull requests 

* Acceptance criteria & guidelines 

* Documents to contribute 

* Common Mistakes 



---

### **2. Repository Architecture (Umbrella Repo)**

*This section reconstructs the hierarchy diagram shown on Page 3.* 

**Root:** `data-models` (Umbrella Repo) 

* **Domains Repositories:**
* Smart Water 


* Smart Cities 


* Smart Environment 


* Cross Sector 


* Smart Destinations 


* Smart Agrifood 


* Smart Energy 


* Smart Manufacturing 


* Smart Aeronautics 


* Smart Robotics 




* **Subject Repositories (Examples):**
* Subject 1 (sewage) 


* Subject 2 (parking) 


* Subject 3 (weather) 


* Subject 4 (Power Transformer) 




* **Lifecycle Management Repositories:**
* Incubated 


* Harmonization 





---

### **3. How to Contribute**

**Determine your case:**

1. 
**Case 1:** Extending an existing data model 


2. 
**Case 2:** Creating a data model from scratch 



**Search Tools:**

* Check if your model exists using the search tool.


* Search properties and descriptions (filtering by Property Name, dataModel, Subject, Data Type, etc.).


* If not found, email `info@smartdatamodels.org`.



#### **Contribution Workflow Logic**

*Reconstruction of the flowchart from Page 5.* 

1. **Do you have a use case?**
* 
**No:** Exception management.


* 
**Yes:** Search if the data model exists.




2. **If Data Model Exists (Update):**
* Create your proposal of update.


* Pull request on the **official repository** of the data model.


* **Manual Review:**
* 
*Pass:* Sign contribution agreement -> Publication process.


* 
*Fail:* Fix the comments and resubmit.






3. **If Data Model Does Not Exist (New Model):**
* 
**Option 1:** Access contribution manual and draft your data model (tool) in your repository.


* 
**Option 2 (Recommended):** Ask permission to contribute in the **incubated repository**.


* Work on the incubated repository and ask for support via issues/mail.




* 
**Submission:** Pull request on the incubated repository after completing the contribution checklist.


* **Manual Review:**
* 
*Pass:* Sign contribution agreement -> Publication process.


* 
*Fail:* Fix the comments.







---

### **4. Guidelines & Pull Requests**

#### **Where to do a Pull Request (PR)**

* 
**Case 1: Domain exists, Subject exists** 


1. PR on the **Subject** repo, including full documentation.
2. Reviewed by Subject Administrator.


* 
**Case 2: Domain exists, Subject does not exist** 


1. PR on **Incubated** folder, including full documentation.
2. Domain administrator decides if it is a new subject or existing one.


* 
**Case 3: Domain does not exist** 


1. PR on **Incubated** folder, including full documentation.
2. Management decides on new Domain creation.



#### **Repository Structure (Acceptance Criteria)**

*Reconstruction of the file tree image from Page 10.* 

```text
DataModel.Subject/
└── DataModel/
    ├── examples/
    │   ├── example.json
    │   ├── example.jsonld
    │   ├── example-normalized.json
    │   └── example-normalized.jsonld
    ├── schema.json
    ├── ADOPTERS.yaml
    ├── notes.yaml
    └── CONTRIBUTORS.yaml

```

**Required Files Description** 

| File Name | Location | Description |
| --- | --- | --- |
| **schema.json** | Root of subject | JSON schema format containing attributes, data types, and descriptions. |
| **examples** | /examples | `example.json` (Key-Values NGSIv2), `example-normalized.json` (Normalized NGSIv2), `example.jsonld` (Key-Values NGSI-LD), `example-normalized.jsonld` (Normalized NGSI-LD). |
| **notes.yaml** | Root | Customization messages for specifications (Header, Middle, Footer, Readme). |
| **ADOPTERS.yaml** | Root | Use cases of the data model. Mandatory existence but can be empty. |
| **CONTRIBUTORS.yaml** | Root of subject | Authors of the data model. |
| **notes_context.jsonld** | Root of subject | Optional IRIs for elements defined in data models when inherited from standards. |

---

### **5. Important Guidelines: Data Types & Syntax**

**Data Type Table** 

| Data type | NGSIv2 type | NGSI-LD type |
| --- | --- | --- |
| **string, number, object, array** | Text, Number, DateTime, StructuredValue | Property, GeoProperty, Relationship |
| **boolean** | Boolean |  |

**Syntax Rules** 

* Use **camelCase** for attribute names.
* **Entity type names** must start with a Capital letter (e.g., `WasteContainer`).
* Use **nouns** not verbs for attribute names (e.g., `totalSpotNumber` or `dateCreated`).
* Avoid plurals in attribute names, but state clearly when a list fits (e.g., `category`).

**Date-Time Attributes Example** 

**schema.json**

```json
"createdAt": {
    "type": "string",
    "format": "date-time",
    "description": "Property..."
}

```

**example-normalized.json**

```json
"createdAt": {
    "type": "DateTime",
    "value": "2022-06-01T07:00:00.00Z"
}

```

**example-normalized.jsonld**

```json
"createdAt": {
    "type": "Property",
    "value": {
        "@type": "DateTime",
        "@value": "2022-06-01T07:00:00.00Z"
    }
}

```

---

### **6. Drafting a Data Model**

**Ways to create `schema.json`:**

1. 
**From a Payload:** Use the Online JSON to JSON Schema Converter.


2. 
**From Scratch:** Use a Notepad/Editor (recommended for scratch builds).


3. 
**Schema Sheet:** Use the provided Google Sheets "Smart Data Models Schema sheet" (Recommended for simple models/low JSON knowledge).



**Validating the Schema:**

* Use the tool: `https://www.jsonschemavalidator.net/`.


* Paste your schema on the left and your payload (battery example) on the right to check for errors.



#### **Common/Shared Attributes**

Link shared elements to make models simpler.

* 
**GSMA-Commons:** `https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons`.


* 
*Includes:* `id`, `type`, `dateCreated`, `dateModified`, `name`, `description`, `owner`, `seeAlso`, `address`, `location`, etc. .





#### **Description Format**

Every first-level property must include a description in this specific order :

1. **Mandatory:** `Property` / `Relationship` / `GeoProperty`.
2. **Optional:** `Model:'[link]'`.
3. **Optional:** `Units:'[unit]'`.
4. **Optional:** `Enum:'item1, item2'`.
5. **Optional:** `Privacy:'[high/medium/low]'`.
6. **Optional:** `Multilingual:`.
7. **Mandatory:** A text description (>15 chars).

**Example:**

```json
"temperature":{
    "description": "Property. Model: 'http://schema.org/Number'. Units: 'Degrees centigrade'. Privacy: 'low'. Enum: 'tempNumber1, tempNumber2'. Temperature of the entity."
}

```

**Multilingual Attributes Example:** 

```json
"name_lang": {
    "type": "object",
    "description": "Property. Model: 'https:schema.org/Text'. Multilingual:. Text of the description",
    "properties": {
        "en": { "type": "string" },
        "fr": { "type": "string" },
        "es": { "type": "string" }
    }
}

```

**Privacy Attribute Options:** 

* **None (default):** No personal data.
* **High:** Ideology, religion, health, sexual life, racial origin.
* **Medium:** Financial solvency, personality/behavior evaluation.
* **Low:** Personal data different from the above (e.g., user device object).

**Enumeration Rule:** 
Use camelCase and strictly avoid spaces (unless mapping existing standards).

---

### **7. Testing Your Data Model**

Before submitting a PR, use the **"Test your data model"** tool.

* **Location:** Home -> Tools -> test your data model.
* 
**Input:** Github repository URL and Email.


* **Tests Performed:**
1. 
**Full check:** File structure, Schema documentation, Examples check, Other files check .




* 
**Output:** JSON or YAML report.



**The tool checks:** 

* **File structure:** URL reachable, schema.json exists, jsonld example exists.
* **Schema:** Valid JSON, right structure, metadata, external references, descriptions included.
* **Examples:** Validates `example.json` and `example-normalized.json`.
* **Other files:** Validates `notes.yaml` and `ADOPTERS.yaml`.

---

### **8. Common Mistakes**

1. Contributing NOT REQUESTED documents 

* 
**DO NOT contribute:** `spec.md`, `README.md`, `model.yaml`, `CSV exports` (these are auto-generated) .


* 
**DO contribute:** `schema.json`, Examples (payloads), `notes.yaml`, `ADOPTERS.yaml`, `CONTRIBUTORS.yaml` .



2. Enumerations with numbers 

* **DON'T:** Use type "number" with min/max for specific values.
* **DO:** Use type "string" with enum list.
```json
"Prop": {
    "type": "string",
    "enum": ["0", "1", "2", "3"],
    "description": "Property. Blab bla"
}

```



3. Leaving percentages without limits 

* **DO:** Set minimum `0` and maximum `1` for percentages.
```json
"Prop": {
    "type": "number",
    "minimum": 0,
    "maximum": 1,
    "description": "Property. Bla bla"
}

```



4. Validating normalized payloads with schema.json 

* Do not try to validate normalized payloads with the schema. The schema only validates key-values format.



5. Not including standard references 

* Don't forget the `$ref` to `GSMA-Commons` and `Location-Commons` at the beginning of the `allOf` section.



---

### **9. Annex: Generated Documents (Do Not Contribute)**

The following files are generated automatically and should **not** be manually created or submitted:

1. **README.md:** Generated daily. Contains descriptions, links, and examples .


2. **model.yaml:** Generated from `schema.json`. Base for the README .


3. 
**swagger.yaml:** Allows interactive representation compliant with OpenAPI 3.0 .


4. 
**csv Exports:** Adds `.csv` suffix to payloads .


5. 
**LICENSE.md:** Templated (Creative Commons or similar allowing free use/mod) .


6. 
**spec.md:** Generated from `schema.json` in English, Spanish, French, German, Italian, Japanese, and Chinese .


7. 
**example-geojsonfeature.json:** Generated if geolocation examples exist.


8. 
**DTDL schema:** Digital Twin Description Language schema .


9. 
**context.jsonld:** Generated with smart-data-models IRIs .


10. 
**schema.sql:** PostgreSQL schema generated from `model.yaml` .



---

### **10. Support**

* 
**Web:** `https://www.smartdatamodels.org` 


* 
**Email:** `info@smartdatamodels.org` 


* 
**GitHub:** `https://github.com/smart-data-models` 



### **Next Step**

Would you like me to create a template for the `schema.json` or `notes.yaml` file based on these guidelines for you to start your contribution?
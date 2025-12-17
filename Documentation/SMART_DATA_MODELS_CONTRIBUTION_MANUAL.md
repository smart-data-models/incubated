# Smart Data Models – Contribution Manual

> Converted from slides for GitHub usage.  
> Original visuals should be added under `images/` and referenced where indicated.

## Agenda
- Overview on the Smart Data Models
- Ways of contribution
- Contribution workflow
- Pull requests
- Acceptance criteria & guidelines
- Documents to contribute
- Common mistakes

---

## Smart Data Models: Domains and Subjects

![Domains and Subjects](images/slide-3.png)

Repositories structure:
- Umbrella repo
- Domain repositories
- Subject repositories
- Lifecycle management (incubated, harmonization)

---

## How to Contribute

### Case 1: Extending an existing data model
### Case 2: Creating a data model from scratch

Search first if your model exists:
https://smartdatamodels.org/index.php/ddbb-of-properties-descriptions/

---

## Contribution Workflow (General)

![Contribution workflow](images/slide-5.png)

Key steps:
1. Identify a use case
2. Check if a data model exists
3. Draft or extend the model
4. Work in `incubated` (recommended)
5. Pull request and manual review
6. Publication

---

## Contribution Workflow (Simple Model)

![Simple workflow](images/slide-6.png)

Alternative using the Schema Sheet:
https://docs.google.com/spreadsheets/d/1yQqkv2I61pK-MZJLW7NBPqIW-9uo-YiWX4HPforQVyE/copy

---

## Pull Requests

### Where to do a Pull Request

- **Case 1**: Domain and subject exist → PR on subject repo
- **Case 2**: Domain exists, subject does not → PR on `incubated`
- **Case 3**: Domain does not exist → PR on `incubated`

https://github.com/smart-data-models/incubated

---

## Acceptance Criteria – Repository Structure

A data model **must** include:
- `schema.json`
- `/examples`
- `notes.yaml`
- `ADOPTERS.yaml`
- `CONTRIBUTORS.yaml`
- (optional) `notes_context.jsonld`

---

## Important Guidelines

- Use `camelCase` for attributes
- Entity types start with capital letter
- Avoid plurals unless necessary
- Use shared attributes from common schema

Common schema:
https://smart-data-models.github.io/data-models/common-schema.json

---

## Documents to be Contributed

1. Schema (JSON Schema)
2. Examples
3. CONTRIBUTORS.yaml
4. ADOPTERS.yaml
5. notes.yaml
6. notes_context.jsonld

---

## Creating `schema.json`

Options:
- JSON → JSON Schema converter
- Manual creation (recommended)
- Schema Sheet (simple models)

https://www.liquid-technologies.com/online-json-to-schema-converter

---

## Validating the Schema

- Use https://www.jsonschemavalidator.net/
- Schema validates **key-value** payloads only

---

## Common Mistakes

1. Contributing non-requested documents
2. Enumerations with numbers instead of strings
3. Percentages without limits
4. Validating normalized payloads
5. Missing standard references

---

## Support

- Web: https://www.smartdatamodels.org
- Email: info@smartdatamodels.org
- GitHub: https://github.com/smart-data-models
- Slack / Discord / LinkedIn

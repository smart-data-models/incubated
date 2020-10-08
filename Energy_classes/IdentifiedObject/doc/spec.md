# IdentifiedObject
type: "object"
description : >
## Description
This is a root class to provide common identification for all classes needing identification and naming attributes.

## Data Model
  - properties:
    - DiagramObjects:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The domain object to which this diagram object is associated. Default: "list"
    - mRID:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Master resource identifier issued by a model authority. The mRID is globally unique within an exchange context. Global uniqueness is easily achieved by using a UUID,  as specified in RFC 4122, for the mRID.  The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552 Edition 1, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements. Default: ''
    - name:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The name is any free human readable and possibly non unique text naming the object. Default: ''
    - description:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy. Default: ''
    - energyIdentCodeEic:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The attribute is used for an exchange of the EIC code (Energy identification Code). The length of the string is 16 characters as defined by the EIC code. References: Default: ''
    - shortName:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The attribute is used for an exchange of a human readable short name with length of the string 12 characters maximum. Default: ''

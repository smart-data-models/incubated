# TopologyBoundaryVersion
type: "object"
description : >
## Description
Version details.

## Data Model
  - properties:
    - baseUML:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base UML provided by CIM model manager. Default: ''
    - baseURI:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the Profile and its version. It is given for information only and to identify the closest IEC profile to which this CGMES profile is based on. Default: ''
    - date:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. Default: ''
    - differenceModelURI:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Difference model URI defined by IEC 61970-552. Default: ''
    - entsoeUML:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : UML provided by ENTSO-E. Default: ''
    - entsoeURI:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile and its version. The last two elements in the URI (http://entsoe.eu/CIM/TopologyBoundary/yy/zzz) indicate major and minor versions where:  - yy - indicates a major version; - zzz - indicates a minor version. Default: ''
    - modelDescriptionURI:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Model Description URI defined by IEC 61970-552. Default: ''
    - namespaceRDF:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : RDF namespace. Default: ''
    - namespaceUML:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : CIM UML namespace. Default: ''
    - shortName:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The short name of the profile used in profile documentation. Default: ''

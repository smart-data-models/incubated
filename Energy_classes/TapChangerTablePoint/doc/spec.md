# TapChangerTablePoint
type: "object"
description : >
## Description


## Data Model
  - properties:
    - b:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The magnetizing branch susceptance deviation in percent of nominal value. The actual susceptance is calculated as follows: calculated magnetizing susceptance = b(nominal) * (1 + b(from this class)/100).   The b(nominal) is defined as the static magnetizing susceptance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
    - g:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The magnetizing branch conductance deviation in percent of nominal value. The actual conductance is calculated as follows: calculated magnetizing conductance = g(nominal) * (1 + g(from this class)/100).   The g(nominal) is defined as the static magnetizing conductance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The resistance deviation in percent of nominal value. The actual reactance is calculated as follows: calculated resistance = r(nominal) * (1 + r(from this class)/100).   The r(nominal) is defined as the static resistance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0
    - ratio:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage ratio in per unit. Hence this is a value close to one. Default: 0.0
    - step:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The tap step. Default: 0
    - x:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The series reactance deviation in percent of nominal value. The actual reactance is calculated as follows: calculated reactance = x(nominal) * (1 + x(from this class)/100).   The x(nominal) is defined as the static series reactance on the associated power transformer end or ends.  This model assumes the star impedance (pi model) form. Default: 0.0

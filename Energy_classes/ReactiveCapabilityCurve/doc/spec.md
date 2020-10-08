# ReactiveCapabilityCurve
type: "object"
description : >
## Description
Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.

## Data Model
  - properties:
    - EquivalentInjection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactive capability curve used by this equivalent injection. Default: "list"
    - InitiallyUsedBySynchronousMachines:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The default reactive capability curve for use by a synchronous machine. Default: "list"

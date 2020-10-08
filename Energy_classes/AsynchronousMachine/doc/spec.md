# AsynchronousMachine
type: "object"
description : >
## Description
A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine with no external connection to the rotor windings, e.g squirrel-cage induction machine.

## Data Model
  - properties:
    - nominalFrequency:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Nameplate data indicates if the machine is 50 or 60 Hz. Default: 0.0
    - nominalSpeed:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Nameplate data.  Depends on the slip and number of pole pairs. Default: 0.0
    - converterFedDrive:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Indicates whether the machine is a converter fed drive. Used for short circuit data exchange according to IEC 60909 Default: False
    - efficiency:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Efficiency of the asynchronous machine at nominal operation in percent. Indicator for converter drive motors. Used for short circuit data exchange according to IEC 60909 Default: 0.0
    - iaIrRatio:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data exchange according to IEC 60909 Default: 0.0
    - polePairNumber:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909 Default: 0
    - ratedMechanicalPower:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data exchange according to IEC 60909. Default: 0.0
    - reversible:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Indicates for converter drive motors if the power can be reversible. Used for short circuit data exchange according to IEC 60909 Default: False
    - rxLockedRotorRatio:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909 Default: 0.0
    - asynchronousMachineType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Indicates the type of Asynchronous Machine (motor or generator). Default: None
    - AsynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Asynchronous machine dynamics model used to describe dynamic behavior of this asynchronous machine. Default: None

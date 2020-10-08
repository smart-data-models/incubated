# ACLineSegment
type: "object"
description : >
## Description
A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use  attributes of the line segment, which describe impedances and admittances for the entire length of the segment.  Additionally impedances can be computed by using length and associated per length impedances. The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same BaseVoltage.nominalVoltage. However, boundary lines  may have slightly different BaseVoltage.nominalVoltages and  variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

## Data Model
  - properties:
    - bch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. Default: 0.0
    - gch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence series resistance of the entire line section. Default: 0.0
    - x:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence series reactance of the entire line section. Default: 0.0
    - b0ch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. Default: 0.0
    - g0ch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. Default: 0.0
    - r0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence series resistance of the entire line section. Default: 0.0
    - shortCircuitEndTemperature:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum permitted temperature at the end of SC for the calculation of minimum short-circuit currents. Used for short circuit data exchange according to IEC 60909 Default: 0.0
    - x0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence series reactance of the entire line section. Default: 0.0

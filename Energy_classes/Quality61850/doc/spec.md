# Quality61850
type: "object"
description : >
## Description
Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.

## Data Model
  - properties:
    - badReference:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value may be incorrect due to a reference being out of calibration. Default: False
    - estimatorReplaced:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience. Default: False
    - failure:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure. Default: False
    - oldData:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval. Default: False
    - operatorBlocked:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value is blocked and hence unavailable for transmission. Default: False
    - oscillatory:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier `oscillatory` is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status `questionable` is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status `questionable` is reset and `invalid` is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status `invalid` is set immediately in addition to the detail quality identifier `oscillatory` (used for status information only). Default: False
    - outOfRange:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value is beyond a predefined range of value. Default: False
    - overFlow:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero. Default: False
    - source:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted. Default: None
    - suspect:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator. Default: False
    - test:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement value is transmitted for test purposes. Default: False
    - validity:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Validity of the measurement value. Default: None

ACDCConverter
type: "object"
description : >
A unit with valves for three phases, together with unit control equipment, essential protective and switching devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

## Data Model

  - properties:
    baseS:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base apparent power of the converter pole. Default: 0.0
    idleLoss:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active power loss in pole at no power transfer. Converter configuration data used in power flow. Default: 0.0
    maxUdc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The maximum voltage on the DC side at which the converter should operate. Converter configuration data used in power flow. Default: 0.0
    minUdc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Min allowed converter DC voltage. Converter configuration data used in power flow. Default: 0.0
    numberOfValves:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Number of valves in the converter. Used in loss calculations. Default: 0
    ratedUdc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rated converter DC voltage, also called UdN. Converter configuration data used in power flow. Default: 0.0
    resistiveLoss:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Converter configuration data used in power flow. Refer to poleLossP. Default: 0.0
    switchingLoss:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP. Default: 0.0
    valveU0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e. the switchLoss depend on numberOfValves * valveU0. Default: 0.0
    DCTerminals:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: "list"
    PccTerminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All converters` DC sides linked to this point of common coupling terminal. Default: None
    p:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    q:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution in the case a simplified power flow model is used. Default: 0.0
    targetPpcc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Real power injection target in AC grid, at point of common coupling. Default: 0.0
    targetUdc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Target value for DC voltage magnitude. Default: 0.0
    idc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Converter DC current, also called Id. Converter state variable, result from power flow. Default: 0.0
    poleLossP:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with losses Pdc=Pac+lossP Converter state variable used in power flow. Default: 0.0
    uc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow. Default: 0.0
    udc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow. Default: 0.0

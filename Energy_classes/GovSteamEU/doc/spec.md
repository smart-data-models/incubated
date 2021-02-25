# GovSteamEU


## Description
Simplified model  of boiler and steam turbine with PID governor.

## Data Model
  - properties:
    - mwbase:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    - tp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power transducer time constant (Tp).  Typical Value = 0.07. Default: 0
    - ke:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain of the power controller (Ke).  Typical Value = 0.65. Default: 0.0
    - tip:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Integral time constant of the power controller (Tip).  Typical Value = 2. Default: 0
    - tdp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Derivative time constant of the power controller (Tdp).  Typical Value = 0. Default: 0
    - tfp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of the power controller (Tfp).  Typical Value = 0. Default: 0
    - tf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Frequency transducer time constant (Tf).  Typical Value = 0. Default: 0
    - kfcor:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain of the frequency corrector (Kfcor).  Typical Value = 20. Default: 0.0
    - db1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Dead band of the frequency corrector (db1).  Typical Value = 0. Default: 0.0
    - wfmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Upper limit for frequency correction (Wfmax).  Typical Value = 0.05. Default: 0.0
    - wfmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lower limit for frequency correction (Wfmin).  Typical Value = -0.05. Default: 0.0
    - pmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximal active power of the turbine (Pmax).  Typical Value = 1. Default: 0.0
    - ten:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Electro hydraulic transducer (Ten).  Typical Value = 0.1. Default: 0
    - tw:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed transducer time constant (Tw).  Typical Value = 0.02. Default: 0
    - kwcor:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain of the speed governor (Kwcor).  Typical Value = 20. Default: 0.0
    - db2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Dead band of the speed governor (db2).  Typical Value = 0.0004. Default: 0.0
    - wwmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Upper limit for the speed governor (Wwmax).  Typical Value = 0.1. Default: 0.0
    - wwmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lower limit for the speed governor frequency correction (Wwmin).  Typical Value = -1. Default: 0.0
    - wmax1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Emergency speed control lower limit (wmax1).  Typical Value = 1.025. Default: 0.0
    - wmax2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Emergency speed control upper limit (wmax2).  Typical Value = 1.05. Default: 0.0
    - tvhp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Control valves servo time constant (Tvhp).  Typical Value = 0.1. Default: 0
    - cho:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Control valves rate opening limit (Cho).  Unit = PU/sec.  Typical Value = 0.17. Default: 0.0
    - chc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Control valves rate closing limit (Chc).  Unit = PU/sec.  Typical Value = -3.3. Default: 0.0
    - hhpmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum control valve position (Hhpmax).  Typical Value = 1. Default: 0.0
    - tvip:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Intercept valves servo time constant (Tvip).  Typical Value = 0.15. Default: 0
    - cio:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Intercept valves rate opening limit (Cio).  Typical Value = 0.123. Default: 0.0
    - cic:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Intercept valves rate closing limit (Cic).  Typical Value = -2.2. Default: 0.0
    - simx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Intercept valves transfer limit (Simx).  Typical Value = 0.425. Default: 0.0
    - thp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : High pressure (HP) time constant of the turbine (Thp).  Typical Value = 0.31. Default: 0
    - trh:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reheater  time constant of the turbine (Trh).  Typical Value = 8. Default: 0
    - tlp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Low pressure(LP) time constant of the turbine (Tlp).  Typical Value = 0.45. Default: 0
    - prhmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum low pressure limit (Prhmax).  Typical Value = 1.4. Default: 0.0
    - khp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fraction of total turbine output generated by HP part (Khp).  Typical Value = 0.277. Default: 0.0
    - klp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fraction of total turbine output generated by HP part (Klp).  Typical Value = 0.723. Default: 0.0
    - tb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Boiler time constant (Tb).  Typical Value = 100. Default: 0
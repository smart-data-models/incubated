# Simulation Scenario

## Description
This entity contains an harmonised description of a generic simulation scenario made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `SimulationScenario`.

### Simulation Scenario Entity Properties

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `duration`: Duration of the simulation, given in seconds.
    -   Attribute type: `Property`.Number
    -   Optional

-   `hydraulicTimeStep`: Determines how often the hydraulic state of the network is calculated. Given in seconds.
    -   Attribute type: `Property`.Number
    -   Optional

-   `flowUnits`: Units in which flow rates are expressed in the simulation. Allowable options are "CFS" (cubic feet per second), "GPM" (gallons per minute), "MGD" (million gallons per day), "IMGD" (imperial MGD), "AFD" (acre-feet per day), "LPS" (litres pre second), "LPM" (litres per minute), "MLD" (million litres per day), "CMH" (cubic metres per hour) and "CMD" (cubic metres per day).
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "CFS", "GPM", "MGD", "IMGD" (imperial MGD), "AFD", "LPS", "LPM", "MLD", "CMH", "CMD"
    -   Optional

-   `headlossFormula`: Formula used for computing head loss for flow through a pipe. The choices are the Hazen-Williams (H-W), Darcy-Weisbach (D-W) or Chezy-Manning (C-M) formulas.
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "H-W", "D-W", "C-M"
    -   Optional

-   `startClockTime`: Time of day at which the simulation begins. Given as seconds from start of day.
    -   Attribute type: `Property`.Number
    -   Optional

-   `reportStep`: Interval at which output results are reported. given in seconds.
    -   Attribute type: `Property`.Text
    -   Optional

-   `reportStart`: Simulation time at which results start to be reported. Given in seconds from start of simulation.
    -   Attribute type: `Property`.Number
    -   Optional

-   `ruleTimeStep`: Time step used to check for changes in system status due to rule-based controls. Given in seconds.
    -   Attribute type: `Property`.Number
    -   Optional

-   `statistic`: The type of statistical post-processing that is done on the time series of simulation results generated. Options are "AVERAGED" (report time-averaged results), "MINIMUM" (report only minimum values), "MAXIMUM" (report only maximum values), "RANGE" (report difference between minimum and maximum values) and "NONE" (report full time series)
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "AVERAGED", "MINIMUM", "MAXIMUM", "RANGE", "NONE"
    -   Optional

-   `trials`: The the maximum number of trials used to solve network hydraulics at each hydraulic time step of a simulation
    -   Attribute type: `Property`.Number
    -   Optional

-   `accuracy`: Total normalized flow change convergence criterion for determining when a hydraulic solution has been reached.
    -   Attribute type: `Property`.Number
    -   Optional

-   `tolerance`: Water quality tolerance
    -   Attribute type: `Property`.Number
    -   Optional

-   `emitterExponent`: Power to which pressure at a junction is raised when computing from from an emitter.
    -   Attribute type: `Property`.Number
    -   Optional

-   `headError`: Maximum headloss convergence criterion for determining when a hydraulic solution has been reached.
    -   Attribute type: `Property`.Number
    -   Optional

-   `flowChange`: Maximum flow change convergence criterion for determining when a hydraulic solution has been reached.
    -   Attribute type: `Property`.Number
    -   Optional

-   `demandCharge`: Energy charge per maximum kW usage.
    -   Attribute type: `Property`.Number
    -   Optional

-   `demandModel`: Specifies whether a the analysis is pressure driven ("PDA") or demand driven ("DDA").
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "PDA", "DDA"
    -   Optional

-   `minimumPressure`: Pressure below which no demand can be delivered under a pressure dirven analysis. Only used if `demandModel` is "PDA".
    -   Attribute type: `Property`.Number
    -   Optional

-   `requiredPressure`: Pressure required to supply a node's full demand under a pressure dirven analysis. Only used if `demandModel` is "PDA".
    -   Attribute type: `Property`.Number
    -   Optional

-   `pressureExponent`: Power to which pressure is raised when calculating the demand delivered under a pressure dirven analysis. Only used if `demandModel` is "PDA".
    -   Attribute type: `Property`.Number
    -   Optional

-   `viscosity`: The kinematic viscosity of the fluid being modeled relative to that of water at 20 deg. C
    -   Attribute type: `Property`.Number
    -   Optional

-   `unbalanced`: Determines what happens if a hydraulic solution cannot be reached within the allowed number of trials. Allowable options are "STOP" (halt analysis), "CONTINUE" (continue analysis but with a warning message) and "CONTINUE_N" (continue for another N trials, where the value of N is given by `unbalancedN`)
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "STOP", "CONTINUE", "CONTINUE_N"
    -   Optional

-   `unbalancedN`: Number of additional trials allowed if `unbalanced` is set to "CONTINUE_N". Mandatory if `unbalanced` is set to "CONTINUE_N", else not required.
    -   Attribute type: `Property`.Number
    -   Optional

-   `checkFrequency`: Frequency of hydraulic status checks
    -   Attribute type: `Property`.Number
    -   Optional

-   `maxCheck`: Number of trials after which status checks are discontinued
    -   Attribute type: `Property`.Number
    -   Optional

-   `dampLimit`: Accuracy value at which solution damping and status checks begin for PRVs and PSVs.
    -   Attribute type: `Property`.Number
    -   Optional

-   `diffusivity`: Molecular diffusivity of the chemical analysed in a quality analysis, relative to diffusivity of chlorine in water.
    -   Attribute type: `Property`.Number
    -   Optional

-   `bulkOrder`: Bulk water reaction order for pipes
    -   Attribute type: `Property`.Number
    -   Optional

-   `wallOrder`: Wall reaction order for pipes
    -   Attribute type: `Property`.Number
    -   Optional

-   `tankOrder`: Bulk water reaction order for tanks
    -   Attribute type: `Property`.Text
    -   Optional

-   `concentrationLimit`: Limiting concentration for growth reactions
    -   Attribute type: `Property`.Text
    -   Optional

-   `qualityType`: Type of water quality analysis
    -   Attribute type: `Property`.Text
    -   Values Restricted to : "NONE", "CHEM", "AGE" and "TRACE"
    -   Optional

-   `chemicalName`: Name of the chemical modelled. Only used if `qualityType` is "CHEM".
    -   Attribute type: `Property`.Text
    -   Optional

-   `chemicalUnits`: Units of the chemical modelled. Only used if `qualityType` is "CHEM".
    -   Attribute type: `Property`.Text
    -   Optional

-   `specificGravity`: The the ratio of the density of the fluid being modeled to that of water at 4 deg. C
    -   Attribute type: `Property`.Number
    -   Optional

-   `qualityTimeStep`: The timestep used to track changes in water quality in the network. Given in seconds.
    -   Attribute type: `Property`.Number
    -   Optional

-   `operationalControl` : Description of a control applied to the network for the simulation
    -   `controlType`: A sub-property.
    -   `controlledLink`:A sub-Relationship.
    -   `setting`: A sub-property.
    -   `monitoredNode`: A sub-Relationship.
    -   `triggerLevel`: A sub-property.
    -   Optional

-   `controlType` : Control type. A sub-property of the Property `control`
    -   Attribute type: `Property`.Text
    -   Values Restricted to :  "LOWLEVEL", "HILEVEL", "TIMER" and "TIMEOFDAY"
    -   Mandatory

-   `setting` : Setting applied in the to the controlled link when trigger level is reached. A sub-property of the Property `control`
    -   Attribute type: `Property`.Number
    -   Mandatory

-   `triggerLevel` : Level at which control is activated. A sub-property of the Property `control`
    -   Attribute type: `Property`.Number
    -   Mandatory

-   `inputParameter` : Description of the set of modifications to be applied to the network for the simulation
    -   water attribute: A sub-property. A water attribute issued from the [Water managemement network model](https://github.com/smart-data-models/dataModel.WaterNetworkManagement/tree/master). It follows fully this data model and it could be a property or a relationship . It is the attribute that will be modified by the simulation.
    -   `targetURI`:A sub-Relationship of the water attribute. It presents the target water node or link that will handle the modification.
    -   Optional


### Simulation Scenario Entity Relationships

-   `createdBy` : The ID of who created/triggered the simulation
    -   Attribute type: `Relationship`. Reference to an entity of type `User`
    -   Optional

-   `hasInputNetwork` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `hasSimulationResult` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `SimulationResult`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `targetURI` : URI of network component with property modified in simulation. A sub-relationship of the Property water attribute.
    -   Attribute type: `Relationship`
    -   Mandatory

-   `controlledLink` : Link controlled. A sub-relationship of the Property `control`
    -   Attribute type: `Relationship`. Reference to an entity of type `Pipe`, `Pump` or `Valve`
    -   Mandatory

-   `monitoredNode` : Node which is monitored for control trigger level. A sub-relationship of the Property `control`
    -   Attribute type: `Relationship`. Reference to an entity of type `Junction`, `Tank` or `Reservoir`
    -   Mandatory

-   `traceNodeID` : URI of Node... 
    -   Attribute type: `Relationship`
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
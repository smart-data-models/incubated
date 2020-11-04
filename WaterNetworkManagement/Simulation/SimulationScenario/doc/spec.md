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

-   duration: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   hydraulicTimeStep: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   flowUnits: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   headlossFormula: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   patternStep: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   patternStart: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   reportStep: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   reportStart: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   ruleStep: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   statistic: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   trials: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   accuracy: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   tolerance: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   emitterExponent: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   headerError: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   flowChange: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   demandCharge: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   demandCharge: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   viscosity: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   unbalanced: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   checkFrequency: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   maxCheck: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   dampLimit: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   diffusivity: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   bulkOrder: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   wallOrder: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   tankOrder: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   concentrationLimit: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   qualityType: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   chemicalName: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   chemicalUnits: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   flowUnits: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   flowUnits: A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   qualityTimeStep: A free text description
    -   Attribute type: `Property`.Text
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

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
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
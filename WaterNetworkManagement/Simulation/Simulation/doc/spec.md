# Simulation

## Description
This entity contains an harmonised description of a generic simulation scenario made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Simulation`.

### Simulation Entity Properties

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

-   demandModel: A free text description
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

### Simulation Entity Relationships

-   `createdBy` : The ID of who created/triggered the simulation
    -   Attribute type: `Relationship`. Reference to an entity of type `User`
    -   Optional

-   `hasInputNetwork` : The ID of the network used in the simulation

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


**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
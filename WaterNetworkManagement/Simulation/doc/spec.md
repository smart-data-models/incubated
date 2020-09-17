# Simulation

## Description
This entity contains an harmonised description of a generic simulation made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Simulation`.

-   `modifiedAt`: Last update timestamp of this
    entity.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

-   `createdAt`: Entity's creation timestamp.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Read-Only. Automatically generated.

### Simulation Entity Properties

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `optionNames` : Names of options applied in the simulation

    -   Attribute type: `Property`. List of String
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `optionValues` : Values of options applied in the simulation

    -   Attribute type: `Property`. List of Number or String
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `operationalControl` : Description of a control applied to the network for the simulation
    -   `controlType`: A sub-property.
    -   `controlledLink`:A sub-Relationship.
    -   `setting`: A sub-property.
    -   `monitoredNode`: A sub-Relationship.
    -   `triggerLevel`: A sub-property.
    -   Optional

-   `controlType` : Control type. A sub-property of the Property `control`
    -   Attribute type: `Property`.Text
    -  Values Restricted to :  "LOWLEVEL", "HILEVEL", "TIMER" and "TIMEOFDAY"
    -   Mandatory

-   `setting` : Setting applied in the to the controlled link when trigger level is reached. A sub-property of the Property `control`
    -   Attribute type: `Property`.Number
    -   Mandatory

-   `triggerLevel` : Level at which control is activated. A sub-property of the Property `control`
    -   Attribute type: `Property`.Number
    -   Mandatory

-   `modifiedInputNetworkParameter` : Description of a modification applied to the network for the simulation
    -   `modificationTargetURI`: A sub-property.
    -   `modificationTargetProperty`:A sub-property.
    -   `modificationTargetValue`: A sub-property.
    -   Optional

-   `modificationTargetProperty` : Name of the property modified in simulation. A sub-property of the Property `modifiedInputNetworkParameter`
    -   Attribute type: `Property`.Text
    -   Mandatory

-   `modificationTargetValue` : New value applied to the modified network property in the simulation. A sub-property of the Property `modifiedInputNetworkParameter`
    -   Mandatory


### Simulation Entity Relationships

-   `createdBy` : The ID of who created/triggered the simulation
    -   Attribute type: `Relationship`. Reference to an entity of type `User`
    -   Optional

-   `hasInputNetwork` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `modificationTargetURI` : URI of network component with property modified in simulation. A sub-relationship of the Property `modifiedInputNetworkParameter`
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
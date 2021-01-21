# Simulation Result

## Description
This entity contains an harmonised description of a generic result of a simulation made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `SimulationResult`.

### Simulation Result Entity Properties

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `outputParameters` : Description of the set of results of applied simulation to the network.
    -   water attribute: A sub-property. A water attribute issued from the [Water managemement network model](https://github.com/smart-data-models/dataModel.WaterNetworkManagement/tree/master). It follows fully this data model and it could be a property or a relationship. It contains the results of the simulation.
   -   Optional


### Simulation Result Entity Relationships

-   `createdBy` : The ID of who created/triggered the simulation
    -   Attribute type: `Relationship`. Reference to an entity of type `User`
    -   Optional

-   `hasInputNetwork` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `WaterNetwork`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Optional

-   `targetURI` : URI of network component with a simulated property value. A sub-relationship of the water attribute Property
    -   Attribute type: `Relationship`
    -   Mandatory

-   `refSimulationScenario` : The ID of the simulation scenario

    -   Attribute type: `Relationship`. Reference to an entity of type `SimulationScenario`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI-LD.


### LD Example

A full example is presented [here](../example-normalized-ld.jsonld).

## Use it with a real service

T.B.D.

## Open Issues
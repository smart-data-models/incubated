# Simulation

## Description
This entity contains an harmonised description of a generic simulation made for the Water Network Management domain. This entity is primarily associated with the water network management vertical and related IoT applications.

## Data Model

A JSON Schema corresponding to this data model can be found [here](../schema.json)

### NGSI-LD common Properties
-   `id`: Unique identifier.

-   `type`: Entity type. It must be equal to `Simulation`.

### Simulation Entity Properties

-   `description` : A free text description
    -   Attribute type: `Property`.Text
    -   Optional

-   `outputParameters` : Description of the set of results of applied simulation to the network.
    -   water attribute: A sub-property. A water attribute issued from the [Water managemement network model](https://github.com/smart-data-models/dataModel.WaterNetworkManagement/tree/master). It follows fully this data model and it could be a property or a relationship. It contains the results of the simulation.
-   `targetUri`: A sub-relationship of the water attribute.
   -   Optiona


### Simulation Entity Relationships

-   `createdBy` : The ID of who created/triggered the simulation
    -   Attribute type: `Relationship`. Reference to an entity of type `User`
    -   Optional

-   `hasInputNetwork` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
    -   Attribute metadata Properties:
        -   `{{metadata Property name}}` : {{Metadata Property Description}}
    -   Mandatory

-   `targetURI` : URI of network component with property modified in simulation. A sub-relationship of the water attribute Property
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
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

-   `createdBy` : Name or other identifier of who created/triggered the simulation
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


### Simulation Entity Relationships

-   `hasInputNetwork` : The ID of the network used in the simulation

    -   Attribute type: `Relationship`. Reference to an entity of type `Network`
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
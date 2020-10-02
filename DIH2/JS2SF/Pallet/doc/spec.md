# Pallet

## Description

A pallet containing stone pieces for manufacturing.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/JS2SF/Pallet/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `Pallet`.

-   `timeOfLoading` : Timestamp of when the pieces were loaded onto the pallet.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) 

-   `refCurrentLocation` : Indicates the location of the pallet.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 

-   `refComingFrom` : Indicates where the pallet came from.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 

-   `refGoiningTo` : Indicates where the pallet is going to.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 


-   `manufacturabilityOnFlexEdge` : Indicates if the Piece can be picked up by robot and be processed.

    -   Attribute type: Property. [Text](https://schema.org/Text) 
	-	Enum values : "CanPickUpOnly", "CannotPickUp", "CanProcess"

-   `refPieceList` : List of stone pieces currently on the pallet.

    -   Attribute type: Property. Array Relationship [Text](https://schema.org/Text) 


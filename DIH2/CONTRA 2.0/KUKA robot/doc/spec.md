# KUKA robot

## Description

A KUKA robot

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/CONTRA%202.0/KUKA%20robot/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `KUKA`.

-   `active` : Information whether the robot is currently working.

-   `carrierId` : Pallet ID.

-   `carrierLayersProgress` : The percentage of the pallet layers transferred

-   `carrierTimeRemaining` : Estimated time of unloading the pallet (in minutes)

-   `lastStateChange` : Date of the last change of the robot's state (on or off)

-   `totalCarrierLayers` : Information about the number of layers.

-   `totalCarrierLayersCompleted` : Information about the number of finishing layers.

-   `startPaletteProcessingTime` : Information on the date of the pallet unloading start.
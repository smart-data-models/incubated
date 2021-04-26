# Tracking Device

## Description

Any type of tracking device that can capture pose and timestamp at which time the pose was captured.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/RoboWeldAR/TrackingDevice/schema.json).

-   `id` : Unique identifier i.e. `TrackingDeviceLHR-1D2D7974` where `LHR-1D2D7974` is the device serial number..

-   `type` : Entity type. It must be equal to `TrackingDevice`.

-   `pose` : The current pose, a List containing 12 elements (9 for rotation and 3 for position).

    -   Attribute type: List.  [ItemList](https://schema.org/ItemList) 
    -   Mandatory

-   `timestamp` : Unix timestamp (epoch) at which the corresponding pose was captured.

    -   Attribute type: Number. [Number](https://schema.org/Number)
    -   Mandatory

# Vacuum Pump

## Description

A vacuum pump.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/JS2SF/VacuumPump/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `VacuumPump`.

-   `vacuumLevel` : The current vacuum level, a value beween 0 and 1.

    -   Attribute type: Property.  [Number](http://schema.org/Number) 
    -   Allowed values: Interval \[0,1\].
    -   Default unit: bar.

-   `on` : Indicates if the pump is on (true) or off (false).
    information

    -   Attribute type: Property. [Boolean](https://schema.org/Boolean)

-   `pumpModel` : The pump model identifier.

    -   Attribute type: Property. [Text](https://schema.org/Text) 


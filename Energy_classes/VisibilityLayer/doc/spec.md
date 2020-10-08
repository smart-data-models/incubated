# VisibilityLayer
type: "object"
description : >
## Description
Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an appropriate 1:n representation if the importing system does not support m:n.

## Data Model
  - properties:
    - VisibleObjects:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A visibility layer can contain one or more diagram objects. Default: "list"
    - drawingOrder:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The drawing order for this layer.  The higher the number, the later the layer and the objects within it are rendered. Default: 0

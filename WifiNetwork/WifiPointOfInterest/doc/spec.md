# Wi-Fi Point Of Interest

## Description

This entity describes a Point of Interest that has a wireless network provided
by a set of [Access Points](../../AccessPoint/).
 
This data model has been developed in cooperation with 
the [Valencia City Hall](https://www.valencia.es).

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json)

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `WifiPointOfInterest`.

-   `name` : Name of this place.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/name` equivalent to [name](https://schema.org/name)
    -   Mandatory	
	
-   `address` : Civic address of this location.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Mandatory if `location` is not present.

-   `location` : Location of the place represented by a GeoJSON Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not defined.

-   `clientsConnected` : Number of clients or users connected in this point of interest.

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Metadata:
        -   `TimeInstant` : Timestamp which reflects the date when the attribute
            value was obtained.
            -   Type: [DateTime](https://schema.org/DateTime)
            -   Optional	
    -   Mandatory
	-   Minimum 0	

-   `wifiStatus` : Indicates if there is a wireless network available at
    this location and the service that it is providing. The allowed values 
	are: `"noService"` when the point of interest has no access points 
	installed, `"working"` when the point of interest has access points installed and 
	all of them	are working (up), `"totalFailure"` when the point of interest has access 
	points installed and all of them are not working (down), and `"workingPartially"` when 
	the point of interest has access points installed and some of them are working (up) 
	and some of then are not working (down).

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`noService`, `working`, `workingPartially`, `totalFailure`).
    -   Metadata:
        -   `TimeInstant` : Timestamp which reflects the date when the attribute
            value was obtained.
            -   Type: [DateTime](https://schema.org/DateTime)
            -   Optional
    -   Optional

-   `service` : This attribute is used to assign the access point to one or several 
    municipal service departments that receive the wireless service. 
	For example: Library, Museums, Social Services, Sports...

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Optional

-   `TimeInstant` :
    [Timestamp](https://github.com/telefonicaid/iotagent-node-lib#TimeInstant)
    saved by FIWARE's IoT Agent. Note: This attribute has not been harmonized to
    keep backwards compatibility with current FIWARE reference implementations.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime). There can be
        production environmments where the attribute type is equal to the
        `ISO8601` string. If so, it must be considered as a synonym of
        `DateTime`.
    -   Optional

-   `category` : Category of this point of interest.

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Allowed values: Those defined by the
        [Factual taxonomy](https://github.com/Factual/places/blob/master/categories/factual_taxonomy.json)
        together with other categories that the user of the datamodel may implement.
    -   Optional

-   `contactPoint` : Contact point of this point of interest.

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional	

-   `dataProvider` : Specifies the information about the provider of this information

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Optional

-   `description` : Description of this point of interest.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/description` equivalent to [description](https://schema.org/description)
    -   Optional


-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

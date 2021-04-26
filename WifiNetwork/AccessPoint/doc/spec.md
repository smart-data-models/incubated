# Access Point

## Description

This entity describes an Access Point which is a networking hardware that generates a 
wireless network and allows other Wi-Fi devices to connect to it.

The access point can provide a wireless network in a building or a place (square, street, beach, 
garden...) modelated with a separated entity type [WifiPointOfInterest](../../WifiPointOfInterest/).

This data model has been developed in cooperation 
with the [Valencia City Hall](https://www.valencia.es).

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json)

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `AccessPoint`.

-   `name` : Name of this access point.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/name` equivalent to [name](https://schema.org/name)
    -   Mandatory	

-   `address` : Civic address of this access point.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Mandatory if `location` is not present.

-   `location` : Location of the access point represented by a GeoJSON Point.

    -   Attribute type: GeoProperty. `geo:json`.
    -   Normative References: [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Mandatory if `address` is not defined.

-   `apState` : Indicates whether the access point is working (value: up), or it is not working or shut down (value: down).

    -   Attribute type: Property. [Text](http://schema.org/Text)
    -   Allowed values: one Of (`up`, `down`).
    -   Metadata:
        -   `TimeInstant` : Timestamp which reflects the date when the attribute
            value was obtained.
            -   Type: [DateTime](https://schema.org/DateTime)
            -   Optional
    -   Optional

-   `ssid` : List of the names of the SSID (service set identifier) that the access point generates. One access point can generate one or several SSID.

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Optional
	
-   `clientsConnected` : Number of clients or users connected to the access point.

    -   Attribute type: Property. [Number](https://schema.org/Number)
    -   Metadata:
        -   `TimeInstant` : Timestamp which reflects the date when the attribute
            value was obtained.
            -   Type: [DateTime](https://schema.org/DateTime)
            -   Optional	
    -   Mandatory
	-   Minimum 0

-   `service` : This attribute is used to assign the access point to one or several 
    municipal service departments that receive the wireless service. 
	For example: Library, Museums, Social Services, Sports...

    -   Attribute type: Property. List of [Text](https://schema.org/Text)
    -   Optional

-   `refPointOfInterest` : The point of interest where the access point is located and provides the service.

    -   Attribute type: Property. Reference to an entity of type
        [WifiPointOfInterest](../../WifiPointOfInterest/doc/spec.md).
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
	
-   `contactPoint` : Contact point of this access point.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `dataProvider` : Specifies the information about the provider of this information.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `dateInstalled` : A timestamp which denotes when the device was installed
    (if it requires installation).

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `dateLastReboot` : A timestamp which denotes the last time when the
    device was successfully rebooted.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional
	
-   `dateLastValueReported` : A timestamp which denotes the last time when the
    device successfully reported data to the cloud.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime)
    -   Optional

-   `description` : Description of this access point.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        `https://uri.etsi.org/ngsi-ld/description` equivalent to [description](https://schema.org/description)
    -   Optional

-   `firmwareVersion` : The firmware version of this device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `hardwareVersion` : The hardware version of this device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional	

-   `ipAddress` : The IP address of the device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `macAddress` : The MAC address of the device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `modelName` : Device's model name.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   See also: [https://schema.org/model](https://schema.org/model)
    -   Optional

-   `osVersion` : The version of the host operating system device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `owner` : The owner of the device.
    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `provider` : The provider of the device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional

-   `serialNumber` : The serial number assigned by the manufacturer.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Normative References:
        [https://schema.org/serialNumber](https://schema.org/serialNumber)
    -   Optional

-   `softwareVersion` : The software version of this device.

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Optional
	
-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional







	
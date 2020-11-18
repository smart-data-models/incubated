# dataModel.WifiNetwork

These data models describe the main entities to model the status and usage of a Wi-Fi network provided in a set of Points of Interest.

It is composed by the usage of the [WifiPointOfInterest](./WifiPointOfInterest/) and [Access Point](./AccessPoint) models define in this repository and the 
standard [KeyPerformanceIndicator](https://github.com/smart-data-models/dataModel.KeyPerformanceIndicator/) model for the usage statistics.

These data models have been developed in cooperation with 
the [Valencia City Hall](https://www.valencia.es).

### List of data models

The following entity types are available:
- [WifiPointOfInterest](./WifiPointOfInterest/). This entity describes a Point of Interest that might have a 
wireless network provided by a set of [Access Points](./AccessPoint/). A Point of Interest could be for example
a building, a beach, a garden, a square, etc. It models a location with a Wi-Fi network or that could 
potentially host a Wi-Fi network.

- [Access Point](./AccessPoint/). This entity describes an Access Point which is a networking hardware 
that generates a wireless network and allows other Wi-Fi devices to connect to it. An access point can be located
in a [WifiPointOfInterest](./WifiPointOfInterest/)

- [KeyPerformanceIndicator](https://github.com/smart-data-models/dataModel.KeyPerformanceIndicator/). The usage of the 
Wi-Fi network generates a set of usage statistics that can be modelated with the standard KeyPerformanceIndicator model.
An example of data modelated by the [Valencia City Hall](https://www.valencia.es) in its
implementation is:
    - Number of Users Connected to the newtork in a WifiPointOfInterest. Unique number of users connected during a 
	  time frame, for example Hourly or Daily. Note that a user can be connected to one or more Access Points located 
	  in a WifiPointOfInterest. However, that user is counted as single user when calculating the hourly or 
	  daily value (unique users).
	- Average Conection Time. Average connection time of the users connected in a WifiPointOfInterest. Daily value.
	- Quality of the Wi-Fi signal received by the users of a WifiPointOfInterest. Daily value.
	
### Contributors
[Link](./CONTRIBUTORS.yaml) to the current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](./issues) or submit your [PR](./pulls) on existing data models

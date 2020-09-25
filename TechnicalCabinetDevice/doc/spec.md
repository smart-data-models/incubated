# **Technical Cabinet Device**

- required:
	- location
	- dateLastReported
	- typeOfUse
	- dimension
- type: "object"
	- allOf:
		- "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
		- "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
- description: >

## Description

The Data Model is intended to to describe the technical characteristics for a technical Cabinet, designed to be placed in an urban or interurban environment. 
The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. 
The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. 

*Additional Information about this data Model :*
This Data Model can be used directly as a main entity to describe the Device [TechnicalCabinet] or as a sub-entity of the Data Model [Device] using a reference by the `refDevice` attribute.

It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model [Device] or [TechnicalCabinet].

## Data Model

- properties:

	### Common parameters for data identification.

	- id:
		- x-ngsi:
			- type: "Property"
			- type : "string"
		- Description: "mandatory element for NGSI"
		- format: "uri"
	- type:
		- x-ngsi:
			- type: "Property"
		- Description: "Entity type, mandatory element for NGSI"
		- type : "string"
		- value: "TechnicalCabinetDevice"
	- dataProvider:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/URL"
		- description: > Specifies the URL to information about the provider of this information
		- type: "string"
			- format: "URL"
	- source:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text", "https://schema.org/URL"
		- description: > A sequence of characters giving the source of the entity data.
		- type: "string"
	- name:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/name"
		- description: > Name given to the observation.
		- type: "string"
	- alternateName:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/alternateName"
		- description: > Alternative Name given to the observation
		- type: "string"
	- description:
		- x-ngsi:
			- type: "Property"
			- model: "https://uri.etsi.org/ngsi-ld/description", "https://schema.org/description"
		- description: > Description of the observation.
		- $ref: 'https://jason-fox.github.io/swagger-datamodel-test/common.yaml#/Description'
	- seeAlso:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text", "https://schema.org/URL"
		- description: > Text or Link that can provide additional information.
		- type: "string"

	### Information about Location and Address.

	- location
		- x-ngsi:
			- type: "Property"
			- model: "https://tools.ietf.org/html/rfc7946".
		- $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.yaml#/Geometry"
		- description: > Location represented by a GeoJSon geometry [Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon]
	- address:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/address"
		- description: > Civic Address
		- $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.yaml#/Address"
	- areaServed:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Zone of level higher to the attributes Location & Address to gather and cross information (ex district, etc)
		- type: "string"

	### Information related to the date of last reporting

	- dateLastReported:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/DateTime"
		- description: > A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.
		- type: "string"
			- format: "date-time"

	### Information about a reference to other Data Models.

	- refDevice : 
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link.  
		- type: "string"
			- format: "URL"
	- refPointOfInterest : 
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.
		- type: "string"
			- format: "URL"
	- refDeviceList : 
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > A list of reference to the [Devices](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which are inside the technical Cabinet Device.  
		- type: "array"
			- format: "URL"		

	### Information related to the model 

	- brandname:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/brand"
		- description: > Brand Name.
		- type: "string"
	- modelName:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/model"
		- description: > Model Name.
		- type: "string"
	- manufacturerName:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/manufacturer"
		- description: > Manufacturer Name.
		- type: "string"
	- serialNumber:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/serialNumber",
		- description: > Serial numbers.
		- type: "number"
	- application:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Target application of the Device regarding the environment. A combination of :
		- type: "string"
		- type: "array"
			- Items:
				- enum : 
					- commercial, industrial, tertiary, road, publicWorks, private, urbanService, distributionService, other
	- typeOfUse :  
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of :
		- type: "string"
		- enum : 
			- indoor, outdoor, mixed, other
	- instalationMode:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Positioning of the device in relation to a ground reference system. A unique value of :
		- type: "string"
		- enum : 
			- ground, underGround, aerial, wall, pole, roofing, other
	- instalationCondition:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Condition and possibility of use in the following environments. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- extremeHeat, extremeCold, extremeHumidity, extremeClimate, desert, sand, marine, saline, dust, seismic, other
	- possibilityOfUse:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Possibility of use. A unique value of :
		- type: "string"
		- enum : 
			- stationary, mobile, mixed, other
	- documentation:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text", "https://schema.org/URL"
		- description: > Technical Documentation (Installation / maintenance / used).
		- type: "string"
	- owner:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text" included references to "http://schema.org/Person", "https://schema.org/Organization", "https://schema.org/URL".
		- description: > The owners of the Device. A list of [Text], [Person], [Organisation] or [URLs].
		- type: "array"
			- items:
				- type: string

	### Information related to Mechanical Data 

	- dimension : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number",
		- description: > External dimension. The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter.
		- type: "number"
		- type: [StructuredValue](http://schema.org/StructuredValue)
			- type: string
			- items:
				- width
				- height
				- depth
	- weight :
			- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"
		- description: Weight. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents KiloGramme.
		- type: "Number"
	- internalDimension : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number",
		- description: > internal dimension corresponding to the place to work inside the technical cabinet. The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter.
		- type: "number"
		- type: [StructuredValue](http://schema.org/StructuredValue)
			- type: string
			- items:
				- width
				- height
				- depth

	### Information about Security Classification

	- protectionIP :   
		- x-ngsi:
			- type: "Property"
			- model: [IP_Code/EN 60529](https://en.wikipedia.org/wiki/IP_Code),
		- description: > IP "*Ingress Protection*" for the Junction Box. Th is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529).
			- First digit: Solid particle protection (Single numeral: 0–6 or "X"). 
			- Second digit: Liquid ingress protection (Single numeral: 0–9 or "X" ).
			- Third digit: Personal Protection  against access to dangerous parts (optional additional letter).
			- Fourth digit: Other protections (optional additional letter).
		- type: "string"
	- protectionIK :   
		- x-ngsi:
			- type: "Property"
			- model: [IP_Code/EN 60529](https://en.wikipedia.org/wiki/IP_Code),
		- description: > IK "*Mecanic Protection*" level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262).
			- IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)
		- type: "Number"

	### Information about Operating Data

	- maximumSystemVoltage : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > Maximum system voltage permitted. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt.
		- type: "number"

	### Information about Temperatures Characteristics

	- operatingTemperature : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number",
		- description: > Ambient operating temperature range. Th is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius.
		- type: [StructuredValue](http://schema.org/StructuredValue)
			- type: string
			- items :
				- min
				- max

	### Information about Technical Characteristics

	- protectionOthers :  
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Others protection of the technical cabinet. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- basement, shielding, solar, water, dust, dampProof, insect, forcedOpening, saltSpray, abrasion, doorTearing, roofOverload, vandalism, graffiti, display, other
	- doorCount : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > Count of doors of the technical Cabinet.
		- type: "number"
	- doorType : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"			
		- description: > Type of door of the technical Cabinet. A unique value of : 
		- type: "string"
			- enum : 
				- solid, transparent, mixed, other
	- doorOpeningAngle : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > Door opening angle expressed in decimal degrees with a range from 0 to 180 degree. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **DD** represents Decimal Degrees.
		- type: "number"
			- min: 0
			- max : 180
	- doorClosingMode :   
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"			
		- description: > Door closing mode. A unique value of : 
		- type: "string"
			- enum : 
				- revolvingHandle, fixedHandle, triangleHandle, other)
	- designMaterials :    
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > design materials to build the cabinet. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- stainlessSteel, galvanizedSteel, aluminum, ABS-Plastic, fiberGlass, polyester, other

	- interiorCoating : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Interior Coating. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- heatInsulating, polyesterResin, fiberGlass, polyester, plastic, Steel, other
	- exteriorCoating :   
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Exterior Coating. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- polyesterResin, fiberGlass, polyester, plastic, Steel, other
	- exteriorFinish : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: >  Exterior finition. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- textured, smooth, roughcast, raised, graffiti, other
	- ventilationMode :  
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text",
		- description: > Ventilation mode. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- selfVentilatedGills, airConditioners, dehumidifier, none, other
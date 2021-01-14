# Event

- required: 
	- location
	- dateLastReported
	- category 
	- locationName
	- title
- type: "object"
	- allOf:
		- "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/Location-Commons"
		- "$ref": "https://smart-data-models.github.io/data-models/common-schema.json#/definitions/GSMA-Commons"
- description: >

## Description

The Data Model is intended to provide information relating to the events listed in the `category` attribute and offers a Generic Data Model to events over a temporary period (eg: concert, exhibition, etc.) or to outings which correspond to a fixed place in the municipality (eg: theater, ...).
Depending on the value of the `category` attribute, common themes (eg : startDate & endDate / openingHoursSpecification / ...  ) or specific (pitch / performer / actors / criticReview / ...) are identified in dedicated sections.
For some attributes, lists of default values are proposed as first repository in order to better understand the meaning of the attribute.

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
			- type : "string"
		- Description: "Entity type, mandatory element for NGSI"
		- type : "string"
		- value: "Events"
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
		- description: > Name given to the Event.
		- type: "string"
	- alternateName:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/alternateName"
		- description: > Alternative Name given to the Event
		- type: "string"
	- description:
		- x-ngsi:
			- type: "Property"
			- model: "https://uri.etsi.org/ngsi-ld/description", "https://schema.org/description"
		- description: > Description of the Event.
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
			- type: type: "Geo Property".
		- description: > Location represented by a GeoJSon geometry [Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon]
		- $ref: "https://github.com/smart-data-models/data-models/blob/master/common-schema.yaml#/Geometry"
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
	
	### Information about the date of last reporting
	
	- dateLastReported:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/DateTime"
		- description: > A timestamps which denotes the last time when the device successfully reported data. The date and time of this Event in ISO8601 UTCformat.
		- type: "string"
		- format: "date-time"
	
	### Information about a reference to other Data Models .
	
	- refPointOfInterest : 
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Event.  
		- type: "string"
		- format: "URL"
	
	### Information about contact point and access Plan to the event
	
	- contactPoint:
		- x-ngsi:
			- type: "Property"
			- model: [Contact Point](https://schema.org/ContactPoint)
		- description: > Contact Point.
		- type: "string"
	- accessPlan:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text", "https://schema.org/URL"
		- description: > Text or Link to the acces plan to the event.
		- type: "string"
	
	### General Information about the event 
	
	- category:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Category of the event. A combination of free text to remain flexible to a specific context is offered below as an initial repository.   
		- type: "string"
			- enum :
				- festival, spectacle, music, theater, concert, sport, exhibition, leisurePark
	- subCategory : 
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Sub-category of the `category` attribute. A combination of free text to remain flexible to a specific context is offered below as an initial repository.  
		- type: "string"
			- enum :
				- festival
					- movies, nautical, equestrian, dance, humor, circus, music, theater,   
					- gastronomic, 
					- multimedia, literary, gaming, robotics,
				- spectacle, 
					- cabaret, theater, cafe-theater, circus, ice, children, puppet, mime
					- worldDance, contemporaryDance, classicDance, country, russianBallet, ballet, folklore, diverseDanse 
					- magicTrick, mentalism, 							
					- humorist, oneManShow, 
					- soundsAndLights, firework, 
					- parade, carnival,  
				- music 
					- classical, contemporary, lyrical, sacred, baroque
				- theater
					- musical, classical, lyrical, contemporary, children, reading, debate,
					- romantic, satirical, boulevard, dramatic, vaudeville, humor,
					- oneManShow, puppet, mime, 
					- opera, operetta,
				- concert 
					- french variety, international variety, 
					- rap, pop, rock, hipHop, soul, funk, reggae, electro, clubbing, rnB,
					- hardrock, metal,		
					- jazz, blues, gospel, country,
					- worldMusic, otherMusic, 
				- sport
					- football, rugby, basketball, handball, volleyball, hockey, cycling, horseRiding, swimming, tennis, martialArts, boxing, catch, wrestling, mechanicalSport,
				- exhibition,
					- museum, monument, guidedTour, workshop, seminar
				- leisurePark
					- attraction, aquatic, animal, aquarium 	
	- thematic
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > A list of thematic as keywords.  
		- type: "array"
			- items:
				- type: "string"
	- locationName:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Name of the event location. 
		- type: "string"
	- title:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Title of the event. 
		- type: "string"
	- slogan:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Event header line, matches the text hook. 
		- type: "string"
	- language:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/language"			
		- description: > List of Formal language used during the Trip expressed from the IETF [BCP 47](https://tools.ietf.org/html/bcp47) standard.
		- type: "array"
			- items:
				- type: "string"
	
	### Detailed information about the event and its hierarchy in a festival  
	
	- superEvent:
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > Reference to the Major Event that includes this event in the case of a festival for example. 
		- type: "string"
	- subEvent:
		- x-ngsi:
			- type: "Relationship"
			- model: "https://schema.org/URL"
		- description: > Reference to a list of Minor Event that are part of this major event in the case of a festival for example. 
		- type: "array"
			- items:
				- type: "string"
	- eventStatus:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Event Status regarding this event. A unique value  : 
		- type: "string"
			- enum : 
				- opened, closed, suspended, cancelled, scheduled, finished, postponed, rescheduled, inProgress, movedOnline
	
	### Information related to the date and period of the event
	
	- startDate:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/DateTime"
		- description: > Start date and time in an ISO8601 UTC format. .
		- type: "string"
		- format: "date-time"
	- endDate:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/DateTime"
		- description: > End date and time in an ISO8601 UTC format. .
		- type: "string"
		- format: "date-time"
	
	### Information about the general Opening Hours specification or EventSchedule of the event.
	##### **- Rules:** ***An Event that is associated with a Schedule using this property should not have `startDate` or `endDate` properties. These are instead defined within the associated Schedule, this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules (different months or seasons).*** 
	
	- openingHoursSpecification : 
		- x-ngsi:
			- type: "Property"
			- model: http://schema.org/openingHoursSpecification
		- description: > General Opening hours specification. 
		- type: "array"
			- items:
				- type: "object"
				- properties :
					- type: 
						- type: "string"
							- values:
								- type: "array"
									- items:
										- type: "string"
	- eventSchedule : 
		- x-ngsi:
			- type: "Property"
			- model: http://schema.org/Schedule
		- description: > Event Schedule. This allows a schedule to be set over a repeated period of time used to describe an event that occurs regularly. eg nota in the beginning of the section for restriction to use this attribute. 
		- type: "string"
	- duration:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > The duration of each show. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HUR** represents **Hours**.
		- type: "number"	
	- doorTimeOpen:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Doors opening time to access the show.
		- type: "string"
	- doorTimeClose:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Doors closing time to access the show.
		- type: "string"
	
	### Detailled Information about the event 
	
	- pitch:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/object"		
		- description: > Pitch of the Event. Each items have the format based on the  [Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with "Language Value" : "Article Value". 
		- type: "Object"
			- items : 
				- language : 
					- x-ngsi:
						- type: "Property"
						- model: "https://schema.org/Text"
					- description: > Language used for the article of the event regarding the norm [WPcode] (https://en.wikipedia.org/wiki/List_of_Wikipedias)
					- type: "string"
						- properties :
							- article : 
								- x-ngsi:
									- type: "Property"
									- model: "https://schema.org/Text"
								- description: > Pitch of the event, corresponding to the language attribut.
								- type: "string"	
	- webSite:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Link to the official website for more information.
		- type: "string"   
	- contenteURL:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/image"
		- description: > Specifies the URL to the official image or video of the event for more information.
		- type: "string"
		- format: "URL"
	- performer:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Main actor or presenter or musician or musical group of the event.
		- type: "array"
			- type: "string"
	- actor:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of actor or music group.
		- type: "array"
			- type: "string"
	- composer:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of person who wrote the composition.
		- type: "array"
			- type: "string"
	- director:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of director who manage the composition.
		- type: "array"
			- type: "string"
	
	### Information about official critics from 
	
	- criticReview
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/object"
		- description: > Review written or published by a source that is recognized for its reviewing activities. Each items have the format based on the [Internationalization (i18N) - W3C recommandation for multilanguage](https://www.w3.org/TR/json-ld/#string-internationalization) integrating all items in a single property (ex number 71). Each item is represented by a string with "Language Value" : { "Article Value" }.
		- type: "Object"
			- items : 
				- language : 
					- x-ngsi:
						- type: "Property"
						- model: "https://schema.org/Text"
					- description: > Language of the description of the critic review regarding the norme [WPcode] (https://en.wikipedia.org/wiki/List_of_Wikipedias)
					- type: "string"
						- properties : 
							- article : 
								- x-ngsi:
									- type: "Property"
									- model: "https://schema.org/Text"
								- description: > Critic of the event.
								- type: "string"			
							- origine : 
								- x-ngsi:
									- type: "Property"
									- model: "https://schema.org/Text"
								- description: > origine of the article.
								- type: "string"			
	- ratingValue
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"		
		- description: > Rating value of events. Usage guidelines: Use values from 0 to 10 depending on your standard. this is the average value of all detailed scores of `starRatingDetailed` attribut.
		- type: "number"	
	- starRatingDetailed
		- x-ngsi:
			- type: "Property"
			- model: "http://schema.org/StructuredValue"		
		- description: > Detailed star ratings which led to the average value expressed in the ratingValue. Instructions for use: A structured value from 1 to 10 occurrences (Stars) where each element is a string in the format: `NumberOfSTar`: Percent. 
		- type: "array"
			- items : 
				- type: "string"   
	
	### Information about Audience 
	
	- audience:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > Type of public concerned by this event. A combinaison of Free text (family, adult, children, teenager, senior, allPublic, ...)
		- type: "array"
			- items:
				- type: string
	- wheelChairAccessible:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/boolean"			
		- description: > Access possible for Person with Reduced Mobility..
		- type: "Booelean"
		- Default value : false
	- maximumAttendeeCapacity
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > The total number of people who can attend to the event at that location.
		- type: "number"	
	
	### Detailled Information about the price of the event.
	
	- isAccessibleForFree:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/boolean"			
		- description: > Free or paid event (True = Free / False = Paid).
		- type: "Booelean"
		- Default value : true
	- eventPriceFrom:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > Min Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.
		- type: "number"	
	- eventPriceTo:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Number"			
		- description: > Max Price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.
		- type: "number"	
	- priceSpecification:
		- x-ngsi:
			- type: "Property"
			- model: http://schema.org/priceSpecification
		- description: > A Object value which can be used in addition to the 2 attributes `eventPriceFrom` `eventPriceTo` to precisely detail the price ranges depending to audience profile or seat categories. The items are :
		- type: "string"
			- categoryDescription
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Number"
				- description: > Description of the seat category. 
				- type: "number"	
			- audience:
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Text"
				- description: > Public concerned by this price. A list of value of Free text (family, adult, children, teenager, senior, allPublic, ...)
				- type: "array"
					- items:
						- type: string
			- eligibleQuantity
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Number"
				- description: > Quantities for which the offer or price specification is valid.
				- type: "number"	
			- price
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Number"
				- description: > The price. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.		
				- type: "number"	
			- minPrice
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Number"
				- description: > The lowest price if the price is a range. The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.		
				- type: "number"	
			- maxPrice
				- x-ngsi:
					- type: "Property"
					- model: "https://schema.org/Number"
				- description: > The highest price if the price is a range.	The unit code (text) of measurement is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **EUR** represents **€uro**.	
			- type: "number"	
	
	### Information related to the price and means of payment of the event 
	
	- paymentAccepted:
		- x-ngsi:
			- type: "Property"
			- model: [Payment Accepted](https://schema.org/paymentAccepted)
		- description: > Accepted payment if `eventFree` is False. A combination of a list of active codes defined in the model :
		- type: "array"
			- items:
				- type: string
				- enum : 
					- Cash, CreditCard, CryptoCurrency, meal vouchers, other 
	- currencyAccepted:
		- x-ngsi:
			- type: "Property"
			- model: [Currencies Accepted](https://schema.org/currenciesAccepted), [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system)
		- description: > Currency accepted for payment if `eventFree` is False. A combination of a list of active codes defined in the model :
		- type: "array"
			- items:
				- type: string
				- enum : 
				- EUR, USD, GBP, CHF, Bitcoin, Neo, ...
	
	### Information detailing the transport proposed near the event
	
	- routeType:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of the urban transports (subway, Bus, Tram, ...) available near the event according to the GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values composed only of the attribute 'description'.
		- type: "array"
			- items:
				- type: string
				- enum : tram, subway, train, bus, ferry, cableTram, cableCar, funicular, trolleybus, monorail
	- transportServices:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of private transport available near the event. for example taxi, uber, vtc, parkingShuttle 
		- type: "array"
			- items:
				- type: string
	- electricTransport:
		- x-ngsi:
			- type: "Property"
			- model: "https://schema.org/Text"
		- description: > List of the different types of electric transport proposed by the city. A combination of :
		- type: "array"
			- items:
				- type: string
				- enum :  
					- electricCar, electricBicycle, electricMotorBike, electricScooter 
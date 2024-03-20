# SUMMARY

Directory to store the structure of the datamodels proposed to map a complete RAMI4.0 Asset Adminitration Shell (AAS).
This is developed, deployed and tested within the scope of [CoRoSect EU project](https://corosect.eu/).

# Origin

This Smart Data Model is a proposal to translate and manage within NGSI (exploiting the capabilities of a FIWARE environment) a [RAMI4.0](https://ec.europa.eu/futurium/en/system/files/ged/a2-schweichhart-reference_architectural_model_industrie_4.0_rami_4.0.pdf) **Asset Administration Shell** (AAS), creating a generic structure to define Digital Twins within the smart manufacturing environment.  This is planned to be used as part of a FIWARE for Industry (F4I) framework to foster the uses cases and pilots to be deployed in the CoRoSect project.
The AAS schema used for these Digital Twins is based on the [IDTA 01001-3-0 specification](https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf)

# Structure

The proposed set of NGSI Entities represents the different parts of the AAS schema proposed by Industry4.0 to create the Digital Twin of a device/system involved in the manufacturing chain of a I4.0 framework. According to the figure below, these entities are linked (refenced) between them to create the final AAS.

![NGSI entyties' tree to map an RAMI4.0 Asset Administration Shell](/SMARTMANUFACTURING/corosect/images/DTwinStructure.png)

# Example

The files provided within the corresponding entities' [folder](/SMARTMANUFACTURING/corosect/DigitalTwinExample/) illustrates the DIGITAL TWIN defined for one of the Kuka Robots (supported by the [University of Maastricht](https://www.maastrichtuniversity.nl/research/department-advanced-computing-sciences)) which is shown in this figure.

![Proposed Digital Twin for Maastricht Kuka's robot](/SMARTMANUFACTURING/corosect/images/MRobot-Example.png)
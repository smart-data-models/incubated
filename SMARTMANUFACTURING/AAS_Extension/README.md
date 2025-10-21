# SUMMARY

Extension of RAMI4.0 Asset Adminitration Shell (AAS) representation in NGSI-LD with two additional submodel elements 'Relationship' and 'Capability' according to AAS standard.

# Origin

The extension has been made to represent agents in a multi-agent system following the principles of capability-based engineering and making use of the proposed AAS ontology by Bayha et al. (see https://industrialdigitaltwin.org/wp-content/uploads/2021/09/11_capabilities_i40_components_en_2020.pdf).


# Structure

The Capability data model describes the abstract goals and tasks an Industry 4.0 component can accomplish in the context of an industrial process. The already existing Operation data model (see https://github.com/smart-data-models/dataModel.AAS/tree/master/I4SubmodelElementOperation) complements this by specifying the concrete executable functions employed to realize the capabilities of an Industry 4.0 component. Together, the Capabilities and Skills data model can establish a hierarchical description linking the strategic goals of an an Industry 4.0 component to the concrete operations required to achieve them. This relationship is formalized through dedicated Relationship Elements, which associate one or more skills with a specific capability. 

# Example

The examples listed illustrate the digital twin created for a planning agent. The planning agent is capable of planning overall operations and, among other things, has the ability to create an operating plan in which an optimized schedule with start and stop times is calculated.


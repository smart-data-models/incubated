import xml.etree.ElementTree as ET

# Parse the XML string
xml_string = '''<?xml version="1.0"?>
<rdf:RDF xmlns="http://data.europa.eu/949/"
     xml:base="http://data.europa.eu/949/"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:ns="http://www.w3.org/2003/06/sw-vocab-status/ns#"
     xmlns:ns1="http://creativecommons.org/ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:data="http://data.europa.eu/949/"
     xmlns:foaf="http://xmlns.com/foaf/0.1/"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:skos="http://www.w3.org/2004/02/skos/core#"
     xmlns:terms="http://purl.org/dc/terms/"
     xmlns:wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <owl:Ontology rdf:about="http://data.europa.eu/949/">
        <owl:imports rdf:resource="http://www.opengis.net/ont/geosparql#"/>
        <ns1:license rdf:resource="https://creativecommons.org/licenses/by/4.0/"/>
        <terms:author>Edna Ruckhaus</terms:author>
        <terms:author>Oscar Corcho</terms:author>
        <terms:contributor rdf:resource="https://dylanvanassche.be/#me"/>
        <terms:contributor rdf:resource="https://julianrojas.org/#me"/>
        <terms:contributor rdf:resource="https://pietercolpaert.be/#me"/>
        <terms:contributor>Ivo Velitchkov</terms:contributor>
        <terms:contributor>Marina Aguado</terms:contributor>
        <terms:contributor>Polymnia Vasilopoulou</terms:contributor>
        <terms:contributor>Wouter Beek</terms:contributor>
        <terms:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-07-29</terms:issued>
        <terms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2023-03-29</terms:modified>
        <terms:publisher>European Union Agency for Railways</terms:publisher>
        <terms:title xml:lang="en">ERA vocabulary</terms:title>
        <rdfs:comment xml:lang="en">This is the human and machine readable Vocabulary/Ontology governed by the European Union Agency for Railways (https://www.era.europa.eu/). It represents the concepts and relationships linked to the sectorial legal framework and the use cases under the Agency´s remit, as described in the Commission Implementing Regulation (EU) [to be updated after publication] on the common specifications for the register of railway infrastructure [to be updated after publication].

Currently, this vocabulary covers the European railway infrastructure and the vehicles types authorized to operate over it. It is a semantic/browsable representation of the RINF application guide (https://www.era.europa.eu/sites/default/files/registers/docs/rinf_application_guide_for_register_en.pdf) and ERATV application guide (https://www.era.europa.eu/sites/default/files/registers/docs/iu-eratv_application_guide_for_register_2016-797_en.pdf) that were built by domain experts in the RINF and ERATV working parties.

The vocabulary also includes the routebook concepts described in appendix D2 &quot;Elements the infrastructure manager has to provide to the railway undertaking for the Route Book&quot; as presented in the Commission Implementing Regulation (EU) [to be updated after publication] 2019/773 of 16 May 2019 on the technical specification for interoperability relating to the operation and traffic management subsystem of the rail system within the European Union and [to be updated after publication] and the Appendix D3 [to be updated after publication].</rdfs:comment>
        <rdfs:label xml:lang="en">ERA vocabulary</rdfs:label>
        <owl:priorVersion xml:lang="en">https://git.fpfis.eu/datateam/ERA/era-vocabulary/-/releases/v2.6.3</owl:priorVersion>
        <owl:versionInfo xml:lang="en">v3.0.0</owl:versionInfo>
        <owl:versionURI xml:lang="en">https://git.fpfis.eu/datateam/ERA/era-vocabulary/-/releases/v3.0.0</owl:versionURI>
    </owl:Ontology>
    <owl:DatatypeProperty rdf:about="http://data.europa.eu/949/additionalBrakingInformationDocument">
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://data.europa.eu/949/SubsetWithCommonCharacteristics"/>
                    <rdf:Description rdf:about="http://data.europa.eu/949/Track"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#anyURI"/>
        <XMLName>CBP_BrakePerfDocRef</XMLName>
        <rinfIndex>1.1.1.3.11.3</rinfIndex>
        <usedInRCCCalculations rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</usedInRCCCalculations>
        <terms:created rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-08-24</terms:created>
        <terms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2021-09-12</terms:modified>
        <rdfs:comment xml:lang="en">Electronic document available in two EU languages from the IM stored by the Agency providing additional information as defined in point (2) of point 4.2.2.6.2 of OPE TSI.</rdfs:comment>
        <rdfs:isDefinedBy rdf:resource="http://data.europa.eu/949/"/>
        <rdfs:label xml:lang="en">Documents available by the IM relating to braking performance</rdfs:label>
        <ns:term_status>stable</ns:term_status>
    </owl:DatatypeProperty></rdf:RDF>'''

root = ET.fromstring(xml_string)

# Find the owl:Class tag and get its content
owl_class = root.find('.//{http://www.w3.org/2002/07/owl#}Class')
content = ET.tostring(owl_class, encoding='unicode', method='xml')
print(content)

from rdflib import Graph

# Read the RDF/XML file into a string variable
with open('one_property.rdf', 'r') as f:
    rdf_string = f.read()

# Parse the RDF/XML string into an RDF graph
g = Graph().parse(data=rdf_string, format='xml')

# Extract the XML structures you are interested in
xml_dict = {}
for s, p, o in g.triples((None, None, None)):
    if str(p).endswith('ObjectProperty'):
        xml_dict[str(s)] = str(g.serialize(format='xml', destination=None, source=s))

# Print the resulting dictionary
print(xml_dict)

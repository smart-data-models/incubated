from rdflib import Graph

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("mandate.ttl", format="turtle")

# Iterate over the triples in the graph
for subj, pred, obj in g:
    print(subj, pred, obj)
    print(type(subj), type(pred), type(obj))
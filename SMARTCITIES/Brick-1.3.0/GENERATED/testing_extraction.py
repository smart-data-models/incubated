from rdflib import Graph

# Parse the TTL file
g = Graph()
g.parse("./../examples/soda_brick.ttl", format="ttl")

# Extract the subject, predicate, and object of each triple
for subj, pred, obj in g:
    print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")

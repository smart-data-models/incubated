import rdflib
import json

def ttl_to_json_schema(ttl_data):
    # Parse the TTL data
    g = rdflib.Graph()
    g.parse(ttl_data)

    # Extract the classes and their properties
    classes = {}
    for resource in g.objects(None, rdflib.RDF.type):
        if isinstance(resource, rdflib.URIRef):
            class_name = resource.toPython()

            # Extract properties
            properties = []
            for predicate in g.objects(resource, rdflib.RDF.property):
                if isinstance(predicate, rdflib.URIRef):
                    property_name = predicate.toPython()
                    value = g.objects(resource, predicate)

                    # Determine data type
                    datatype = None
                    for object_in_graph in value:
                        if isinstance(object_in_graph, rdflib.Literal):
                            datatype = object_in_graph.datatype

                    # Create dictionary for property
                    property = {
                        "name": property_name,
                        "type": None if datatype is None else datatype.toPython()
                    }

                    # Handle nested properties
                    if isinstance(value[0], rdflib.BNode):
                        if value[0] in g:
                            nested_properties = ttl_to_json_schema(g.serialize(value[0]))
                            property["properties"] = nested_properties

                    properties.append(property)

            classes[class_name] = {
                "type": "object",
                "properties": properties
            }

    # Generate JSON schema
    json_schema = {
        "definitions": classes
    }

    return json_schema

# Convert TTL data from a file
# with open("./examples/air_quality_sensors/air_quality_sensor_example.ttl", "r") as f:
with open("Brick.ttl", "r") as f:
    json_schema = ttl_to_json_schema(f.read())
from pprint import pprint
from jsonref import JsonRef
import jsonref
import sys

# Sample JSON data, like from json.load
inFile = "schema.json"
inFileHandler = open(inFile, "r")

schemaContent = inFileHandler.read()
schema = jsonref.loads(schemaContent)

# The JsonRef.replace_refs class method will return a copy of the document
# with refs replaced by :class:`JsonRef` objects
# pprint(JsonRef.replace_refs(schema))
outFile = "extended_schema.json"
outHandler = open(outFile, "w")
sys.stdout = outHandler
print(schema)

# Sample JSON data, like from json.load
inFile = "schema2.json"
inFileHandler = open(inFile, "r")

schemaContent = inFileHandler.read()
schema = jsonref.loads(schemaContent)

# The JsonRef.replace_refs class method will return a copy of the document
# with refs replaced by :class:`JsonRef` objects
# pprint(JsonRef.replace_refs(schema))
outFile = "extended_schema2.json"
outHandler = open(outFile, "w")
sys.stdout = outHandler
print(schema)

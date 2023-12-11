from jsonschema import validate

def open_jsonref(fileUrl):
    import jsonref
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            output = jsonref.loads(pointer.content.decode('utf-8'), load_on_repr=True)
            return output
        except:
            return ""
    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return jsonref.loads(file.read())
        except:
            return ""

def validate_dcat_ap_distribution_sdm(json_data):
    """The function takes a distribution DCAT-AP in json and validates if the downloadURL contains a valid payload against conformsTo.
    It works when the downloadURL contains a json keyvalues payload and
    conformsTo point to the raw version of a Smart Data Model
       Parameters:
           json_data: metadata in DCAT-AP distribution format (See https://github.com/smart-data-models/dataModel.DCAT-AP/blob/master/Distribution/schema.json and
           https://semiceu.github.io/DCAT-AP/releases/3.0.0/
                conformsTo: Attribute (Array) with links to the json schemas of SDM
                downloadURL: Public available link to the raw format of the payload

       Returns:
           It prints a version of the attributes separated by the separator listing the meta_attributes specified
           A variable with the same strings
           if any of the input parameters is not found it returns False """

    validated = False
    conforms_to = json_data.get('conformsTo', [])   # retrieves the attriute conformsTo

    ################## SECTION FOR VALIDATION WITH SMART DATA MODELS ##################
    valid_link = any(link.startswith('https://github.com/smart-data-models') or link.startswith("https://raw.githubusercontent.com/smart-data-models") for link in conforms_to)
    # it checks that the link belong to smart data Models
    # it should point to the raw version of the json schema
    if not valid_link:
        print('Warning: "conformsTo" attribute should contain at least one link belonging to the domain github.com/smart-data-models')
        return validated
    schemas = [link for link in conforms_to if link.startswith('https://github.com/smart-data-models') or link.startswith("https://raw.githubusercontent.com/smart-data-models")]
    # only those schemas belonging to Smart Data Models are analysed

    # Check if 'downloadURL' attribute points to a valid location to download a file
    if json_data.get('downloadURL', '') is None:
        print('Warning: "I cannot access the distribution URL')
        return validated
    else:
        download_url = json_data.get('downloadURL')
        print(download_url)


    for distribution in download_url:
        payload = open_jsonref(distribution)    # It retrieves the content of the payload to be validated
        for schema in schemas:
            print(schema)
            schema = open_jsonref(schema)       # It retrieves the schema for validating the payload
            try:
                validate(instance=payload, schema=schema)
                print("The download URL content is validated by the JSON schema.")
                # If you reach this point, the content is validated by the current schema
                validated = True
                break
            except Exception as e:
                # If the content is not validated by the current schema, try the next one
                continue
        else:
            print("The download URL content is not validated by any of the JSON schemas.")
            return validated
    return validated

    ################## END OF SECTION FOR VALIDATION WITH SMART DATA MODELS ##################



json_payload = open_jsonref("https://raw.githubusercontent.com/smart-data-models/dataModel.DCAT-AP/master/Distribution/examples/example.json")
# Call the function with the JSON payload
if validate_dcat_ap_distribution_sdm(json_payload):
    print("ok")
else:
    print("Next one")

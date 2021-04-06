def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        pointer = requests.get(fileUrl)
        return json.loads(pointer.content.decode('utf-8'))
    else:
        # es file
        file = open(fileUrl, "r")
        return json.loads(file.read())

def translateBasicType(type):
    if type == "time":
        return {"type": "string", "format": "date-time"}
    elif type == "string":
        return {"type": "string"}
    elif type == "duration":
        return {"type": "string", "format": "date-time"}
    elif type == "uint8":
        return {"type": "integer", "minimum": 0, "maximum": 255}
    elif type == "bool":
        return {"type": "boolean"}
    elif type == "int8":
        return {"type": "integer", "minimum": -127, "maximum": 128}
    elif type == "uint16":
        return {"type": "integer", "minimum": 0, "maximum": 65535}
    elif type == "int16":
        return {"type": "integer", "minimum": -32768, "maximum": 32767}
    elif type == "uint32":
        return {"type": "integer", "minimum": 0}
    elif type == "int32":
        return {"type": "integer"}
    elif type == "uint64":
        return {"type": "integer", "minimum": 0}
    elif type == "int64":
        return {"type": "integer"}
    elif type == "float32":
        return {"type": "number"}
    elif type == "float64":
        return {"type": "number"}
    else:
        return type


def parse_model(payload):
    output = {}
    lines = payload.splitlines()
    message = ""
    for line in lines:
        print(line)
        if len(line) > 0:
            if line[0] != "#":
                if "#" in line:
                    lineToParse = line[:line.find("#")]
                    message += line[line.find("#"):]
                else:
                    lineToParse = line
                arguments = lineToParse.split(" ")
                print(arguments)
                if "[]" in arguments[0]:
                    output[arguments[1]] = {"type": "array", "description": "Property." + message, "items": {"type": translateBasicType(arguments[0][:-2])}}
                    message = ""
                else:
                    output[arguments[1]] = {"type": translateBasicType(output[arguments[0]]), "description": "Property." + message}
                    message = ""
            else:
                message += line[2:]
    return output


def list_files(pattern, path):
    from github import Github
    credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
    # credentials = "/home/fiware/credentials.json
    credentials = open_json(credentialsFile)
    token = credentials["token"]
    globalUser = credentials["globalUser"]
    g = Github(token)
    mainRepo = "ros/common_msgs"
    repo = g.get_repo(mainRepo)
    contents = repo.get_contents(path)
    output = []
    while contents:
        file_content = contents.pop(0)
        print(file_content.path)
        if file_content.type == "dir":
            result = list_files(pattern, file_content.path)
            if result:
                for element in result:
                    output.append(element)
        else:
            fileName = file_content.path.split("/")[-1]
            if pattern in fileName:
                output.append(file_content.path)
    return output


from github import Github
credentialsFile = "/home/aabella/transparentia/CLIENTES/EU/FIWARE/credentials.json"
# credentials = "/home/fiware/credentials.json
credentials = open_json(credentialsFile)
token = credentials["token"]
globalUser = credentials["globalUser"]
g = Github(token)
mainRepo = "ros/common_msgs"
repo = g.get_repo(mainRepo)

msgList = list_files(".msg", "")
file_content = repo.get_contents(msgList[1])
payload = file_content.decoded_content.decode()
print(parse_model(payload))
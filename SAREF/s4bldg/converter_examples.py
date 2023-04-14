import json


def open_json(fileUrl):
    import json
    import requests
    if fileUrl[0:4] == "http":
        # es URL
        try:
            pointer = requests.get(fileUrl)
            return json.loads(pointer.content.decode('utf-8'))
        except:
            return None

    else:
        # es file
        try:
            file = open(fileUrl, "r")
            return json.loads(file.read())
        except:
            return None


fileName = "example.json"
# directories = ["EvaporativeCooler", "Evaporator", "Fan", "Filter", "FireSuppressionTerminal", "FlowInstrument",
#                "FlowMeter", "HeatExchanger", "Humidifier", "Interceptor", "Lamp", "MedicalDevice", "Outlet",
#                "ProtectiveDevice", "ProtectiveDeviceTrippingUnit", "Pump", "SanitaryTerminal", "ShadingDevice",
#                "SolarDevice", "SpaceHeater", "SwitchingDevice", "Tank", "Transformer", "TransportElement", "TubeBundle",
#                "UnitaryControlElement", "Valve", "VibrationIsolator" ]
directories = ["EvaporativeCooler"]
new_payload = {}
for directory in directories:
    payload = open_json(directory + "/examples/" + fileName)
    # Iterate over all the attributes and extract the "value" field
    for key in payload:
        if isinstance(payload[key], dict) and 'value' in payload[key] and "value" in payload[key]["value"]:
            new_payload[key] = payload[key]['value']['value']
        else:
            new_payload[key] = payload[key]
    # Save the updated payload
    with open(directory + "/examples/" + 'updated_payload.json', 'w') as f:
        json.dump(new_payload, f, indent=4)

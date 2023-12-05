import re
source_file = "air_quality_sensor_example.ttl"
with open(source_file, "r") as file:
    lines = file.readlines()
# print(lines)
elements = []
for line in lines:
    # print("__________")
    # print(line)
    # print(line[0:4])
    if line[0:4] == "bldg":
        # print("last piece")
        last_piece = line.split(" ")[2].replace("brick:", "")
        elements.append(last_piece)
        # print(last_piece)

print(elements)

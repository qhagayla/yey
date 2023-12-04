import json

with open('sample.json', 'r') as json_file:
    json_data = json.load(json_file)
    for certification in json_data["certifications"]:
        print(certification["courses"])


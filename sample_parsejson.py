import json
import yaml

x = '{"name": "John", "age": "30", "city": "New York City"}'

#parse json

y = json.loads(x)
print("The output of json file is ", y)
print("Age:", y["age"])
print("Name:", y["name"]) 
print("City:", y["city"])

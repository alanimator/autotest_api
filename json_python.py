import json

with open("json_example.json", "r", encoding="utf-8") as file:
    data_json = json.load(file)
    print(data_json)

with open("json_user.json", "w", encoding="utf-8") as file:
  data = {"name": "Vasy", "age": "14"}
  json.dump(data, file, indent=2)
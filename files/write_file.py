import json

list_of_names = {
    1: 'Jin',
    2: 'Sam',
    3: 'Leah'
}

with open("./my_data.json", "w") as file:
    json_data = json.dumps(list_of_names)
    file.write(json_data)
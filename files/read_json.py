import json

def read_my_data():
    with open("./my_data.json", "r") as file:
        my_data = json.load(file)

        print(type(my_data))

        for key, value in my_data.items():
            print(key, value)

with open('./sample_data/json-example.json') as file:
    gov_data = json.load(file)
    for obj in gov_data['items']:
        name = obj.get('name')
        if name:
            print(name)
import json

# write
# json.dump()

new_data = {"Amazon": {
    "email": "some email",
    "password": "some password"
}}

# write
# with open("data.json", mode="w") as file:
#     json.dump(new_data, file, indent=4)

# read
with open("data.json", mode="r") as file:
    data = json.load(file)
    print(data)
#
# update
data_to_add = {"Lentop": {
    "email": "orshkuri2000@gmail.com",
    "password": "or123"
}}
try:
    with open("data.json", mode="r") as file:
        data = json.load(file)
except FileNotFoundError:
    with open("json.data", mode="w") as file:
        json.dump(data_to_add, file, indent=4)
else:
    with open("data.json", "w") as file:
        data.update(data_to_add)
        json.dump(data, file, indent=4)

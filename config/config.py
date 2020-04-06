import json


def __get_attributes_from_json(attribute):
    with open("config.json", "r") as f:
        data = json.load(f)
    return data[attribute]


api_key = __get_attributes_from_json("api_key")

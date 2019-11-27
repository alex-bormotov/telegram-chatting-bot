import json


def get_config():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)
        return config

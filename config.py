import json


def get_telegram_config():
    with open("config_telegram.json", "r") as read_file:
        config = json.load(read_file)
        return config


def get_email_config():
    with open("config_email.json", "r") as read_file:
        config = json.load(read_file)
        return config

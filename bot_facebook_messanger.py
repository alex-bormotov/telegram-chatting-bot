import json
import requests
from flask import Flask, request

from config import get_fb_config

app = Flask(__name__)

FB_API_URL = get_fb_config()["fb_api_url"]
VERIFY_TOKEN = get_fb_config()["fb_verify_token"]
PAGE_ACCESS_TOKEN = get_fb_config()["page_access_token"]


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


################################################################################


def is_user_message(message):

    return (
        message.get("message")
        and message["message"].get("text")
        and not message["message"].get("is_echo")
    )


def respond(sender, message):

    response = get_bot_response(message)
    send_message(sender, response)


################################################################################


def get_bot_response(message):

    return message


def send_message(recipient_id, text):

    payload = {
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://alexbormotov.com",
                            "title": "My web site",
                        },
                        {
                            "type": "phone_number",
                            "title": "My phone",
                            "payload": "+13231234567",
                        },
                        {"type": "account_link", "url": "https://fb.com"},
                    ],
                },
            }
        },
        "recipient": {"id": recipient_id},
        "notification_type": "regular",
    }

    auth = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(FB_API_URL, params=auth, json=payload)

    return response.json()


################################################################################


@app.route("/webhook", methods=["GET", "POST"])
def listen():

    if request.method == "GET":
        return verify_webhook(request)

    if request.method == "POST":
        payload = request.json
        event = payload["entry"][0]["messaging"]
        for x in event:
            if is_user_message(x):
                text = x["message"]["text"]
                sender_id = x["sender"]["id"]
                respond(sender_id, text)

        return "ok"
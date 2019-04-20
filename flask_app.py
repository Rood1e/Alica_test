# -*- coding: utf-8 -*-
from flask import Flask, request
import json, logging
from alica_sdk import *
from main_function import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
session_storage = {}
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=["POST"])
def main():
    alice_request = AliceRequest(request.json)
    alice_response = AliceResponce(alice_request)
    logging.info("Request {}".format(alice_request))

    alice_response, session_storage[alice_response.user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(alice_request.user_id)
    )

    logging.info("Responce {}".format(alice_response))

    return alice_response.dumps()


if __name__ == '__main__':
    app.run()

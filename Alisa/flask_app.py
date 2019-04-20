from flask import Flask, request
import logging
from alice_sdk import *
from main_function import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=["POST"])
def main():
    alice_request = AliceRequest(request.json)
    alice_response = AliceResponse(alice_request)
    logging.info("Request {}".format(alice_request))
    session_storage = {}
    alice_response, session_storage[alice_request.user_id] = handle_diolog(
        alice_request, alice_response, session_storage.get(alice_request.user_id)
    )
    logging.info(f"Response {alice_response}")
    return alice_response.dumps()


if __name__ == '__main__':
    app.run()

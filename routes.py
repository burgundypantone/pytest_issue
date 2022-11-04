import json

from dependency_injector.wiring import Provide, inject
from flask import jsonify, make_response
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import HTTPException

from src.service.MyService import MyService
from .containers import Container

auth = HTTPTokenAuth(scheme="Bearer")


def configure(app):
    app.add_url_rule("/", "check", check)
    app.add_url_rule("/health", "health", health)
    app.add_url_rule("/cool", "cool", cool)

    exceptions_to_handle = [
        HTTPException,  # all other errors
    ]
    for i in exceptions_to_handle:
        app.register_error_handler(i, handle_errors)


def handle_errors(error):
    response = make_response(
        json.dumps(error), 500
    )
    response.content_type = "application/json"

    return response


def check():
    return "You hit /"


def health():
    return "Health Check OK"


@inject
def cool(my_service: MyService = Provide[Container.my_service]):
    return jsonify(my_service.do_something())

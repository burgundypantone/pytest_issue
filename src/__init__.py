import logging

from flask import Flask
from flask_log_request_id import RequestID, RequestIDLogFilter

from . import routes
from .containers import Container


def create_app():
    print("@@@@@@ in create_app() @@@@@@@")
    container = Container()
    container.init_resources()

    app = Flask(__name__)
    app.container = container

    # connect url rules and register error handlers
    routes.configure(app)

    # set flask configuration and logging
    app.config.from_mapping(app.container.config.get("app"))
    setup_logging(app)

    return app


def setup_logging(app):
    """
    Set up logging so as to include RequestId and relevant logging info
    """
    RequestID(app)
    handler = logging.FileHandler(app.container.config.get("app.LOG_FILE"))

    handler.setFormatter(
        logging.Formatter("%(module) %(asctime)s : %(levelname)s : %(request_id)s - %(message)s")
    )

    handler.addFilter(RequestIDLogFilter())  # << Add request id contextual filter
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(level="DEBUG")

import json
import os
from unittest import mock

import pytest
import requests
from flask import url_for

from test.util.mock_db import MockDB

"""
These tests spin up a testing instance of the app and test the APIs end to end
"""


@pytest.fixture(scope='module', autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(
            os.environ,
            {
                "ENV": "TEST",
                "DB_USERNAME": os.environ.get("DB_USERNAME", "root"),
                "DB_PASSWORD": os.environ.get("DB_PASSWORD", "admin"),
                "DB_HOST": os.environ.get("DB_HOST", "localhost"),
                "DB_PORT": os.environ.get("DB_PORT", "3306"),
            },
    ):
        yield


@pytest.fixture(scope='module', autouse=True)
def app():
    # test if pytest fixture for env vars works as expected
    assert os.environ["ENV"] == "TEST", f"ENV is set to {os.environ['ENV']}"
    print(f"********* HIIIII ********* {os.environ['ENV']}")
    from src import create_app

    mock_db = MockDB(
        os.environ["DB_USERNAME"],
        os.environ["DB_PASSWORD"],
        os.environ["DB_HOST"],
        os.environ["DB_PORT"],
    )
    mock_db.setup()
    app = create_app()
    yield app
    mock_db.teardown()
    app.container.unwire()


def test_check(client, app):
    response = client.get(url_for("check"))
    assert response.status_code == 200
    assert response.data == b"You hit /"


def test_health(client, app):
    response = client.get(url_for("health"))
    assert response.data == b"Health Check OK"
    assert response.status_code == 200


def test_cool(client, app):
    response = client.get(url_for("cool"))
    assert response.status_code == 200
    assert response.data == b'{"ok":true}\n'

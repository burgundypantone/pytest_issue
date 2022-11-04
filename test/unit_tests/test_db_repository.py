import os

import pytest

from src.repository.db_repository import DBRepository
from test.util.mock_db import MockDB

DB_USERNAME = os.environ.get("DB_USERNAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "123")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", 30003)


@pytest.fixture(autouse=True, scope="module")
def db():
    _db = MockDB(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT)
    _db.setup()
    yield DBRepository(
        dict(
            connection=dict(
                dialect="mysql",
                driver="pymysql",
                username=DB_USERNAME,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
                schema="test",
            ),
        )
    )
    # executed after tests are executed
    _db.teardown()


def test_db_repository_init(db):
    assert db.config == dict(
        connection=dict(
            dialect="mysql",
            driver="pymysql",
            username=DB_USERNAME,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            schema="test",
        ),
    ), "Config incorrectly initialized"


def test_build_connection_string():
    expected_connection_string = (
        "mysql+pymysql://test_user:supersecurepwd@mysql.host.com:9008/schema"
    )
    result = DBRepository.build_connection_str(
        dialect="mysql",
        driver="pymysql",
        username="test_user",
        password="supersecurepwd",
        host="mysql.host.com",
        port=9008,
        schema="schema",
    )
    assert (
        result == expected_connection_string
    ), f"Connection string should be {expected_connection_string}"


def test_sample_query(db):
    assert db.sample_query() == 1, "DB connection failed"

import pytest

from src.repository.db_repository import DBRepository
from src.service.MyService import MyService


# autouse set to True ensures that this function is invoked before every test
@pytest.fixture(autouse=True)
def my_service():
    db_repository = DBRepository(
        dict(
            connection=dict(
                dialect="mysql",
                driver="pymysql",
                username="username",
                password="password",
                host="host",
                port=3306,
                schema="schema",
            ),
        )
    )
    return MyService(
        dict(greet="Hello, World!"),
        db_repository,
    )


def test_mhpm_service_init(my_service):
    assert my_service.config == dict(greet='Hello, World!'), "Config incorrectly initialized"

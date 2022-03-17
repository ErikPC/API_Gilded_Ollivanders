import json
import pytest

from app import create_app
from repository.connect import conectar_BBDD


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def pytest_sessionstart(session):
    with open("test\ollivandersTest.json") as f:
        conectar_BBDD().insert_many(json.load(f))


def pytest_sessionfinish(session, exitstatus):
    conectar_BBDD().delete_many({})

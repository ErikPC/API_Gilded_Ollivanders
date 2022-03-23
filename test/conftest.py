import json
import pytest

from app import create_app
from repository.connect import conectar_BBDD


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture(scope="module")
def client(app):
    with app.app_context():
        with open("test\\repository\\ollivandersTest.json") as f:
            conectar_BBDD().insert_many(json.load(f))

        yield app.test_client()

        conectar_BBDD().delete_many({})


# Esto definia una base de datos que se crea para todos los casos test
# se ha cambiado por el fixture module=session para que la base de datos
#  este controlada por cada file

# def pytest_sessionstart(session):
#     with open("test\\repository\\ollivandersTest.json") as f:
#         conectar_BBDD().insert_many(json.load(f))


# def pytest_sessionfinish(session, exitstatus):
#     conectar_BBDD().delete_many({})

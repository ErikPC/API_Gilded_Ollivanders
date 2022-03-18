import pytest
from factory import create_app

create_app()


@pytest.fixture
def client():
    return create_app().test_client()


def test_aged_brie(client):
    resp = client.get("/item/Aged-brie")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [{"name": "Aged-brie", "quality": 8, "sell_in": 5}]


def test_backstage(client):
    resp = client.get("/item/Backstage")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [{"name": "Backstage", "quality": 8, "sell_in": 5}]


def test_normal_item(client):
    resp = client.get("/item/Normal-item")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [{"name": "Normal-item", "quality": 8, "sell_in": 5}]


def test_conjured(client):
    resp = client.get("/item/Conjured")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [{"name": "Conjured", "quality": 8, "sell_in": 5}]


def test_sulfuras(client):
    resp = client.get("/item/Sulfuras")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [{"name": "Sulfuras", "quality": 80, "sell_in": 0}]

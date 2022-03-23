import pytest


@pytest.mark.test_update_aged_brie
def test_update_aged_brie(client):
    resp = client.get("/item/update/Aged-brie")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Aged-brie", "quality": 9, "sell_in": 4},
    ]


@pytest.mark.test_update_normal_item
def test_update_normal_item(client):
    resp = client.get("/item/update/Normal-item")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Normal-item", "quality": 7, "sell_in": 4},
    ]


@pytest.mark.test_update_conjured
def test_update_conjured(client):
    resp = client.get("/item/update/Conjured")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Conjured", "quality": 6, "sell_in": 4},
    ]


@pytest.mark.test_update_backstage
def test_update_backstage(client):
    resp = client.get("/item/update/Backstage")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Backstage", "quality": 11, "sell_in": 4},
    ]


@pytest.mark.test_update_sulfuras
def test_update_sulfuras(client):
    resp = client.get("/item/update/Sulfuras")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Sulfuras", "quality": 80, "sell_in": 0},
    ]

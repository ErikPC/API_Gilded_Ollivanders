import pytest


@pytest.mark.test_añadir_aged_brie
def test_añadir_aged_brie(client):
    resp = client.post("/item/Aged-brie/10/7")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Creado": True,
        "Item": {"name": "Aged-brie", "quality": "10", "sell_in": "7"},
    }


@pytest.mark.test_añadir_normal_item
def test_añadir_normal_item(client):
    resp = client.post("/item/Normal-item/5/2")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Creado": True,
        "Item": {"name": "Normal-item", "quality": "5", "sell_in": "2"},
    }


@pytest.mark.test_añadir_conjured
def test_añadir_conjured(client):
    resp = client.post("/item/Conjured/15/1")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Creado": True,
        "Item": {"name": "Conjured", "quality": "15", "sell_in": "1"},
    }


@pytest.mark.test_añadir_backstage
def test_añadir_backstage(client):
    resp = client.post("/item/Backstage/9/5")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Creado": True,
        "Item": {"name": "Backstage", "quality": "9", "sell_in": "5"},
    }


@pytest.mark.test_añadir_sulfuras
def test_añadir_sulfuras(client):
    resp = client.post("/item/Sulfuras/80/0")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Creado": True,
        "Item": {"name": "Sulfuras", "quality": "80", "sell_in": "0"},
    }

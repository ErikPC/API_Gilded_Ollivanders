import pytest


@pytest.mark.test_delete_aged_brie
def test_delete_aged_brie(client):
    resp = client.delete("/item/Aged-brie/8/5")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Eliminado": True,
        "Item": {"name": "Aged-brie", "quality": "8", "sell_in": "5"},
    }


@pytest.mark.test_delete_backstage
def test_delete_backstage(client):
    resp = client.delete("/item/Backstage/8/5")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Eliminado": True,
        "Item": {"name": "Backstage", "quality": "8", "sell_in": "5"},
    }


@pytest.mark.test_delete_normal_item
def test_delete_normal_item(client):
    resp = client.delete("/item/Normal-item/8/5")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Eliminado": True,
        "Item": {"name": "Normal-item", "quality": "8", "sell_in": "5"},
    }


@pytest.mark.test_delete_conjured
def test_delete_conjured(client):
    resp = client.delete("/item/Conjured/8/5")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Eliminado": True,
        "Item": {"name": "Conjured", "quality": "8", "sell_in": "5"},
    }


@pytest.mark.test_delete_sulfuras
def test_delete_sulfuras(client):
    resp = client.delete("/item/Sulfuras/80/0")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == {
        "Eliminado": True,
        "Item": {"name": "Sulfuras", "quality": "80", "sell_in": "0"},
    }

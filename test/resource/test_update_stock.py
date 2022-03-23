def test_update_stock(client):
    resp = client.get("/stock/update-stock")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.json == [
        {"name": "Aged-brie", "quality": 9, "sell_in": 4},
        {"name": "Normal-item", "quality": 7, "sell_in": 4},
        {"name": "Conjured", "quality": 6, "sell_in": 4},
        {"name": "Backstage", "quality": 11, "sell_in": 4},
        {"name": "Sulfuras", "quality": 80, "sell_in": 0},
    ]

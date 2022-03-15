from src.Aged_brie import AgedBrie
import pytest



@pytest.mark.update_quality_brie
def test_update_quality_brie():
    cheese = AgedBrie("Aged Brie", 2, 0)
    cheese.updateQuality()
    assert 1 == cheese.getSell_in()
    assert 1 == cheese.getQuality()

@pytest.mark.update_quality_expired
def test_update_quality_expired():
    cheese = AgedBrie("Aged Brie", 0, 0)
    cheese.updateQuality()
    assert -1 == cheese.getSell_in()
    assert 2 == cheese.getQuality()

@pytest.mark.max_quality
def test_max_quality():
    cheese = AgedBrie("Aged Brie", -1, 50)
    cheese.updateQuality()
    assert -2 == cheese.getSell_in()
    assert 50 == cheese.getQuality()

    cheese = AgedBrie("Aged Brie", -1, 49)
    cheese.updateQuality()
    assert -2 == cheese.getSell_in()
    assert 50 == cheese.getQuality()
from domain.NormalItem import NormalItem
import pytest


@pytest.mark.update_quality_normal_item
def test_update_quality_normal_item():
    normal = NormalItem("+5 Dexterity Vest", 20, 10)
    normal.updateQuality()
    assert 9 == normal.getSell_in()
    assert 19 == normal.getQuality()


@pytest.mark.update_quality_normal_item_expired
def test_update_quality_normal_item_expired():
    normal = NormalItem("+5 Dexterity Vest", 20, 0)
    normal.updateQuality()
    assert -1 == normal.getSell_in()
    assert 18 == normal.getQuality()


@pytest.mark.quality_min_ZERO
def test_quality_min_ZERO():
    normal = NormalItem("+5 Dexterity Vest", 0, 10)
    normal.updateQuality()
    assert 9 == normal.getSell_in()
    assert 0 == normal.getQuality()

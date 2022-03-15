from src.Conjured import Conjured
import pytest

@pytest.mark.update_quality_conjured
def test_update_quality_conjured():
    conjured = Conjured("Conjured Mana Cake", 3, 6)
    conjured.updateQuality()
    assert 2 == conjured.getSell_in()
    assert 4 == conjured.getQuality()

@pytest.mark.update_quality_conjured_just_expired
def test_update_quality_conjured_just_expired():
    conjured = Conjured("Conjured Mana Cake", 0, 6)
    conjured.updateQuality()
    assert -1 == conjured.getSell_in()
    assert 2 == conjured.getQuality()

@pytest.mark.update_quality_conjured_expired
def test_update_quality_conjured_expiredU():
    conjured = Conjured("Conjured Mana Cake", -1, 6)
    conjured.updateQuality()
    assert -2 == conjured.getSell_in()
    assert 2 == conjured.getQuality()

@pytest.mark.quality_min_ZERO
def test_quality_min_ZERO():    
    brie = Conjured("Conjured Mana Cake", 1, 1)
    brie.updateQuality()
    assert 0 == brie.getSell_in()
    assert 0 == brie.getQuality()

    brie = Conjured("Conjured Mana Cake", -1, 0)
    brie.updateQuality()
    assert -2 == brie.getSell_in()
    assert 0 == brie.getQuality()
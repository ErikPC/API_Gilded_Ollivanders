import pytest
from src.Sulfuras import Sulfuras

@pytest.mark.update_quality_sulfuras
def test_update_quality_():
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    sulfuras.updateQuality()
    assert 0 == sulfuras.getSell_in()
    assert 80 == sulfuras.getQuality()
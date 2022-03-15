from src.Backstage import Backstage
import pytest

@pytest.mark.update_quality_over_TEN
def test_update_quality_over_TEN():
    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)
    ticket.updateQuality()
    assert 14 == ticket.getSell_in()
    assert 21 == ticket.getQuality()

@pytest.mark.update_quality_over_FIVE
def test_update_quality_over_Five():
    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 6, 20)
    ticket.updateQuality()
    assert 5 == ticket.getSell_in()
    assert 22 == ticket.getQuality()

@pytest.mark.update_quality_over_ZERO
def test_update_quality_over_ZERO():
    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 20)
    ticket.updateQuality()
    assert 4 == ticket.getSell_in()
    assert 23 == ticket.getQuality()

@pytest.mark.update_quality_pass_expired
def test_quality_pass_expired():
    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 0, 20)
    ticket.updateQuality()
    assert -1 == ticket.getSell_in()
    assert 0 == ticket.getQuality()

@pytest.mark.max_quality
def test_max_quality():
    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49)
    ticket.updateQuality()
    assert 4 == ticket.getSell_in()
    assert 50 == ticket.getQuality()

    ticket = Backstage("Backstage passes to a TAFKAL80ETC concert", 9, 49)
    ticket.updateQuality()
    assert 8 == ticket.getSell_in()
    assert 50 == ticket.getQuality()

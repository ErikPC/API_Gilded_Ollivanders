from domain.Aged_brie import AgedBrie
from domain.Conjured import Conjured


def create_item(name, quality=0, sell_in=0):
    if name == "Aged_brie":
        return AgedBrie(name, quality, sell_in)
    elif name == "Conjured":

        return Conjured(name, quality, sell_in)

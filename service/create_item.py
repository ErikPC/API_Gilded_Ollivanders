from domain.Aged_brie import AgedBrie
from domain.Conjured import Conjured
from domain.Backstage import Backstage
from domain.NormalItem import NormalItem
from domain.Sulfuras import Sulfuras


def create_item(item):
    name = item["name"]
    quality = item["quality"]
    sell_in = item["sell_in"]
    if name == "Aged-brie":
        return AgedBrie(name, quality, sell_in)
    elif name == "Conjured":
        return Conjured(name, quality, sell_in)
    elif name == "Backstage":
        return Backstage(name, quality, sell_in)
    elif name == "Normal-item":
        return NormalItem(name, quality, sell_in)
    else:
        return Sulfuras(name, quality, sell_in)

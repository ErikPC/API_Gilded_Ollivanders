from domain.Item import Item
from domain.updateable import updateable


class Sulfuras(Item, updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def getSell_in(self):
        return self.sell_in

    def getQuality(self):
        return self.quality

    def updateQuality(self):
        pass

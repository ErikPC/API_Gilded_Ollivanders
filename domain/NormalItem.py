from domain.Item import Item
from domain.updateable import updateable


class NormalItem(Item, updateable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def getSell_in(self):
        return self.sell_in

    def getQuality(self):
        return self.quality

    def updateQuality(self):
        if self.sell_in <= 0:
            self.quality -= 2
            self.sell_in -= 1
        else:
            self.quality -= 1
            self.sell_in -= 1
        if self.quality <= 0:
            self.quality = 0

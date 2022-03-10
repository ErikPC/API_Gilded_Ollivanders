from domain.Item import Item
from domain.updateable import updateable


class Conjured(Item, updateable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def getSell_in(self):
        return self.sell_in

    def getQuality(self):
        return self.quality

    def updateQuality(self):
        if self.sell_in <= 0:
            self.quality -= 4
        else:
            self.quality -= 2
        self.checkQuality()
        self.sell_in -= 1

    def checkQuality(self):
        if self.quality <= 0:
            self.quality = 0
        elif self.quality >= 50:
            self.quality = 50


class GildedRose:
    def __init__(self, stock):
        self.stock = stock

    def update_quality(self):
        for item in self.stock:
            item.updateQuality()
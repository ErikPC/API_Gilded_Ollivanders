from unittest import case
from flask_restful import Resource
from domain.Aged_brie import AgedBrie
from service.service import Service


class Update_stock(Resource):
    def get():
        stock = Service.get_stock()
        for item in stock:
            if item["name"] == "Aged_brie":
                AgedBrie.updateQuality()

        return Service.get_stock()

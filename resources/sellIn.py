from flask_restful import Resource
from service.service import Service


class SellIn(Resource):
    def get(self, sell_in):
        return Service.get_sell_in(sell_in)

from flask_restful import Resource
from repository.db import DB


class SellIn(Resource):
    def get(self , sell_in):
        return DB.get_sell_in(sell_in)
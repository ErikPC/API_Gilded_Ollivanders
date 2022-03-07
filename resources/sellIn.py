from flask_restful import Resource
from repository.repository import DB_atlas


class SellIn(Resource):
    def get(self, sell_in):
        return DB_atlas.get_sell_in(sell_in)

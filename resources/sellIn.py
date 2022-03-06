from flask_restful import Resource
from repository.db_atlas import DB_atlas


class SellIn(Resource):
    def get(self, sell_in):
        return DB_atlas.get_sell_in(sell_in)

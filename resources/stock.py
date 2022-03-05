from flask_restful import Resource
from repository.db_atlas import DB_atlas


class Stock(Resource):
    def get(self):
        return DB_atlas.get_stock()

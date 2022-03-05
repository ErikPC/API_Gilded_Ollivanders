from flask_restful import Resource
from repository.db_atlas import DB_atlas


class Item(Resource):
    def get(self, name):
        return DB_atlas.get_item(name)

from flask_restful import Resource
from repository.db import DB


class Item(Resource):
    def get(self, name):
        return DB.get_item(name)

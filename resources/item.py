from flask_restful import Resource
from service.service import Service


class Item(Resource):
    def get(self, name):
        return Service.get_item(name)

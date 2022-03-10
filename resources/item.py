from flask_restful import Resource
from service.service import Service


class Item(Resource):
    def get(self, name):
        return Service.get_item(name)

    def get(self, name, quality, sell_in):
        return Service.get_item(name, quality, sell_in)

    def delete(self, name, quality, sell_in):
        return Service.delete_item(name, quality, sell_in)

    def post(self, name, quality, sell_in):
        return Service.create_item(name, quality, sell_in)

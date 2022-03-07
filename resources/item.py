from flask_restful import Resource
from service.service import Service


class Item(Resource):
    def get(self, name):
        return Service.get_item(name)

    def delete(self, name, sell_in, quality):
        return Service.delete_item(name, sell_in, quality)

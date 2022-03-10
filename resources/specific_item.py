from flask_restful import Resource
from service.service import Service


class Specific_item(Resource):
    def get(self, name, quality, sell_in):
        return Service.get_specific_item(name, quality, sell_in)

    def delete(self, name, quality, sell_in):
        return Service.delete_item(name, quality, sell_in)

    def post(self, name, quality, sell_in):
        return Service.create_item(name, quality, sell_in)

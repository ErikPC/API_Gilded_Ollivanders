from flask_restful import Resource
from service.service import Service


class Stock(Resource):
    def get(self):
        return Service.get_stock()

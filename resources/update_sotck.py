from flask_restful import Resource
from service.service import Service


class Update_stock(Resource):
    def get():
        return Service.get_stock()

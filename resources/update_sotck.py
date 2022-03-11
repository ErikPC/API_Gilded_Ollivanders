from flask_restful import Resource
from service.service import Service


class Update_stock(Resource):
    def get(self):
        Service.update_stock()
        return Service.get_stock()

from flask_restful import Resource
from service.service import Service


class Update_item(Resource):
    def get(self, name):
        Service.update_item(name)
        return Service.get_item(name)

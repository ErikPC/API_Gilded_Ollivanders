from flask_restful import Resource
from service.service import Service


class Quality(Resource):
    def get(self, quality):
        return Service.get_quality(quality)

from flask_restful import Resource
from repository.db import DB

class Quality(Resource):
    def get(self, quality):
        return DB.get_quality(quality)
from flask_restful import Resource
from repository.repository import DB_atlas


class Quality(Resource):
    def get(self, quality):
        return DB_atlas.get_quality(quality)

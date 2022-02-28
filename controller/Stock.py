from flask_restful import Resource
from repository.db import DB   

class Stock(Resource):
    def get(self):
        return DB.get_stock()
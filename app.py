from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from resources.quality import Quality

from resources.sellIn import SellIn
from resources.wellcome import Wellcome
from resources.item import Item
from resources.stock import Stock


def create_app():
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)
    api.add_resource(Wellcome, "/")
    api.add_resource(Item, "/item/<name>")
    api.add_resource(SellIn,"/item/sell-in/<sell_in>")
    api.add_resource(Quality,"/item/quality/<quality>")
    api.add_resource(Stock, "/stock")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

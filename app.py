from flask import Flask
from flask_restful import Api
from resources.quality import Quality

from resources.sellIn import SellIn
from resources.specific_item import Specific_item
from resources.update_item import Update_item
from resources.update_sotck import Update_stock
from resources.wellcome import Wellcome
from resources.item import Item
from resources.stock import Stock


def create_app():
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)
    api.add_resource(Wellcome, "/")
    api.add_resource(Item, "/item/<name>")
    api.add_resource(Specific_item, "/item/<name>/<quality>/<sell_in>")
    api.add_resource(SellIn, "/item/sell-in/<sell_in>")
    api.add_resource(Quality, "/item/quality/<quality>")
    api.add_resource(Stock, "/stock")
    api.add_resource(Update_stock, "/stock/update-stock")
    api.add_resource(Update_item, "/item/update/<name>")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

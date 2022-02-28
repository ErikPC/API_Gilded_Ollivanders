from repository.stock import stock


class DB:
    @staticmethod
    def get_stock():
        return stock

    @staticmethod
    def get_item(name):
        return [item for item in stock if item["name"] == name]

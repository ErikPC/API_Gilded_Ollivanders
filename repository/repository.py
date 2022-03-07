from repository.connect import conectar_BBDD


class DB_atlas:
    @staticmethod
    def get_stock():
        return list(conectar_BBDD().find({}, {"_id": False}))

    @staticmethod
    def get_item(name):
        return list(conectar_BBDD().find({"name": name}, {"_id": False}))

    @staticmethod
    def get_quality(quality):
        return list(conectar_BBDD().find({"quality": int(quality)}, {"_id": False}))

    @staticmethod
    def get_sell_in(sell_in):
        return list(conectar_BBDD().find({"sell_in": int(sell_in)}, {"_id": False}))

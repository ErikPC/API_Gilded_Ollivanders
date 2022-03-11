from repository.connect import conectar_BBDD


class DB_atlas:
    @staticmethod
    def get_stock():
        return list(conectar_BBDD().find({}, {"_id": False}))

    @staticmethod
    def get_item(name):
        return list(conectar_BBDD().find({"name": name}, {"_id": False}))

    @staticmethod
    def get_specific_item(name, quality, sell_in):
        return list(
            conectar_BBDD().find(
                {"name": name, "quality": int(quality), "sell_in": int(sell_in)},
                {"_id": False},
            )
        )

    @staticmethod
    def get_quality(quality):
        return list(conectar_BBDD().find({"quality": int(quality)}, {"_id": False}))

    @staticmethod
    def get_sell_in(sell_in):
        return list(conectar_BBDD().find({"sell_in": int(sell_in)}, {"_id": False}))

    @staticmethod
    def delete_item(name, quality, sell_in):
        return conectar_BBDD().delete_one(
            {"name": name, "quality": int(quality), "sell_in": int(sell_in)}
        )

    @staticmethod
    def create_item(name, quality, sell_in):
        return conectar_BBDD().insert_one(
            {"name": name, "quality": int(quality), "sell_in": int(sell_in)}
        )

    @staticmethod
    def update_item(name, quality, sell_in):
        return conectar_BBDD().update_one(
            {"name": name, "quality": int(quality), "sell_in": int(sell_in)}
        )

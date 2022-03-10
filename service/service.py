from repository.repository import DB_atlas


class Service:
    @staticmethod
    def get_stock():
        return DB_atlas.get_stock()

    @staticmethod
    def get_sell_in(sell_in):
        return DB_atlas.get_sell_in(sell_in)

    @staticmethod
    def get_quality(quality):
        return DB_atlas.get_quality(quality)

    @staticmethod
    def get_item(item):
        return DB_atlas.get_item(item)

    @staticmethod
    def get_specific_item(name, quality, sell_in):
        return DB_atlas.get_specific_item(name, quality, sell_in)

    @staticmethod
    def delete_item(name, quality, sell_in):
        eliminado = DB_atlas.delete_item(name, quality, sell_in)
        return {
            "Item": {
                "name": name,
                "quality": quality,
                "sell_in": sell_in,
            },
            "Eliminado": True
            if eliminado.deleted_count == 1
            else "No se ha encontrado item",
        }

    @staticmethod
    def create_item(name, quality, sell_in):
        comprobacion = DB_atlas.create_item(name, quality, sell_in)
        return {
            "Item": {"name": name, "quality": quality, "sell_in": sell_in},
            "Creado": True if comprobacion.inserted_id else "No se ha creado el item",
        }

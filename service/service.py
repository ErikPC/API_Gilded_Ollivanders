from repository.repository import DB_atlas


class Service:
    @staticmethod
    def get_stock():
        return DB_atlas.get_stock()

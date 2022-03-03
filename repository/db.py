from turtle import st
from repository.stock import stock


class DB:
    @staticmethod
    def get_stock():
        return stock

    @staticmethod
    def get_item(name):
        return [item for item in stock if item["name"] == name]
    
    @staticmethod
    def get_sell_in(sell_in):
        return [item for item in stock if item["sell_in"] == int(sell_in)]
        
    @staticmethod
    def get_quality(quality):
        return [item for item in stock if item["quality"] == int(quality)]

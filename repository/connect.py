from repository.configuration import DB_URI
from mongoengine import connect
import certifi


def conectar_BBDD():
    ca = certifi.where()
    conexion = connect(host=DB_URI, tlsCAFile=ca)
    return conexion["ollivanders"]["ollivanders"]

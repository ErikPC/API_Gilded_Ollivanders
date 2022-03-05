from mongoengine import connect
import certifi

DB_URI = "mongodb+srv://Falopio:Ollivanders123@ollivanders.ovnru.mongodb.net/ollivanders?retryWrites=true&w=majority"
COLLECTION = "ollivanders"


def conectar_BBDD():
    ca = certifi.where()
    conexion = connect(host=DB_URI, tlsCAFile=ca)
    return conexion["ollivanders"]["ollivanders"]

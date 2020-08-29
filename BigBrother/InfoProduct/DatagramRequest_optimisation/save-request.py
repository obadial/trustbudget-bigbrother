import unittest
import pymongo
from pymongo import MongoClient

from pprint import pprint

# 1 STATUT SERVEUR

db_trustbudget = MongoClient("url_mongo_db")
db_saverequest = db_trustbudget['save-product-data']

db_champ1 = db_saverequest["product_id"]
db_champ2 = db_saverequest["date_request"]
db_champ3 = db_saverequest["product_data"]

serverStatusResult=db_saverequest.command("serverStatus")
pprint(serverStatusResult)

# 2 VERIFICATION DE LA BDD EXISTANTE

dblist = db_trustbudget.list_database_names()
if "SAVE_REQUEST_DATAGRAM" in dblist:
    print("La base de donnees existe")
else:
    print("La base de donnees n'existe pas")

# 3 VERIFICATION DES CHAMPS EXISTANTS

champlist = db_trustbudget.list_collection_names()
if "ID" in champlist:
    print("Le champ ID existe")
if "DATE_REQUEST" in champlist:
    print("Le champ DATE_REQUEST existe")
if "DATA_DATAGRAM" in champlist:
    print("Le champ DATA_DATAGRAM existe")

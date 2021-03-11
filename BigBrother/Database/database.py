import pymongo

class Mydata:

    def __init__(self):
        return


    def connection_dataBase(self): 
        client = pymongo.MongoClient()
        db = client['TrustBudget']
        my_client = db['user-profiles']
        return my_client

    def connection_dataBase_item(self):
        client = pymongo.MongoClient()
        db = client['TrustBudget']
        my_client = db['save-product-data']
        return my_client






    


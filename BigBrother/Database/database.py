import pymongo

class Mydata:

    def __init__(self):
        return


    def connection_dataBase(self): 
        client = pymongo.MongoClient('193.70.89.169', 27017, username="lucasO", password="k[NWun695msH")
        db = client['TrustBudget']
        my_client = db['user-profiles']
        return my_client

    def connection_dataBase_item(self):
        client = pymongo.MongoClient('193.70.89.169', 27017, username="tozziH", password="s3Ep7A5e")
        db = client['TrustBudget']
        my_client = db['save-product-data']
        return my_client






    


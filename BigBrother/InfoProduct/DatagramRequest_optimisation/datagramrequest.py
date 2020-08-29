from pymongo import MongoClient
# from BigBrother.Datagram.datagram import *
from BigBrother.BigBrother import BigBrother
from pprint import pprint
from BigBrother.localeData.Date.date import Date
from BigBrother.Database.database import Mydata
from BigBrother.Process.BuyGestion.buygestion import PlayData
import json
from bson.json_util import dumps
from datetime import datetime

class DatagramRequest:

    def __init__(self):
        # Call bigbrother
        self.mybigbrother = BigBrother()
        self.date = Date()
        self.today = self.date.getDate()
        self.db = Mydata()
        self.database = self.db.connection_dataBase_item()

    # Fonction permettant de vérifier si le code barre existe dans la BDD avant d'appeler Bigbrother()
    def findInBase(self, barrecode):
        data = self.database.find({"ID": int(barrecode)})
        if data.count() == 1:
            #On formate correctement les données en JSON
            data = dumps(data)
            data = json.loads(data)
            return json.dumps(data[0]["DATA_DATAGRAM"], indent=4, sort_keys=True, ensure_ascii=False)
        return None

    # Fonction appelant Bigbrother et recupere les informations relative au codebarre
    def saveRequestDatagram(self, barrecode):
        data_datagram = self.mybigbrother.ask_info_for_app(barrecode)
        data = self.UpdateDatabase(barrecode, self.today, data_datagram)
        return data

    # Mise à jour de la base de données en ajoutant un nouveau document
    def UpdateDatabase(self, barrecode, date, data_datagram):
        new_insertion = {"ID": barrecode, "DATE_REQUEST": date, "DATA_DATAGRAM": data_datagram}
        data = json.dumps(data_datagram, indent=4, sort_keys=True, ensure_ascii=False)
        elem = self.database.find({"ID": int(barrecode)})
        if elem.count() == 0:
            self.database.insert(new_insertion)
        else:
            myquery = {"ID" : barrecode}
            newvalues = {"$set": {"DATE_REQUEST": date, "DATA_DATAGRAM": data_datagram}}
            self.database.update_one(myquery, newvalues)
        return data

    # Fonction permettant de vérifier si les infos produits existent déjà et les afficher
    def FindProductInDatabase(self, barrecode):
        data = self.database.find({"ID": int(barrecode)})
        if data.count() > 0:
            data = dumps(data)
            data = json.loads(data)
            return json.dumps(data[0], indent=4, sort_keys=False, ensure_ascii=False)
        return None

    # Fonction permettant d'afficher une donnee stocke dans la BDD en fonction du barrecode
    def printDataInDatabase(self, barrecode):
        data = self.database.find({"ID": int(barrecode)})
        for document in data:
            pprint(document)

    # Fonction permettant d'afficher la date d'un code barre
    # (Récupérer la date, la parser afin de vérifier si, par exemple < 6 mois par rapport à maintenant
    # Si oui : rien faire, sinon : appeler saveRequestDatagram() et mettre à jour la donnée ?
    def returnDate(self, barrecode):
        converted_barrecode = int(float(barrecode))
        date = self.database.find({"ID": int(converted_barrecode)})
        for document in date:
            pprint('{0} : {1}'.format(document['ID'], document['DATE_REQUEST']))
            return True
        return False

    # Fonction permettant d'afficher la liste des codes barre dont la requête a été faite avant la date
    def findBarreCode(self, codebarre):
        #print("je suis dans findBarreCode\n")
        #print(codebarre)
        date = Date()
        date_format = "%d/%m/%y"
        end_date = datetime.strptime(date.getDate(), date_format)
        cursor = self.database.find({})
        data = []
        for doc in cursor:
            item_date = datetime.strptime(doc['DATE_REQUEST'], date_format)
            if item_date <= end_date:
                #pprint('{0} : {1}'.format(doc['ID'], doc['DATE_REQUEST']))
                data.append('{0}'.format(doc['ID']))
        if len(data) == 0:
            data = None
            return data
        x = 0
        for x in data:
            if x == str(codebarre):
                retour = self.findInBase(codebarre)
                return retour
        return None
    #
    # PARTIE DATABASE
    #

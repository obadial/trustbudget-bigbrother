from BigBrother.InfoProduct.Datagram.datagram import Datagram
from BigBrother.Bank.OBP_Python.HandlerOBP import HandlerOBP
from BigBrother.Process.BuyGestion.buygestion import PlayData
from BigBrother.Database.database import Mydata
from BigBrother.localeData.Date.date import Date
from BigBrother.localeData.Distance.distance import Distance
from BigBrother.localeData.Map.Map import Map
from bson.objectid import ObjectId
import json

class   Algo():

    def _init_(self):
        return

    def verif_si_total_transaction_superieur_argent_dispo(self, info, db_of_the_user, my_list_de_course):
        total_of_account = db_of_the_user["current_budget_of_period"]
        total_of_account = float(total_of_account)
        total_on_info = int(info['amount'])
        if total_on_info == 0: 
            total_of_operation = PlayData.create_total(PlayData(), my_list_de_course)
        else:
            total_of_operation = total_on_info
        if total_of_operation > total_of_account:
            return 400
        else:
            return 200
        
    def verif_si_totale_non_alimentaire_ne_depasse_pas_le_budget_non_alimentaire(self, info, db_of_the_user, my_list_de_course):
        total_of_account = db_of_the_user["current_budget_of_period"]
        total_of_account = float(total_of_account)
        total_of_vital = db_of_the_user["current_budget_vital"]
        total_of_vital = float(total_of_vital)
        total_of_no_vital = total_of_account - total_of_vital
        total_of_no_vital_of_basket = PlayData.create_total_no_vital(PlayData(), PlayData.create_list_of_buy(PlayData(), my_list_de_course)) 
        if total_of_no_vital_of_basket > total_of_no_vital:
            return 400
        else:
            return 200
    
    def make_change_in_database(self, BigBrother, info, my_list_de_course):
        db = BigBrother.connect_data_base()
        db_of_the_user = db.find_one({"user_id" : ObjectId(info["id_obp_sender"])})
        total_on_info = int(info['amount'])
        if total_on_info == 0:
            total_of_operation = PlayData.create_total(PlayData(), my_list_de_course)
        else:
            total_of_operation = total_on_info
        nw_current_budget_of_period = str(float(db_of_the_user["current_budget_of_period"]) - total_of_operation)
        my_query = {"user_id": ObjectId(info["id_obp_sender"])}
        new_value = {"$set": {"current_budget_of_period": nw_current_budget_of_period}}
        db.update_one(my_query, new_value)
        total_vital_of_basket = PlayData.create_total_vital(PlayData(), PlayData.create_list_of_buy(PlayData(), my_list_de_course))
        # total_of_vital_of_basket = total_of_vital_of_basket - total_of_operation # a corriger 
        nw_current_budget_vital = str(float(db_of_the_user["current_budget_vital"]) - total_vital_of_basket)
        my_query2 = {"user_id": ObjectId(info["id_obp_sender"])}
        new_value2 = {"$set": {"current_budget_vital": nw_current_budget_vital}}
        db.update_one(my_query2, new_value2)

    def routine(self, BigBrother, info):
        response = {}
        response["id_client"] = info["id_obp_sender"]
        response["code_reponse"] = "200"
        response["message_erreure"] = "Operation autorisée"
        response["reponse"] = []
        tab_achat = info["item"]
        my_list_de_course = []
        for x in tab_achat:
            my_list_de_course.append(x["barre_code"])
        db = BigBrother.connect_data_base()
        db_of_the_user = db.find_one({"user_id": ObjectId(info["id_obp_sender"])})
        return_value = self.verif_si_total_transaction_superieur_argent_dispo(info, db_of_the_user, my_list_de_course)
        if return_value == 400:
            response["code_reponse"] = "401"
            response["message_erreure"] = "Operation refusée : Total dans la transaction est supérieur a l'argent disponible"
            response["reponse"] = []
            return response
        else:
            return_value = self.verif_si_totale_non_alimentaire_ne_depasse_pas_le_budget_non_alimentaire(info, db_of_the_user, my_list_de_course)
            if return_value == 400:
                response["code_reponse"] = "402"
                response["message_erreure"] = "Operation refusée : Votre achat est refusé car vous empietez sur votre budget alimentaire avec cette achet, veiller retire des article non-alimentaire de votre panier"
                response["reponse"] = []
                return response
            else:
                response["code_reponse"] = "200"
                response["message_erreure"] = "Operation autorisée"
                response["reponse"] = PlayData.create_list_of_buy(PlayData(), my_list_de_course)
                return response

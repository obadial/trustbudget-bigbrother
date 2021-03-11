import pandas as pd
import pymongo
from datetime import datetime
from bson.objectid import ObjectId


class BasketParser:
    DATASET_COLUMN = ['total_price', 'money_amount',
                      'Ration_vital/nonvital_type']
    DATA_FRAME = None

    def __init__(self, data):
        self.client_mongo = pymongo.MongoClient()
        self.client_mongo = self.client_mongo[]
        self.data = data
        self.data_dict = {
            self.DATASET_COLUMN[0]: [int(float(data["amount"]))],
            self.DATASET_COLUMN[1]: [int(0)],
            self.DATASET_COLUMN[2]: [int(0)],
        }

    def build(self, big_brother):
        if not big_brother:
            raise
        self.fetch_budget()
        if self.data_dict[self.DATASET_COLUMN[0]][0] > self.data_dict[self.DATASET_COLUMN[1]][0]:
            return False
        self.fetch_history(big_brother)
        self.DATA_FRAME = pd.DataFrame(data=self.data_dict)
        return self.data_dict[self.DATASET_COLUMN[2]][0] > 0

    def fetch_history(self, big_brother):
        user_stats_collection = self.client_mongo['big-brother-stats']
        user_historic_collection = self.client_mongo['user-purchase-historics']
        user_stats = user_stats_collection.find_one({"user_id": ObjectId(self.data["id_obp_sender"])})
        today_date = datetime.now()
        vital = 0
        non_vital = 0
        if not user_stats:
            raise
        user_historic = user_historic_collection.find({"user_id": ObjectId(self.data["id_obp_sender"]),
                                                       "_id": {'$in': user_stats['stat_month_buy']}})
        for item in user_historic:
            elyps = today_date - item['date']
            if elyps.days < 7 and item['status'] == '200':
                for article in item['items']:
                    #article_info = big_brother.ask_info_for_app(article['barre_code'])
                    if not ('categorie' in article) or article['categorie'] == 'vitale':
                        vital += 1
                    else:
                        non_vital += 1
        for item in self.data['item']:
         #   article_info = big_brother.ask_info_for_app(item['barre_code'])
            if not ('categorie' in item) or item['categorie'] == 'vitale':
                vital += 1
            else:
                non_vital += 1
        print("vital => {} / non vitale => {}".format(vital, non_vital))
        self.data_dict[self.DATASET_COLUMN[2]][0] = float(vital - non_vital)

    def fetch_budget(self):
        user_profile_collection = self.client_mongo['user-profiles']
        user_profile = user_profile_collection.find_one({"user_id": ObjectId(self.data["id_obp_sender"])})
        if not user_profile:
            raise
        self.data_dict[self.DATASET_COLUMN[1]][0] = int(float(user_profile['current_budget_vital']))

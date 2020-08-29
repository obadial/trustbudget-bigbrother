from BigBrother.InfoProduct.Datagram.datagram import Datagram
from BigBrother.InfoProduct.OpenBeautyFacts.package.openbeautyfacts import OpenBeautyFacts
from BigBrother.InfoProduct.OpenPetFoodFacts.package.openpetfoodfacts import OpenPetFoodFacts
from BigBrother.InfoProduct.OpenFactFood.package.openfactfood import OpenFactFood
from BigBrother.InfoProduct.WebScraping.catch_price import WebScrap
from BigBrother.Process.BuyGestion.thread_info import Hello
import json
import os
import re
import requests
import profile,time

class PlayData:

    def _init_(self):

        """
        Ici la li
        """
    def web_scraping(self, codebarre, opt_id):
        hello = WebScrap().Search_on_web(codebarre, opt_id)
        return hello

    def web_thread_scraping(self, codebarre):
        tab = Hello().check_by_thread_codebarre(codebarre)
        result = {}
        result["price"] = 0
        result["categorie"] = "not found"
        if tab["carrefour"] != 0:
            result["price"] = str(tab["carrefour"])
            result["categorie"] = "vitale"
        if tab["naturalia"] != 0:
            result["price"] = str(tab["naturalia"])
            result["categorie"] = "vitale"
        if tab["picard"] != 0:
            result["price"] = str(tab["picard"])
            result["categorie"] = "vitale"
        if tab["fnac"] != 0:
            result["price"] = str(tab["fnac"])
            result["categorie"] = "non vitale"
        if tab["amazon"] != 0:
            result["price"] = str(tab["amazon"])
            result["categorie"] = "non vitale"
        if tab["jouet_club"] != 0:
            result["price"] = str(tab["jouet_club"])
            result["categorie"] = "non vitale"
        if tab["castorama"] != 0:
            result["price"] = str(tab["castorama"])
            result["categorie"] = "non vitale"
        #if tab["ikea"] != 0:
            #result["price"] = str(tab["ikea"])
            #result["categorie"] = "non vitale"
            print("result du webscraping : ")
            print(tab)
        return result

    def ask_list_retail(self):
      #  line = json.dumps(Datagram.retailersList(Datagram()), sort_keys=True, indent=4)
        #os.remove("./shop.json")
        with open('./shop.json', 'r') as f:
            distros_dict = json.load(f)
        os.remove("./tmp/file_retailers_list.json")
        text_file = open("./tmp/file_retailers_list.json", "w")
        text_file.write(line)
        text_file.close()
        return line

    def ask_price_upc(self, codebarre):
        product = json.dumps(Datagram.productSearchByBarreCode(Datagram(), codebarre), sort_keys=True, indent=4)
        os.remove("./tmp/file_product_search_by_upc.json")
        text_file = open("./tmp/file_product_search_by_upc.json", "w")
        text_file.write(product)
        text_file.close()
        text_file = open("./tmp/file_product_search_by_upc.json", "r")
        a = 0
        while text_file.readline():
            a = a + 1
        text_file.close()
        os.remove("./tmp/file_price_to_calculate_price_moyen.json")
        write_file = open("./tmp/file_price_to_calculate_price_moyen.json", "w")
        text_file = open("./tmp/file_product_search_by_upc.json", "r")
        while a > 0:
            str_line = text_file.readline()
            find_r = str_line.find('price')
            if find_r != -1:
                find_null = str_line.find('null')
                if find_null == -1:
                    write_file.writelines(str_line)
            a = a - 1
        text_file.close()
        write_file.close()
        data = PlayData.calculate_price_of_article(PlayData(), write_file, codebarre)
        return data

    def calculate_price_of_article(self, write_file, codebarre):
        write_file = open("./tmp/file_price_to_calculate_price_moyen.json", "r")
        a = 0
        sum = 0
        list_float = []
        max_num = 0
        min_num = 0
        v = 0
        while write_file.readline():
            a = a + 1
        write_file.close()
        write_file = open("./tmp/file_price_to_calculate_price_moyen.json", "r")
        my_float = 0
        str_float = ''
        while a > 0:
            str_line = write_file.readline()
            for x in str_line:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.':
                    str_float = str_float + x
            if str_float != '':
                my_float = float(str_float)
                list_float.append(my_float)
                if v == 0:
                    max_num = my_float
                    min_num = my_float
                    v = 1
            if my_float > max_num:
                max_num = my_float
            if my_float < min_num:
                min_num = my_float
            str_float = ''
            a = a - 1
        write_file.close()

        for num in list_float:
            sum = sum + num
        base = len(list_float)
        if base == 0:
            base = 1
        moyenne = sum / base
        result = {}
        if moyenne == 0.0:
            result = self.web_thread_scraping(codebarre)
            return result
        result["price"] = moyenne
        result["categorie"] = "vitale"
        return result

    def format_data_for_app_mobile(self, code_barre):
        my_dic = {}
        my_dic = self.initialise_data(my_dic)
        my_dic = self.add_data_from_openFactfood(code_barre, my_dic)
        #my_dic = self.add_data_from_openPetFoodFacts(code_barre, my_dic)
        my_dic = self.add_data_from_openBeautyFacts(code_barre, my_dic)
        my_dic = self.add_data_from_web(code_barre, my_dic)
        if my_dic["prix"] == "not found":
            my_dic["prix"] = 0
        #my_json = json.dumps(my_dic, indent=4, ensure_ascii=False)
        return my_dic

    def format_data_for_app_mobile2(self, code_barre):
        my_dic = {}
        my_dic = self.initialise_data(my_dic)
        my_dic = self.add_data_from_openFactfood(code_barre, my_dic)
        #my_dic = self.add_data_from_openPetFoodFacts(code_barre, my_dic)
        my_dic = self.add_data_from_openBeautyFacts(code_barre, my_dic)
        return my_dic

    def initialise_data(self, my_dic):
        my_dic["nom"] = "not found"
        my_dic["prix"] = "not found"
        my_dic["code_barre"] = "not found"
        my_dic["status_code"] = "not found"
        my_dic["image"] = "not found"
        my_dic["categorie"] = "not found"
        my_dic["list_des_ingredients"] = "not found"
        my_dic["allergenes"] = []
        my_dic["date_expiration"] = "not found"
        my_dic["grade_nutrition_fr"] = "not found"
        my_dic["prohibited"] = "not found"
        return my_dic

    def check_and_return_allergens(self, allergenes):
        temp = []
        for i in allergenes:
            if i == "en:soybeans":
                temp.append("Soja")
            elif i == "en:eggs":
                temp.append("Oeufs")
            elif i == "en:gluten":
                temp.append("Gluten")
            elif i == "en:milk":
                temp.append("Lait")
            elif i == "en:nuts":
                temp.append("Fruits à coque")
            elif i == "en:mustard":
                temp.append("Moutarde")
            elif i == "en:sulphur-dioxide-and-sulphites":
                temp.append("Anhydride sulfureux et sulfites")
            elif i == "en:sesame-seeds":
                temp.append("Graines de sésame")
            elif i == "en:peanuts":
                temp.append("Arachides")
            elif i == "en:crustaceans":
                temp.append("Crustacés")
        return temp

    def add_data_from_openFactfood(self, code_barre, my_dic):
        response = OpenFactFood.getProductByBarrecode(self, code_barre)
        if response == None:
            return my_dic
        data = response.json()
        if data['status_verbose'] == "product found" and my_dic["nom"] == "not found":
            my_dic["nom"] = data['product']['product_name']
        my_dic["code_barre"] = code_barre
        if data['status_verbose'] == 'product found' and my_dic["image"] == "not found":
            my_dic["image"] = data['product']['image_thumb_url']
        if data['status_verbose'] == "product found" and my_dic["categorie"] == "not found":
            my_dic["categorie"] = "vitale"
        if data['status_verbose'] == "product found" and my_dic["list_des_ingredients"] == "not found":
            my_dic["list_des_ingredients"] = data['product']['ingredients_text_debug']
        if data['status_verbose'] == "product found" and len(my_dic["allergenes"]) == 0:
            my_dic["allergenes"] = self.check_and_return_allergens(data['product']['allergens_tags'])
            # my_dic["allergenes"] = data["product"]["allergens_from_ingredients"]
        if data['status_verbose'] == "product found" and my_dic["prohibited"] == "not found":
            my_dic["prohibited"] = "alcool" if data["product"]["pnns_groups_2"] == "Alcoholic beverages" else "not found"
        return my_dic

    def add_data_from_openBeautyFacts(self, code_barre, my_dic):
        response = OpenBeautyFacts.getProductByBarrecode(self, code_barre)
        if response == None:
            return my_dic
        data = response.json()
        if data['status_verbose'] == 'product found' and my_dic["nom"] == "not found":
            my_dic["nom"] = data['product']['product_name_fr']
        my_dic["code_barre"] = code_barre
        if data['status_verbose'] == 'product found' and my_dic["image"] == "not found":
            my_dic["image"] = data['product']['image_front_thumb_url']
        if data['status_verbose'] == "product found" and my_dic["categorie"] == "not found":
            my_dic["categorie"] = "non vitale"
        if data['status_verbose'] == "product found" and my_dic["list_des_ingredients"] == "not found":   
            my_dic["list_des_ingredients"] = data['product']['ingredients_text_with_allergens_fr']
        return my_dic

    def add_data_from_web(self, code_barre, my_dic):
        my_dic["code_barre"] = code_barre
        result = {}
        if my_dic["nom"] == "not found":
            my_dic["nom"] = str(WebScrap().Search_on_barrecode(code_barre))
        result = self.web_thread_scraping(code_barre)
        if my_dic["prix"] == "not found":
              my_dic["prix"] = result["price"]
        if my_dic["categorie"] == "not found":
              my_dic["categorie"] = result["categorie"]
        #result = self.ask_price_upc(code_barre)
        ##if my_dic["prix"] == "not found":
          ##  my_dic["prix"] = result["price"]
        ##if my_dic["categorie"] == "not found":
          ##  my_dic["categorie"] = result["categorie"]
        return my_dic
    """
     Recuperer en argument la liste des codesbarre et creer un tableau d'articles (nom, prix unitaire, categorie de produits)
    """
    
    def create_list_of_buy(self, codebarrelist):
        a = 0
        for x in codebarrelist:
            a = a + 1
        x = x         
        lignes = (3  * a)
        i = 0
        my_tab_of_buy = ["" * a] * lignes
        for y in codebarrelist:
            product = PlayData.format_data_for_app_mobile2(self, y)
            my_tab_of_buy[i] = product["nom"]
            i = i + 1
            my_tab_of_buy[i] = product["prix"]
            i = i + 1
            if product["categorie"] == "vitale":
                my_tab_of_buy[i] = "vitale"
            else:
                my_tab_of_buy[i] = "non vitale"
            i = i + 1
        return my_tab_of_buy

    def create_total(self, codebarrelist):
        a = 0
        for x in codebarrelist:
            a = a + 1
        x = x         
        lignes = (3  * a)
        i = 0
        my_tab_of_buy = ["" * a] * lignes
        for y in codebarrelist:
            product = PlayData.format_data_for_app_mobile2(self, y)
            my_tab_of_buy[i] = product["nom"]
            i = i + 1
            my_tab_of_buy[i] = product["prix"]
            i = i + 1
            if product["categorie"] == "vitale":
                my_tab_of_buy[i] = "vitale"
            else:
                my_tab_of_buy[i] = "non vitale"
            i = i + 1
        my_tab_of_vital = PlayData.create_list_vital(PlayData(), my_tab_of_buy)
        my_tab_of_no_vital = PlayData.create_list_no_vital(PlayData(), my_tab_of_buy)
        total_of_vital = PlayData.create_total_vital(PlayData(), my_tab_of_vital)
        total_no_vital = PlayData.create_total_vital(PlayData(), my_tab_of_no_vital)
        total = total_of_vital + total_no_vital
        return total
    

    """
    Recuperer en argument le tableau de create_list_of_buy et creer la liste des article vitaux
    """

    def create_list_vital(self, my_tab_of_buy):
        a = 0
        for x in my_tab_of_buy:
            if x == "vitale":
                a = a + 1
        lignes = (3  * a)
        i = 0
        k = 0
        my_tab_of_vital = ["" * a] * lignes
        for y in my_tab_of_buy:
            if y == "vitale":
                my_tab_of_vital[i] = my_tab_of_buy[k-2]
                i = i + 1
                my_tab_of_vital[i] = my_tab_of_buy[k - 1]
                i = i + 1
                my_tab_of_vital[i] = "vitale"
                i = i + 1
            k = k + 1
        return my_tab_of_vital

    """
    Recuperer en argument le tableau de create_list_of_buy et creer la liste des articles non vitaux
    """

    def create_list_no_vital(self, my_tab_of_buy):

        a = 0
        for x in my_tab_of_buy:
            if x == "non vitale":
                a = a + 1
        lignes = (3  * a)
        i = 0
        k = 0
        my_tab_of_no_vital = ["" * a] * lignes
        for y in my_tab_of_buy:
            if y == "non vitale":
                my_tab_of_no_vital[i] = my_tab_of_buy[k - 2]
                i = i + 1
                my_tab_of_no_vital[i] = my_tab_of_buy[k - 1]
                i = i + 1
                my_tab_of_no_vital[i] = "non vitale"
                i = i + 1
            k = k + 1
        return my_tab_of_no_vital

    """
    Recuperer en argument le tableau de create_list_of_buy et calculer un total en euros des article vitaux
    """

    def create_total_vital(self, my_tab_of_buy):
        total_vital = 0
        k = 0
        for x in my_tab_of_buy:
            if x == "vitale":
                total_vital = total_vital + my_tab_of_buy[k - 1]
            k = k + 1
        return total_vital

    """
    Recuperer en argument le tableau de create_list_of_buy et calculerBy un total en euros des article non-vitaux
    """

    def create_total_no_vital(self, my_tab_of_buy):
        total_non_vital = 0
        k = 0
        for x in my_tab_of_buy:
            if x == "non vitale":
                total_non_vital = total_non_vital + my_tab_of_buy[k - 1]
            k = k + 1 
        return total_non_vital

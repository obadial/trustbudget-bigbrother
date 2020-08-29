from BigBrother.InfoProduct.Datagram.default import *
import requests
import json


class Datagram :

    #def retailersList(self):
     #   url = BASE_URL + RETAILERS_URL_ADD
      #  hheaders = {'x-rapidapi-host': "datagram-products-v1.p.rapidapi.com",
       #             'x-rapidapi-key': CONSUMER_KEY}
       # response = requests.request("GET", url, headers=headers)

        #if response.status_code != 200:
         #   print("ERROR : Pendant retailersList")
        #print(response.text)
        #data = response.text
        #print(data)
        #return (data)

    #def productSearchByName(self, stringToSearch):
     #   url = BASE_URL + STOREPRODUCT_URL_ADD + "search/?q=" + stringToSearch
      #  headers = {'x-rapidapi-host': BASE_URL,
       #     'x-rapidapi-key': CONSUMER_KEY}
       # response = requests.request("GET", url, headers=headers)

       # if response.status_code != 200:
        #    print("ERROR: Pendant productSearchByName")
       # print(response.text)
       # data = response.text
       # print(data)
       # return (data)

    def productSearchByBarreCode(self, barrecode):
        url = "https://datagram-products-v1.p.rapidapi.com/storeproduct/ean/"+ barrecode + "/"
        headers = {'x-rapidapi-host': "datagram-products-v1.p.rapidapi.com",
                   'x-rapidapi-key': CONSUMER_KEY}
        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            print("ERROR: Pendant productSearchByBarreCode")
        print(response.text)
        data = response.text
        print(data)
        return (data)

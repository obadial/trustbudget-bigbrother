# -*- coding: utf-8 -*-

from __future__ import print_function    # (at top of module)
import sys
import time
import requests
import json

from BigBrother.Bank.OBP_Python.default import *
from BigBrother.Bank.OBP_Python.OAuthConnect import *

URL_MY_BANK = '{}/banks/{}'.format(BASE_URL_OA, MY_BANK)
URL_ACCOUNTS = '{}/accounts'.format(URL_MY_BANK)
URL_PRIVATE_ACCOUNTS = '{}/accounts/private'.format(URL_MY_BANK)

class HandlerOBP :

    api = ""

    def _init_(self) :
        self.api = ""
        print("init HandlerOBP")

    def mergeHeaders(self, base, add):
        z = base.copy()
        z.update(add)
        return z

    def setToken(self, t):
        global DC_TOKEN
        DC_TOKEN = { 'Authorization' : 'DirectLogin token=%s' % t}

    # Logger
    def log(self, m):
        global LOGGING
        if LOGGING:
            print(m)

    def connect(self) :
        self.api = get_api()
        response = self.api.get(BASE_URL_OA)
        status_code = response.status_code

        if status_code != 200:
            print("ERROR: PAS DE CONNEXION AVEC L'API")
        else :
            print("API CONNEXION => OK")

    #login as User
    def directConnect(self):
        login_url = '{0}/my/logins/direct'.format(BASE_URL)#For Direct Login
        login_header  = { 'Authorization' : 'DirectLogin username="%s",password="%s",consumer_key="%s"' % (USERNAME, PASSWORD, CONSUMER_KEY)}
        # Login and receive authorized token
        self.log('Login as {0} to {1}'.format(login_header, login_url))
        r = requests.post(login_url, headers=login_header)
        # If error
        if (r.status_code != 201):
            self.log("error: could not login")
            self.log("text: " + r.text)
            return r.text
        #else
        t = r.json()['token']
        self.log("Received token: {0}".format(t))
        self.setToken(t)
        return t


    def getSandAccountICanUse(self) :
        """Get the accounts (id) owned by the actual user of the Sandbox from the API"""

        print('Getting private accounts actual user of the Sandbox own ...')
        #response = self.api.get(URL_PRIVATE_ACCOUNTS)
        response = requests.get(URL_PRIVATE_ACCOUNTS, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        data = response.json()
        status_code = response.status_code
        if status_code != 200:
            print("ERROR: Pendant getSandAccountICanUse")
        else :
            print("getSandAccountICanUse => OK")
        return (data)

    def getMoneyAmountOnAccountId(self, id):
        """Get Money amount from the account owner by his ID"""

        amount = -1
        url_answer = '{}/{}/owner/account'.format(URL_ACCOUNTS, id)
        #response = self.api.get(url_answer)
        response = requests.get(url_answer, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        status_code = response.status_code
        if status_code != 200:
            print("ERROR: Pendant getMoneyAmountOnAccountId")
        else :
            print("getMoneyAmountOnAccountId (id={})=> OK".format(id))
            data = response.json()
            amount = data['balance']['amount']
        return amount

    def changeLabelOnAccount(self, id, label):
        """Change the label of one account"""

        headers = {'content-type': 'application/json'}

        url = '{}/{}'.format(URL_ACCOUNTS, id)
        data = {'label': label,
        'id': id,
        'bank_id': MY_BANK}
        #self.api.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        requests.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        pass

    def doSandTransaction(self, idSender, idReceiver, amount):
        headers = {'content-type': 'application/json'}
        url = "{}/{}/owner/transaction-request-types/SANDBOX_TAN/transaction-requests".format(URL_ACCOUNTS, idSender)
        data = {'to': {
        "bank_id": MY_BANK,
        "account_id": idReceiver
        },
        "value": {
        "currency": OUR_CURRENCY,
        "amount": amount
        },
        "description": "This is a sand transaction"}
        #self.api.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        requests.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        pass

    def doCounterpartyTransaction(self, idSender, counterpartyId, amount, message):
        url = "{}/{}/owner/transaction-request-types/COUNTERPARTY/transaction-requests".format(URL_ACCOUNTS, idSender)
        data = {'to': {
        "counterparty_id": counterpartyId
        },
        'value': {
        "currency": OUR_CURRENCY,
        "amount": amount
        },
        'description': message,
        'charge_policy': 'SHARED',
        'future_date': ''
        }
        response = requests.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        data = response.json()
        #print(data['status'])
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print(data)
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print(data['id'])
        #Validation du challenge de Paiment
        if (data['status'] == 'INITIATED'):
            url = "{}/{}/owner/transaction-request-types/COUNTERPARTY/transaction-requests/{}/challenge".format(URL_ACCOUNTS, idSender, data['id'])
            newData = {}
            newData = {
            "id": data['challenge']['id'],
            "answer": "123"
            }
            response = requests.post(url, json=newData, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
            newData = response.json()
            print(newData)
            #print(newData['status'])
        return (newData)
        pass

#    def validationChallenge(self, id_client, challenge_type, id_transaction, id_challenge):
#        url = "{}/{}/owner/transaction-request-types/{}/transaction-requests/{}/challenge".format(URL_ACCOUNTS, id_client, challenge_type, id_transaction)
#        data = {
#        "id": id_challenge,
#        "answer": "123"
#        }
#        response = requests.post(url, json=data, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
#        print(response['status'])
        #if response['status'] == "COMPLETED":
        #    print("Validation Transaction OK")
        #else:
        #    print(response['status'])
#        pass


    def addCounterpartie(self, data):
        data = json.loads(data)
        url = "{}/{}/owner/counterparties".format(URL_ACCOUNTS, data['id_obp_sender'])
        headers = {'content-type': 'application/json'}#cette ligne est probablement obsolète (et ça partout ou on la voit sauf dans default.py)
        requestData = {
        "name": data['name'],
        "description": data['description'],
        "other_bank_routing_scheme": "",
        "other_bank_routing_address": MY_BANK,
        "other_account_routing_scheme": "",
        "other_account_routing_address": data['id_obp_receiver'],
        "is_beneficiary": True,
        "other_account_secondary_routing_scheme": "",
        "other_account_secondary_routing_address": "",
        "other_branch_routing_scheme": "",
        "other_branch_routing_address": "",
        "bespoke": []
        }
        response = requests.post(url, json=requestData, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        print("Réponse de la counterparty request = ")
        print (response.status_code)
        print (url)
        pass

    def getCounterParties(self, id):
        url = "{}/{}/owner/counterparties".format(URL_ACCOUNTS, id)
        response = requests.get(url, headers=self.mergeHeaders(DC_TOKEN, CONTENT_JSON))
        data = response.json()
        print("HERE")
        return (data)
        pass

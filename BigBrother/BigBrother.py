from BigBrother.InfoProduct.Datagram.datagram import Datagram
from BigBrother.Bank.OBP_Python.HandlerOBP import HandlerOBP
from BigBrother.Process.BuyGestion.buygestion import PlayData
from BigBrother.Process.BuyGestion.routine import Algo
from BigBrother.Database.database import Mydata
from BigBrother.localeData.Date.date import Date
from BigBrother.localeData.Distance.distance import Distance
from BigBrother.localeData.Map.Map import Map

import json

class BigBrother:

	myOBPHandler = HandlerOBP()
	myDatagramHandler = Datagram()
	myData = Mydata()

	def _init_(self):
		self.myOBPHandler = HandlerOBP()
		self.myDatagramHandler = Datagram()

	def connect_data_base(self):
		db = self.myData.connection_dataBase()
		return db

	def myroutine(self, info):
		response = Algo.routine(Algo(), self, info)
		return response
	
	def my_change_in_database(self, info):
		tab_achat = info["item"]
		my_list_de_course = []
		for x in tab_achat: 
			my_list_de_course.append(x["barre_code"])
		Algo.make_change_in_database(Algo(), self, info, my_list_de_course)

	def connectOBP(self):
		self.myOBPHandler.connect()

	def directConnectOBP(self):
		self.myOBPHandler.directConnect()
		pass

	def OBPWhichAccountOwnedByCurrentApiUser(self):
		id_list = self.myOBPHandler.getSandAccountICanUse()
		return (id_list)

	def OBPHowMuchMoneyOnThisAccount(self, id):
		money = self.myOBPHandler.getMoneyAmountOnAccountId(id)
		return money

	def OBPChangeLabelOnAccount(self, id, label):
		self.myOBPHandler.changeLabelOnAccount(id, label)
		pass

	def OBPSandTransaction(self, idSender, idReceiver, amount):
		self.myOBPHandler.doSandTransaction(idSender, idReceiver, amount)
		pass

	def OBPCounterpartyTransaction(self, idSender, counterpartyId, amount, message):
		answer = self.myOBPHandler.doCounterpartyTransaction(idSender, counterpartyId, amount, message)
		return (answer)
		pass

	def OBPValidationTransaction(self, id_client, challenge_type, id_transaction, id_challenge):
		self.myOBPHandler.validationChallenge(id_client, challenge_type, id_transaction, id_challenge)
		pass

	def OBPAddCounterpartie(self, data):
		self.myOBPHandler.addCounterpartie(data)
		pass

	def OBPGetCounterParties(self, id):
		counterparties = self.myOBPHandler.getCounterParties(id)
		return (counterparties)
		pass

	def returnAvailaibleIdAccount(self):
		id_list = self.OBPWhichAccountOwnedByCurrentApiUser()

		for account in id_list["accounts"]:
			if (int(account["id"]) >= 100 and account["label"] == "availaible"):
				self.OBPChangeLabelOnAccount(int(account["id"]), "used")
				return int(account["id"])
		pass

	def reInitialiseAccount(self):
		i = 100
		for i in range(100, 121):
			self.OBPChangeLabelOnAccount(i, "availaible")
			money = self.OBPHowMuchMoneyOnThisAccount(i)
			if (float(money) < 10):
				self.OBPSandTransaction(50, i, 10 - float(money))
			elif (float(money) > 10):
				self.OBPSandTransaction(i, 50, float(money) - 10)
		pass

	def ask_info_for_app(self, codebarre):
		data_app_format = PlayData.format_data_for_app_mobile(PlayData(), codebarre)
		return data_app_format

	def my_web_scraping(self, codebarre, opt_id):
		hello = PlayData.web_scraping(PlayData(), codebarre, opt_id)
		return hello

	def my_web_thread_scraping(self, codebarre):
		hello = PlayData.web_thread_scraping(PlayData(), codebarre)
		return hello

	def validate_basket(self, codebarre_list):
		my_tab = PlayData.create_list_of_buy(PlayData(), codebarre_list)
		return (my_tab)

	def check_list_buyer(self):
		list = PlayData.ask_list_retail(PlayData())
		return (list)

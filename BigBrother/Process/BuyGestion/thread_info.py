from BigBrother.InfoProduct.Datagram.datagram import Datagram
from BigBrother.InfoProduct.WebScraping.catch_price import WebScrap
import sys
from threading import Thread
import time

class MyThread(Thread):

    def __init__(self, codebarre, id_obp, result):
        Thread.__init__(self)
        self.codebarre = codebarre
        self.id_obp = id_obp
    
    def run(self):
        data = WebScrap().Search_on_web(self.codebarre, self.id_obp)
        self.result = data
        return data


class Hello(MyThread):

    def __init__(self):
        """
        hello
        """

    def check_by_thread_codebarre(self, codebarre):

        result_carrefour = 0
        result_naturalia = 0
        result_picard = 0
        result_fnac = 0
        result_amazon = 0
        result_jouet_club = 0
        result_castorama = 0

        thread_1 = MyThread(codebarre, "carrefour", result_carrefour)
        thread_2 = MyThread(codebarre, "naturalia", result_naturalia)
        thread_3 = MyThread(codebarre, "picard", result_picard)
        thread_4 = MyThread(codebarre, "fnac", result_fnac)
        thread_5 = MyThread(codebarre, "amazon", result_amazon)
        thread_6 = MyThread(codebarre, "jouet_club", result_jouet_club)
        thread_7 = MyThread(codebarre, "castorama", result_castorama)



        # Lancement des threads
        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        thread_5.start()
        thread_6.start()
        thread_7.start()


        # Attend que les threads se terminent
        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()
        thread_5.join()
        thread_6.join()
        thread_7.join()


        tab = {}
        tab["carrefour"] = thread_1.result
        tab["naturalia"] = thread_2.result
        tab["picard"] = thread_3.result
        tab["fnac"] = thread_4.result
        tab["amazon"] = thread_5.result
        tab["jouet_club"] = thread_6.result
        tab["castorama"] = thread_7.result
        return tab
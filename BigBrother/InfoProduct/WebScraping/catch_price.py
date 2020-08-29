import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json 
import time
from BigBrother.InfoProduct.WebScraping.create_headers import HelloWorld

"""
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
"""

class WebScrap:

    def __init__(self):
        """
        Ici on va recuperer des datas depuis le web thanks Timothy John Berners-Lee :)
        """

    def Search_on_web(self, barrecode, opt_id) :
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'referrer': 'https://google.fr',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': '',
            'Accept-Language': 'en-US,fr,en;q=0.9',
            'Pragma': 'no-cache',
             }


        """
        fait
        """
        if opt_id == "carrefour":
            response_carrefour = requests.get('https://www.carrefour.fr/s?q=' + str(barrecode), headers=headers)
            soup_carrefour = BeautifulSoup(response_carrefour.text,'html.parser')
            soup_carrefour = self.Search_on_carrefour(soup_carrefour)
            return soup_carrefour

        """
        fait
        """
        if opt_id == "picard":
            response_picard = requests.get('https://www.picard.fr/recherche?q=' + str(barrecode), headers=headers)
            soup_picard = BeautifulSoup(response_picard.text, 'html.parser')
            soup_picard = self.Search_on_picard(soup_picard)
            return soup_picard


        """
        fait
        """
        if opt_id == "naturalia":
            response_naturalia = requests.get('https://naturalia.fr/catalogsearch/result/?q=' + str(barrecode), headers=headers)
            soup_naturalia = BeautifulSoup(response_naturalia.text, 'html.parser')
            soup_naturalia = self.Search_on_naturalia(soup_naturalia)
            return soup_naturalia

        """
        fait
        """
        if opt_id == "fnac":
            response_fnac = requests.get('https://www.fnac.com/SearchResult/ResultList.aspx?SCat=0%211&Search=' + str(barrecode), headers=headers)
            soup_fnac = BeautifulSoup(response_fnac.text, 'html.parser')
            soup_fnac = self.Search_on_fnac(soup_fnac)
            return soup_fnac
        

        """
        fait
        """
        if opt_id == "amazon":
            response_amazon = requests.get('https://www.amazon.fr/s?k=' + str(barrecode), headers=headers)
            soup_amazon = BeautifulSoup(response_amazon.text, 'html.parser')
            soup_amazon = self.Search_on_amazon(soup_amazon)
            return soup_amazon

        """
        fait
        """
        if opt_id == "rue_du_commerce":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            #print(soup_barrecode)
            if (soup_barrecode == -1):
                return (0)
            response_rue_du_commerce = requests.get('https://www.rueducommerce.fr/recherche/' + str(soup_barrecode), headers=headers)
            soup_rue_du_commerce = BeautifulSoup(response_rue_du_commerce.text, 'html.parser')
            soup_rue_du_commerce = self.Search_on_rue_du_commerce(soup_rue_du_commerce)
            return soup_rue_du_commerce

        if opt_id == "sephora":
            response_sephora = requests.get('https://www.sephora.fr/recherche?q={' + str(barrecode) + '}', headers=headers)
            soup_sephora = BeautifulSoup(response_sephora.text, 'html.parser')
            soup_sephora = self.Search_sephora(soup_sephora)
            return soup_sephora

        """
        fait
        """
        if opt_id == "jouet_club":
            headers_1 = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'referrer': 'https://google.fr',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': '',
            'Accept-Language': 'en-US,fr,en;q=0.9',
            'Pragma': 'no-cache',
            }
            response_jouet_club = requests.get('https://www.joueclub.fr/contenu/resultat-de-recherche-produits.html?searchText=' + str(barrecode), headers=headers_1)
            soup_jouet_club = BeautifulSoup(response_jouet_club.text, 'html.parser')
            #print(soup_jouet_club)
            soup_jouet_club = self.Search_jouet_club(soup_jouet_club)
            return soup_jouet_club

        """
        fait
        """
        #if opt_id == "ikea":
         #   driver = webdriver.Chrome(ChromeDriverManager().install())
          #  driver.get('https://www.ikea.com/fr/fr/search/products/?q=' + str(barrecode))
           # time.sleep(2)
            #print(driver.page_source)
            #response_ikea = requests.get('https://www.ikea.com/fr/fr/search/products/?q=' + str(barrecode), headers=headers)
            #soup_ikea = BeautifulSoup(driver.page_source, 'html.parser')
            #soup_ikea = self.Search_ikea(soup_ikea)
            #return soup_ikea

        """
        fait
        """
        if opt_id == "castorama":
            response_castorama = requests.get('https://www.castorama.fr/search?Ntt=' + str(barrecode), headers=headers)
            soup_castorama = BeautifulSoup(response_castorama.text, 'html.parser')
            soup_castorama = self.Search_castorama(soup_castorama)
            return soup_castorama

        if opt_id == "decathlon":
            soup_barrecode = self.Search_on_barrecode("decathlon" + str(barrecode))
            if (soup_barrecode == -1):
                return (0)
            response_decathlon = requests.get('https://www.decathlon.fr/search?Ntt=' + str(barrecode), headers=headers)
            soup_decathlon = BeautifulSoup(response_decathlon.text, 'html.parser')
            soup_decathlon = self.Search_decathlon(soup_decathlon)
            return soup_decathlon

        if opt_id == "nicolas":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if soup_barrecode == -1:
                return 0
            response_nicolas = requests.get('https://www.nicolas.com/fr/search/?text=' + str(barrecode), headers=headers)
            soup_nicolas = BeautifulSoup(response_nicolas.text, 'html.parser')
            soup_nicolas = self.Search_nicolas(soup_nicolas)
            return soup_nicolas

        if opt_id == "zara":
            soup_barrecode = self.Search_on_barrecode("zara" + barrecode)
            if soup_barrecode == -1:
                return 0
            response_zara = requests.get('https://www.zara.com/fr/fr/search?searchTerm=' + str(barrecode), headers=headers)
            soup_zara = BeautifulSoup(response_zara.text, 'html.parser')
            soup_zara = self.Search_zara(soup_zara)
            return soup_zara

        if opt_id == "desigual":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if (soup_barrecode == -1):
                return (0)
            response_desigual = requests.get('https://www.desigual.com/fr_FR/' + str(soup_barrecode), headers=headers)
            soup_desigual = BeautifulSoup(response_desigual.text, 'html.parser')
            soup_desigual = self.Search_desigual(soup_desigual)
            return soup_desigual

        if opt_id == "gstar":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if soup_barrecode == -1:
                return 0
            response_gstar = requests.get('https://www.g-star.com/fr_fr/search?q=' + str(barrecode), headers=headers)
            soup_gstar = BeautifulSoup(response_gstar.text, 'html.parser')
            soup_gstar = self.Search_gstar(soup_gstar)
            return soup_gstar

        """
        prioritaire
        """
        if opt_id == "leclerc":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if (soup_barrecode == -1):
                return (0)
            response_leclerc = requests.get('https://www.recherche.leclerc/recherche?q=' + str(barrecode),headers=headers)
            #response_leclerc = requests.get('https://www.recherche.leclerc/recherche?q=' + str(soup_barrecode), headers=headers)
            soup_leclerc = BeautifulSoup(response_leclerc.text, 'html.parser')
            soup_leclerc = self.Search_leclerc(soup_leclerc)
            if soup_leclerc == 0:
                response_leclerc = requests.get('https://www.prixing.fr/search/' + str(barrecode), headers=headers)
                soup_leclerc = BeautifulSoup(response_leclerc.text, 'html.parser')
                soup_leclerc = self.Search_leclerc2(soup_leclerc)
            return soup_leclerc

        """
        prioritaire
        """
        if opt_id == "auchan":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if soup_barrecode == -1:
                return (0)
            response_auchan = requests.get('https://www.auchan.fr/recherche?text=' + str(barrecode), headers=headers)
            #response_auchan = requests.get('https://www.auchan.fr/recherche?text=' + str(soup_barrecode), headers=headers)
            soup_auchan = BeautifulSoup(response_auchan.text, 'html.parser')
            #print(soup_auchan)
            soup_auchan = self.Search_auchan(soup_auchan)
            if soup_auchan == 0:
                response_auchan = requests.get('https://www.prixing.fr/search/' + str(barrecode), headers=headers)
                soup_auchan = BeautifulSoup(response_auchan.text, 'html.parser')
                soup_auchan = self.Search_auchan2(soup_auchan)
            return soup_auchan
        
        """
        A faire
        """
        if opt_id == "darty":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if (soup_barrecode == -1):
                return (0)
            response_darty = requests.get('https://www.darty.com/nav/recherche?text=' + str(barrecode), headers=headers)
            soup_darty = BeautifulSoup(response_darty.text, 'html.parser')
            soup_darty = self.Search_darty(soup_darty)
            return soup_darty

        if opt_id == "intersport":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if (soup_barrecode == -1):
                return (0)
            response_intersport = requests.get('https://www.intersport.fr/search/?text=' + str(barrecode), headers=headers)
            soup_intersport = BeautifulSoup(response_intersport.text, 'html.parser')
            soup_intersport = self.Search_intersport(soup_intersport)
            return soup_intersport

        if opt_id == "nocibe":
            soup_barrecode = self.Search_on_barrecode(barrecode)
            if soup_barrecode == -1:
                return 0
            response_nocibe = requests.get('https://www.nocibe.fr/resultats/' + str(soup_barrecode), headers=headers)
            soup_nocibe = BeautifulSoup(response_nocibe.text, 'html.parser')
            soup_nocibe = self.Search_nocibe(soup_nocibe)
            return soup_nocibe

        
        #response_go_sport = requests.get('https://www.go-sport.com' + str(soup_barrecode), headers=headers) ca a plante
        #response_monoprix = requests.get('https://www.monoprix.fr/courses/search/' + str(soup_barrecode), headers=headers) ca plante
        #response_celio = requests.get('' + str(soup_barrecode), headers=headers)
        #response_camaieu = requests.get('' + str(soup_barrecode), headers=headers)
        #response_toysrus = requests.get('' + str(soup_barrecode), headers=headers)

       
        #soup_go_sport = BeautifulSoup(response_go_sport.text, 'html.parser')
        #soup_monoprix = BeautifulSoup(response_monoprix.text, 'html.parser')

        #soup_go_sport = self.Search_go_sport(soup_go_sport)
        #soup_monoprix = self.Search_monoprix(soup_monoprix)
    
    def Search_on_barrecode(self, barrecode):
        headers_1 = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.fr',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': '',
        'Accept-Language': 'en-US,fr,en;q=0.9',
        'Pragma': 'no-cache',
        }
        response_barrecode = requests.get('https://www.google.com/search?q=' + str(barrecode), headers=headers_1)
        soup_barrecode = BeautifulSoup(response_barrecode.text, "html.parser")
        #print("\n\nhello Google\n\n\n")
        price_product = soup_barrecode.find('h3' , class_ = 'LC20lb')
        if not price_product:
            return (-1)
        else:
            #print("hello\n")
            string_barrecode = str(barrecode)
            #print(string_barrecode)
            #print("\n")
            title = price_product.get_text()
            x = title.replace(string_barrecode, '')
            y = x.replace('UPC', '')
            v = y.replace('upcitemdb.com', '')
            new_string = v
            return (new_string)

    def Search_zara(self, soup_zara):
        #print("\n\nHello Zara\n\n")
        #print(soup_zara)
        if soup_zara.find(class_="main-price") is None:
            return 0
        price_product = soup_zara.find(class_='main-price').get_text().strip()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product
    
    def Search_gstar(self, soup_gstar):
        #print("\n\nHello Gstar\n\n")
        #print(soup_gstar)
        if soup_gstar.find(class_="productPrice-value") is None:
            return 0
        price_product = soup_gstar.find(class_='productPrice-value').get_text().strip()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_nocibe(self, soup_nocibe):
        #print("\n\nHello Nocibe\n\n")
        #print(soup_nocibe)
        if soup_nocibe.find(class_="product-item__only-price") is None:
            return 0
        price_product = soup_nocibe.find(class_='product-item__only-price').get_text().strip()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_intersport(self, soup_intersport):
        #print("\n\nHello Intersport\n\n")
        #print(soup_intersport)
        if soup_intersport.find(class_="current-price") is None:
            return 0
        price_product = soup_intersport.find(class_='current-price').get_text().strip()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return (price_product)

    def Search_leclerc(self, soup_leclerc):
        #print("\n\nHello Leclerc\n\n")
        if soup_leclerc.find(class_="txt_prix_final").getText().strip() == "Sélectionner un drive pour voir la disponibilité et le prix du produit":
            return 0
        price_product = soup_leclerc.find(class_="txt_prix_final").getText().strip()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_leclerc2(self, soup_leclerc):
        #print("\n\nHello Leclerc\n\n")
        if soup_leclerc.find(class_="mainPrix") is None:
            return 0
        price_product = soup_leclerc.find(class_="mainPrix").getText()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_auchan(self, soup_auchan):
        #print("\n\nHello Auchan\n\n")
        if soup_auchan.find(itemprop="price") is None:
            return 0
        price_product = float(soup_auchan.find(itemprop="price")['content'])
        #print(soup_auchan)
        return price_product

    def Search_auchan2(self, soup_auchan):
        if soup_auchan.find(class_="mainPrix") is None:
            return 0
        price_product = soup_auchan.find(class_="mainPrix").getText()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_darty(self, soup_darty):
        #print("\n\nHello Darty\n\n")
        if soup_darty.find(class_='darty_prix') is None:
            return 0
        price_product = soup_darty.find(class_='darty_prix').get_text().strip()
        #print(soup_darty)
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return (price_product)

    #def Search_monoprix(self, soup_monoprix):
        #print("\n\nHello Monoprix\n\n")
        #print(soup_monoprix)
        #return (soup_monoprix)

    def Search_desigual(self, soup_desigual):
        #print("\n\nHello Desigual\n\n")
        #print(soup_desigual)
        return (soup_desigual)

    #def Search_go_sport(self, soup_nicolas):
        #print("\n\nHello Go Sport\n\n")
        #print(soup_nicolas)
        #return (soup_nicolas)

    def Search_nicolas(self, soup_nicolas):
        #print("\n\nHello Nicolas\n\n")
        #print(soup_nicolas)
        if soup_nicolas.find(class_='ns-Price-unity') is None:
            return 0
        price_product = soup_nicolas.find(class_='ns-Price-unity').get_text() + soup_nicolas.find(class_='ns-Price-decimal').get_text()
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_castorama(self, soup_castorama):
        #print("\n\nhello Castorama\n\n")
        price_product = soup_castorama.find(class_="pricing")
        if price_product is None:
            price_float = 0
            return(price_float)
        price = price_product.get_text()
        new_price = ''
        for x in price:
            if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                if (x == ','):
                    x = '.'
                new_price = new_price + x
        price_float = float(new_price)
        #print(price_float)
        return (price_float)

    def Search_jouet_club(self, soup_jouet_club):
        price_product = soup_jouet_club.find(class_="col-md-9")
        if price_product is None:
            price_float = 0
            return(price_float)
        price_product = price_product.find(type="application/javascript")
        if price_product is None:
            price_float = 0
            return(price_float)
        text = price_product.get_text()
        a = text.replace('window.__change[\'5\'] = ', '')
        b = a.replace(';','')
        data = json.loads(b)
        #print(data)
        if (data["context"]['detailed'] == "True"):
            data2 = data["productsData"][0]['price']['valueWithTax']
            return (data2)
        else:
            return 0

    def Search_ikea(self, soup_ikea):
        if soup_ikea.find(class_="products__zero-results-text") is None:
            price_product = soup_ikea.find(class_="product-compact__price__value")
            #print(price_product)
            if price_product is None:
                price_float = 0
                return(price_float)
            text = price_product.get_text()
            new_price = ''
            for x in text:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
            #print(price_float)
            return (price_float)
        else:
            price_float = 0
            return price_float

    def Search_decathlon(self, soup_decathlon):
        #print("\n\nhello Decathlon\n\n\n")
        #print(soup_decathlon)
        if soup_decathlon.find(class_='dkt-price__cartridge') is None:
            return 0
        price_product = soup_decathlon.find(class_='dkt-price__cartridge').get_text().strip()
        #print(price_product)
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return price_product

    def Search_on_naturalia(self, soup_naturalia):
        #print("\n\nhello naturalia\n\n")
        price_product = soup_naturalia.find(class_='price')
        if price_product is None:
            price_float = 0
            return price_float
        else:
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
        #print(price_float)
        return (price_float)

    def Search_sephora(self, soup_sephora):
        #print("\n\nhello sephora\n")
        #print(soup_sephora)
        price_product = soup_sephora.find(class_='price-sales').get_text().strip()
        #print(price_product)
        price_product = price_product.replace(",", ".")
        price_product = price_product.replace("€", "")
        price_product = float(price_product)
        return (price_product)

    def Search_on_rue_du_commerce(self, soup_rue_du_commerce):
        price_product = soup_rue_du_commerce.find(class_='price')
        if price_product is None:
            price_float = 0
            return price_float
        else:
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',' or x == '€':
                    if (x == ',' or x == '€'):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
        return (price_float)

    def Search_on_carrefour(self, soup_carrefour):
        #print("hello Carrefour\n")
        #print(soup_carrefour)
        price_product = soup_carrefour.find(class_='product-card-price__pricing')
        #print(price_product)
        if price_product is None:
            price_float = 0
        else:
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
        #print(price_float)
        return (price_float)

    def Search_on_picard(self, soup_picard):
        #print("\n\n\nhello Picard\n\n\n")
        price_product = soup_picard.find(class_='price')
        if price_product is None:
            price_float = 0
            #print(price_float)
            return (price_float)
        else:
            #print(price_product)
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
            #print(price_float)
            return (price_float)
            price_product = soup_picard.find(class_='price promo-picardetmoi')
            if price_product is None:
                price_product = soup_picard.find(class_='old_price price-promo')
                if price_product is None:
                    price_float = 0
                    return price_float
            else:
                if price_product is None:
                    price_float = 0
                    #print(price_float)
                    return(price_float)
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
            #print(price_float)
            return (price_float)

    def Search_on_fnac(self, soup_fnac):
        #print("\n\n\nhello Fnac\n\n\n")
        price_product = soup_fnac.find(class_='thumbnail-price')
        if price_product is None:
            price_product = soup_fnac.find(class_='userPrice')
            if price_product is None:
                price_product = 0
                #print(price_product)
                return(price_product)
            else:
                price_product = price_product.get_text()
                new_price = ''
                for x in price_product:
                    if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                        if (x == ','):
                            x = '.'
                        new_price = new_price + x
                price_float = float(new_price)
                #print(price_float)
                return (price_float)
        else:
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
            #print(price_float)
            return (price_float)

    def Search_on_amazon(self, soup_amazon):
        #print("\n\n\nhello Amazon\n\n\n")
        price_product = soup_amazon.find(class_='a-price-whole')
        if price_product is None:
            price_float = 0
        else:
            #print(price_product)
            price_product = price_product.get_text()
            new_price = ''
            for x in price_product:
                if x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '.' or x == ',':
                    if (x == ','):
                        x = '.'
                    new_price = new_price + x
            price_float = float(new_price)
        #print(price_float)
        return (price_float)



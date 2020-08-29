import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from BigBrother.BigBrother import BigBrother
from BigBrother.localeData.Distance.distance import Distance
from BigBrother.localeData.Date.date import Date
from BigBrother.InfoProduct.DatagramRequest_optimisation.datagramrequest import DatagramRequest


bigbrother = BigBrother()
bigbrother.directConnectOBP()
datagramRequest = DatagramRequest()

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8000


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()


    def askInfoArticle(self, data):
        data = json.loads(data)
        response = datagramRequest.findBarreCode(int(data['code_barre']))
        if response:
            response_json = json.loads(response)
            json_retour = {}
            json_retour['status_code'] = 200 
            json_retour['reponse'] = response_json
            json_retour['reponse']['status_code'] = 200
            if json_retour['reponse']['prix'] == 0:
                json_retour['reponse']['status_code'] = 413
                json_retour['status_code'] = 413
            return json.dumps(json_retour)
        else:
            response = bigbrother.ask_info_for_app(data['code_barre'])
            json_retour = {}
            json_retour['status_code'] = 200 
            json_retour['reponse'] = response
            json_retour['reponse']['status_code'] = 200
            if json_retour['reponse']['prix'] == 0:
                json_retour['reponse']['status_code'] = 413
                json_retour['status_code'] = 413
            return json.dumps(json_retour)

    def askRetailList(self, data):
        data = json.loads(data)
        with open('./shop.json', 'r') as f:
            complet_list = json.load(f)
        #complet_list = bigbrother.myDatagramHandler.retailersList()
        dist = Distance(data['latitude'], data['longitude'], complet_list, data['distance'])
        list_distance = dist.getListDistance()
        json_retour = {}
        json_retour['id_client'] = data['id_client']
        if list_distance != []:
            json_retour['status_code'] = 200
            json_retour['status_reponse'] = "Good"
        else:
            json_retour['status_code'] = 400
            json_retour[
                'status_reponse'] = "Error : Aucun magasin disponible dans votre rayon. Faites une nouvelles recherche avec un rayon plus grand"
        json_retour['reponse'] = list_distance
        return json.dumps(json_retour)

    def do_GET(self):
        paths = {
            '/MoneyOnAccount': {'status': 200},
            '/getExistCounterparties': {'status': 200},
            '/askInfoArticle': {'status': 200},
            '/askRetailList': {'status': 200}
        }
        if self.path in paths:
            self.respond(paths[self.path], "GET")
        else:
            self.respond({'status': 500}, "GET")

    def do_POST(self):
        paths = {
            '/NewCustomerRegister': {'status': 200},
            '/doSandTransaction': {'status': 200},
            '/doCounterpartyTransaction': {'status': 200},
            '/validateChallenge': {'status': 200},
            '/addCounterpartie': {'status': 200},
            '/resetAccount': {'status': 200}
        }
        if self.path in paths:
            self.respond(paths[self.path], "POST")
        else:
            self.respond({'status': 500}, "POST")

    def handle_http(self, status_code, path, type):
        if type == "GET":
            my_json = self.headers['Content']
        else:
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            my_json = body.decode('utf8').replace("'", '"')
        data = ""
        if path == "/NewCustomerRegister":
            data = self.NewCustomerRegister(my_json)
        elif path == "/MoneyOnAccount":
            data = self.HowMuchMoney(my_json)
        elif path == "/doSandTransaction":
            data = self.doSandTransaction(my_json)
        elif path == "/doCounterpartyTransaction":
            data = self.doCounterpartyTransaction(my_json)
        elif path == "/validateChallenge":
            self.validateChallenge(my_json)
            self.send_response(status_code)
            return bytes("", 'UTF-8')
        elif path == "/addCounterpartie":
            self.addCounterpartie(my_json)
        elif path == "/getExistCounterparties":
            data = self.getExistCounterparty(my_json)
        elif path == "/resetAccount":
            self.resetAccount()
            self.send_response(status_code)
            return bytes("", 'UTF-8')
        elif path == "/askInfoArticle":
            data = self.askInfoArticle(my_json)
        elif path == "/askRetailList":
            data = self.askRetailList(my_json)
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(data, 'utf-8'))
        content = "".format(path)
        return bytes(content, 'UTF-8')

    def respond(self, opts, type):
        response = self.handle_http(opts['status'], self.path, type)
        self.wfile.write(response)


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))

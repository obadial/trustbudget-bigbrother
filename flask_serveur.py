from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
from flask_socketio import send, emit
import json

from BigBrother.BigBrother import BigBrother
from BigBrother.localeData.Distance.distance import Distance
from BigBrother.localeData.Date.date import Date
from BigBrother.InfoProduct.DatagramRequest_optimisation.datagramrequest import DatagramRequest
import basket_validation.core as pred_core

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
bigbrother = BigBrother()
bigbrother.directConnectOBP()
datagramRequest = DatagramRequest()

@socketio.on('connect')
def connect():
    print('One client is Connected\n')

@socketio.on('disconnect')
def disconnect():
    print('One Client is disconnected\n')


@socketio.on("askInfoArticle")
def askInfoArticle(data):
    data = json.loads(data)
    #response = datagramRequest.findBarreCode(int(data['code_barre']))
    #if response == None:
    #    response = datagramRequest.saveRequestDatagram(int(data['code_barre']))
    response = bigbrother.ask_info_for_app(data['code_barre'])
    json_retour = {}
    json_retour['status_code'] = 200 # toujours good
    json_retour['reponse'] = response
    json_retour['reponse']['status_code'] = 200
    if json_retour['reponse']['prix'] == 0:
        json_retour['reponse']['status_code'] = 413
        json_retour['status_code'] = 413
    json_retour['nsp'] = data['nsp']
    emit('askInfoArticle', json.dumps(json_retour))


@socketio.on("askRetailList")
def askRetailList(data):
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
        json_retour['status_reponse'] = "Error : Aucun magasin disponible dans votre rayon. Faites une nouvelles recherche avec un rayon plus grand"
    json_retour['reponse'] = list_distance
    emit('askRetailList', json.dumps(json_retour))


if __name__ == '__main__':
    socketio.run(app, port=8080, host='0.0.0.0')

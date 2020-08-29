//node client_http.js
//client.js
//var io = require('socket.io-client');
var json = require('json');

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhttp = new XMLHttpRequest();
var Url = 'http://0.0.0.0:8000';
//var Url = 'http://193.70.89.169:8000';
//var Url = 'https://93.28.57.72:8000';
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        obj = JSON.parse(this.responseText);
        console.log(obj)
    }
  };

//MoneyOnAccount
//arg = {"id_client": 3, "id_obp": 119}//Id de l'utilisateur dans ton API et son id OBP
//path = "/MoneyOnAccount"

//getExistCounterparties
/*arg = {"id_client": 3, "id_obp": 3}
path = "/getExistCounterparties"*/

//askRetailList
/*arg = ? //Pas d'exemple en dessous
path = "/askRetailList"*/

//askInfoArticle
//arg = {"id_client": 3, "code_barre": "3560070820542"}
//path = "/askInfoArticle"

arg = { "id_client": 3, "code_barre": "3068320120256" }
path = "/askInfoArticle"

//arg = { "id_client": 3, "latitude": 48.839, "longitude": 2.35349, "distance":50}
//path = "/askRetailList"

//arg = { "id_client": 3, "code_barre": "8712100824630" }
//path = "/askInfoArticle"


xhttp.open("GET", Url + path, true);
xhttp.setRequestHeader("Content", JSON.stringify(arg));
xhttp.send();

//NewCustomerRegister
/*arg = {"id_client": 3};//Exemple ton utilisateur a l'id -> 3
path = "/NewCustomerRegister"*/

//doSandTransaction
/*arg = {"id_client": 3, "id_obp_sender": 119, "id_receiver": 4, "id_obp_receiver": 118, "amount" : 2}
path = "/doSandTransaction"*/

//doCounterpartyTransaction
/*arg = {"id_client": 3, "id_obp_sender": 3, "id_receiver": 1, "id_counterparty": "817464da-5835-41f7-8574-92fc0ecf3942",
  "amount": 3000, "message": "Test depuis le client node"};
path = "/doCounterpartyTransaction"*/

//validateChallenge
/*arg = {"id_obp": 3, "challenge_type": "COUNTERPARTY", "id_transaction": "3b536d94-c9a5-4fb0-8f20-c10b9aa500c0",
  "id_challenge": "c340fe12-4c28-4656-8ce1-4e38bbc7f1c8"}
path = "/validateChallenge"*/

//addCounterpartie
/*arg = {"id_client": 3, "id_obp_sender": 3, "id_obp_receiver": 4, "name": "TestMerge", "description": "TestMerge"};
path = "/addCounterpartie"*/

/*xhttp.open("POST", Url + path, true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.send(JSON.stringify(arg));*/

//resetAccount
/*xhttp.open("POST", Url + "/resetAccount", true);
xhttp.send();*/


//client.js
var io = require('socket.io-client');
var json = require('json');
//var socket = io.connect('http://localhost:8080', { reconnect: true, transports: ['websocket'] });
var socket = io.connect('http://193.70.89.169:8080', {reconnect: true, transports: ['websocket']});
console.log("ok")
//var socket = io.connect('http://localhost:8080', {reconnect: true});

/*socket.on('my response', function(data) {
  console.log(data);
  console.log('my response');
});*/

//socket.on('newBankId', function(data) {
  //data = JSON.parse(data)
  //console.log("data = ", data, "  id_client = ", data.id_client, "  id_obp = ", data.id_obp);
  //L'id réccupéré ici doit etre passé en int et enregistré dans la bdd
//});

//socket.on('MoneyOnAccountReceipt', function(data) {
//  data = JSON.parse(data)
  //console.log("data = ", data, "  solde = ", data.solde);
  //La réponse pour savoir combien d'argent sur un compte.
//});

//socket.on('sandTransactionReply', function(data) {
  //data = JSON.parse(data);
  //console.log("data = ", data);
  //réponse pour savoir si la sand transaction a réussi ou non
//});

//socket.on('counterpartyTransactionReply', function(data) {
  //data = JSON.parse(data);
  //console.log("data = ", data);
//});

//socket.on('existCounterPartiesReply', function(data) {
  //data = JSON.parse(data);
  //console.log("ExistCounterparty")
  //console.log("counterparties = ", data.counterparties[0].counterparty_id);
  //arg = {"id_client": 3, "id_obp_sender": 3, "id_receiver": 1, "id_counterparty": data.counterparties[0].counterparty_id,
  //"amount": 3000, "message": "Test depuis le client node"};
  //socket.emit("doCounterpartyTransaction", JSON.stringify(arg));
//});

socket.on('MoneyOnAccountReceipt', function(data) {
  data = JSON.parse(data);
  console.log(data)
});

/*socket.on('askInfoArticle', function(data) {
  data = JSON.parse(data);
  console.log(data)
});*/

socket.on('connect', function () {
  console.log('client Connected to server');

  //arg = {"id_client": 3, "id_obp": 119}//Id de l'utilisateur dans ton API et son id OBP
  //socket.emit("MoneyOnAccount", JSON.stringify(arg));
  /*arg = {"id_client": 3, "id_obp": 3}
  socket.emit("getExistCounterparties", JSON.stringify(arg))*/

  //socket.emit('resetAccount');//Pour remettre tout les comptes "availaibles" et avec 10 balles dessus

  //Pour NewCustomerRegister
  /*arg = {"id_client": 3};//Exemple ton utilisateur a l'id -> 3
  socket.emit("NewCustomerRegister", JSON.stringify(arg));//réponse sur newBankId


  //Pour MoneyOnAccount
  arg = {"id_client": 3, "id_obp": 119}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));

  arg = {"id_client": 3, "id_obp_sender": 119, "id_receiver": 4, "id_obp_receiver": 118, "amount" : 2}
  socket.emit('doSandTransaction', JSON.stringify(arg));//arg1 -> Compte qui envoie les sous arg2 -> Compte qui les recoit, arg3 -> montant

  arg = {"id_client": 3, "id_obp": 119}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));
  arg = {"id_client": 3, "id_obp": 118}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));*/

  /*arg = {"id_client": 3, "id_obp_sender": 3, "id_obp_receiver": 4, "name": "TestMerge", "description": "TestMerge"};
  socket.emit("addCounterpartie", JSON.stringify(arg));*/
  //arg = {"id_client": 3, "id_obp": 3}
  //socket.emit("getExistCounterparties", JSON.stringify(arg))
  //arg = {"barrecode": 3249760011063};
  //socket.emit("getProductByBarreCode", JSON.stringify(arg))


  /*arg = {"id_client": 3, "id_obp": 3}
  socket.emit("getExistCounterparties", JSON.stringify(arg))*/

  /*arg = {"id_client": 3, "id_obp_sender": 3, "id_receiver": 1, "id_counterparty": "817464da-5835-41f7-8574-92fc0ecf3942",
  "amount": 3000, "message": "Test depuis le client node"};
  socket.emit("doCounterpartyTransaction", JSON.stringify(arg));*/
  /*arg = {"id_obp": 3, "challenge_type": "COUNTERPARTY", "id_transaction": "3b536d94-c9a5-4fb0-8f20-c10b9aa500c0",
  "id_challenge": "c340fe12-4c28-4656-8ce1-4e38bbc7f1c8"}
  socket.emit("validateChallenge", JSON.stringify(arg))*/
 });

//OLD
/*socket.on('connect', function () {
  console.log('client Connected to server');

  //socket.emit('resetAccount');//Pour remettre tout les comptes "availaibles" et avec 10 balles dessus

  //Pour NewCustomerRegister
  //arg = {"id_client": 3};//Exemple ton utilisateur a l'id -> 3
  //socket.emit("NewCustomerRegister", JSON.stringify(arg));//réponse sur newBankId


  //Pour MoneyOnAccount
  arg = {"id_client": 3, "id_obp": 3}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));

  //arg = {"id_client": 3, "id_obp_sender": 119, "id_receiver": 4, "id_obp_receiver": 118, "amount" : 2}
  //socket.emit('doSandTransaction', JSON.stringify(arg));//arg1 -> Compte qui envoie les sous arg2 -> Compte qui les recoit, arg3 -> montant

  arg = {"id_client": 3, "id_obp": 3}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));
  arg = {"id_client": 3, "id_obp": 3}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));

  console.log("je suis dans askInfoArticle")
  arg = {"id_client": 3, "code_barre": "3560070820542", "nsp":"je sais pas"}
  console.log("arg = ")
  console.log(arg)
  retour_a  socket.emit("askInfoArticle", JSON.stringify(arg));

  console.log("je suis dans doSandTransaction")
  arg = { "id_obp_sender": 118, "id_obp_receiver": 116, item:[{barre_code: "3174780000431", name: 'Grand lait'}, {barre_code: "3560070820542", name: 'Jus dorange'}], amount: 3.56}
  console.log("arg de transaction = ")
  console.log(arg)
  socket.emit("doSandTransaction", JSON.stringify(arg));
})*/

arg = { "id_client": 3, "code_barre": "9782364051645", "nsp":"je sais pas"}
socket.emit("askInfoArticle", JSON.stringify(arg));

//arg = { "id_client": 3, "code_barre": "9782311405606", "nsp": "je sais pas" }
//socket.emit("askInfoArticle", JSON.stringify(arg));

//arg = { "id_client": 3, "code_barre": "9782067138865", "nsp": "je sais pas" }
//socket.emit("askInfoArticle", JSON.stringify(arg));

//arg = { "id_client": 3, "code_barre": "3292070004010", "nsp": "je sais pas" }
//socket.emit("askInfoArticle", JSON.stringify(arg));

//arg = { "id_client": 3, "code_barre": "5000157026231", "nsp": "je sais pas" }
//socket.emit("askInfoArticle", JSON.stringify(arg));

//arg = { "id_client": 3, "code_barre": "3155251209515", "nsp": "je sais pas" }
//socket.emit("askInfoArticle", JSON.stringify(arg));



//En DESSOUS VERSION CONNECT POUR DEMO GUILLAUME
//socket.on('connect', function () {
  //console.log('client Connected to server');
  //});
  //arg = {"client_id":"AQ5ewVpC4k1ZGcOfBQCT0lePlGp1athvhlv7WbGeciIILGTvbpHLVhAkZM1Sx6LhZGRlqxe6OEHDOEzz", "client_secret":"ELDNHzCanRTFoYLUDjJjsgzzCdQ9Broh0C49srpQcNYIbvkepmlMFiSXnoX_DlR1tpVfEtb-ymFMT2df", "total":"15", "currency":"EUR", "description":"Voici la desciption de ton 1er achat avec paypal et TrustBudget"}
  //socket.emit("payment_paypal", JSON.stringify(arg));
  /*arg = {"id_client": 3, "id_obp": 3}
  socket.emit("getExistCounterparties", JSON.stringify(arg))*/

  //socket.emit('resetAccount');//Pour remettre tout les comptes "availaibles" et avec 10 balles dessus

  //Pour NewCustomerRegister
  /*arg = {"id_client": 3};//Exemple ton utilisateur a l'id -> 3
  socket.emit("NewCustomerRegister", JSON.stringify(arg));//réponse sur newBankId

  */
 /*
  //Pour MoneyOnAccount
  arg = {"id_client": 3, "id_obp": 1}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));

  arg = {"id_client": 3, "id_obp": 4}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));
*/
//arg = { "id_client": 3, "id_obp_sender": "5d7fc20d62660a0018f788ab", "id_receiver": 12, "id_obp_receiver": 1, item: [{ barre_code: "3174780000431", name: 'Grand lait' }, { barre_code: "3560070820542", name: 'Jus dorange' }], amount: 3.56}
  //socket.emit('doSandTransaction', JSON.stringify(arg));//arg1 -> Compte qui envoie les sous arg2 -> Compte qui les recoit, arg3 -> montant
/*
  arg = {"id_client": 3, "id_obp": 1}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));
  arg = {"id_client": 3, "id_obp": 4}//Id de l'utilisateur dans ton API et son id OBP
  socket.emit("MoneyOnAccount", JSON.stringify(arg));

  /*arg = {"id_client": 3, "id_obp_sender": 4, "id_obp_receiver": 2, "name": "TestMerge", "description": "TestMerge"};
  socket.emit("addCounterpartie", JSON.stringify(arg));*/

  //arg = {"id_client": 3, "id_obp": 4}
  //socket.emit("getExistCounterparties", JSON.stringify(arg))
  //arg = {"barrecode": 3249760011063};
  //socket.emit("getProductByBarreCode", JSON.stringify(arg))


  /*arg = {"id_client": 3, "id_obp": 3}
  socket.emit("getExistCounterparties", JSON.stringify(arg))*/

  /*arg = {"id_client": 3, "id_obp_sender": 4, "id_receiver": 3, "id_counterparty": "78982796-84ec-42f1-ac9a-2ed3a59714e1",
  "amount": 50, "message": "Test depuis le client node"};
  socket.emit("doCounterpartyTransaction", JSON.stringify(arg));
  arg = {"id_obp": 4, "challenge_type": "COUNTERPARTY", "id_transaction": "3b536d94-c9a5-4fb0-8f20-c10b9aa500c0",
  "id_challenge": "c340fe12-4c28-4656-8ce1-4e38bbc7f1c8"}
  socket.emit("validateChallenge", JSON.stringify(arg))*/
 //});


//Syntaxe incorecte bonne syntaxe en dessous
/*socket.on('reconnect_attempt', () => {
  socket.io.opts.transports = ['polling', 'websocket'];
});*/

socket.on('reconnect_attempt', function() {
    socket.io.opts.transports = ['polling', 'websocket'];
});
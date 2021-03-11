# TrustBudget-BigBrother

---

 ### Description :

 Le programme de contrôle Alias: BigBrother utilise plusieurs outils, tels que [Datagram][1], [OpenBankProject][2], [OpenFactFood][3].

 BigBrother est appelé par un serveur *flask_serveur.py* qui communique avec l'API via la techno [flask-socketIO][4].

[1]: <https://rapidapi.com/Datagram/api/products> "Datagram"
[2]: <https://bnpparibas-api.openbankproject.com/> "OpenBankProject"
[3]: <https://fr.openfoodfacts.org/> "OpenFactFood"
[4]: <https://github.com/miguelgrinberg/Flask-SocketIO> "FlaskSocketIO"

**!!! Pour Datagram, seul 15 requêtes par jours sont gratuites !!!**

---

### Instructions installation: 

#### Serveur: 

##### Requis:

Python 3 *[Python3 téléchargement](https://www.python.org/downloads/)*
 
Pip3 *[Installer Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)*

###### (Ensuite)

*A la racine du dossier, executer `sudo pip3 install -r requirements.txt`*
    
#### Client:

##### Requis:

NodeJs & npm *[Comment installer ?](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04)*

###### (Ensuite)

*Se rendre dans le dossier client*

*`sudo npm install package.json`*


---

### Tester le client et le serveur

#### Serveur :

`Python3 flask_serveur.py`
    
#### Client :

`node client.js`
    
**!!! Pour tester il est important de lancer le serveur avant le client, sinon cela ne marchera pas!!!**




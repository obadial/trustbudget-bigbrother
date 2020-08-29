#INFO FOR LOGIN CONNECTION // To the OBPBNP Account and the API PUBLIC AND SECRET KEY
#USERNAME = 'alban'
#PASSWORD = 'XXflp634RY9XXalban'

#CONSUMER_KEY = 'dr55hvbepz4uhsq4as5fxhlzp31fly05cpdajed4'
#CONSUMER_SECRET = 'o2r1u3wjacu2xg5td2ol5n2a3tpwnkcywvatce3o'

#INFO FOR LOGIN CONNECTION // To the OBPFR Account and the API PUBLIC AND SECRET KEY
USERNAME = 'trustbudget'
PASSWORD = 'XXflp634RY9XXalban'

CONSUMER_KEY = 'hitgs2l0f5ghp1yxynqxipxrcm1jele040txks5e'
CONSUMER_SECRET = 'kargjwcn0bckkkf3md52aqaekpoio3qdidt5s1sl'


# URL you are redirected to when OAuth has succeeded. Doesn't need to exist for
# the example scripts.
REDIRECT_URL = 'http://eip.epitech.eu/2020/trustbudget'

# API SERVER URL
#BASE_URL = "https://bnpparibas-api.openbankproject.com"
BASE_URL = "https://apisandbox.openbankproject.com"

#API_VERSION  = "v2.0.0"
API_VERSION  = "v3.1.0"
BASE_URL_OA = '{}/obp/{}'.format(BASE_URL, API_VERSION)

#API USER URL
# For the current user (hack)
USER_URL = '{}/obp/{}/users/current'.format(BASE_URL, API_VERSION)

# Our currency to use
OUR_CURRENCY = 'EUR'# 'GBP'

# Affiche message de connexion
LOGGING = True
# The Direct Connection Token
DC_TOKEN    = { 'Authorization' : 'DirectLogin token=' }

CONTENT_JSON  = { 'content-type'  : 'application/json' }

# My bank we want to send money from
#MY_BANK = 'bnpparibas.07.fr'
MY_BANK = 'gh.29.fr'

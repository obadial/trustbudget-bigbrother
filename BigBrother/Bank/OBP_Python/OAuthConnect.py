#This 2 modules are install by pip
from requests_oauthlib import OAuth1Session
from six.moves import input

from BigBrother.Bank.OBP_Python.default import BASE_URL, REDIRECT_URL, CONSUMER_SECRET, CONSUMER_KEY

OAUTH_BASE = '{}/oauth'.format(BASE_URL)

def get_api():
    """Initiates the OAuth authorisation returns an API session object"""
    request_token_url = '{}/initiate'.format(OAUTH_BASE)
    authorization_url = '{}/authorize'.format(OAUTH_BASE)
    access_token_url = '{}/token'.format(OAUTH_BASE)

    # initiate Oauth by fetching request token
    api = OAuth1Session(
        CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri=REDIRECT_URL)
    #api = OAuth1Session(
        #CLIENT_KEY, client_secret=CLIENT_SECRET, callback_uri=REDIRECT_URL)
    api.fetch_request_token(request_token_url)

    # ask user to visit authorization URL and paste response
    authorization_url = api.authorization_url(authorization_url)
    print('Please visit this URL and authenticate/authorise:')
    print(authorization_url)
    redirect_response = input('Paste the full redirect URL here: ')

    # parse authorization response (contains callback_uri) and access token
    api.parse_authorization_response(redirect_response.strip())
    api.fetch_access_token(access_token_url)
    return api

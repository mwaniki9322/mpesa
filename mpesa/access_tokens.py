import requests
import keys
from requests.auth import HTTPBasicAuth


#genarate access tokens
def generate_access_tokens():
    consumer_key=keys.consumer_key
    consumer_secret=keys.consumer_secret 
    api_url = (
        "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    )
    r=requests.get(api_url,auth=HTTPBasicAuth(consumer_key,consumer_secret))


    json_response=r.json()


    #extract access token from a key pair value
    my_access_token=json_response['access_token']

    return my_access_token


import requests
import keys
from requests.auth import HTTPBasicAuth
from access_tokens import generate_access_tokens




my_access_token=generate_access_tokens()




def register_url():
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    headers= {'Authorization':'Bearer %s'%my_access_token}
    request={
    "ShortCode": "600986",
    "ResponseType": "Completed",
    "ConfirmationURL": "https://mydomain.com/confirmation",
    "ValidationURL": "https://mydomain.com/validation_url"
    }

    response = requests.post(api_url,json=request,headers=headers)
    print(response.text)

# register_url()




def simulate_c2b_transaction():
    access_token = my_access_token
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
    headers= {'Authorization':'Bearer %s'%access_token}
    request={
        "ShortCode":keys.short_code,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":keys.test_msisdn,
        "BillRefNumber":"12345678"
    }

    response = requests.post(api_url,json=request,headers=headers)
    print(response.text)

simulate_c2b_transaction()
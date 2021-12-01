
import requests
from requests.api import request
from requests.auth import HTTPBasicAuth
import keys
from access_tokens import generate_access_tokens
from encode import generate_password
from utils import get_timestamp



#request query
def lipa_na_mpesa():
    my_access_token = generate_access_tokens()
    formatted_time =get_timestamp()
    decoded_password=generate_password(formatted_time)
    
    access_token = my_access_token
    api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {'Authorization':'Bearer %s' %access_token}
    request={
       "BusinessShortCode": keys.business_shortcode,
       "Password": decoded_password,
       "Timestamp": formatted_time,
       "TransactionType": "CustomerPayBillOnline",
       "Amount": "1",
       "PartyA": keys.phone_number,
       "PartyB": keys.business_shortcode,
       "PhoneNumber": keys.phone_number,
       "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
       "AccountReference": "123456",
       "TransactionDesc": "school fees"
    };

    response = requests.post(api_url,json=request,headers=headers)
    print(response.text)

lipa_na_mpesa()

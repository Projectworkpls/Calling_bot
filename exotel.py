import os
import requests

EXOTEL_SID = os.environ.get('EXOTEL_SID')
EXOTEL_TOKEN = os.environ.get('EXOTEL_TOKEN')
EXOTEL_NUMBER = os.environ.get('EXOTEL_NUMBER')

def make_call(to_number, webhook_url):
    url = f'https://{EXOTEL_SID}:{EXOTEL_TOKEN}@api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect.json'
    data = {
        'From': to_number,
        'To': to_number,  # Caller's number
        'CallerId': EXOTEL_NUMBER,
        'Url': webhook_url  # This is where Exotel sends call events (your backend/Voiceflow bridge)
    }
    resp = requests.post(url, data=data)
    return resp.json()

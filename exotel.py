import os
import requests

EXOTEL_SID = os.environ.get('EXOTEL_SID')
EXOTEL_TOKEN = os.environ.get('EXOTEL_TOKEN')
EXOTEL_NUMBER = os.environ.get('EXOTEL_NUMBER')

def make_call(to_number, webhook_url):
    try:
        url = f'https://{EXOTEL_SID}:{EXOTEL_TOKEN}@api.exotel.com/v1/Accounts/{EXOTEL_SID}/Calls/connect.json'
        data = {
            'From': EXOTEL_NUMBER,
            'To': to_number,
            'CallerId': EXOTEL_NUMBER,
            'Url': webhook_url
        }
        resp = requests.post(url, data=data)
        print('Exotel API call status:', resp.status_code)
        print('Exotel API response:', resp.text)
        resp.raise_for_status()  # Raise error for bad status codes
        return resp.json()
    except Exception as e:
        print('Error calling Exotel API:', e)
        raise e

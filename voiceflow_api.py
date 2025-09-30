import os
import requests

VOICEFLOW_PROJECT_ID = os.environ.get('VOICEFLOW_PROJECT_ID')
VOICEFLOW_API_KEY = os.environ.get('VOICEFLOW_API_KEY')

def interact(user_id, payload=None):
    url = f'https://general-runtime.voiceflow.com/state/{VOICEFLOW_PROJECT_ID}/user/{user_id}/interact'
    headers = {
        "Authorization": VOICEFLOW_API_KEY,
        "Content-Type": "application/json"
    }
    data = payload if payload is not None else {"request": {"type": "launch"}}
    resp = requests.post(url, json=data, headers=headers)
    return resp.json()

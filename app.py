import os
from flask import Flask, request, jsonify, abort
from exotel import make_call
from voiceflow_api import interact
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SECRET = os.environ.get('CALLBOT_WEBHOOK_SECRET')

@app.route('/start-call', methods=['POST'])
def start_call():
    data = request.json
    to_number = data.get('to')
    webhook_url = data.get('webhook_url')  # This should be your /call-events handler endpoint
    call_response = make_call(to_number, webhook_url)
    return jsonify(call_response)

@app.route('/call-events', methods=['POST'])
def call_events():
    # Verify webhook secret for security
    if request.headers.get('X-Webhook-Secret') != SECRET:
        abort(403)
    event = request.json

    # Extract caller/session unique ID for Voiceflow state
    user_id = str(event.get('CallSid') or event.get('call_sid') or 'default')
    # Extract user speech or input from Exotel payload
    user_input = event.get('SpeechResult') or event.get('input') or None

    # Compose Voiceflow request payload
    if user_input:
        payload = {"request": {"type": "text", "payload": user_input}}
    else:
        payload = None

    # Interact with Voiceflow API to get next bot response
    vf_response = interact(user_id, payload)
    message = ""
    if vf_response and 'trace' in vf_response:
        messages = [t.get('payload', {}).get('message') 
                    for t in vf_response['trace'] 
                    if t.get('type') == 'text']
        if messages:
            message = messages[0]

    # Respond to Exotel accordingly (format depends on Exotel needs)
    return jsonify({"response": message})

if __name__ == "__main__":
    app.run(port=5000)

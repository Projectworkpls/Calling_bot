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
    try:
        data = request.json
        to_number = data.get('to')
        webhook_url = data.get('webhook_url')
        if not to_number or not webhook_url:
            return jsonify({"error": "Missing 'to' or 'webhook_url'"}), 400

        call_response = make_call(to_number, webhook_url)
        return jsonify(call_response)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500

@app.route('/call-events', methods=['POST'])
def call_events():
    # your code here
    pass

@app.route('/', methods=['GET'])
def home():
    return "Callbot is running!"

if __name__ == "__main__":
    app.run(port=5000)

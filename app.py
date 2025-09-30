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
    # your code here
    pass

@app.route('/call-events', methods=['POST'])
def call_events():
    # your code here
    pass

@app.route('/', methods=['GET'])
def home():
    return "Callbot is running!"

if __name__ == "__main__":
    app.run(port=5000)

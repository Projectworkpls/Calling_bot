import requests

url = "https://calling-bot.onrender.com/start-call"

payload = {
    "to": "+919663192931",  # Replace with the phone number you want to call, with country code
    "webhook_url": "https://calling-bot.onrender.com/call-events"  # Your backend webhook to handle call events
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())


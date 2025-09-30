# Voiceflow Callbot with Exotel

1. Clone this repo and set up Python virtual environment.
2. Fill the `.env` with Exotel and Voiceflow API credentials.
3. Deploy this Flask app publicly (for example, on Render, Heroku, or any VPS).
4. In Voiceflow: Set the call events webhook as `https://your-domain.com/call-events`
5. To initiate calls (optionally), POST `{ "to": "<target_number>", "webhook_url": "https://your-domain.com/call-events" }` to `/start-call`

This connects Exotel calls to your Voiceflow bot runtime via webhooks, enabling IVR and phone conversation flow as designed on Voiceflow.

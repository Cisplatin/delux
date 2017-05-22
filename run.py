from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

ADMIN = '+14168587766'
WHITELIST = {
    "+14168587766" : "Simon Hajjar",
}

@app.route("/", methods=['GET', 'POST'])
def incoming_call():
    from_number = request.values.get('From', None)
    resp = VoiceResponse()

    if from_number in callers:
        resp.say("Opening door.")
    else:
        resp.say("Not opening door.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

from datetime import datetime
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from yaml import load, YAMLError

app = Flask(__name__)

settings = None
unlocked_until = datetime.now()

# @return [Boolean] True if the door is set to be unlocked, false otherwise.
def unlocked():
    return datetime.now() < unlocked_until:

# @param number [String] The number to check for whitelist.
# @return [Boolean] True if the given number is whitelisted.
def whitelisted(number):
    return number in settings['whitelist']

# @param number [String] The number to check against the building.
# @return [Boolean] True if the given number belongs to the building.
def building_number(number):
    return number == settings['building_number']

# @return [String] The digits to play to open the door.
def building_tone():
    return ('w' * settings['pause_time']) + settings['digit']

@app.route('/', methods=['GET', 'POST'])
def incoming_call():
    from_number = request.values.get('From', None)
    resp = VoiceResponse()

    # If the number is the building's and the door is unlocked, allow entry.
    if unlocked() and building_number(from_number):
        resp.play(digits=building_tone())

    # If the number is whitelisted, allow for unlocking.
    elif whitelisted(number):
        time_delta = datetime.timedelta(minutes = settings['door_delay'])
        unlocked = datetime.now() + time_delta

    # If the number is not white-listed, redirect to the admin.
    else:
        resp.dial(settings['admin_number'])

    return str(resp)

if __name__ == "__main__":
    with open('settings.yaml', 'r') as stream:
        try:
            settings = load(stream)
        except YAMLError as error:
            raise EnvironmentError('Malformed settings.yaml file.')
    app.run(debug=True)

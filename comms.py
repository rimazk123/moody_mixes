# Download the helper library from https://www.twilio.com/docs/python/install
import requests
import json
from vision import get_face_emotions
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
DOWNLOAD_DIR = './images'

@app.route("/sms", methods=['GET', 'POST'])
def mms_reply():
	"""Respond to incoming with a simple text message."""
	resp = MessagingResponse()
	res = {}

	if request.values['NumMedia'] != '0':

		# Use the message SID as a filename.
		filename = request.values['MessageSid']  + '.png'
		with open('{}/{}'.format(DOWNLOAD_DIR, filename), 'wb') as f:
			image_url = request.values['MediaUrl0']
			f.write(requests.get(image_url).content)

		res = get_face_emotions(filename)
		print(json.dumps(res))
		resp.message(json.dumps(res))
	else:
		resp.message("Try sending a picture message.")

	
	
	return str(resp)


if __name__ == "__main__":
    app.run(debug=True)

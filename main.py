import requests
import json
from vision import get_face_emotions
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from query import get_playlist
import random
import base64

app = Flask(__name__)
DOWNLOAD_DIR = './images'

search_map = {
	'sorrow' : ['sad boi hours', 'feeling low', 'fuck life'],
	'joy' : ['joyful songs', 'bangers', 'hype up'],
	'anger' : ['Mood: Anger', 'fuck off'],
	'surprise' : ['haydn symphony 94']
}


@app.route("/sms", methods=['GET', 'POST'])
def mms_reply():
	"""Respond to incoming with a simple text message."""
	resp = MessagingResponse()
	res = {}

	# If there is an image sent
	if request.values['NumMedia'] != '0':

		image_url = request.values['MediaUrl0']
		data = requests.get(image_url).content
		
		# Read faces from image 
		res = get_face_emotions(data)
		maxValue = list(res.values())[0]
		emo = list(res.keys())[0]
		
		# Get highest emotion
		for emotion in res.keys():
			if res[emotion] > maxValue:
				emo = emotion
				maxValue = res[emotion]
			
		search_list = search_map[emo][:]

		# Pick search query		
		num = random.randint(0, len(search_list) - 1)
		print(search_list, num)
		search_query = search_list[num]
		
		# Respond with a message
		resp.message(get_playlist(search_query))

	# No message detected
	else:
		resp.message("Try sending a picture message.")
	
	return str(resp)



if __name__ == "__main__":
    app.run(debug=False)

import requests
import json

# Upload an image first & detect whether it is Not Suitable for Work (NSFW)
# https://pixlab.io/#/cmd?id=nsfw

req = requests.post('https://api.pixlab.io/nsfw',
	files = {'file': open('local_image.png', 'rb')},
	data={
		'key':'PIXLAB_API_KEY', # Get your API key from the console at: https://console.pixlab.io
	}
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("NSFW Score: "+ str(reply['score']))

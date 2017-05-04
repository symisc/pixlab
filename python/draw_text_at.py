import requests
import json

# Draw some funny text at the specified offset on the famous Michael Jordan crying face.
# https://pixlab.io/#/cmd?id=drawtextat && https://pixlab.io/#/cmd?id=drawtext for more info.

req = requests.get('https://api.pixlab.io/drawtextat',params={
	'img': 'https://pixlab.io/images/jdr.jpg',
	'text': 'monday morning mood',
	'x':75,
        'y':150,
	'cap':True, # Capitalize text,
	'strokecolor': 'black',
	'key':'Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Meme: "+ reply['link'])

import requests
import json
# Draw some funny text on top & button of the famous Michael Jordan crying face.
# https://pixlab.io/#/cmd?id=drawtext is the target command
req = requests.get('https://api.pixlab.io/drawtext',params={
	'img': 'https://pixlab.io/images/jdr.jpg',
	'top': 'someone bumps the table',
	'bottom':'right before you win',
	'cap':True, # Capitalize text,
	'strokecolor': 'black',
	'key':'Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Meme: "+ reply['link'])

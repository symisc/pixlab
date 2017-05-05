# Composite a static image on top of a this GIF which should be displayed starting from the frame number 5
# If you want to composite multiple images, the use the 'merge' command instead.

import requests
import json

# https://pixlab.io/#/cmd?id=gifcomposite

gif = 'http://i.stack.imgur.com/h8Hjm.gif'
#Static images to be displayed starting from frame 5
static = 'http://i.stack.imgur.com/WFr1K.png'

req = requests.get('https://api.pixlab.io/gifcomposite',params={
	'img': gif,
	'composite': static,
        'x':10,
	'y':30,
	'frame': 5, #Display the result starting from frame number 5
	'key':'Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("GIF location: "+ reply['link'])

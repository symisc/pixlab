import requests
import json

# Convert JPEG image to PNG with transparent background.
# https://pixlab.io/#/cmd?id=convert for more info.

req = requests.get('https://api.pixlab.io/convert',params={
	'img':'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
	'export': 'png',
	'background':'tr',
	'key':'Pix_Key'
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    print ("Pic Link: "+ reply['link'])

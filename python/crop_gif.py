import requests
import json

# Extracts a region from each frame of a given GIF file
# https://pixlab.io/#/cmd?id=cropgif for more info.

req = requests.get('https://api.pixlab.io/cropgif',params={
	'img': 'http://cloud.addictivetips.com/wp-content/uploads/2009/testing.gif',
	'key':'My_PixLab_Key',
	"x":150,
	"y":70,
	"width":256
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("GIF location: "+ reply['link'])

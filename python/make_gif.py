import requests
import json

# Generate GIF from a set of static image
# https://pixlab.io/#/cmd?id=makegif

req = requests.post('https://api.pixlab.io/makegif',headers={'Content-Type':'application/json'},data=json.dumps({
	'key':'My_Pix_Key',
	'frames': [
	{
		"img":"https://cdn1.iconfinder.com/data/icons/human-6/48/266-512.png"
	},
	{
		"img":"https://cdn1.iconfinder.com/data/icons/human-6/48/267-512.png"
	},
	{
		"img":"https://cdn1.iconfinder.com/data/icons/human-6/48/278-512.png"
	},
	{
		"img":"https://cdn1.iconfinder.com/data/icons/human-6/48/279-512.png"
	}
	]
}))
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("GIF location: "+ reply['link'])

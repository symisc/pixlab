import requests
import json

# Resize an image to half its original size hence the 50% field.

req = requests.get('https://api.pixlab.io/scale',params={
	'img': 'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
	'key':'My_Pix_Key',
	"scale":50
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Pic location: "+ reply['link'])

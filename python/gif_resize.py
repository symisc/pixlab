import requests
import json
# Scales a GIF file to the desired dimensions: https://pixlab.io/#/cmd?id=resizegif

req = requests.get('https://api.pixlab.io/resizegif',params={
	'img': 'http://cloud.addictivetips.com/wp-content/uploads/2009/testing.gif',
	'key':'My_PixLab_Key',
	"width":256,
  "height":256,
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("GIF location: "+ reply['link'])

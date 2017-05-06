
import requests
import json

# Rotate this image 180 degree clockwise via https://pixlab.io/#/cmd?id=rotate
img = 'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg'

degree = 180

req = requests.get('https://api.pixlab.io/rotate',params={'img':img,'degree':degree,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    print ("Link to the pic: "+ reply['link'])

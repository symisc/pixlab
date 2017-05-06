import requests
import json

# Simulates an oil painting. Each pixel is replaced by the most frequent color occurring in a circular region defined by radius.
# https://pixlab.io/#/cmd?id=oilpaint

req = requests.get('https://api.pixlab.io/oilpaint',params={'img':'http://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg','radius':3,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    print ("Link to the pic: "+ reply['link'])

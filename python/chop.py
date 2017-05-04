import requests
import json
# Removes a region of an image and collapses the image to occupy the removed portion.
# https://pixlab.io/#/cmd?id=chop for more info.
req = requests.get('https://api.pixlab.io/chop',params={'img':'http://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg','height':20,'x':45,'y':72,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the pic: "+ reply['link'])

import requests
import json

# Convert a given image to gray color model. A grayscale (or graylevel) image is simply one in which the only colors are shades of gray.
# https://pixlab.io/#/cmd?id=grayscale for additional information.

req = requests.get('https://api.pixlab.io/grayscale',params={'img':'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg','key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the grayscaled picture: "+ reply['link'])

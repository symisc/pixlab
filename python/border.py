import requests
import json
# Generate a border with a desired color for a given image.
# https://pixlab.io/#/cmd?id=border for more info.
req = requests.get('https://api.pixlab.io/border',params={
  'img':'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
  'width':20,
  'color':'yellow',
  'key':'My_PixLab_Key'
 })
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    print ("Link to the pic: "+ reply['link'])

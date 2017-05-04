import requests
import json
# Censure the bird picture
# https://pixlab.io/#/cmd?id=blur for more info.
req = requests.get('https://api.pixlab.io/blur',params={
  'img':'https://www.allaboutbirds.org/guide/PHOTO/LARGE/blue_jay_8.jpg',
  'radius':50,
  'sigma':30,
  'key':'My_PixLab_Key'
 })
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the Blurred picture: "+ reply['link'])

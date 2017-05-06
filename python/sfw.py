import requests
import json
# Detect whether a given image is Suitable for Work (SFW)
# https://pixlab.io/#/cmd?id=sfw

req = requests.get('https://api.pixlab.io/sfw',params={'img':'https://i.redd.it/oetdn9wc13by.jpg','key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
elif reply['score'] > 0.5 :
	print ("This image is pretty safe & does not appear to have any adult content!")
else:
    print ("This picture is highly NSFW & may contain adult content, perhaps censure it?")
    #call api.pixlab.io/blur, api.pixlab.io/encrypt to make a censured version of the picture

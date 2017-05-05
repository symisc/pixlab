import requests
import json

# Tag an image based on detected visual content which mean running a CNN on top of it.
# https://pixlab.io/#/cmd?id=tagimg for more info.

# Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the sample set for more info.
img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg' 
# Your PixLab key
key = 'My_PixLab_Key'

# Censure an image based on its NSFW score
req = requests.get('https://api.pixlab.io/tagimg',params={'img':img,'key':key})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    total = len(reply['tags']) # Total tags
    print ("Total tags: "+str(total))
    for tag in reply['tags']:
		print("Tag: "+tag['name']+" - Confidence: "+str(tag['confidence']))

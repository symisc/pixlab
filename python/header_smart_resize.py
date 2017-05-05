import requests
import json

# Check if a given image is of the right size: 800x600 and if not try to resize it.
# The command of interest here are header: https://pixlab.io/#/cmd?id=header & smartresize: https://pixlab.io/#/cmd?id=smartresize
img = 'https://s-media-cache-ak0.pinimg.com/736x/60/aa/e4/60aae45858ab6ce9dc5b33cc2e69baf7.jpg'

key = 'My_PixLab_Key'
# Obtain image metadata at first via header
req = requests.get('https://api.pixlab.io/header',params={'img':img,'key':key})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit()
w = reply['width']
h =  reply['height']
if w > 800 or h > 600:
	print("Resizing image from "+str(w)+"x"+str(h)+" to 800x600...")
	# Invoke smart resize...
	req = requests.get('https://api.pixlab.io/smartresize',params={'img':img,'key':key,'width':800,'height':600})
	reply = req.json()
	if reply['status'] != 200:
		print (reply['error'])
	else:
		print("Resized image: "+reply['link'])
else:
	print("Uploaded image is of the correct size!")

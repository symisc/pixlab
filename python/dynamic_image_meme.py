import requests
import json

# Dynamically create a 300x300 PNG image with a yellow background and draw some text on the center of it later.
# Refer to https://pixlab.io/#/cmd?id=newimage && https://pixlab.io/#/cmd?id=drawtext for additional information.

req = requests.get('https://api.pixlab.io/newimage',params={
	'key':'My_Pix_Key',
	"width":300,
	"height":300,
	"color":"yellow"
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();
# Link to the new image
img = reply['link'];

# Draw some text now on the new image
req = requests.get('https://api.pixlab.io/drawtext',params={
	'img':img, #The newly created image
	'key':'My_Pix_Key',
	"cap":True, #Uppercase
	"color":"black", #Text color
	"font":"wolf",
	"center":"bonjour"
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Pic location: "+ reply['link'])

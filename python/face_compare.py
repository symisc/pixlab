import requests
import json

# Check whether the given faces belong to the same person or not.
# https://pixlab.io/#/cmd?id=facecompare for additional information.
src = 'https://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg'
target = 'https://static01.nyt.com/images/2011/07/31/sunday-review/FACES/FACES-jumbo.jpg'

# Unrelated face
#target = 'https://s-media-cache-ak0.pinimg.com/736x/60/aa/e4/60aae45858ab6ce9dc5b33cc2e69baf7.jpg'

req = requests.get('https://api.pixlab.io/facecompare',params={
	'src': src,
	'target': target,
	'key':'My_Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Same Face: "+ str(reply['same_face']))
    print ("Confidence: "+ str(reply['confidence']))

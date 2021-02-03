import requests
import json

# Generates a set of random pixels. This endpoint is similar to /newimage except that the image contents is filled with random pixels. This is very useful for generating background (negative) samples for feeding Machine Learning training algorithms
req = requests.get('https://api.pixlab.io/pixelgenerate',params={
	'key':'PIXLAB_API_KEY',
	"width":300,
	"height":300
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();
#Link to the newly generated image
print ("Randomly generated image location: "+ reply['ssl_link'])

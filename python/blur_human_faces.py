import requests
import json

imgUrl = 'https://pixlab.io/images/m3.jpg' # Target picture we want to blur any face on

# Detect all human faces in a given image via /facedetect first and blur all of them later via /mogrify.
# https://pixlab.io/cmd?id=facedetect and https://pixlab.io/cmd?id=mogrify for additional information.

req = requests.get('https://api.pixlab.io/facedetect',params={
	'img': imgUrl,
	'key':'PIXLAB_API_KEY',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
print(str(total)+" faces were detected")
if total < 1:
	# No faces were detected, exit immediately
	exit()

# Pass the facial coordinates for each detected face untouched to mogrify 
coordinates = reply['faces']

# Call mogrify & blur the face(s)
req = requests.post('https://api.pixlab.io/mogrify',headers={'Content-Type':'application/json'},data=json.dumps({
	'img': imgUrl,
	'key':'PIXLAB_API_KEY',
	'cord': coordinates # The field of interest
}))
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Blurred Picture URL: "+ reply['ssl_link'])

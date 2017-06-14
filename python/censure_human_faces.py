import requests
import json

img = 'http://anewscafe.com/wp-content/uploads/2012/05/Brave-Faces-Group-shot.jpg' 

# Detect all human faces in a given image via facedetect and censure all of them via mogrify.
# https://pixlab.io/#/cmd?id=facedetect & https://pixlab.io/#/cmd?id=mogrify for additional information.

req = requests.get('https://api.pixlab.io/facedetect',params={
	'img': img,
	'key':'Pix_Key',
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
# Pass the detected faces coordinates untouched to mogrify 
coordinates = reply['faces']

# Call mogrify & proceed to the censure
req = requests.post('https://api.pixlab.io/mogrify',headers={'Content-Type':'application/json'},data=json.dumps({
	'img': img,
	'key':'Pix_Key',
	'cord': coordinates #The field of interest
}))
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Censured pic location: "+ reply['link'])

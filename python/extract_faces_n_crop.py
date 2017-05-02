import requests
import json

# Detect all human faces present in a given image via 'facedetect' and extract each one of them via 'crop'.

# Target image: Feel free to change to whatever image holding as many human faces you want
img = 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg'

req = requests.get('https://api.pixlab.io/facedetect',params={
	'img': img,
	'key':'My_Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
print(str(total)+" faces were detected")
# Extract each face via crop now 
for face in reply['faces']:
	req = requests.get('https://api.pixlab.io/crop',params={
		'img':img,
		'key':'My_Pix_Key',
		'width': face['width'],
		'height': face['height'],
		'x': face['left'],
		'y': face['top']
	})
	reply = req.json()
	if reply['status'] != 200:
		print (reply['error'])
	else:
		print ("Face #"+str(face['face_id'])+" location: "+ reply['link'])

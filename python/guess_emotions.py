import requests
import json


# Detect all human faces present in a given image and try to guess their emotions.
# https://pixlab.io/#/cmd?id=facemotion for additional information

# Target image: Feel free to change to whatever image holding as many human faces you want
img = 'http://www.scienceforums.com/uploads/1282315190/gallery_1625_35_9165.jpg'

req = requests.get('https://api.pixlab.io/facemotion',params={
	'img': img,
	'key':'My_Pixlab_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
print(str(total)+" faces were detected")
# Extract each face via crop now 
for face in reply['faces']:
	cord = face['rectangle']
	print ('Face coordinate: width: ' + str(cord['width']) + ' height: ' + str(cord['height']) + ' x: ' + str(cord['left']) +' y: ' + str(cord['top']))
	print ('Emotion guess')
	for emotion in face['emotion']:
		print (emotion['state']+': '+str(emotion['score']))

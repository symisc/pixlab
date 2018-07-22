import requests
import json


# Detect all human faces present in a given image and
# try to guess their emotions, age and gender.


# Target image: Feel free to change to whatever image holding as many human faces as you want
img = 'http://www.scienceforums.com/uploads/1282315190/gallery_1625_35_9165.jpg'

req = requests.get('http://api.pixlab.io/facemotion',params={
	'img': img,
	'key':'PixLab_API_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
print(str(total)+" faces were detected")
# Extract each face now 
for face in reply['faces']:
	cord = face['rectangle']
	print ('Face coordinate: width: ' + str(cord['width']) + ' height: ' + str(cord['height']) + ' x: ' + str(cord['left']) +' y: ' + str(cord['top']))
	# Guess emotion
	for emotion in face['emotion']:
		if emotion['score'] > 0.5:
			print ("Emotion - "+emotion['state']+': '+str(emotion['score']))
	# Grab the age and gender
	print ("Age ~: " + str(face['age']))
	print ("Gender: " + str(face['gender']))
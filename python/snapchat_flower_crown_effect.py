import requests
import json

# Detect all human faces & extract their landmark regions via facelandmarks & make a small Snapchat filter effect.
# Only three commands are actually needed in order to mimic the Snapchat filters effects:
# face landmarks:         https://pixlab.io/#/cmd?id=facelandmarks
# smart resize:           https://pixlab.io/#/cmd?id=smartresize
# merge:                  https://pixlab.io/#/cmd?id=merge
# Optionally: blur, grayscale, oilpaint, etc. for cool background effects.

img = 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg'

req = requests.get('https://api.pixlab.io/facelandmarks',params={
	'img': img,
	'key':'My_PixLab_Key',
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
print(str(total)+" faces were detected")
snap = []
# Iterate all over the detected faces
for face in reply['faces']:
	cord = face['rectangle']
	# Show the face coordinates 
	print ("Coordinates...")
	print ('\twidth: ' + str(cord['width']) + ' height: ' + str(cord['height']) + ' x: ' + str(cord['left']) +' y: ' + str(cord['top']))
	
	# Show landmarks:
	print ("Landmarks...")
	
	landmarks = face['landmarks']
	
	print ("\tNose: X: "       + str(landmarks['nose']['x'] )     + ", Y: "+str(landmarks['nose']['y']))
	print ("\tBottom Lip: X: " + str(landmarks['bottom_lip']['x'])+ ", Y: "+str(landmarks['bottom_lip']['y']))
	print ("\tTop Lip: X: "    + str(landmarks['top_lip']['x'])   + ", Y: "+str(landmarks['top_lip']['y']))
	print ("\tChin: X: "       + str(landmarks['chin']['x'])      + ", Y: "+str(landmarks['chin']['y']))
	
	print ("\tBone Center: X: "     + str(landmarks['bone']['center']['x'])     + ", Y: "+str(landmarks['bone']['center']['y']))
	print ("\tBone Outer Left: X: " + str(landmarks['bone']['outer_left']['x']) + ", Y: "+str(landmarks['bone']['outer_left']['y']))
	print ("\tBone Outer Right: X: "+ str(landmarks['bone']['outer_right']['x'])+ ", Y: "+str(landmarks['bone']['outer_right']['y']))
	
	print ("\tBone Center: X: " + str(landmarks['bone']['center']['x']) + ", Y: "+str(landmarks['bone']['center']['y']))
	
	print ("\tEye Pupil Left: X: " + str(landmarks['eye']['pupil_left']['x']) + ", Y: "+str(landmarks['eye']['pupil_left']['y']))
	print ("\tEye Pupil Right: X: " + str(landmarks['eye']['pupil_right']['x']) + ", Y: "+str(landmarks['eye']['pupil_right']['y']))
	
	print ("\tEye Left Brown Inner: X: " + str(landmarks['eye']['left_brow_inner']['x']) + ", Y: "+str(landmarks['eye']['left_brow_inner']['y']))
	print ("\tEye Right Brown Inner: X: " + str(landmarks['eye']['right_brow_inner']['x']) + ", Y: "+str(landmarks['eye']['right_brow_inner']['y']))
	
	print ("\tEye Left Outer: X: " + str(landmarks['eye']['left_outer']['x']) + ", Y: "+str(landmarks['eye']['left_outer']['y']))
	print ("\tEye Right Outer: X: " + str(landmarks['eye']['right_outer']['x']) + ", Y: "+str(landmarks['eye']['right_outer']['y']))
	
	# More landmarks on the docs..
	
	# Pick the last face in this loop for the sack of simplicity. Refer to the sample set for a complete example
	snap = face

# Make a quick Snapchat filter on top of the last detected face
if total < 1:
    # No faces were detected
    exit()
# The flower crown to be composited on top of the target face
flower = 'http://data.whicdn.com/images/261686993/original.png'

# Resize the flower crown which is quite big right now to exactly the face width using smart resize.
print ("Resizing the snap flower crown...")
req = requests.get('https://api.pixlab.io/smartresize',params={
	'img':flower,
	'key':'My_PixLab_Key',
	'width': 20 + snap['rectangle']['width'], # Face width
	'height':0 # Let Pixlab decide the best height for this picture
	})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit()
else:
    flower = reply['link']
    
# Finally, Perform the composite operation
print ("Composite operation...")
req = requests.post('https://api.pixlab.io/merge',
	headers={'Content-Type':'application/json'},
	data=json.dumps({
		'src':img,
		'key':'My_PixLab_Key',
		'cord':[
		{
		   'img': flower,
		   'x': snap['rectangle']['left'],
		   'y': snap['rectangle']['top']-45 # Adjust for optimal effect
		}]
	})
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    # Optionally call blur, oilpaint, grayscale for more stuff..
    print ("Snap Filter Effect: "+ reply['link'])

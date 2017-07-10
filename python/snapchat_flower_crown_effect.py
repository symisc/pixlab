import requests
import json

# Detect all human faces & extract their facial landmarks via `facelandmarks`.
# Once done, mimic the famous Snapchat flower crown filter.
# Only three commands are actually needed in order to mimic the Snapchat filters:
# face landmarks:         https://pixlab.io/#/cmd?id=facelandmarks
# smart resize:           https://pixlab.io/#/cmd?id=smartresize
# merge:                  https://pixlab.io/#/cmd?id=merge
# Optionally: blur, grayscale, drawtext, oilpaint, etc. for cool background effects.

# The following is target image that we'll superpose our filter on top of it.
# This image must contain at least one face. free free to change the link to whatever your want.
# Note that you can upload your own images from your app very easily. Refer to the docs for additional info.
img = 'https://ak6.picdn.net/shutterstock/videos/10819841/thumb/8.jpg'

# The flower crown to be composited on top of the target face
flower_crown = 'http://pixlab.xyz/images/flower_crown.png'

# You PixLab API key
key = 'My_PixLab_Key'

# This list contain all the coordinates of the regions where the flower crown should be
# Composited on top of the target face later using the `merge` command.
coordinates = []

# First off, call `facelandmarks` and extract all present faces plus their landmarks.
print ("Detecting and extracting facial landmarks..")
req = requests.get('https://api.pixlab.io/facelandmarks',params={
	'img': img,
	'key': key,
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit();

total = len(reply['faces']) # Total detected faces
if total < 1:
    # No faces were detected
    print ("No faces were detected..exiting")
    exit()

print(str(total)+" faces were detected")

# Iterate all over the detected faces and make our flower crown filter..
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
	
	# More landmarks on the docs..Let's make our flower crown filter now
	
    	
	# Resize the flower crown which is quite big right now to exactly the face width using smart resize.
	print ("Resizing the snap flower crown...")
	req = requests.get('https://api.pixlab.io/smartresize',params={
		'img':flower_crown,
		'key':key,
		'width': 20 + cord['width'], # Face width
		'height':0 # Let Pixlab decide the best height for this picture
		})
	reply = req.json()
	if reply['status'] != 200:
		print (reply['error'])
		exit()
	else:
		fit_crown = reply['link']
	    # Composite the flower crown at the bone center region
        coordinates.append({
		   'img': fit_crown, # The resized crown flower
		   'x': landmarks['bone']['center']['x'],
		   'y': landmarks['bone']['center']['y'] - 10,
		   'center':   True,
		   'center_y': True
        })


# Finally, Perform the composite operation
print ("Composite operation...")
req = requests.post('https://api.pixlab.io/merge',
	headers={'Content-Type':'application/json'},
	data=json.dumps({
		'src':img, # The target image.
		'key':key,
		'cord': coordinates # The coordinates list filled earlier with the resized images (i.e. The flower crown & the dog parts) and regions of interest 
	})
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    # Optionally call blur, oilpaint, grayscale, meme for cool background effects..
    print ("Snap Filter Effect: "+ reply['link'])

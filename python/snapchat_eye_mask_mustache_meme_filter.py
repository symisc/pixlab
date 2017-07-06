import requests
import json

	
# Make an eye mask plus a mustache filter and finally draw some text on the bottom of the image.
# 
# Only three commands are actually needed in order to mimic the Snapchat filters:
# face landmarks:         https://pixlab.io/#/cmd?id=facelandmarks
# smart resize:           https://pixlab.io/#/cmd?id=smartresize
# merge:                  https://pixlab.io/#/cmd?id=merge
# rotate (Optionally):    https://pixlab.io/#/cmd?id=rotate
# meme (Optionally):       https://pixlab.io/#/cmd?id=meme Draw some funny text
# Optionally: blur, grayscale, oilpaint, etc. for cool background effects.

# Target image to composite stuff on. Must contain at least one face.
img = 'http://pixlab.xyz/images/wm.jpg'

# The eye mask.
eye_mask = 'http://pixlab.xyz/images/eye_mask.png'

# The mustache!
mustache  = 'http://pixlab.xyz/images/mustache.png'


# Your PixLab API key
key = 'My_Pix_Key'


# Resize and image (Eye mask, mustache, etc.) to fit the face dimension using smart resize.
def smart_resize(img,width,height):
    print ("Resizing image...")
    req = requests.get('https://api.pixlab.io/smartresize',params={
		'img':img,
		'key':key,
		'width': width,
		'height': height
	})
    reply = req.json()
    if reply['status'] != 200:
        print (reply['error'])
        exit()
    else:
        return reply['link'] # Resized image

# First step, Detect & extract the landmarks for each human face present in the image.
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
    print ("No faces were detected..exiting")
    exit()
	
print(str(total)+" faces were detected")

# This list contain all the coordinates of the regions where the flower crown or the dog part should be
# Composited on the target image later using the `merge` command.
coordinates = []

# Iterate all over the detected faces and make our stuff
for face in reply['faces']:
	
	# Show the face coordinates 
	print ("Coordinates...")
	cord = face['rectangle']
	print ('\twidth: ' + str(cord['width']) + ' height: ' + str(cord['height']) + ' x: ' + str(cord['left']) +' y: ' + str(cord['top']))
	
	# Show landmarks of interest:
	print ("Landmarks...")
	landmarks = face['landmarks']
	print ("\tNose: X: "       + str(landmarks['nose']['x'] )     + ", Y: "+str(landmarks['nose']['y']))
	print ("\tBottom Lip: X: " + str(landmarks['bottom_lip']['x'])+ ", Y: "+str(landmarks['bottom_lip']['y']))
	print ("\tTop Lip: X: "    + str(landmarks['top_lip']['x'])   + ", Y: "+str(landmarks['top_lip']['y']))
	print ("\tChin: X: "       + str(landmarks['chin']['x'])      + ", Y: "+str(landmarks['chin']['y']))
	print ("\tMouth Left: X: "       + str(landmarks['mouth_left']['x'])      + ", Y: "+str(landmarks['mouth_left']['y']))
	print ("\tMouth Right: X: "       + str(landmarks['mouth_right']['x'])      + ", Y: "+str(landmarks['mouth_right']['y']))
	
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
	
	
	# Do the mustache using the top lip coordinates.
	print ("\tMustache...")
	coordinates.append({
		'img': smart_resize(mustache, cord['width']/2,0),
		'x': landmarks['top_lip']['x'], # Adjust to get optimal effect
		'y': landmarks['top_lip']['y'] - 50,  # Adjust to get optimal effect
		'center': True # Composite at the center of the X coordinate.
	})
	# Do the eye mask using the top lip coordinates.
	print ("\tEye Mask...")
	coordinates.append({
		'img': smart_resize(eye_mask, cord['width'],0),
		'x': landmarks['bone']['center']['x'], # Adjust to get optimal effect
		'y': landmarks['eye']['left_brow_inner']['y'],  # Adjust to get optimal effect
		'center': True, # Composite at the center of the X coordinate.
		'center_y': True # Composite at the center of the Y coordinate.
	})

# Finally, Perform the composite operation when we exit the loop
print ("Composite operation...")
req = requests.post('https://api.pixlab.io/merge',
	headers={'Content-Type':'application/json'},
	data=json.dumps({
		'src':img, # The target image.
		'key':key,
		'cord': coordinates # The coordinates list filled earlier with the composited image & regions of interest 
	})
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    snap = reply['link'];
    # Snap created, let's draw some MEME at the bottom of the pic.
    req = requests.get('http://api.pixlab.io/meme',params={
		'img': snap,
		'bottom': 'sounds good?',
		'cap':True, # Capitalize text,
		'strokecolor': 'black',
		'key':key
	})
    reply = req.json()
    if reply['status'] != 200:
  	    print (reply['error'])
    else:
	    print ("Snap Filter + Meme: "+ reply['link'])

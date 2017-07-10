import requests
import json

# Mimic the two famous Snapchat filters: The flower crown & the dog facial parts filter.
# The target image must contain at least one human face. The more faces you got, the more funny it should be!
# 
# Only three commands are actually needed in order to mimic the Snapchat filters:
# face landmarks:         https://pixlab.io/#/cmd?id=facelandmarks
# smart resize:           https://pixlab.io/#/cmd?id=smartresize
# merge:                  https://pixlab.io/#/cmd?id=merge
# rotate (Optionally):    https://pixlab.io/#/cmd?id=rotate
# meme (Optionally):      https://pixlab.io/#/cmd?id=meme for Drawing some funny text
# Optionally: blur, grayscale, oilpaint, etc. for cool background effects.

# Target image to composite stuff on. Must contain at least one face.
img = 'https://trekkerscrapbook.files.wordpress.com/2013/09/face-08.jpg'

# The flower crown.
flower = 'http://pixlab.xyz/images/flower_crown.png'

# The dog facial parts: Left & right ears, nose & optionally the tongue
dog_left_ear  = 'http://pixlab.xyz/images/dog_left_ear.png'
dog_right_ear = 'http://pixlab.xyz/images/dog_right_ear.png'
dog_nose      = 'http://pixlab.xyz/images/dog_nose.png'
dog_tongue    = 'http://pixlab.xyz/images/dog_tongue.png'

# Your PixLab API key
key = 'Your_Pixlab_Key'

# If set to True then composite the flower crown. Otherwise, composite the dog stuff.
draw_crown = False

# Resize an image (Dog facial parts or the flower crown) to fit the face dimension using smartresize.
def smart_resize(img,width,height):
    print ("Resizing filter image...")
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

# This list contain all the coordinates of the regions where the flower crown or the dog facial parts should be
# Composited on top of the target image later using the `merge` command.
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
	
	
	draw_crown = not draw_crown
	if draw_crown:
        # Resize the flower crown to fit the face width
		fit_crown = smart_resize(
			flower,
			cord['width'] + 20, # Face width
			0 # Let Pixlab decide the best height for this picture
		)
		# Composite the flower crown at the bone center region.
		print ("\tCrown flower at: X: " + str(landmarks['bone']['center']['x']) + ", Y: "+str(landmarks['bone']['center']['y']))
		coordinates.append({
		   'img': fit_crown, # The resized crown flower
		   'x': landmarks['bone']['center']['x'],
		   'y': landmarks['bone']['center']['y'] + 5,
		   'center':   True,
		   'center_y': True
		})
	else:
		# Do the dog facial parts using the bone left & right regions and the nose coordinates.
		print ("\tDog Facial Parts...")
		coordinates.append({
			'img': smart_resize(dog_left_ear, cord['width']/2,cord['height']/2),
			'x': landmarks['bone']['outer_left']['x'], # Adjust to get optimal effect
			'y': landmarks['bone']['outer_left']['y']  # Adjust to get optimal effect
		})
		coordinates.append({
			'img': smart_resize(dog_right_ear, cord['width']/2,cord['height']/2),
			'x': landmarks['bone']['outer_right']['x'], # Adjust to get optimal effect
			'y': landmarks['bone']['outer_right']['y']  # Adjust to get optimal effect
		})
		coordinates.append({
			'img': smart_resize(dog_nose, cord['width']/2,cord['height']/2),
			'x': landmarks['nose']['x'], # Adjust to get optimal effect
			'y': landmarks['nose']['y'] + 2, # Adjust to get optimal effect
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
    # Optionally call blur, oilpaint, grayscale,meme for cool background effects..
    print ("Snap Filter Effect: "+ reply['link'])

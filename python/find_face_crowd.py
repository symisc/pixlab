import requests
import json

# Find a person face in a crowd or group of people. https://pixlab.io/#/cmd?id=facelookup for additional information.

# This is the target face that we are searching for in the people crowd.
face = 'http://static-secure.guim.co.uk/sys-images/Guardian/Pix/pictures/2012/7/9/1341860104423/obama_face.jpg'
# The people crowd to look on
crowd = 'http://www.acclaimimages.com/_gallery/_free_images/0519-0908-1001-0556_president_barack_obama_walking_with_a_crowd_of_people_o.jpg'

req = requests.get('https://api.pixlab.io/facelookup',params={
	'face': face,
	'crowd': crowd,
	'key':'My_Pix_Key',
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
	found = reply['found'] # Boolean value telling whether we got the face or not
	if found:
		print("Face found with confidence value = "+ str(reply['confidence']))
		rectangle = reply['rectangle'] # Rectangle coordinates of the target face
		print("Face Coordinates: top: "+str(rectangle['top'])+" left: "+str(rectangle['left'])+" width: "+str(rectangle['width'])+" height:"+str(rectangle['height']))
	else:
		print("Face NOT found in the target crowd..picking up the best candidate:")
		best = reply['best']
		rectangle = best['rectangle'] # Rectangle coordinates of the best candidate
		print ("Confidence: "+ str(best['confidence']))
		print ("Best Candidate Coordinates: top: "+str(rectangle['top'])+" left: "+str(rectangle['left'])+" width: "+str(rectangle['width'])+" height:"+str(rectangle['height']))

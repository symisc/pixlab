import requests
import json

# Given a submitted/uploaded, US Driver License image document from any of the 50 US state
# crop the license holder face, and extract all document fields (see below) ready to be consumed by your application.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://pixlab.io/dashboard
# so that any extracted face is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/cmd?id=docscan for additional information.

req = requests.get(
	'https://api.pixlab.io/docscan',params={ # swtich to POST if you want to upload the picture directly
	'img':'https://www.aulicense.com/wp-content/uploads/2020/12/USA-DRIVERS-LICENSE.jpg', # US Driver license input image
	'type':'usdl', # Type of document we are a going to scan, hence US driver license
	'key':'PIXLAB_API_KEY' # Your PixLab API Key - Get yours from https://console.pixlab.io/
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print (f"User Cropped Face: {reply['face_url']}\n")
	print ("Extracted Fields:\n\t")
	# Display all extracted fields from the input US driver license image
	print (f"Issuing Country: {reply['fields']['country']}\n\t")
	print (f"Issuing State: {reply['fields']['issuingState']}\n\t")
	print (f"Issuing State Code: {reply['fields']['issuingStateCode']}\n\t")
	print (f"Full Name: {reply['fields']['fullName']}")
	print (f"License Number: {reply['fields']['licenseNumber']}\n\t")
	print (f"Address: {reply['fields']['address']}\n\t")
	print (f"Date Of Birth: {reply['fields']['dateOfBirth']}\n\t")
	print (f"issuing Date: {reply['fields']['issuingDate']}\n\t")
	print (f"Date Of Expiry: {reply['fields']['expiryDate']}\n\t")
	print (f"Gender: {reply['fields']['gender']}\n\t")

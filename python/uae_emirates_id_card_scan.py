import requests
import json

# Given a government issued ID card from the UAE (emirates). Extract the holder's face and d aisplay all scanned fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://console.pixlab.io/
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/cmd?id=docscan&&country=uae for additional information.

req = requests.get('https://api.pixlab.io/docscan',params={
	'img':'https://pixlab.xyz/images/pixlab-uae-id.jpg', # UAE ID Card Input image (https://pixlab.xyz/images/pixlab-uae-id.jpg). POST method for direct upload is also supported
	'type':'idcard', # We are expecting an ID card
	'country': 'uae', # from the Emirates, we support also Malaysia/India/Singapore/US and Passports
	'key':'PIXLAB_API_KEY' # Your PixLab API key. Get yours from https://console.pixlab.io/
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print (f"ID Card Holder's Face: {reply['face_url']}")
	print ("Scanned ID Card Fields:\n\t")
	if "issuingCountry" in reply['fields']:
		print ("Issuing Country: " + reply['fields']['issuingCountry'])
	if "documentNumber" in reply['fields']:
		print ("Document Number: " + reply['fields']['documentNumber'])
	if "fullName" in reply['fields']:
		print ("Holder Full Name: " + reply['fields']['fullName'])
	if "nationality" in reply['fields']:
		print ("Holder's Nationality: " + reply['fields']['nationality'])

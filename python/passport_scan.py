import requests
import json

# Given a government issued passport document, extract the user face and parse all MRZ fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://pixlab.io/dashboard
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/#/cmd?id=docscan for additional information.

req = requests.get('https://api.pixlab.io/docscan',params={
	'img':'https://i.stack.imgur.com/oJY2K.png', # Passport sample
	'type':'passport', # Type of document we are a going to scan
	'key':'Pixlab_key'
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("User Cropped Face: " + reply['face_url'])
	print ("MRZ Cropped Image: " + reply['mrz_img_url'])
	print ("Raw MRZ Text: " + reply['mrz_raw_text'])
	print ("MRZ Fields: ")
	# Display all parsed MRZ fields
	print ("\tIssuing Country: " + reply['fields']['issuingCountry'])
	print ("\tFull Name: "       + reply['fields']['fullName'])
	print ("\tDocument Number: " + reply['fields']['documentNumber'])
	print ("\tCheck Digit: "   + reply['fields']['checkDigit'])
	print ("\tNationality: "   + reply['fields']['nationality'])
	print ("\tDate Of Birth: " + reply['fields']['dateOfBirth'])
	print ("\tSex: "           + reply['fields']['sex'])
	print ("\tDate Of Expiry: "    + reply['fields']['dateOfExpiry'])
	print ("\tPersonal Number: "   + reply['fields']['personalNumber'])
	print ("\tFinal Check Digit: " + reply['fields']['finalcheckDigit'])

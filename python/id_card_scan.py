import requests
import json

# Given a government issued ID card from Malaysia, Singapore, etc., extract the user face and parse all fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://pixlab.io/dashboard
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/#/cmd?id=docscan for additional information.

req = requests.get('https://api.pixlab.io/docscan',params={
	'img':'https://buletinonline.net/v7/wp-content/uploads/2016/06/Mykad-penghuni-puan-Noraini-2.jpg', # ID Card sample
	'type':'idcard', # We are expecting an ID card
	'country': 'malaysia', # from Malysia. You can use the 'my' country code also
	'key':'PIXLAB_API_KEY' # https://pixlab.io/dashboard
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("User Cropped Face: " + reply['face_url'])
	# print ("Scanned Text: " + reply['full_text'])
	print ("Fields: ")
	# Display all scanned fields
	if "country" in reply['fields']:
		print ("\tIssuing Country: " + reply['fields']['country'])
	if "id" in reply['fields']:
		print ("\tID number: " + reply['fields']['id'])
	if "name" in reply['fields']:
		print ("\tName: " + reply['fields']['name'])
	if "address" in reply['fields']:
		print ("\tAddress: " + reply['fields']['address'])
	if "religion" in reply['fields']:
		print ("\tReligion: " + reply['fields']['religion'])
	if "sex" in reply['fields']:
		print ("\tSex: " + reply['fields']['sex'])
	if "race" in reply['fields']:
		print ("\tRace: " + reply['fields']['race'])
	if "birth" in reply['fields']:
		print ("\tDate of birth: " + reply['fields']['birth'])
	if "birth_country" in reply['fields']:
		print ("\tCountry of birth: " + reply['fields']['birth_country'])
	if "nationality" in reply['fields']:
		print ("\tNationality: " + reply['fields']['nationality'])

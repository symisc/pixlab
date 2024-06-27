import requests
import json


# Scan over 11K ID Documents from over 197 countries using the PixLab DOCSCAN API Endpoint
# documented at: https://ekyc.pixlab.io/docscan
#
# In this example, given a ID document from over 197+ countries, extract the ID holder face and convert/parse all Machine Readable Zone
# to textual content ready to be consumed by your application.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://console.pixlab.io
# so that any extracted face or MRZ crop is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# Refer to the official documentation at: https://ekyc.pixlab.io/docscan for the API reference guide and more code samples.

req = requests.get(
	'https://api.pixlab.io/docscan',
	params={
		'img': 'https://buletinonline.net/v7/wp-content/uploads/2016/06/Mykad-penghuni-puan-Noraini-2.jpg', # ID Card sample
		'type': 'idcard', # We are expecting a Malaysian (MyKAD) ID card
		'country': 'my',  # Malaysia Country Code if known in advance
		'key':'PIXLAB_API_KEY' # Visit https://console.pixlab.io/ to get your API key
	})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("User Cropped Face: " + reply['face_url'])
	print ("Extracted ID Fields:")
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
	if "dateOfBirth" in reply['fields']:
		print ("\tDate of birth: " + reply['fields']['dateOfBirth'])
	if "birth_country" in reply['fields']:
		print ("\tCountry of birth: " + reply['fields']['birth_country'])
	if "nationality" in reply['fields']:
		print ("\tNationality: " + reply['fields']['nationality'])

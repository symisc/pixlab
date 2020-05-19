import requests
import json

# Given a government issued ID card from India (Aadhaar), Malaysia, Singapore, etc., extract the user face and parse all fields.
#
# PixLab recommend that you connect your AWS S3 bucket via your dashboard at https://pixlab.io/dashboard
# so that any cropped face or MRZ crop is stored automatically on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# https://pixlab.io/cmd?id=docscan for additional information.
# Blog Post: https://blog.pixlab.io/2020/03/full-scan-support-for-india-aadhar-id-card

req = requests.get('https://api.pixlab.io/docscan',params={
	'img':'https://currenthunt.com/wp-content/uploads/2019/07/Aadhaar-Card-min.jpg', # Aadhaar ID Card sample
	'type':'idcard', # We are expecting an ID card
	'country': 'india', # from India, we support also Malaysia/Singapore/US and Passports, 
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
	if "sex" in reply['fields']:
		print ("\tGender: " + reply['fields']['sex'])
	if "birth" in reply['fields']:
		print ("\tDate of birth: " + reply['fields']['birth'])

import requests
import json

# Scan over 11K ID Documents from over 197 countries using the PixLab DOCSCAN API Endpoint
# documented at: https://ekyc.pixlab.io/docscan
#
# In this example, given a Passport document, extract the passport holder face and convert/parse all Machine Readable Zone
# to textual content ready to be consumed by your application.
#
# PixLab recommend that you connect your AWS S3 bucket via the dashboard at https://console.pixlab.io
# so that any extracted face or MRZ crop is automatically stored on your S3 bucket rather than the PixLab one.
# This feature should give you full control over your analyzed media files.
#
# Refer to the official documentation at: https://ekyc.pixlab.io/docscan for the API reference guide and more code samples.

req = requests.post('https://api.pixlab.io/docscan',
  files = {'file': open('./local_passport_image.png', 'rb')},
  data={
  'type':'passport', # Type of document we are a going to scan,
  'key':'PIXLAB_API_KEY' # PixLab API Key - Get yours from https://console.pixlab.io/'
})
reply = req.json()
if reply['status'] != 200:
  print (reply['error'])
else:
  print ("User Cropped Face: " + reply['face_url'])
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

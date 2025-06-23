
import requests
import json

# Generate a natural language description of an image content using the 
# https://pixlab.io/endpoints/describe API endpoint

# Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the REST API code samples for more info.
img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg' 

key = 'PIXLAB_API_KEY' # Get your API key from https://console.pixlab.io/

req = requests.get('https://api.pixlab.io/describe',params={
  'img':img,
  'key':key,
  'lang':'english',
  'short':False
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
  description = reply['description']
  print(f"Natural language content description: {description}")



import requests
import json

# Get natural language responses to image-related queries

# Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the REST API code samples for more info.
img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg' 

key = 'PIXLAB_API_KEY' # Get your API key from https://console.pixlab.io/

req = requests.get('https://api.pixlab.io/query',params={
  'img':img,
  'key':key,
  'lang':'english',
  'query':'What does this image depict? Can you guess the location where it was taken?'
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
  response = reply['response']
  print(f"Query Response: {response}")

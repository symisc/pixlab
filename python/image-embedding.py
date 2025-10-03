import requests
import json

# Generate image embedding vector for a given image using the PixLab image embedding API
# Refer to: https://pixlab.io/endpoints/img-embed for the official documentation.
#
# Convert images into numerical vectors for efficient image classification, similarity search, and so on.

# Target Image we want to generate embedding for
# Change to any link or switch to POST if you want to upload your image directly.
img = 'https://pixlab.io/assets/images/nature31.jpg' 

key = 'PIXLAB_API_KEY' # Get your API key from https://console.pixlab.io/

# Make the API call; Switch to POST if you want to upload your image directly.
req = requests.get('https://api.pixlab.io/imgembed',params={
  'img': img,
  'key': key,
  'dimension': 1024, # Output vector dimension
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
  embedding = reply['embedding']
  print(f"Image embedding vector: {embedding}")

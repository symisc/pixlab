import requests
import json

# Upload a local media file to the remote https://pixlab.xyz storage server or your own S3 bucket depending on the configuration on your PixLab dashboard.
# Use the output link for other purposes such as processing via mogrify, drawrectangles, etc. or simply serving content.
# https://pixlab.io/cmd?id=store for more info.

req = requests.post('http://api.pixlab.io/store', # Switch to http:// for fast upload
	files = {'file': open('./local_image.png', 'rb')},
	data={
		'comment':'Super Secret Stuff',
		'key': 'PIXLAB_API_KEY' # PixLab API Key - Get yours from https://pixlab.io/dashboard
	}
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Upload Pic Link: "+ reply['link'])

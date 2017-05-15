import requests
import json

# Upload a local image to the remote https://pixlab.xyz storage server or your own S3 bucket depending on the configuration from your dashboard.
# Use the output link for other purposes such as processing via mogrify, drawrectangles, etc. or simply serving content.
# https://pixlab.io/#/cmd?id=store for more info.

req = requests.post('https://api.pixlab.io/store',
	files = {'file': open('./local_image.png', 'rb')},
	data={
		'comment':'Super Secret Stuff',
		'key':'My_Pix_Key',
	}
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Upload Pic Link: "+ reply['link'])

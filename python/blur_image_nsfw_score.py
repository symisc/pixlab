import requests
import json

# Target Image: Change to any link (Possibly adult) you want or switch to POST if you want to upload your image directly, refer to the sample set for more info.
img = 'https://i.redd.it/oetdn9wc13by.jpg' 
# Your PixLab API Key. Obtain from https://pixlab.io/dashboard
key = 'PIXLAB_API_KEY'

# Censor an image according to its NSFW score
req = requests.get('https://api.pixlab.io/nsfw',params={'img':img,'key':key})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
elif reply['score'] < 0.5 :
	print ("No adult content were detected on this picture")
else:
	# Highly NSFW picture
	print ("Censoring NSFW picture...")
	# Call blur with the highest possible radius and sigma
	req = requests.get('https://api.pixlab.io/blur',params={'img':img,'key':key,'rad':50,'sig':30})
	reply = req.json()
	if reply['status'] != 200:
		print (reply['error'])
	else:
		print ("Blurred Image URL: "+ reply['link'])

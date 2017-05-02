import requests
import json

# Target Image: Change to any link (Possibly adult) you want or switch to POST if you want to upload your image directly, refer to the sample set for more info.
img = 'https://i.redd.it/oetdn9wc13by.jpg' 
# Your PixLab key
key = 'Pixlab_Key'

# Censure an image based on its NSFW score
req = requests.get('https://api.pixlab.io/nsfw',params={'img':img,'key':key})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
elif reply['score'] < 0.5 :
    print ("No adult content were detected on this picture")
else:
	# Highly NSFW picture
	print ("Censuring NSFW picture...")
	# Call blur with the highest possible radius and sigma
	req = requests.get('https://api.pixlab.io/blur',params={'img':img,'key':key,'rad':50,'sig':30})
	reply = req.json()
	if reply['status'] != 200:
		print (reply['error'])
	else:
		print ("Censured image: "+ reply['link'])

import requests
import json

# Extract a screen capture from a given website
website = 'https://sqlite.org'

key = 'My_PixLab_Key'

req = requests.get('https://api.pixlab.io/screencapture',params={'url':website,'key':key}) # Specify the desired width & height if you want to
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("The Website screen capture is located on: " + reply['link'])

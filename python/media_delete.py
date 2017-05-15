import requests
import json
# Generate an oilpaint pic and then delete it
req = requests.get('https://api.pixlab.io/oilpaint',params={'img':'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg','radius':3,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
	exit()
print ("Deleting: "+ reply['link'] +"...")
req = requests.get('https://api.pixlab.io/delete',params={'link':reply['link'],'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Deletion succeed")

# Extract Jeremy's face. The rectangle coordinates were obtained from the facedetect command and passed untouched to this command. 
# Refer to https://pixlab.io/#/cmd?id=crop for additional information.

import requests
import json

req = requests.get('https://api.pixlab.io/crop',params={
	'img': 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg',
	'key':'My_PixLab_Key',
	"x":164,
	"y":95,
	"width":145,
	"height":145
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Face location: "+ reply['link'])

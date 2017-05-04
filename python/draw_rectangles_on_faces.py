# Mark Jeremy's face by drawing a rectangle on it. The rectangle coordinates was obtained from the facedetect command and passed untouched to this command. 
# Refer to the command page https://pixlab.io/#/cmd?id=drawrectangles for more info.

import requests
import json

req = requests.post('https://api.pixlab.io/drawrectangles',headers={'Content-Type':'application/json'},data=json.dumps({
	'img': 'http://cf.broadsheet.ie/wp-content/uploads/2015/03/jeremy-clarkson_3090507b.jpg',
	'key':'My_PixLab_Key',
	'cord': [
	{
		"x":164,
		"y":95,
		"width":145,
		"height":145,
		#"color":"green"
	}
	]
}))
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Pic location: "+ reply['link'])

import requests
import json

# Composite two smiley on top of the famous Michael jordan crying face.
# A more sophisticated approach would be to extract the face landmarks using facelandmarks and composite something on the different regions.
# https://pixlab.io/#/cmd?id=merge for more info.

req = requests.post('https://api.pixlab.io/merge',
	headers={'Content-Type':'application/json'},
	data=json.dumps({
		'src':'https://pbs.twimg.com/media/CcEfpp0W4AEQVPf.jpg',
		'key':'My_Pix_Key',
		'cord':[
		{
		   'img': 'http://www.wowpng.com/wp-content/uploads/2016/10/lol-troll-face-png-image-october-2016-370x297.png',
		   'x': 30,
		   'y': 320
		},
		{
		   'img': 'http://orig08.deviantart.net/67d1/f/2010/216/6/7/lol_face_by_bloodyhalfdemon.png',
		   'x': 630,
		   'y': 95
		}]
	})
)
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
	print ("Pic Link: "+ reply['link'])

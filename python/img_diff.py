import requests
import json

# Compute the difference between two images and output the reconstructed image and the diff output.
# Keep in mind that the two images must be of the same size or call 'resize' or 'crop' before to
# fit the images to the same dimension.
# Read more on imgdiff here: https://pixlab.io/#/cmd?id=imgdiff

src = 'https://pixlab.io/images/jdr.jpg' # Source image which is the famous Michael Jordan's crying face.
target = 'https://pixlab.io/images/jdr_draw.jpg' # Target image which is the same Jordan's face but a MEME is drawn on top of it.

req = requests.get('https://api.pixlab.io/imgdiff',params={
	'src': src,
	'target': target,
	'key':'My_Key'
})
reply = req.json()
if reply['status'] != 200:
	print (reply['error'])
else:
    print ("Diff Output: "+str(reply['diff']))
    print ("Reconstructed image link: "+ reply['link'])
	

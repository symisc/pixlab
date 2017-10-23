import requests
import json
# Colorize this 1933 picture of this little girl via: https://pixlab.io/cmd?id=colorize
req = requests.get('https://api.pixlab.io/colorize',params={'img':'https://i.redd.it/7z1q27vaa9tz.png','key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the colorized picture: "+ reply['link'])

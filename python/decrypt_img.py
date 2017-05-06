import requests
import json

# Decrypt a previously encrypted image using the passphrase 'superpass'
# https://pixlab.io/#/cmd?id=encrypt && https://pixlab.io/#/cmd?id=decrypt

# Password used for decryption
pwd = 'superpass'

req = requests.get('https://api.pixlab.io/decrypt',params={'img':'https://pixlab.xyz/wxfnq5886bad496f95.png','pwd':pwd,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the decrypted picture: "+ reply['link'])

import requests
import json

# Converts plain pixels of a given image to enciphered pixels. The image is not readable until it has been deciphered using decrypt.
# https://pixlab.io/#/cmd?id=encrypt && https://pixlab.io/#/cmd?id=decrypt

# Target image to enrypt
img = 'https://pixlab.io/images/bencrypt.png'
# Password used for decryption
pwd = 'superpass'

req = requests.get('https://api.pixlab.io/encrypt',params={'img':img,'pwd':pwd,'key':'My_PixLab_Key'})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the encrypted picture: "+ reply['link'])
    #use https://api.pixlab.io/decrypt with your passphrase to make it readable again

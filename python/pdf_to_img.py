import requests
import json
# Convert a PDF document to JPEG/PNG image via /pdftoimg endpoint - https://pixlab.io/cmd?id=pdftoimg
req = requests.get('https://api.pixlab.io/pdftoimg',params={
  'src':'https://www.getharvest.com/downloads/Invoice_Template.pdf',
  'export': 'jpeg',
  'key':'My_PixLab_Key'
})
reply = req.json()
if reply['status'] != 200:
    print (reply['error'])
else:
    print ("Link to the image output (Converted PDF page): "+ reply['link'])

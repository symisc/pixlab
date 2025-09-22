
import requests
import json
import base64
import os

# Programmatically remove text & watermarks from input images using the PixLab TXT-REMOVE API endpoint.
#
# Refer to the official documentation at: https://pixlab.io/endpoints/text-watermark-remove-api for the API reference
# guide and more code samples.

# Use POST to upload the image directly from your local folder. If your image is publicly available
# then make a simple GET request with a link to your image.
req = requests.post(
    'https://api.pixlab.io/txtremove',
    files={
        'file': open('./local_image.png', 'rb')  # The local image we are going to remove text & watermark from
    },
    data={
        'key': 'PIXLAB_API_KEY'  # PixLab API Key - Get yours from https://console.pixlab.io/'
    }
)
reply = req.json()
if reply['status'] != 200:
    print(reply['error'])
else:
    imgData = reply['imgData']  # Base64 encoding of the output image
    mimetype = reply['mimeType']  # MIME type (i.e image/jpeg, etc.) of the output image
    extension = reply['extension']  # File extension (e.g., 'png', 'jpeg')

    # Decode base64 and save to disk
    try:
        img_bytes = base64.b64decode(imgData)
        output_filename = f"output_image.{extension}"
        with open(output_filename, "wb") as f:
            f.write(img_bytes)
        print(f"Text Removed Image saved to: {output_filename}")
    except Exception as e:
        print(f"Error saving output image: {e}")

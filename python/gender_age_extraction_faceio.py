# Age Verification & Gender Extraction using the FACEIO REST API - https://faceio.net/rest-api#age-check
#
# The age verification API endpoint allows you to verify customer age and gender
# by directly uploading a base64 encoded image of the person being verified. 
# No prior face enrollment is required; Age verification operates directly on the uploaded images.
# This API endpoint expects a single face to be present in the source image being checked.

import requests
import json
import base64

# Load an image from disk and encode it in base64.
def load_image_and_encode(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    mime_type = "image/jpeg"  # Or determine the MIME type dynamically
    return f"data:{mime_type};base64,{encoded_string}"

# Source image we want to exract the face from, and output the gender & age estimation of the target person
source_face_img_path = "path/to/face1.jpg"  # Replace with the actual path to your source face image

payload = {
    "key": "apiKey", # Get your API key from the FACEIO Console at - https://console.faceio.net/
    "img": load_image_and_encode(source_face_img_path), # Face image we want to extract the gender & age from
}

try:
    response = requests.post(
        "https://api.faceio.net/agecheck", # Target API endpoint for static gender & age extraction
        headers={"Content-Type": "application/json"},
        json=payload
    )

    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    print(response.json())
    # JSON Object is always returned
    # {
    #   age: 'Age approximation of the target person',
    #   gender:  'Gender of the target person',
    #   status: 'Status Code'
    # }

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

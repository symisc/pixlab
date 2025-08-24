# Determine if the provided faces represent the same individual or not
# using the FACEIO FACEVERIFY API Endpoint - https://faceio.net/rest-api#faceverify

import requests
import json
import base64

# Load an image from disk and encode it in base64.
def load_image_and_encode(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    mime_type = "image/jpeg"  # Or determine the MIME type dynamically
    return f"data:{mime_type};base64,{encoded_string}"

source_face_img_path = "path/to/face1.jpg"  # Replace with the actual path to your source face image
target_face_img_path = "path/to/face2.jpg"  # Replace with the actual path to your target face (to compare to source) image

payload = {
    "key": "apiKey", # Get your API key from the FACEIO Console at - https://console.faceio.net/
    "src": load_image_and_encode(source_face_img_path),
    "target": load_image_and_encode(target_face_img_path)
}

try:
    response = requests.post(
        "https://api.faceio.net/faceverify",
        headers={"Content-Type": "application/json"},
        json=payload
    )

    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    print(response.json())
    # JSON Object is always returned
    # {
    #   dist: 'Distance Metric',
    #   sim:  'Similarity Score',
    #   same_person: 'Boolean Value'
    # }

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

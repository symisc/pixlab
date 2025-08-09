<?php
# Age Verification & Gender Extraction using the FACEIO REST API - https://faceio.net/rest-api#age-check
#
# The age verification API endpoint allows you to verify customer age and gender
# by directly uploading a base64 encoded image of the person being verified. 
# No prior face enrollment is required; Age verification operates directly on the uploaded images.
# This API endpoint expects a single face to be present in the source image being checked.

# Load an image from disk and encode it in base64.
function load_image_and_encode($image_path) {
    $imageData = file_get_contents($image_path);
    return base64_encode($imageData);
}

# Source image we want to exract the face from, and output the gender & age estimation of the target person
$source_face_img_path = "path/to/face1.jpg";  # Replace with the actual path to your source face image

$payload = json_encode([
    "key" => "apiKey", // Get your API key from the FACEIO Console at - https://console.faceio.net/
    "img" => load_image_and_encode($source_face_img_path), // Face image we want to extract the gender & age from
]);

$ch = curl_init("https://api.faceio.net/agecheck");

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json"
]);

$response = curl_exec($ch);

if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($httpCode >= 200 && $httpCode < 300) {
        $responseData = json_decode($response, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            print_r($responseData);
            # JSON Object is always returned
            # {
            #   age: 'Age approximation of the target person',
            #   gender:  'Gender of the target person',
            #   status: 'Status Code'
            # }
        } else {
            echo "Error decoding JSON: " . json_last_error_msg();
        }
    } else {
        echo "HTTP request failed with code: " . $httpCode . "\n";
        echo "Response body: " . $response . "\n";
    }
}
curl_close($ch);
```

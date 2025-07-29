<?php
# Determine if the provided faces represent the same individual or not
# using the FACEIO FACEVERIFY API Endpoint - https://faceio.net/rest-api#faceverify

function load_image_and_encode($image_path) {
    $imageData = file_get_contents($image_path);
    return base64_encode($imageData);
}

$source_face_img_path = "path/to/face1.jpg";  // Replace with the actual path to your source face image
$target_face_img_path = "path/to/face2.jpg";  // Replace with the actual path to your target face (to compare to source) image

$payload = json_encode([
    "key" => "apiKey", // Get your API key from the FACEIO Console at - https://console.faceio.net/
    "src" => load_image_and_encode($source_face_img_path),
    "target" => load_image_and_encode($target_face_img_path)
]);

$ch = curl_init("https://api.faceio.net/faceverify");

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
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($http_code >= 200 && $http_code < 300) {
        $json_response = json_decode($response, true);
        if (json_last_error() === JSON_ERROR_NONE) {
            print_r($json_response);
            // JSON Object is always returned
            // {
            //   dist: 'Distance Metric',
            //   sim:  'Similarity Score',
            //   same_person: 'Boolean Value'
            // }
        } else {
            echo "Error decoding JSON: " . json_last_error_msg();
        }
    } else {
        echo "HTTP Error: " . $http_code . "\n";
        echo "Response: " . $response . "\n";
    }
}

curl_close($ch);

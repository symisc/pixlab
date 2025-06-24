<?php
# Get natural language responses to image-related queries

# Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the REST API code samples for more info.
$img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg';

$key = 'PIXLAB_API_KEY'; // Get your API key from https://console.pixlab.io/

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://api.pixlab.io/query?img=' . urlencode($img) . '&key=' . $key . '&query=What does this image depict?');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

$reply = json_decode(curl_exec($ch), true);
curl_close($ch);

if ($reply['status'] != 200) {
    echo $reply['error'];
} else {
    $response = $reply['response'];
    echo "Query Response: " . $response;
}

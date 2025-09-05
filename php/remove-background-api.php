<?php
# Programmatically remove backgrounds from input images using the PixLab BG-REMOVE API endpoint.
#
# Refer to the official documentation at: https://pixlab.io/endpoints/background-remove-api for the API reference
# guide and more code samples.

# Use POST to upload the image directly from your local folder. If your image is publicly available
# then make a simple GET request with a link to your image.

$url = 'https://api.pixlab.io/bgremove';
$apiKey = 'PIXLAB_API_KEY'; // PixLab API Key - Get yours from https://console.pixlab.io/
$imagePath = './local_image.png'; // The local image we are going to remove background from
$outputFilename = 'output_image';

$ch = curl_init();

$postData = [
    'key' => $apiKey,
    'file' => new CURLFile(realpath($imagePath))
];

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

$reply = json_decode($response, true);

if ($reply['status'] != 200) {
    echo $reply['error'] . PHP_EOL;
} else {
    $imgData = $reply['imgData'];  // Base64 encoding of the output image
    $mimeType = $reply['mimeType'];  // MIME type (i.e image/jpeg, etc.) of the output image
    $extension = $reply['extension'];  // File extension (e.g., 'png', 'jpeg')

    // Decode base64 and save to disk
    try {
        $imgBytes = base64_decode($imgData);
        $outputFilename = $outputFilename . "." . $extension;
        file_put_contents($outputFilename, $imgBytes);
        echo "Background Removed Image saved to: " . $outputFilename . PHP_EOL;
    } catch (Exception $e) {
        echo "Error saving output image: " . $e->getMessage() . PHP_EOL;
    }
}

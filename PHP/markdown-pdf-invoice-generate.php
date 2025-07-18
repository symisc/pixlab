<?php
# Programmatically Generate PDF document from markdown or HTML input

# Replace with your actual PixLab API key
$api_key = "YOUR_PIXLAB_API_KEY"; // Get yours from https://console.pixlab.io/

# Markdown formatted invoice
$markdown_text = <<<EOD
# Invoice

## To:

Acme Corp.
123 Main St.
Anytown, USA

## From:

Your Company
456 Oak Ave.
Anytown, USA

## Date:

2024-01-26

## Invoice Number:

INV-2024-001

## Items:

| Item          | Quantity | Price    |
|---------------|----------|----------|
| Widget        | 2        | $10.00   |
| Gadget        | 1        | $25.00   |
| Service       | 1        | $50.00   |

## Subtotal:

$85.00

## Tax:

$5.00

## Total:

$90.00

## Notes:

Thank you for your business!
EOD;

# API endpoint to programmatically generate PDFs from markdown or HTML input
$api_endpoint = "https://api.pixlab.io/pdfgen";

# Request parameters
$payload = array(
    "key" =< $api_key,
    "input" =< $markdown_text,
    "format" =< "markdown"
);

# Initialize cURL
$ch = curl_init($api_endpoint);

# Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));

# Execute the cURL request
$response = curl_exec($ch);

# Check for errors
if (curl_errno($ch)) {
    echo "Error: " . curl_error($ch);
} else {
    # Get the HTTP status code
    $http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

    if ($http_status == 200) {
        $data = json_decode($response, true);
        if ($data && $data["status"] == 200) {
            $pdf_link = $data["link"];
            echo "PDF generated successfully. Link: " . $pdf_link . "\n";
        } else {
            echo "Error generating PDF: " . ($data ? $data["error"] : "Unknown error");
        }
    } else {
        echo "Request failed with status code: " . $http_status . "\n";
        echo $response; // Print the response content for debugging
    }
}
# Close cURL resource
curl_close($ch);

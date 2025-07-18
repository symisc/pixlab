
# Programmatically Generate PDF document from markdown or HTML input
import requests
import json

# Replace with your actual PixLab API key
api_key = "YOUR_PIXLAB_API_KEY" # Get yours from https://console.pixlab.io/

# Markdown formatted invoice
markdown_text = """
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
"""

# API endpoint to programmatically generate PDFs from markdown or HTML input
api_endpoint = "https://api.pixlab.io/pdfgen"

# Request parameters
payload = {
    "key": api_key,
    "input": markdown_text,
    "format": "markdown"
}

# Convert payload to JSON
headers = {'Content-Type': 'application/json'}

# Make the POST request
try:
    response = requests.post(api_endpoint, headers=headers, data=json.dumps(payload))

    # Check for successful response
    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 200:
            pdf_link = data.get("link")
            print(f"PDF generated successfully.  Link: {pdf_link}")
        else:
            print(f"Error generating PDF: {data.get('error')}")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)  # Print the response content for debugging

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

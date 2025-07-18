
// Programmatically Generate PDF document from markdown or HTML input
// Replace with your actual PixLab API key
const apiKey = "YOUR_PIXLAB_API_KEY"; // Get yours from https://console.pixlab.io/

// Markdown formatted invoice
const markdownText = `
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
`;

// API endpoint to programmatically generate PDFs from markdown or HTML input
const apiEndpoint = "https://api.pixlab.io/pdfgen";

// Request parameters
const payload = {
    key: apiKey,
    input: markdownText,
    format: "markdown"
};

// Make the POST request
fetch(apiEndpoint, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
})
.then(response => {
    if (response.status === 200) {
        return response.json();
    } else {
        console.error(`Request failed with status code: ${response.status}`);
        return response.text().then(text => { throw new Error(text) }); // Throw error to be caught in catch block
    }
})
.then(data => {
    if (data.status === 200) {
        const pdfLink = data.link;
        console.log(`PDF generated successfully. Link: ${pdfLink}`);
    } else {
        console.error(`Error generating PDF: ${data.error}`);
    }
})
.catch(error => {
    console.error(`An error occurred: ${error}`);
});

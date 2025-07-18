// Convert PDF Document to image format using the PixLab PDFTOIMG SDK-Free REST API Endpoint
fetch('https://api.pixlab.io/pdftoimg?src=https://www.getharvest.com/downloads/Invoice_Template.pdf&export=jpeg&key=PIXLAB_API_KEY')
  .then(response => response.json())
  .then(reply => {
    if (reply.status !== 200) {
      console.log(reply.error);
    } else {
      console.log("Link to the image output (Converted PDF page): " + reply.link);
    }
  })
  .catch(error => console.error('Error:', error));

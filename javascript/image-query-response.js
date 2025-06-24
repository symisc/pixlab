
// Get natural language responses to image-related queries

// Target Image: Change to any link or switch to POST if you want to upload your image directly, refer to the REST API code samples for more info.
const img = 'https://s-media-cache-ak0.pinimg.com/originals/35/d0/f6/35d0f6ee0e40306c41cfd714c625f78e.jpg';

const key = 'PIXLAB_API_KEY'; // Get your API key from https://console.pixlab.io/

fetch('https://api.pixlab.io/query', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    img: img,
    key: key,
    lang: 'english',
    query: 'What does this image depict?'
  })
})
  .then(response => response.json())
  .then(reply => {
    if (reply.status !== 200) {
      console.error(reply.error);
    } else {
      const response = reply.answer;
      console.log(`Query Response: ${response}`);
    }
  })
  .catch(error => console.error('Error:', error));

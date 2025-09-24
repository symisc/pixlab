
// Programmatically remove backgrounds from input images using the PixLab BG-REMOVE API endpoint.
//
// Refer to the official documentation at: https://pixlab.io/endpoints/background-remove-api for the API reference
// guide and more code samples.

// Use POST to upload the image directly from your local folder. If your image is publicly available
// then make a simple GET request with a link to your image.

const apiKey = 'PIXLAB_API_KEY'; // PixLab API Key - Get yours from https://console.pixlab.io/
const apiUrl = 'https://api.pixlab.io/bgremove';
const imageFile = document.querySelector('input[type="file"]'); // Assuming you have an input file element

async function removeBackground() {
    if (!imageFile || !imageFile.files || !imageFile.files[0]) {
        console.error('Please select an image file.');
        return;
    }

    const file = imageFile.files[0];
    const formData = new FormData();
    formData.append('file', file);
    formData.append('key', apiKey);

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            body: formData,
        });

        const reply = await response.json();

        if (reply.status !== 200) {
            console.error(reply.error);
        } else {
            const imgData = reply.imgData; // Base64 encoding of the output image
            const mimetype = reply.mimeType; // MIME type (i.e image/jpeg, etc.) of the output image
            const extension = reply.extension; // File extension (e.g., 'png', 'jpeg')

            // Decode base64 and save to disk
            try {
                const img_bytes = atob(imgData); // Decode base64
                const output_filename = `output_image.${extension}`;

                // Create a Blob from the base64 string
                const byteCharacters = atob(imgData);
                const byteArrays = [];

                for (let offset = 0; offset < byteCharacters.length; offset += 512) {
                    const slice = byteCharacters.slice(offset, offset + 512);
                    const byteNumbers = new Array(slice.length);
                    for (let i = 0; i < slice.length; i++) {
                        byteNumbers[i] = slice.charCodeAt(i);
                    }
                    const byteArray = new Uint8Array(byteNumbers);
                    byteArrays.push(byteArray);
                }

                const blob = new Blob(byteArrays, {type: mimetype});


                // Create a download link
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = output_filename;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url); // Clean up

                console.log(`Background Removed Image saved to: ${output_filename}`);
            } catch (e) {
                console.error(`Error saving output image: ${e}`);
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Example: Attach to a button click
const button = document.querySelector('#removeBackgroundButton'); // Assuming you have a button with this ID
if (button) {
    button.addEventListener('click', removeBackground);
}

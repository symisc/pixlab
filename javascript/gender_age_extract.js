// Age Verification & Gender Extraction using the FACEIO REST API - https://faceio.net/rest-api#age-check
//
// The age verification API endpoint allows you to verify customer age and gender
// by directly uploading a base64 encoded image of the person being verified. 
// No prior face enrollment is required; Age verification operates directly on the uploaded images.
// This API endpoint expects a single face to be present in the source image being checked.

// Load an image from disk and encode it in base64.
async function loadImageAndEncode(imagePath) {
    try {
        const response = await fetch(imagePath);
        const blob = await response.blob();
        const reader = new FileReader();
        return new Promise((resolve, reject) => {
            reader.onload = () => {
                resolve(reader.result.split(',')[1]); // Extract base64 data
            };
            reader.onerror = reject;
            reader.readAsDataURL(blob);
        });
    } catch (error) {
        console.error("Error loading or encoding image:", error);
        throw error; // Re-throw the error to be caught by the caller
    }
}

// Source image we want to exract the face from, and output the gender & age estimation of the target person
const sourceFaceImgPath = "path/to/face1.jpg"; // Replace with the actual path to your source face image
const apiKey = "apiKey"; // Get your API key from the FACEIO Console at - https://console.faceio.net/
// Or if the face image is on Public URL, just pass it as is:
const source_face_url = "https://example.com/face1.jpg"; // In case of public image URL

async function verifyAgeAndGender() {
    try {
        const imgBase64 = await loadImageAndEncode(sourceFaceImgPath);

        const payload = {
            key: apiKey,
            img: imgBase64,
        };

        const response = await fetch(
            "https://api.faceio.net/agecheck", // Target API endpoint for static gender & age extraction
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        // JSON Object is always returned
        // {
        //   age: 'Age approximation of the target person',
        //   gender:  'Gender of the target person',
        //   status: 'Status Code'
        // }

    } catch (error) {
        console.error("An error occurred:", error);
    }
}
verifyAgeAndGender();
```

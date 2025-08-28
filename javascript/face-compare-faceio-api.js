// Determine if the provided faces represent the same individual or not
// using the FACEIO FACEVERIFY API Endpoint - https://faceio.net/rest-api#faceverify

async function load_image_and_encode(image_path) {
    try {
        const response = await fetch(image_path);
        const blob = await response.blob();
        const buffer = await new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsDataURL(blob);
        });
        return buffer.split(',')[1]; // Extract base64 part
    } catch (error) {
        console.error("Error loading or encoding image:", error);
        throw error; // Re-throw to be caught by the caller
    }
}

async function verifyFaces() {
    const source_face_img_path = "path/to/face1.jpg"; // Replace with the actual path to your source face image
    const target_face_img_path = "path/to/face2.jpg"; // Replace with the actual path to your target face (to compare to source) image
    // Or if the face image is on Public URL, just pass it as is:
    const source_face_url = "https://example.com/face1.jpg"; // In case of public image URL
    
    const payload = {
        "key": "apiKey", // Get your API key from the FACEIO Console at - https://console.faceio.net/
        "src": await load_image_and_encode(source_face_img_path),
        "target": await load_image_and_encode(target_face_img_path)
    };

    try {
        const response = await fetch(
            "https://api.faceio.net/faceverify",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        // JSON Object is always returned
        // {
        //   dist: 'Distance Metric',
        //   sim:  'Similarity Score',
        //   same_person: 'Boolean Value'
        // }

    } catch (error) {
        console.error("An error occurred:", error);
    }
}

verifyFaces();

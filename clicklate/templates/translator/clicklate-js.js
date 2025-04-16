
document.getElementById('text-input').addEventListener('keydown', async function(event) {
    console.log('pressed')
    const resultElement = document.getElementById('text-detected');
    const apiKey = '6dd8715b0219b1a87976ddfced65fe59'; // Replace with your Detect Language API key

    // if (text.trim() === "") {
    //     resultElement.textContent = "Please enter some text.";
    //     return;
    // }

    const apiUrl = 'https://ws.detectlanguage.com/0.2/detect';
    
    try {
        const response = await axios.post(apiUrl, null, {
            params: {
                q: text,
                key: apiKey,
            }
        });

        const detectedLanguage = response.data.data.detections[0].language;
        resultElement.textContent = `Detected language: ${detectedLanguage}`;
    } catch (error) {
        resultElement.textContent = 'Error detecting language. Please try again.';
        console.error(error);
    }
}
);

// const apiKey = '6dd8715b0219b1a87976ddfced65fe59'; // Replace with your Detect Language API key

// async function detectLanguage() {
//     const text = document.getElementById('text').value;
//     const resultElement = document.getElementById('text-area');

//     if (text.trim() === "") {
//         resultElement.textContent = "Please enter some text.";
//         return;
//     }

//     const apiUrl = 'https://ws.detectlanguage.com/0.2/detect';
    
//     try {
//         const response = await axios.post(apiUrl, null, {
//             params: {
//                 q: text,
//                 key: apiKey,
//             }
//         });

//         const detectedLanguage = response.data.data.detections[0].language;
//         resultElement.textContent = `Detected language: ${detectedLanguage}`;
//     } catch (error) {
//         resultElement.textContent = 'Error detecting language. Please try again.';
//         console.error(error);
//     }
// }






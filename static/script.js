document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const textarea = document.querySelector("#review");

    form.addEventListener("submit", async function (event) {
        event.preventDefault(); // Prevent form from reloading the page

        const sentence = textarea.value.trim();
        if (!sentence) return alert("Please enter a review!");

        // Determine the correct URL based on the environment
        const apiUrl = window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost' 
            ? 'http://127.0.0.1:5001/predict' // Local URL
            : 'https://emotion-detection-j2mx.onrender.com/predict'; // Production URL

        try {
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ sentence }),
            });

            const data = await response.json();
            console.log(data); // Log response (for debugging)

            // Update the UI dynamically
            document.querySelector("#result").innerHTML = `
                <p>Sentence: ${data.sentence}</p>
                <p>Naive Bayes Label: ${data.nb_label}</p>
                <p>RNN Label: ${data.rnn_label}</p>
            `;

        } catch (error) {
            console.error("Error:", error);
            alert("Failed to fetch prediction!");
        }
    });
});

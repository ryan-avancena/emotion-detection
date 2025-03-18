fetch("https://emotion-detection-j2mx.onrender.com/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sentence: "i am happy" }),
})
const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");
const cors = require("cors");

const app = express();
app.use(cors()); // Enable CORS for frontend requests
app.use(express.static("public")); // Serve frontend static files

// Proxy API requests to Flask
app.use(
  "/api",
  createProxyMiddleware({
    target: "http://127.0.0.1:5001", // Flask backend URL
    changeOrigin: true
  })
);

// Serve index.html
app.get("/", (req, res) => {
  res.sendFile(__dirname + "/templates/index.html");
});

app.use(
    "/predict",
    createProxyMiddleware({
      target: "http://127.0.0.1:5001", // Flask backend URL
      changeOrigin: true
    })
);
  

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Node.js server running on http://localhost:${PORT}`);
});

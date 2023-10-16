const express = require('express');
const bodyParser = require('body-parser');
const QRCode = require('qrcode');
const cors = require('cors'); // Import the cors middleware.

const app = express();
const port = process.env.PORT || 5000;

app.use(bodyParser.json());

// Enable CORS for all routes or specify allowed origins.
app.use(cors());

app.post('/generate', async (req, res) => {
  const { text } = req.body;
  console.log(text);
  try {
    const qrCode = await QRCode.toDataURL(text);
    console.log(qrCode);
    res.json(qrCode);
  } catch (error) {
    console.error('Error generating QR code:', error);
    res.status(500).json({ error: 'QR code generation failed' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

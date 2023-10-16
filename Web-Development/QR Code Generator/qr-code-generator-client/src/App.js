import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [qrCodeUrl, setQRCodeUrl] = useState('');

  const generateQRCode = async () => {
    const response = await fetch('http://localhost:5000/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    if (response.ok) {
      const data = await response.json();
      setQRCodeUrl(data); // Assuming the backend returns a 'url' property.
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="input-container">
          <input
            className='textbar'
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter text for QR code"
          />
          <button className="button" onClick={generateQRCode}>Generate QR Code</button>
        </div>
        {qrCodeUrl && (
          <img className="qrcode" src={qrCodeUrl} alt="QR Code" />
        )}
      </header>
    </div>
  );
}

export default App;

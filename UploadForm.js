import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

  // Handle file change event
  const handleChange = (e) => {
    setFile(e.target.files[0]);
  };

  // Handle file upload
  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      alert('Видео файлыг сонгоно уу.');
      return;
    }

    const formData = new FormData();
    formData.append('video', file);

    try {
      // Send video to the Flask server
      const res = await axios.post('http://127.0.0.1:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      // Update the response state with the server response
      setResponse(res.data);
    } catch (err) {
      console.error('Error uploading video:', err);
    }
  };

  return (
    <div>
      <form onSubmit={handleUpload}>
        <input type="file" accept="video/*" onChange={handleChange} required />
        <br />
        <button type="submit">Видео илгээх</button>
      </form>

      {response && (
        <div>
          <h3>Хариу:</h3>
          <pre style={{ textAlign: 'left', backgroundColor: '#f4f4f4', padding: '1rem' }}>
            {JSON.stringify(response, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

export default UploadForm;

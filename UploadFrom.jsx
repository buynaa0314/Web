import React, { useState } from "react";
import axios from "axios";

function UploadForm() {
  const [videoFile, setVideoFile] = useState(null);
  const [response, setResponse] = useState(null);

  const handleFileChange = (e) => {
    setVideoFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!videoFile) {
      alert("Файл сонгоно уу.");
      return;
    }

    const formData = new FormData();
    formData.append("file", videoFile);

    try {
      const res = await axios.post("http://localhost:5001/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      setResponse(res.data);
    } catch (error) {
      console.error("Алдаа:", error);
      alert("Файл илгээхэд алдаа гарлаа.");
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-xl font-semibold mb-4">🚗 Машины зогсоол илрүүлэлтийн видео илгээх</h2>
      
      <input
        type="file"
        accept="video/*"
        onChange={handleFileChange}
        className="mb-4"
      />
      
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Upload
      </button>

      {response && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h3 className="font-bold mb-2">📊 Илрүүлэлтийн үр дүн:</h3>
          <p>Нийт машин: {response.total_cars}</p>
          <p>Сул зогсоол: {response.free_spots}</p>
          <p>Зогсоолууд: {response.occupied_spots.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default UploadForm;

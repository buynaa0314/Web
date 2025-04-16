from flask import Flask, request, jsonify

app = Flask(__name__)

# Түр хадгалах хувьсагч
latest_report = {
    "total_cars": 0,
    "free_spots": 0,
    "occupied_spots": []
}

# POST хүсэлт хүлээн авч хадгалах
@app.route("/detect", methods=["POST"])
def receive_report():
    global latest_report
    data = request.get_json()

    if not data:
        return jsonify({"error": "Хоосон эсвэл буруу өгөгдөл"}), 400

    latest_report["total_cars"] = data.get("total_cars", 0)
    latest_report["free_spots"] = data.get("free_spots", 0)
    latest_report["occupied_spots"] = data.get("occupied_spots", [])

    print("📥 Шинэ мэдээлэл хүлээн авлаа:", latest_report)
    return jsonify({"message": "Мэдээлэл амжилттай хадгалагдлаа"}), 200

# Сүүлийн хадгалсан мэдээллийг авах
@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(latest_report)

# Default home page
@app.route("/")
def home():
    return "🚗 Parking Detection API ажиллаж байна!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

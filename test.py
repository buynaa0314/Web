import requests
import json

def send_data_to_server(total_cars, free_spots, occupied_spots, filename):
    url = "http://127.0.0.1:5000/detect"  # Маршрут сервер дээр тохирсон байх ёстой
    data = {
        "total_cars": total_cars,
        "free_spots": free_spots,
        "occupied_spots": occupied_spots,
        "filename": filename
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("✅ Амжилттай илгээлээ:", data)
        else:
            print("❌ Алдаа гарлаа:", response.status_code, response.text)
    except Exception as e:
        print("🚫 Сервер рүү илгээх үед алдаа гарлаа:", str(e))

# Туршилт
send_data_to_server(10, 4, 6, "video.mp4")

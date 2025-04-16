import requests
import json

def send_to_server(total_cars, free_spots, occupied_spots, filename="video.mp4"):
    url = "http://127.0.0.1:5000/detect"
    data = {
        "total_cars": total_cars,
        "free_spots": free_spots,
        "occupied_spots": occupied_spots,
        "filename": filename
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.text)

# send_to_server(10, 5, 5) гэх мэтээр Colab-аас дуудаж болно

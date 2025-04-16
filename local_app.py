import requests
import cv2
from ultralytics import YOLO

# Server endpoint
SERVER_URL = "http://localhost:5000/report"

# Load model
model = YOLO("yolov8n.pt")

# Parking slot polygonууд (жишээ)
parking_spots = [
    [(100, 200), (200, 200), (200, 300), (100, 300)],  # Spot 1
    [(220, 200), (320, 200), (320, 300), (220, 300)],  # Spot 2
    # Та өөрийн координатыг оруулна
]

def is_car_inside(spot, box):
    # Хайрцаг болон зогсоол давхацаж байгааг шалгах (x1,y1,x2,y2 болон polygon)
    x1, y1, x2, y2 = box
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    return cv2.pointPolygonTest(np.array(spot, np.int32), (center_x, center_y), False) >= 0

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    free_spots = [True] * len(parking_spots)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        boxes = results[0].boxes.xyxy.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()

        for box, cls in zip(boxes, classes):
            if int(cls) == 2:  # car class (coco)
                for i, spot in enumerate(parking_spots):
                    if is_car_inside(spot, box):
                        free_spots[i] = False

        break  # зөвхөн 1 frame шалгана, хүсвэл устгаарай

    cap.release()

    total_spots = len(parking_spots)
    free_count = free_spots.count(True)

    return {
        "total_spots": total_spots,
        "free_spots": free_count,
        "occupied_spots": total_spots - free_count
    }

def send_to_server(data):
    res = requests.post(SERVER_URL, json=data)
    print(res.status_code, res.text)

if __name__ == "__main__":
    video_path = "parking_video.mp4"
    data = analyze_video(video_path)
    send_to_server(data)

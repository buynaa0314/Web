import requests

def upload_file(filepath):
    url = "http://127.0.0.1:5000/upload"
    files = {'file': open(filepath, 'rb')}

    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("✅ Файл илгээсэн:", filepath)
        else:
            print("❌ Файл илгээхэд алдаа:", response.status_code, response.text)
    except Exception as e:
        print("🚫 Алдаа:", str(e))

# Туршилт
upload_file("example.mp4")

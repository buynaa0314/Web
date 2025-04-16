from flask import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import os
from google.auth.transport.requests import Request  # Засварласан хэсэг

# Google Drive API-аар холбогдох
def get_google_drive_service():
    creds = None
    # Таны OAuth2 credential файл
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive'])
    # Хэрвээ token байхгүй бол OAuth flow-г ашиглаж шинэ token авах
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Request импортлосон
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        # Сэргээх token хадгалах
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('drive', 'v3', credentials=creds)
    return service

# Google Drive-оос файл татаж авах
def download_video_from_drive(file_id, save_path):
    service = get_google_drive_service()

    # Файлын мэдээллийг авах
    request = service.files().get_media(fileId=file_id)
    fh = open(save_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Downloading {int(status.progress() * 100)}%.")

    print(f"Файл {save_path} болгон амжилттай татагдлаа.")

# Видео татаж авах
file_id = '18TKMZHIj2YNV-cHE-Hnbv6ATO1dNAhxL'  # Таны видео файлын ID
download_video_from_drive(file_id, 'downloaded_video.mp4')  # Видео хадгалах зам хадгалах file нэр

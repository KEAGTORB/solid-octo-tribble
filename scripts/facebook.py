import os
import requests

def download_facebook():
    url = input("Enter Facebook URL: ")
    print("Downloading Facebook video...")

    # Set the path to the 'downloads' folder relative to downstream.py
    download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')

    try:
        # Example method to download Facebook videos (this needs an actual implementation)
        video_content = requests.get(url).content  # This is a placeholder. You will need a Facebook video downloader logic.
        
        file_path = os.path.join(download_path, 'facebook_video.mp4')  # Save video as .mp4
        with open(file_path, 'wb') as f:
            f.write(video_content)
        
        print(f"Download completed successfully! File saved in {file_path}")
    except Exception as e:
        print(f"Error downloading Facebook video: {e}")

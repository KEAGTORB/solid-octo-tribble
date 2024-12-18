import os
import yt_dlp

def download_twitter():
    url = input("Enter Twitter URL: ")
    print("Downloading Twitter video...")

    # Set the path to the 'downloads' folder relative to downstream.py
    download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')
    
    try:
        # Create a custom configuration for yt-dlp
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Save in the downloads folder
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Download completed successfully! File saved in {download_path}")
    except Exception as e:
        print(f"Error downloading Twitter video: {e}")

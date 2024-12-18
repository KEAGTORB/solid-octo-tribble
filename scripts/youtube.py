import os
import yt_dlp

def download_youtube():
    url = input("Enter YouTube URL: ")

    print("Available formats: ")
    print("[1] Video")
    print("[2] Audio")
    format_choice = input("Choose format (1 or 2): ")

    
    download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', 
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
        'noplaylist': True  
    }

    if format_choice == "1":
        ydl_opts['format'] = 'bestvideo+bestaudio/best'  
    elif format_choice == "2":
        ydl_opts['format'] = 'bestaudio/best' 
    else:
        print("Invalid choice.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Downloading...")
            ydl.download([url])
            print("Download completed successfully!")
        except Exception as e:
            print(f"Error downloading video: {e}")

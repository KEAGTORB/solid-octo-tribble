import os
import instaloader

def download_instagram():
    url = input("Enter Instagram URL: ")
    print("Downloading Instagram post...")

    # Set the path to the 'downloads' folder relative to downstream.py
    download_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'downloads')

    try:
        L = instaloader.Instaloader(dirname_pattern=download_path, filename_pattern='{shortcode}')  # Updated filename pattern
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])  # Extract shortcode from URL
        L.download_post(post, target=download_path)
        print(f"Download completed successfully! File saved in {download_path}")
    except Exception as e:
        print(f"Error downloading Instagram post: {e}")

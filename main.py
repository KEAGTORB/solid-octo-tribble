from pytube import Playlist, YouTube

def playlist(option, location):
    url = input("Enter the Url: ")
    playlist = Playlist(url)

    # Wait until valid playlist is loaded
    while len(playlist.video_urls) == 0:
        print("Invalid URL or empty playlist. Please try again.")
        url = input("Enter the Url: ")
        playlist = Playlist(url)

    print(f'Number of videos in playlist: {len(playlist.video_urls)}')

    if option == 1:
        playlist.download_all()
    elif option == 2:
        for video_url in playlist.video_urls:
            print("\nDownloading:", video_url)
            i = 0
            while True:
                i += 1
                try:
                    YouTube(video_url).streams.filter(audio_only=True)[-1].download(location)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    cont = input("\nAn error occurred, try again? (y/n): ")
                    if cont.lower() == "y":
                        continue
                    elif cont.lower() == "n":
                        break

def video(option, location):
    url = YouTube(input("Enter the Url: "))
    
    if option == 1:
        url.streams.get_highest_resolution().download(location)
    elif option == 2:
        url.streams.filter(only_audio=True)[-1].download(location)

def main():
    option1 = input("What do you want to download: \n[1] Video \n[2] Playlist\n: ")
    option2 = input("Do you want it to be Audio or Original: \n[1] Original \n[2] Audio\n: ")
    location = input("\nWhere do you want your files to be saved: ")

    if option1 == "1":
        if option2 == "1":
            video(1, location)
        elif option2 == "2":
            video(2, location)
    elif option1 == "2":
        if option2 == "1":
            playlist(1, location)
        elif option2 == "2":
            playlist(2, location)

main()

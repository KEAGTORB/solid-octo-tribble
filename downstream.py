import os
import sys
import time

def print_header():
    print("""

  _____                       _____ _                            
 |  __ \                     / ____| |                           
 | |  | | _____      ___ __ | (___ | |_ _ __ ___  __ _ _ __ ___  
 | |  | |/ _ \ \ /\ / / '_ \ \___ \| __| '__/ _ \/ _` | '_ ` _ \ 
 | |__| | (_) \ V  V /| | | |____) | |_| | |  __/ (_| | | | | | |
 |_____/ \___/ \_/\_/ |_| |_|_____/ \__|_|  \___|\__,_|_| |_| |_|
Welcome to DownStream - Author: github.com/saltx5
    """)

def main_menu():
    print("\nWhich platform do you want to download from?")
    print("[1] YouTube")
    print("[2] Instagram")
    print("[3] Facebook")
    print("[4] Twitter")
    print("[5] Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def handle_choice(choice):
    if choice == '1':
        from scripts.youtube import download_youtube
        download_youtube()
    elif choice == '2':
        from scripts.instagram import download_instagram
        download_instagram()
    elif choice == '3':
        from scripts.facebook import download_facebook
        download_facebook()
    elif choice == '4':
        from scripts.twitter import download_twitter
        download_twitter()
    elif choice == '5':
        print("Exiting DownStream. Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    while True:
        print_header()
        choice = main_menu()
        handle_choice(choice)
        time.sleep(2) 

if __name__ == "__main__":
    main()

# DownStream

DownStream is a versatile multi-platform downloader tool that allows you to download videos and audio from YouTube, Instagram, Facebook, and Twitter. It supports both video and audio formats with easy-to-use commands.

## Installation

### Termux (Android)

1. Install `ffmpeg` and required dependencies:
    ```bash
    pkg install ffmpeg python
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/saltX5/downstream
    cd downstream
    ```

3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the code:
    ```bash
    python downstream.py
    ```    

### Windows

1. Install `ffmpeg` using PowerShell:
    ```bash
    winget install ffmpeg
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/saltX5/downstream
    cd downstream
    ```

3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the code:
    ```bash
    python downstream.py
    ```        

### Linux

1. Install `ffmpeg` and required dependencies:
    ```bash
    sudo apt install ffmpeg python3-pip
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/saltX5/downstream
    cd downstream
    ```

3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the code:
    ```bash
    python downstream.py
    ```        
    
## Requirements

- Python 3.x
- ffmpeg (for video/audio merging)

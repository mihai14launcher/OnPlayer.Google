import os
import subprocess
import urllib.request
import zipfile
import sys

def install_ffmpeg(destination_folder):
    print("Installing FFmpeg...")

    # URL for FFmpeg Windows builds
    ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    temp_zip_path = "ffmpeg.zip"

    # Download FFmpeg
    urllib.request.urlretrieve(ffmpeg_url, temp_zip_path)
    print("Downloaded FFmpeg.")

    # Extract FFmpeg
    with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
    print(f"Extracted FFmpeg to {destination_folder}.")

    # Clean up
    os.remove(temp_zip_path)
    print("Removed temporary zip file.")

def install_python_packages():
    print("Installing Python packages...")

    packages = ['yt-dlp', 'tkinter']

    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Installed {package}.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}.")

def main():
    ffmpeg_folder = r"C:\VOX\Extensions\OnPlayer\Required\FFMPEG"
    
    # Create the directory if it doesn't exist
    os.makedirs(ffmpeg_folder, exist_ok=True)

    # Install FFmpeg
    install_ffmpeg(ffmpeg_folder)

    # Install Python packages
    install_python_packages()

if __name__ == "__main__":
    main()

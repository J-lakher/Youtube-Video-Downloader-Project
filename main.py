import yt_dlp

def download_video():
    """Prompts the user for a video URL and downloads it using yt-dlp."""

    url = input("Enter video URL: ")

    ydl_opts = {}  # You can add options here later if needed

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Congratulations! Video downloaded successfully!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error downloading video: {e}")
    except Exception as e:  # Catching general errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    download_video()

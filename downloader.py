from yt_dlp import YoutubeDL
import os

def download_video(url, output_path=None):
    try:
        if not url.strip():
            raise ValueError("URL cannot be empty")

        # Set default output path if none provided
        if output_path is None:
            output_path = os.path.join(os.getcwd(), "downloads")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        print("Connecting to YouTube...")
        
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download best quality
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
        }
        
        # Download the video
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"\nDownload completed! Saved to: {output_path}")
            return True
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

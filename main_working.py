import os
from downloader import download_video

def main():
    print("YouTube Video Downloader")
    print("----------------------")
    
    while True:
        # Get video URL from user
        url = input("\nEnter YouTube video URL (or 'q' to quit): ").strip()
        
        if url.lower() == 'q':
            break
            
        # Get output path (optional)
        output_path = input("Enter output path (press Enter for default): ").strip()
        if not output_path:
            output_path = os.path.join(os.getcwd(), "downloads")
            
        # Download the video
        success = download_video(url, output_path)
        
        if success:
            print("\nWould you like to download another video?")
        else:
            print("\nWould you like to try again?")

if __name__ == "__main__":
    main()

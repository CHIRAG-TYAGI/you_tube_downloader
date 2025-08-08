import os
from downloader import download_video

def main():
    print("YouTube Video Downloader")
    print("----------------------")
    
    while True:
        if not downloader:
            # First run or after output path change
            print("\nSetup:")
            print("Enter output path (press Enter for default downloads folder)")
            print("Example: C:\\Downloads\\YouTube")
            output_path = input("Path: ").strip()
            
            try:
                downloader = YouTubeDownloader(output_path if output_path else None)
                print(f"\nVideos will be saved to: {downloader.output_dir}")
            except Exception as e:
                print(f"\nError setting up output directory: {str(e)}")
                continue
        
        # Get video URL from user
        print("\nEnter a command:")
        print("- Paste a YouTube URL to download")
        print("- Type 'path' to change save location")
        print("- Type 'q' to quit")
        choice = input("\nCommand: ").strip()
        
        if choice == 'q':
            break
        elif choice == 'path':
            downloader = None  # Will trigger path input on next loop
            continue
        else:
            # Treat as URL
            success = downloader.download_video(choice)
            
            if success:
                print("\nWould you like to download another video?")
            else:
                print("\nWould you like to try again?")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDownload canceled. Exiting...")

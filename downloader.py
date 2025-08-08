from yt_dlp import YoutubeDL
import os

def download_video(url, output_path=None):
    """Download a video from YouTube.
    
    Args:
        url: The YouTube video URL
        output_path: Optional path to save the video (default: ./downloads)
        self.output_dir = output_dir or os.path.join(os.getcwd(), "downloads")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Default configuration
        self.ydl_opts = {
            'format': 'best',  # Best quality
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': True,
        }
    
    def get_video_info(self, url: str) -> Optional[Dict[str, Any]]:
        """Get information about a video without downloading.
        
        Args:
            url: YouTube video URL
            
        Returns:
            Dictionary containing video information or None if error occurs
        """
        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Error getting video info: {str(e)}")
            return None
    
    def download_video(self, url: str) -> bool:
        """Download a video from YouTube.
        
        Args:
            url: YouTube video URL
            
        Returns:
            True if download was successful, False otherwise
        """
        try:
            if not url.strip():
                raise ValueError("URL cannot be empty")

            print("Connecting to YouTube...")
            
            # Get video info first
            info = self.get_video_info(url)
            if info:
                print(f"Title: {info.get('title', 'Unknown')}")
                if 'filesize' in info:
                    print(f"Size: {info['filesize'] / (1024*1024):.1f} MB")
            
            # Download the video
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([url])
                print(f"\nDownload completed! Saved to: {self.output_dir}")
                return True
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

def download_video(url: str, output_path: Optional[str] = None) -> bool:
    """Convenience function to download a video without creating a class instance.
    
    Args:
        url: YouTube video URL
        output_path: Optional custom output directory
        
    Returns:
        True if download was successful, False otherwise
    """
    downloader = YouTubeDownloader(output_path)
    return downloader.download_video(url)

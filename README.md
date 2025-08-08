# YouTube Downloader

A robust Python application to download YouTube videos using yt-dlp.

## Features

- Download YouTube videos in best available quality
- Show download progress and file information
- User-friendly command-line interface
- Customizable output directory
- Object-oriented design with clean separation of concerns
- Type hints for better code maintainability
- Error handling and user feedback

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. The program offers several commands:
   - Paste a YouTube URL to download a video
   - Type 'path' to change the save location
   - Type 'q' to quit

3. Videos are downloaded in the best available quality

## Requirements

- Python 3.6 or higher
- yt-dlp
- tqdm

## Technical Details

The application is structured into two main components:

1. `downloader.py`:
   - Contains the `YouTubeDownloader` class
   - Handles all video downloading logic
   - Provides both OOP and functional interfaces
   - Includes type hints and documentation

2. `main.py`:
   - Provides the command-line interface
   - Handles user input and program flow
   - Uses the `YouTubeDownloader` class

## Notes

- Downloads are saved in a 'downloads' folder by default
- Creates output directory automatically if it doesn't exist
- Uses yt-dlp for reliable downloading and better compatibility
- Includes error handling for common issues
- Supports keyboard interrupt (Ctrl+C) for canceling downloads

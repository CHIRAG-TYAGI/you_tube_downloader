# YouTube Downloader Application Documentation

## Table of Contents
1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation Guide](#installation-guide)
4. [Technical Architecture](#technical-architecture)
5. [Usage Guide](#usage-guide)
6. [Code Documentation](#code-documentation)
7. [Troubleshooting](#troubleshooting)
8. [FAQ](#faq)

## Overview

### Purpose
The YouTube Downloader is a versatile application that allows users to download videos from YouTube in the highest available quality. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for downloading videos while handling various edge cases and errors gracefully.

### Key Features
- Download YouTube videos in best available quality
- Support for custom download locations
- Progress tracking during downloads
- Two interface options:
  - User-friendly graphical interface (GUI)
  - Interactive command-line interface (CLI)
- Real-time download progress indication
- Error handling and user feedback
- Support for various YouTube URL formats
- Browse functionality for output directory selection (GUI)

## System Requirements

### Prerequisites
1. **Python Environment**
   - Python 3.9 or higher
   - pip (Python package manager)

### Dependencies
- **yt-dlp**: Core library for YouTube video downloads
- **tqdm**: Progress bar functionality
- **tkinter**: GUI library (usually comes with Python)
- **os**: File system operations (built-in)

## Installation Guide

### Step-by-Step Installation

1. **Clone/Download the Application**
   ```bash
   git clone <repository-url>
   cd yt-downloader
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   python main.py
   ```

### File Structure
```
yt-downloader/
│
├── main_working.py      # CLI application entry point
├── downloader_working.py# Core downloading functionality
├── downloader_ui.py     # GUI application
├── requirements.txt     # Package dependencies
└── downloads/           # Default download directory (created automatically)
```

## Technical Architecture

### Application Flow

#### CLI Flow
```
Start (main_working.py)
    │
    ├─► Get YouTube URL from user
    │       │
    ├─► Get output directory (optional)
    │       │
    ├─► Validate inputs
    │       │
    ├─► Call download_video function
    │       │
    │       ├─► Check URL validity
    │       │
    │       ├─► Create output directory if needed
    │       │
    │       ├─► Configure yt-dlp options
    │       │
    │       ├─► Download video with progress
    │       │
    │       └─► Return success/failure status
    │
    └─► Ask to download another video or quit

```

#### GUI Flow
```
Start (downloader_ui.py)
    │
    ├─► Initialize GUI window
    │       │
    ├─► User enters YouTube URL
    │       │
    ├─► User can either:
    │       │
    │       ├─► Use default downloads folder
    │       │
    │       └─► Browse for custom folder
    │
    ├─► User clicks Download button
    │       │
    ├─► Disable UI elements during download
    │       │
    ├─► Call download_video function
    │       │
    │       ├─► Same download process as CLI
    │       │
    │       ├─► Update progress in GUI
    │       │
    │       └─► Show success/error message
    │
    └─► Enable UI elements for next download
```

### Component Overview

1. **CLI Module (`main_working.py`)**
   - Command-line interface handling
   - Input validation
   - Application flow control
   - Download directory management

2. **GUI Module (`downloader_ui.py`)**
   - Graphical user interface
   - Event handling
   - Real-time progress updates
   - Directory browsing functionality

3. **Downloader Module (`downloader_working.py`)**
   - YouTube video downloading logic
   - Error handling
   - Progress tracking
   - File system operations

### Core Functions

#### `download_video(url, output_path=None)` in downloader_working.py
- **Purpose**: Downloads a YouTube video to the specified location
- **Parameters**:
  - `url` (str): YouTube video URL
  - `output_path` (str, optional): Custom download location
- **Returns**: 
  - `bool`: True if download successful, False otherwise
- **Process Flow**:
  1. Validate URL input
  2. Set up output directory
  3. Configure download options
  4. Initialize download process
  5. Monitor and report progress
  6. Handle completion/errors
- **Error Handling**:
  - Empty URL validation
  - Network errors
  - File system errors

#### `YouTubeDownloaderUI` in downloader_ui.py
- **Purpose**: GUI class for the application
- **Components**:
  - Main window setup
  - URL entry field
  - Directory selection components
  - Download button
  - Progress indicator
- **Methods**:
  1. `__init__`: Initialize GUI components
  2. `browse_directory`: Handle directory selection
  3. `start_download`: Manage download process
- **Features**:
  - URL input field
  - Directory selection with browse button
  - Download progress indication
  - Error and success notifications
  - Real-time status updates

#### `main()` in main_working.py (CLI version)
- **Purpose**: Command-line interface loop
- **Process Flow**:
  1. Display welcome message
  2. Enter input loop
  3. Get URL from user
  4. Get optional output path
  5. Initiate download
  6. Show results
  7. Offer to download another
- **Features**:
  - Interactive command prompt
  - URL input handling
  - Output path customization
  - User feedback

### Data Flow
1. User inputs YouTube URL
2. Application validates input
3. Creates output directory if needed
4. Initializes download configuration
5. Processes download with progress tracking
6. Provides success/failure feedback

## Usage Guide

### Basic Usage

1. **Start the Application**
   ```bash
   python main.py
   ```

2. **Download a Video**
   - Enter the YouTube URL when prompted
   - Press Enter for default download location or specify custom path
   - Wait for download to complete

3. **Exit the Application**
   - Type 'q' when prompted for URL

### URL Format Support
- Standard YouTube URLs: `https://www.youtube.com/watch?v=VIDEO_ID`
- Short URLs: `https://youtu.be/VIDEO_ID`
- URLs with timestamps
- URLs with playlists (downloads single video)

### Output Directory
- Default: `./downloads/` in the application directory
- Custom: Any valid directory path on your system
- Creates directories automatically if they don't exist

## Code Documentation

### Main Module (`main.py`)
```python
def main():
    """
    Main application loop.
    Handles user interaction and coordinates video downloads.
    """
```

### Downloader Module (`downloader.py`)
```python
def download_video(url, output_path=None):
    """
    Downloads a YouTube video.
    
    Args:
        url (str): YouTube video URL
        output_path (str, optional): Download directory
        
    Returns:
        bool: Success status of download
    """
```

## Troubleshooting

### Common Issues and Solutions

1. **"URL cannot be empty" Error**
   - **Cause**: Empty or invalid URL input
   - **Solution**: Provide a valid YouTube URL

2. **Download Directory Access Error**
   - **Cause**: Insufficient permissions or invalid path
   - **Solution**: 
     - Use a directory with write permissions
     - Ensure path exists or use default

3. **Network-Related Issues**
   - **Cause**: Poor connection or YouTube API changes
   - **Solution**:
     - Check internet connection
     - Ensure yt-dlp is up to date

4. **Video Unavailable**
   - **Cause**: Video is private, deleted, or region-locked
   - **Solution**: 
     - Verify video availability in browser
     - Check for region restrictions

### Error Messages

| Error Message | Meaning | Solution |
|--------------|---------|----------|
| "URL cannot be empty" | No URL provided | Enter a valid YouTube URL |
| "An error occurred: HTTP Error 4xx" | Client-side error | Check URL validity |
| "An error occurred: HTTP Error 5xx" | Server-side error | Try again later |

## FAQ

### General Questions

1. **Q: Where are my downloaded videos saved?**
   - A: By default, in the 'downloads' folder in the application directory. You can specify a custom location during download.

2. **Q: What video quality will I get?**
   - A: The application downloads the best available quality automatically.

3. **Q: Can I download multiple videos at once?**
   - A: The application handles one video at a time, but you can queue multiple downloads in sequence.

4. **Q: Does it support playlist downloads?**
   - A: Currently, the application supports single video downloads only.

### Technical Questions

1. **Q: Why use yt-dlp instead of youtube-dl?**
   - A: yt-dlp is actively maintained and provides better compatibility with YouTube's latest changes.

2. **Q: Can I use this in a script?**
   - A: Yes, the `download_video()` function can be imported and used in other Python scripts.

3. **Q: How does error handling work?**
   - A: The application uses try-except blocks to catch and handle various errors, providing user-friendly feedback.

### Best Practices

1. **For Regular Use**
   - Keep yt-dlp updated
   - Use default download location for consistency
   - Check available disk space regularly

2. **For Custom Locations**
   - Use absolute paths when possible
   - Ensure write permissions
   - Avoid special characters in paths

3. **For Troubleshooting**
   - Check internet connection
   - Verify URL validity
   - Ensure sufficient disk space
   - Check for yt-dlp updates

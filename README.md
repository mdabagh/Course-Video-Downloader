# General Course Video Downloader

This is a general-purpose Python script to download videos from online course platforms. It uses Selenium to navigate course pages, extract video links, and download high-quality (or low-quality) videos with progress bars. The script is designed to be easy to customize for any user.

## Features
- **Sequential Downloading**: Downloads videos in the order specified in the `video_links` array.
- **Quality Selection**: Downloads high-quality videos by default; switch to low-quality by changing `quality_index`.
- **Progress Bar**: Shows download progress using `tqdm`.
- **Sequential File Naming**: Files are named like `01-Title.mp4`, `02-Title.mp4`, etc.
- **Link Extraction**: Extracts and prints all video URLs for each page, stored in an array.
- **Authentication**: Uses cookies for logged-in access to protected videos.

## Requirements
- **Python 3.8+**: The script is tested on Python 3.12 but should work on earlier versions.
- **Browser**: By default, uses Microsoft Edge. Ensure your browser version matches the WebDriver.
- **Libraries**:
  - `selenium`: For browser automation.
  - `requests`: For downloading videos.
  - `tqdm`: For progress bars.
- **WebDriver**: Download the version matching your browser:
  - For Microsoft Edge: From [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
  - For Google Chrome: From [ChromeDriver](https://googlechromelabs.github.io/chromedriver/).
  - For Mozilla Firefox: From [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

## Installation
1. Install Python from [python.org](https://www.python.org/) if not already installed.
2. Install required libraries using pip:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import requests
import os
from tqdm import tqdm

# Driver path for Microsoft Edge WebDriver (replace with your actual path)
driver_path = "C:\\msedgedriver.exe"  # Replace with the path to msedgedriver.exe

# Check if the driver exists
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"msedgedriver.exe not found at: {driver_path}. Please download it from https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ and match your Edge browser version.")

# Cookies for authentication (extract from your browser after logging into the course platform)
cookies = {
    'sessionid': 'your_session_id_here',  # Replace with your actual sessionid
    'csrftoken': 'your_csrf_token_here',  # Replace with your actual csrftoken
}

# Headers for download requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://example-course-site.com/',  # Replace with the course platform's URL
}

# Array of video links (replace with your course video paths and titles)
# Format: ("/course/path/to/video/", "Video Title")
video_links = [
    ("/course/path/to/video1/", "Video Title 1"),
    ("/course/path/to/video2/", "Video Title 2"),
    # Add more video links here
]

# Base URL for the site (replace with the actual course platform URL)
base_url = "https://example-course-site.com"  # Replace with the platform's base URL

# Quality selection: 0 for high quality (default), 1 for low quality
quality_index = 0  # Change to 1 if you want low quality

# Setup Edge browser with the driver path
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

try:
    # Loop through the video links with sequential numbering for file names
    for index, (link, title) in enumerate(video_links, 1):
        print(f"\nProcessing video {index:02d}: {title}")
        full_url = base_url + link

        # Open the page
        driver.get(full_url)

        # Add cookies
        for name, value in cookies.items():
            driver.add_cookie({'name': name, 'value': value})

        # Refresh page to apply cookies
        driver.get(full_url)

        # Wait for the <video> tag to appear (max 30 seconds)
        try:
            video_element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))
            )

            # Extract <source> tags and store links in array
            source_elements = video_element.find_elements(By.TAG_NAME, "source")
            video_urls = []
            if source_elements:
                for source_index, source in enumerate(source_elements, 1):
                    source_url = source.get_attribute("src")
                    if source_url:
                        video_urls.append(source_url)
                        print(f"Video URL {source_index} for '{title}': {source_url}")
                # Print the array of links
                print(f"All Video URLs for '{title}': {video_urls}")

                # Download only the selected quality
                if video_urls:
                    source_url = video_urls[quality_index]  # Select quality based on index
                    try:
                        # Get file size for progress bar
                        response = requests.head(source_url, headers=headers, cookies=cookies, allow_redirects=True)
                        file_size = int(response.headers.get('content-length', 0))

                        # Download with progress bar
                        response = requests.get(source_url, headers=headers, cookies=cookies, stream=True, timeout=10)
                        if response.status_code == 200:
                            # Sequential file naming (e.g., 01-Video Title 1.mp4)
                            filename = f"{index:02d}-{title}.mp4"
                            # Remove invalid characters in file name
                            filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()
                            with open(filename, 'wb') as f:
                                with tqdm(total=file_size, unit='B', unit_scale=True, desc=filename) as pbar:
                                    for chunk in response.iter_content(chunk_size=8192):
                                        if chunk:
                                            f.write(chunk)
                                            pbar.update(len(chunk))
                            print(f"Downloaded: {filename}")
                        else:
                            print(f"Failed to download video for '{title}': Status code {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"Error downloading video for '{title}': {str(e)}")
            else:
                print(f"No <source> tags found in <video> for '{title}'.")
        except Exception as e:
            print(f"Error processing '{title}': No video tag found or another issue occurred. {str(e)}")

finally:
    # Close the browser
    driver.quit()

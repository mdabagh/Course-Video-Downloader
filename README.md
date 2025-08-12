# 📥 General Course Video Downloader
*A universal Python script for downloading online course videos.*

---

### 📌 Overview
This is a general-purpose Python script to download videos from online course platforms.  
It uses **Selenium** to navigate course pages, extract video links, and download high- or low-quality videos with a **progress bar**.  
The script is **easy to customize** for any platform.

---

### ✨ Features
- **Sequential Downloading** – Downloads videos in the order specified in `video_links`.
- **Quality Selection** – High quality by default; switch to low quality with `quality_index`.
- **Progress Bar** – Shows download progress using `tqdm`.
- **Sequential File Naming** – Files named like `01-Title.mp4`, `02-Title.mp4`, etc.
- **Link Extraction** – Extracts and prints video URLs from course pages.
- **Authentication Support** – Uses cookies for protected videos.

---

### 📦 Requirements
- **Python**: 3.8+ (tested on 3.12)
- **Browser**: Edge (default), Chrome, or Firefox.
- **Libraries**:

```bash
pip install selenium requests tqdm
```

- **WebDriver**:  
  - [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
  - [ChromeDriver](https://googlechromelabs.github.io/chromedriver/)  
  - [GeckoDriver](https://github.com/mozilla/geckodriver/releases)  

---

### ⚙️ Installation
1. Install Python from [python.org](https://www.python.org/).
2. Install dependencies:

```bash
pip install selenium requests tqdm
```

3. Download and set up WebDriver:
   - **Edge** → Place `msedgedriver.exe` in `C:\WebDrivers\`
   - **Chrome** → Place `chromedriver.exe` in `C:\WebDrivers\`
   - **Firefox** → Place `geckodriver.exe` in `C:\WebDrivers\`
4. Update `driver_path` in the script.  
5. (Optional) Add WebDriver path to your **system PATH**.

---

### 🚀 Usage
1. **Extract Cookies**  
   - Log in to the course platform.  
   - Press `F12` → **Application** → **Cookies**.  
   - Copy `sessionid`, `csrftoken` (or relevant cookies) to the script.

2. **Customize the Script**  
   - **Driver Path** → set `driver_path` to your WebDriver location.  
   - **Browser** → change `webdriver.Edge` to `webdriver.Chrome` or `webdriver.Firefox` if needed.  
   - **Base URL** → set `base_url` (e.g., `"https://example.com"`).  
   - **Video Links**:

```python
video_links = [
    ("/course/path/to/video1/", "Video Title 1"),
    ("/course/path/to/video2/", "Video Title 2"),
]
```

   - **Quality** → `quality_index = 0` (high) or `1` (low).

3. **Run**

```bash
python download_course_videos.py
```

---

### 🛠 Troubleshooting
- **Driver Not Found** → Check path/version match with your browser.
- **Expired Cookies** → Extract cookies again.
- **No Video Found** → Inspect HTML; adjust tag search in code.
- **SSL Errors** → Try another network.

---

### 📜 License
Educational use only. Respect the platform’s terms of service.


</

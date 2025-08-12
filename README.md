```markdown
# General Course Video Downloader

[English](#english) | [فارسی](#فارسی)

## English

This is a general-purpose Python script to download videos from online course platforms. It uses Selenium to navigate course pages, extract video links, and download high-quality (or low-quality) videos with progress bars. The script is designed to be easy to customize for any user.

### Features
- **Sequential Downloading**: Downloads videos in the order specified in the `video_links` array.
- **Quality Selection**: Downloads high-quality videos by default; switch to low-quality by changing `quality_index`.
- **Progress Bar**: Shows download progress using `tqdm`.
- **Sequential File Naming**: Files are named like `01-Title.mp4`, `02-Title.mp4`, etc.
- **Link Extraction**: Extracts and prints all video URLs for each page, stored in an array.
- **Authentication**: Uses cookies for logged-in access to protected videos.

### Requirements
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

### Installation
1. Install Python from [python.org](https://www.python.org/) if not already installed.
2. Install required libraries using pip:
   ```
   pip install selenium requests tqdm
   ```
3. Download and set up WebDriver:
   - For Edge: Download from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), extract `msedgedriver.exe` to a folder like `C:\WebDrivers\`, and update `driver_path` in the script.
   - For Chrome: Download from [ChromeDriver](https://googlechromelabs.github.io/chromedriver/), extract `chromedriver.exe`, update `driver_path`, and change `webdriver.Edge` to `webdriver.Chrome`.
   - For Firefox: Download from [GeckoDriver](https://github.com/mozilla/geckodriver/releases), extract `geckodriver.exe`, update `driver_path`, and change `webdriver.Edge` to `webdriver.Firefox`.
4. Add the WebDriver path to your system's PATH (optional but recommended for easier use).

### Usage
1. **Extract Cookies**:
   - Log in to the course platform in your browser (e.g., Edge, Chrome, or Firefox).
   - Press `F12` to open Developer Tools.
   - Go to the **Application** tab > **Cookies** > Select the platform's domain.
   - Copy the values of relevant session cookies (e.g., `sessionid` and `csrftoken`).
   - Paste them into the `cookies` dictionary in the script.

2. **Customize the Script**:
   - **Driver Path**: Update `driver_path` with the full path to your WebDriver executable (e.g., `"C:\\WebDrivers\\msedgedriver.exe"` for Edge, `"C:\\WebDrivers\\chromedriver.exe"` for Chrome, or `"C:\\WebDrivers\\geckodriver.exe"` for Firefox). Use double backslashes (`\\`) in the path.
   - **Browser Selection**: The script defaults to Edge (`webdriver.Edge`). For Chrome, replace with `webdriver.Chrome(service=Service(executable_path=driver_path))`. For Firefox, replace with `webdriver.Firefox(service=Service(executable_path=driver_path))`.
   - **Video Links Array**: Fill the `video_links` array with tuples of (video path, title). The path is the relative URL after the base URL (copy from the course page URL). Titles are used for file naming.
     Example:
     ```python
     video_links = [
         ("/course/path/to/video1/", "Video Title 1"),
         ("/course/path/to/video2/", "Video Title 2"),
     ]
     ```
   - **Base URL**: Update `base_url` with the platform's base URL (e.g., `"https://example-course-site.com"`).
   - **Quality Selection**: Set `quality_index = 0` for high quality (default) or `1` for low quality. Video links are usually in the `<video>` tag's `src` attribute or in nested `<source>` tags' `src` attributes. The script extracts from `<source>` tags; high quality is typically the first `<source>` (index 0), low quality the second (index 1).
   - **HTML Structure**: Videos are often embedded in a `<video>` tag. The direct link may be in the `<video src="...">` attribute or in `<source src="...">` tags inside `<video>`. The script checks `<source>` tags; if your platform uses a different structure, inspect the page HTML with Developer Tools and adjust the code (e.g., change `By.TAG_NAME, "source"` if needed).

3. **Run the Script**:
   - Save the script as `download_course_videos.py`.
   - Run it in your terminal:
     ```
     python download_course_videos.py
     ```
   - The script will process each video, extract links, print the URL array, and download the selected quality with a progress bar.
   - Downloaded files will be saved in the current directory with names like `01-Video Title 1.mp4`.

### Troubleshooting
- **Driver Not Found**: Ensure the WebDriver path is correct and the file exists. Match the version with your browser (e.g., Edge, Chrome, or Firefox).
- **Cookies Expired**: Re-extract cookies if authentication fails (e.g., 401/403 errors).
- **Timeout or No Video Tag**: Increase the wait time in `WebDriverWait(driver, 30)` if videos load slowly. Verify the `<video>` or `<source>` tags exist by inspecting the page HTML.
- **SSL Handshake Errors**: Use a different network or check browser settings if network issues occur.
- **Link Expiration**: Video links may be temporary. Re-run the script if links expire during download.

### License
This script is provided "as is" for educational purposes. Respect the platform's terms of service.

### Contributing
Fork the repository on GitHub, make changes, and submit a pull request. Suggestions for improvements are welcome!

---

## فارسی

# دانلودکننده عمومی ویدیوهای دوره‌های آنلاین

این ابزار پایتون یک اسکریپت عمومی برای دانلود ویدیوهای دوره‌های آنلاین است. از Selenium برای استخراج لینک‌های ویدیو از صفحات دوره استفاده می‌کند، فقط ویدیوهای با کیفیت بالا (یا پایین اگر مشخص شود) دانلود می‌کند، پیشرفت دانلود را نمایش می‌دهد، و فایل‌ها را به‌صورت ترتیبی با عنوان نام‌گذاری می‌کند. کاربران می‌توانند آرایه `video_links` را با لینک‌های ویدیوها و عناوین سفارشی کنند.

## ویژگی‌ها
- **دانلود ترتیبی**: ویدیوها را به ترتیب مشخص‌شده در آرایه `video_links` دانلود می‌کند.
- **انتخاب کیفیت**: به‌طور پیش‌فرض کیفیت بالا دانلود می‌شود؛ برای کیفیت پایین `quality_index` را تغییر دهید.
- **نوار پیشرفت**: پیشرفت دانلود را با استفاده از `tqdm` نمایش می‌دهد.
- **نام‌گذاری ترتیبی فایل‌ها**: فایل‌ها به‌صورت `01-عنوان.mp4`، `02-عنوان.mp4` و غیره نام‌گذاری می‌شوند.
- **استخراج لینک**: لینک‌های ویدیو را برای هر صفحه استخراج و در آرایه ذخیره می‌کند و چاپ می‌کند.
- **احراز هویت**: از کوکی‌ها برای دسترسی به ویدیوهای محافظت‌شده استفاده می‌کند.

## نیازمندی‌ها
- **پایتون 3.8+**: اسکریپت روی پایتون 3.12 تست شده اما روی نسخه‌های قدیمی‌تر نیز کار می‌کند.
- **مرورگر**: به‌طور پیش‌فرض از Microsoft Edge استفاده می‌کند. مطمئن شوید نسخه WebDriver با مرورگر شما مطابقت دارد.
- **کتابخانه‌ها**:
  - `selenium`: برای اتوماسیون مرورگر.
  - `requests`: برای دانلود ویدیوها.
  - `tqdm`: برای نوار پیشرفت.
- **WebDriver**: نسخه متناظر با مرورگر را دانلود کنید:
  - برای Microsoft Edge: از [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
  - برای Google Chrome: از [ChromeDriver](https://googlechromelabs.github.io/chromedriver/).
  - برای Mozilla Firefox: از [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

## نصب
1. اگر پایتون نصب نیست، از [python.org](https://www.python.org/) دانلود و نصب کنید.
2. کتابخانه‌های موردنیاز را با pip نصب کنید:
   ```
   pip install selenium requests tqdm
   ```
3. WebDriver را دانلود و تنظیم کنید:
   - برای Edge: از [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) دانلود کنید، `msedgedriver.exe` را در پوشه‌ای مثل `C:\WebDrivers` استخراج کنید، و `driver_path` را در اسکریپت به‌روزرسانی کنید.
   - برای Chrome: از [ChromeDriver](https://googlechromelabs.github.io/chromedriver/) دانلود کنید، `chromedriver.exe` را استخراج کنید، `driver_path` را به‌روزرسانی کنید، و `webdriver.Edge` را به `webdriver.Chrome` تغییر دهید.
   - برای Firefox: از [GeckoDriver](https://github.com/mozilla/geckodriver/releases) دانلود کنید، `geckodriver.exe` را استخراج کنید، `driver_path` را به‌روزرسانی کنید، و `webdriver.Edge` را به `webdriver.Firefox` تغییر دهید.
4. مسیر WebDriver را به PATH سیستم اضافه کنید (اختیاری اما توصیه‌شده برای استفاده آسان‌تر).

## نحوه استفاده
1. **استخراج کوکی‌ها**:
   - در مرورگر خود (مثل Edge، Chrome یا Firefox) وارد حساب پلتفرم دوره شوید.
   - کلید `F12` را فشار دهید تا ابزار توسعه‌دهندگان باز شود.
   - به تب **Application** > **Cookies** بروید و دامنه پلتفرم را انتخاب کنید.
   - مقادیر کوکی‌های جلسه مرتبط (مثل `sessionid` و `csrftoken`) را کپی کنید.
   - این مقادیر را در دیکشنری `cookies` اسکریپت جای‌گذاری کنید.

2. **سفارشی‌سازی اسکریپت**:
   - **مسیر درایور**: `driver_path` را با مسیر کامل WebDriver به‌روزرسانی کنید (مثلاً `"C:\\WebDrivers\\msedgedriver.exe"` برای Edge، `"C:\\WebDrivers\\chromedriver.exe"` برای Chrome، یا `"C:\\WebDrivers\\geckodriver.exe"` برای Firefox). از دو بک‌اسلش (`\\`) استفاده کنید.
   - **انتخاب مرورگر**: اسکریپت به‌طور پیش‌فرض از Edge (`webdriver.Edge`) استفاده می‌کند. برای Chrome، آن را به `webdriver.Chrome(service=Service(executable_path=driver_path))` تغییر دهید. برای Firefox، به `webdriver.Firefox(service=Service(executable_path=driver_path))` تغییر دهید.
   - **آرایه لینک‌های ویدیو**: آرایه `video_links` را با تاپل‌های (مسیر ویدیو، عنوان) پر کنید. مسیر، URL نسبی پس از پایه URL است (از URL صفحه دوره کپی کنید). عناوین برای نام‌گذاری فایل استفاده می‌شوند.
     مثال:
     ```python
     video_links = [
         ("/course/path/to/video1/", "عنوان ویدیو 1"),
         ("/course/path/to/video2/", "عنوان ویدیو 2"),
     ]
     ```
   - **پایه URL**: `base_url` را با URL پایه پلتفرم به‌روزرسانی کنید (مثل `"https://example-course-site.com"`).
   - **انتخاب کیفیت**: `quality_index = 0` برای کیفیت بالا (پیش‌فرض) یا `1` برای کیفیت پایین تنظیم کنید. لینک‌های ویدیو معمولاً در ویژگی `src` تگ `<video>` یا ویژگی `src` تگ‌های `<source>` داخل `<video>` قرار دارند. اسکریپت از تگ‌های `<source>` استخراج می‌کند؛ کیفیت بالا معمولاً اولین تگ `<source>` (اندیس 0) است و کیفیت پایین دومین (اندیس 1). برای بررسی ساختار HTML، صفحه را با ابزار توسعه‌دهندگان مرورگر باز کنید و تگ `<video>` را چک کنید. اگر پلتفرم ساختار متفاوتی دارد، کد را تنظیم کنید (مثل تغییر `By.TAG_NAME, "source"`).

3. **اجرای اسکریپت**:
   - اسکریپت را به عنوان `download_course_videos.py` ذخیره کنید.
   - در ترمینال اجرا کنید:
     ```
     python download_course_videos.py
     ```
   - اسکریپت هر ویدیو را پردازش می‌کند، لینک‌ها را استخراج می‌کند، آرایه URLها را چاپ می‌کند، و ویدیو با کیفیت انتخاب‌شده را با نوار پیشرفت دانلود می‌کند.
   - فایل‌های دانلودشده در دایرکتوری فعلی با نام‌هایی مثل `01-عنوان ویدیو 1.mp4` ذخیره می‌شوند.

## عیب‌یابی
- **درایور پیدا نشد**: مطمئن شوید مسیر WebDriver درست است و فایل وجود دارد. نسخه را با مرورگر (مثل Edge، Chrome یا Firefox) مطابقت دهید.
- **کوکی‌های منقضی**: اگر احراز هویت شکست خورد (خطاهای 401/403)، کوکی‌ها را دوباره استخراج کنید.
- **زمان انتظار یا عدم وجود تگ ویدیو**: اگر ویدیوها کند بارگذاری می‌شوند، زمان انتظار در `WebDriverWait(driver, 30)` را افزایش دهید. ساختار HTML صفحه را بررسی کنید تا تگ `<video>` یا `<source>` وجود داشته باشد.
- **خطاهای SSL**: اگر مشکلات شبکه وجود دارد، تنظیمات مرورگر را چک کنید یا شبکه دیگری امتحان کنید.

## لایسنس
این اسکریپت "به همان صورت" برای اهداف آموزشی ارائه شده است. شرایط خدمات پلتفرم را رعایت کنید.

## مشارکت
ریپازیتوری را در گیت‌هاب فورک کنید، تغییرات را اعمال کنید و pull request ارسال کنید. پیشنهادات برای بهبود استقبال می‌شود!
```

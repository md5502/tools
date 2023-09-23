# tools
in this ripo i publish my codes that make my life easy 

Certainly! Here's a README.md file for your GitHub repository to explain the code usage, required packages to install, and any additional information:

---

# Video Downloader

This Python script allows you to download videos from Aparat playlists. It utilizes Selenium and requests to automate the process of navigating through a playlist and downloading videos in 720p quality.

### Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install requests selenium tqdm webdriver_manager
   ```

3. Download and install ChromeDriver using `webdriver_manager`:

   ```bash
   webdriver_manager chrome
   ```

4. Run the script:

   ```bash
   python video_downloader.py
   ```

5. You will be prompted to enter the URL of the Aparat playlist you want to download.

6. The script will download the videos in 720p quality and save them in the specified directory.

### Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/): Python library for web automation
- [Requests](https://pypi.org/project/requests/): Python library for making HTTP requests
- [tqdm](https://pypi.org/project/tqdm/): Python library for displaying progress bars
- [webdriver_manager](https://pypi.org/project/webdriver-manager/): Python library for managing web drivers like ChromeDriver

### Configuration

You can modify the script to change the quality of downloaded videos or adjust the waiting time between video downloads by modifying the `time.sleep()` value in the `main()` function.

```python
# Adjust the sleep time between video downloads (in seconds)
time.sleep(10)
```
=======================================================================================================

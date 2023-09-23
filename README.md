# TOOLS Repository

Welcome to my tools repository! This repository contains various code snippets and projects that have made my life easier. Whether it's a single file utility or a collection of scripts organized in a folder, you'll find a variety of useful code here.

## About the Repository

In this repository, I follow a simple convention:

- **Single File Codes:** If a code is contained in a single file, it will be committed directly to the repository.

- **Folder of Files:** If a code consists of multiple files and requires a folder structure, the entire folder will be committed. You'll find explanations and usage instructions for the code in a separate section within this README.md file.

Each section is divided by "---" to help you navigate and find the code you need quickly.

## How to Use

To access and use a specific code or project, follow these steps:

1. Navigate to the code or project folder in the repository.

2. Download the corresponding file or folder to your local machine.

3. Refer to the "Usage" section within the README.md file of that specific code or project for detailed instructions on how to use it effectively.

## Disclaimer

Please make sure to review and respect the licenses and terms of use associated with each code snippet or project. Use these resources responsibly and only for legal and ethical purposes.

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
---

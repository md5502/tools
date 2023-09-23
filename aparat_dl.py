import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Function to download a video
def download_video(video_url, save_path, video_name, playlist_name):
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        os.makedirs(os.path.join(save_path, playlist_name), exist_ok=True)
        file_name = os.path.join(save_path, playlist_name, video_name + '.mp4')
        
        print(f'Downloading {video_name}:')
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, ncols=100)

        with open(file_name, 'wb') as file:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                progress_bar.update(len(data))

        progress_bar.close()

        if total_size != 0 and progress_bar.n != total_size:
            print("Download failed.")
        else:
            print(f"{video_name} downloaded successfully to {file_name}")
    except Exception as e:
        print(f"Failed to download {video_name}: {str(e)}")

# Function to get video URLs from a playlist
def get_video_urls(driver):
    playlist_name = driver.find_element(By.CLASS_NAME, "playlist-field").text
    playlist = driver.find_element(By.CLASS_NAME, "playlist-list")
    video_posters = playlist.find_elements(By.CLASS_NAME, "poster")
    video_urls = []

    for index, video in enumerate(video_posters):
        titled_link = video.find_element(By.CLASS_NAME, "titled-link")
        video_url = titled_link.get_attribute("href")
        video_urls.append((index, titled_link.text, video_url))

    return playlist_name, video_urls

# Main function
def main():
    try:
        url = input('Enter the URL: ')
        
        driver = webdriver.Chrome()
        
        driver.get(url)

        playlist_name, video_urls = get_video_urls(driver)
        videos = []

        for index, name, video_url in video_urls:
            driver.get(video_url)
            time.sleep(10)
            download_button = driver.find_element(By.CLASS_NAME, "download-button")
            download_button.click()
            
            try:
                dl_720 = driver.find_element(By.ID, "720p").get_attribute("href")
                videos.append((index, f"{index}-{name}", dl_720))
                print("=" * 50, "\n", index, ' DONE')
            except NoSuchElementException:
                print(f"720p video not found for {name}")

        for video_index, video_name, video_url in videos:
            download_video(video_url, r"C:\Users\mohammad\Desktop\aparat_dl", video_name, playlist_name)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

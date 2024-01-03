import os
import requests
from threading import Thread
from urllib.parse import urlparse
import time

def download_file(url):
    start_time = time.time()  # Start measuring time

    response = requests.head(url)
    file_size = int(response.headers.get('content-length', 0))

    # Getting the file name from the URL
    file_name = os.path.basename(urlparse(url).path)
    if not file_name:
        print("Could not determine file name from URL")
        return

    if file_size <= 1 * 1024 * 1024:  # 1MB
        simple_download(url, file_name)
    else:
        parallel_download(url, file_name, file_size)

    end_time = time.time()  # Stop measuring time
    download_time = end_time - start_time
    print(f"Download completed in {download_time:.2f} seconds")

def simple_download(url, file_name):
    r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded {file_name} using a simple method")

def parallel_download(url, file_name, file_size):
    # Define a function to download a piece of the file
    def download_chunk(url, start, end, file_name):
        headers = {'Range': f'bytes={start}-{end}'}
        r = requests.get(url, headers=headers)
        with open(file_name, "r+b") as f:
            f.seek(start)
            f.write(r.content)

    # Split the file into chunks and download them in parallel
    num_threads = 4
    chunk_size = file_size // num_threads
    threads = []
    with open(file_name, "wb") as f:
        f.truncate(file_size)
    for i in range(num_threads):
        start = chunk_size * i
        end = start + chunk_size
        if i == num_threads - 1:
            end = file_size
        thread = Thread(target=download_chunk, args=(url, start, end, file_name))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print(f"Downloaded {file_name} using parallel method")

# Example URL (you can replace this with any URL of your choice)
url = ""
download_file(url)


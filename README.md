# Parallel File Downloader

This Python script enables parallel file downloads from a URL, utilizing multiple threads for enhanced performance. The script intelligently selects between parallel download and a simple method based on the file's content length.

## Features

- **Parallel Download:** Utilizes multiple threads for faster downloads.
- **Simple Download:** Falls back to a single-threaded method if content length is unavailable or exceeds a specified limit.
- **Performance Measurement:** Tracks download time for analysis.

## Requirements

- Python 3.x
- [Requests library](https://docs.python-requests.org/en/latest/): `pip install requests`

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/rajibhasan01/parallel-file-downloader.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd parallel-file-downloader
    ```

3. **Run the script with a URL:**

    ```bash
    python parallel-file-downloader.py
    ```

    Replace the url with the desired file url in code.

## Configuration

Adjust the `num_threads` variable in the script to control the number of parallel download threads.


## Contributing

Contributions are welcome! Open an issue or submit a pull request.


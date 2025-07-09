import threading
import requests
from tqdm import tqdm
import os

# Model file URL from HuggingFace (you can change this)
FILE_URL = 'https://huggingface.co/bert-base-uncased/resolve/main/pytorch_model.bin'
OUTPUT_FILE = 'bert_model.bin'
NUM_THREADS = 8

# Shared progress bar lock
progress_lock = threading.Lock()


def get_file_size(url):
    response = requests.head(url, allow_redirects=True)
    if response.status_code == 200:
        return int(response.headers.get('Content-Length', 0))
    else:
        raise Exception(f"Failed to get file size: {response.status_code}")


def download_range(url, start, end, thread_id, result, progress_bar):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code not in (200, 206):
        raise Exception(
            f"[Thread-{thread_id}] Failed with status {response.status_code}")

    data = bytearray()
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            data.extend(chunk)
            with progress_lock:
                progress_bar.update(len(chunk))

    result[thread_id] = data


def multi_threaded_download(url, output_file, num_threads):
    file_size = get_file_size(url)
    print(f"📦 Total file size: {file_size // (1024*1024)} MB")

    chunk_size = file_size // num_threads
    ranges = [(i * chunk_size,
               (i + 1) * chunk_size - 1 if i < num_threads - 1 else file_size - 1)
              for i in range(num_threads)]

    result = [None] * num_threads
    threads = []

    with tqdm(total=file_size, unit='B', unit_scale=True, desc='Downloading') as progress_bar:
        for i, (start, end) in enumerate(ranges):
            t = threading.Thread(target=download_range,
                                 args=(url, start, end, i, result, progress_bar))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    with open(output_file, 'wb') as f:
        for part in result:
            f.write(part)

    print(f"\n✅ Download complete: {output_file}")


if __name__ == '__main__':
    multi_threaded_download(FILE_URL, OUTPUT_FILE, NUM_THREADS)

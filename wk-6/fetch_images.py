import requests
import os
import hashlib
from urllib.parse import urlparse
from datetime import datetime

def get_file_hash(filepath):
    """Generate SHA256 hash of a file to detect duplicates."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def log_message(folder, message):
    """Append log messages to a log file with timestamp."""
    log_path = os.path.join(folder, "download_log.txt")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")

def get_unique_filename(folder, filename):
    """Ensure filename is unique by appending _1, _2, etc. if needed."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename

def download_image(url, folder, existing_hashes, stats):
    try:
        # Fetch the image
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check HTTP headers
        content_type = response.headers.get("Content-Type", "")
        content_length = response.headers.get("Content-Length")

        if not content_type.startswith("image/"):
            msg = f"Skipped {url} (not an image: {content_type})"
            print(f"✗ {msg}")
            log_message(folder, msg)
            stats["skipped"] += 1
            return

        if content_length and int(content_length) > 5 * 1024 * 1024:  # limit: 5MB
            msg = f"Skipped {url} (file too large: {content_length} bytes)"
            print(f"✗ {msg}")
            log_message(folder, msg)
            stats["skipped"] += 1
            return

        # Extract filename or assign default
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        # Ensure unique filename
        filename = get_unique_filename(folder, filename)
        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        # Check for duplicates using file hash
        file_hash = get_file_hash(filepath)
        if file_hash in existing_hashes:
            os.remove(filepath)  # delete duplicate
            msg = f"Duplicate found. Skipped {filename} ({url})"
            print(f"✗ {msg}")
            log_message(folder, msg)
            stats["duplicates"] += 1
            return
        else:
            existing_hashes.add(file_hash)

        msg = f"Downloaded {filename} from {url}"
        print(f"✓ {msg}")
        log_message(folder, msg)
        stats["downloaded"] += 1

    except requests.exceptions.RequestException as e:
        msg = f"Connection error while fetching {url}: {e}"
        print(f"✗ {msg}")
        log_message(folder, msg)
        stats["skipped"] += 1
    except Exception as e:
        msg = f"Error saving {url}: {e}"
        print(f"✗ {msg}")
        log_message(folder, msg)
        stats["skipped"] += 1

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Please enter image URLs (comma-separated): ").split(",")

    # Create directory if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Track hashes of downloaded files
    existing_hashes = set()

    # Stats for summary
    stats = {"downloaded": 0, "skipped": 0, "duplicates": 0}

    # Download each image
    for url in urls:
        url = url.strip()
        if url:
            download_image(url, folder, existing_hashes, stats)

    total = len([u for u in urls if u.strip()])

    # Summary Report
    print("\n✓ All processing done. Check 'download_log.txt' for details.")
    print("Summary:")
    print(f"- Total URLs provided: {total}")
    print(f"- Successfully downloaded: {stats['downloaded']}")
    print(f"- Skipped (not images / too large / errors): {stats['skipped']}")
    print(f"- Duplicates removed: {stats['duplicates']}")
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()

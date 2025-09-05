# Image Fetcher

A simple Python script to download images from the web and save them locally. This project demonstrates how to use Python’s `requests` library, file handling, and logging and is part of the week 6 assignment for python module at PLP.

## 📂 Project Structure
Desktop/ └── Python/ ├── venv/ # Virtual environment └── wk-6/ ├── fetch_images.py # Main script ├── README.md # Project documentation └── Fetched_Images/ # Folder where images & logs are saved └── download_log.txt


## ⚙️ Setup Instructions

1. **Clone or Copy Project**

   Navigate to your working directory:

   ```bash
   cd ~/Desktop/Python/wk-6
   Create a Virtual Environment (recommended)

    python -m venv venv
    Activate the virtual environment:

    Windows (Git Bash / PowerShell):

    source venv/Scripts/activate
    Linux/Mac:

    source venv/bin/activate
    You should see
    (venv)
    at the start of your terminal line.

### Install Dependencies

This project requires requests:

pip install requests
▶️ Running the Script
Run the script from inside the
wk-6 folder: python fetch_images.py
Or from the root folder using the full path: python wk-6/fetch_images.py

### 📦 Output
Downloaded images will be saved inside the Fetched_Images/ folder.

A download_log.txt file will also be created inside Fetched_Images/ , containing a log of all downloads (successful or failed).

### 🛠️ Requirements
Python 3.10+ (tested with Python 3.13) requests library (pip install requests)
📝 Example Log File
Inside Fetched_Images/download_log.txt you’ll see entries like:

[2025-09-05 14:32:10] SUCCESS - Downloaded: cat.jpg
[2025-09-05 14:32:11] ERROR   - Failed to fetch: dog.jpg (404 Not Found)

### 🚀 Future Improvements
Add a progress bar for downloads.
Allow batch downloading from a .txt file of URLs.
Add a retry mechanism for failed downloads.

## Author
[Salome Mundia]
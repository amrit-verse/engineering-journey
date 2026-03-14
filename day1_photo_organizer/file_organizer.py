import os
import shutil

downloads = os.path.expanduser("~/Downloads")

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".gz"]
}

for filename in os.listdir(downloads):
    file_path = os.path.join(downloads, filename)

    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if any(filename.lower().endswith(ext) for ext in extensions):

                folder_path = os.path.join(downloads, folder)
                os.makedirs(folder_path, exist_ok=True)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved {filename} → {folder}")
                break

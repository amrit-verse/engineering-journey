import os
import shutil
from datetime import datetime

source_folder = "/media/D/iPhone Photos"

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):

        timestamp = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(timestamp)

        year = date.strftime("%Y")
        month = date.strftime("%m_%B")

        target_folder = os.path.join(source_folder, year, month)

        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder, filename))

        print(f"Moved {filename} → {year}/{month}")

import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

source_folder = "/media/D/iPhone Photos"

def get_photo_date(path):
    try:
        img = Image.open(path)
        exif = img._getexif()
        if exif:
            for tag, value in exif.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except:
        pass
    return None


for file in os.listdir(source_folder):
    path = os.path.join(source_folder, file)

    if os.path.isfile(path):

        ext = file.lower().split(".")[-1]

        if ext in ["jpg", "jpeg", "png", "heic"]:

            date = get_photo_date(path)

            if date:
                year = date.strftime("%Y")
                month = date.strftime("%Y-%m")

                dest = os.path.join(source_folder, "Photos", year, month)

                os.makedirs(dest, exist_ok=True)

                shutil.move(path, os.path.join(dest, file))

                print(f"Moved {file} → {dest}")

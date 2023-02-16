# /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import os
import shutil


download_path = r"/Users/ishkandamishra/Downloads"
wallpaper_path = r"/Users/ishkandamishra/Pictures/Wallpaper Dump"

def sort_wallpaper(download_path, wallpaper_path):
    #image_extensions = [".jpeg", ".jpg" , ".png", ".webp"]
    for dirpath, dnames, fnames in os.walk(download_path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp") or f.endswith(".jpeg"):
                sourcepath = os.path.join(download_path, f)
                destination_path = os.path.join(wallpaper_path, f)
                shutil.copy(sourcepath, destination_path)
                os.remove(sourcepath)
    print("Done")

sort_wallpaper(download_path, wallpaper_path)
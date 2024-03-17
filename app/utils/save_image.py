import os
import shutil

PATH = "../assets/images/"

def save_image(file, path):
    try:
        os.makedirs(PATH, exist_ok=True)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        print(f"Supuesto PATH: {path}")
    finally:
        file.file.close()

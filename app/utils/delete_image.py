import os


def delete_image(path: str):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Error: {e}")
        raise e

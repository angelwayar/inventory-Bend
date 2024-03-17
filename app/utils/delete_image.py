import os


def delete_image(path: str):
    try:
        print(f"El path es: {path}")
        os.remove(path)
    except Exception as e:
        print(f"Error: {e}")
        raise e

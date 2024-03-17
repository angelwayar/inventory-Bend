import base64


def read_image(path: str | None):
    try:
        if path is not None:
            with open(path, 'rb') as image_file:
                image_bytes = image_file.read()

            image_base64 = base64.b64encode(image_bytes)

            return image_base64.decode("utf-8")

        return ''
    except Exception as _e:
        return ''


def image_exists(path: str):
    try:
        with open(path, 'rb') as image_file:
            image_file.read()

        return True

    except Exception as _e:
        return False

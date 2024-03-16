import base64

from typing import List, Optional

from pydantic import BaseModel

PATH = "../assets/images/"


class Product(BaseModel):
    id: Optional[str] = None
    code: Optional[str] = None
    supplier: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    height: Optional[float] = None
    width: Optional[float] = None
    depth: Optional[float] = None
    retail: Optional[int] = None
    images: Optional[List[str]] = None
    brand: Optional[str] = None

    def get_image_product(path: str | None):
        try:
            if path is not None:
                with open(path, 'rb') as image_file:
                    image_bytes = image_file.read()

                image_base64 = base64.b64encode(image_bytes)

                return image_base64.decode("utf-8")

            return ''
        except Exception as _e:
            print(f"Error al leer la imagen: {path}")
            return ''

    @classmethod
    def from_document(cls, document: dict) -> "Product":
        document["code"] = str(document.get("code", ""))
        document["year"] = str(document.get("year", ""))
        image_array = []
        images = document.get("images", None)

        _id = document.get("_id", None)

        if _id:
            document["id"] = str(_id)

        if images and len(images) > 0:
            for image in images:
                imagebase64 = cls.get_image_product(path=image)
                image_array.append(imagebase64)

            document["images"] = image_array

        return cls(**document)


class UpdateProduct(BaseModel):
    code: Optional[str] = None
    supplier: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    height: Optional[float] = None
    width: Optional[float] = None
    depth: Optional[float] = None
    retail: Optional[int] = None
    images: Optional[List[str]] = None
    brand: Optional[str] = None

    @classmethod
    def from_document(cls, document: dict) -> "UpdateProduct":
        document["code"] = str(document.get("code", ""))
        document["year"] = str(document.get("year", ""))

        return cls(**document)

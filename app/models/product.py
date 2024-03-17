import base64

import json
from typing import List, Optional

from pydantic import BaseModel, model_validator

from app.utils.read_image import read_image

PATH = "../assets/images/"


class ProductCreate(BaseModel):
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

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


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
                imagebase64 = read_image(path=image)
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

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value

    @classmethod
    def from_document(cls, document: dict) -> "UpdateProduct":
        document["code"] = str(document.get("code", ""))
        document["year"] = str(document.get("year", ""))

        return cls(**document)

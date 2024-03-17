from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel
from pymongo import MongoClient

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
        images_array = []
        images = document.get("images", "")

        document["code"] = str(document.get("code", ""))
        document["year"] = str(document.get("year", ""))

        if images:
            value =  images[0].replace('.0', '')
            images_array.append(value)
            document["images"] = images_array

        return cls(**document)


client = MongoClient("mongodb://127.0.0.1:27017/inventory")
db = client["inventory"]
collection = db["products"]

cursor = collection.find({})

for document in cursor:
    id = document.get("_id", None)
    print(id)

    product_updated = UpdateProduct.from_document(document=document)

    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": product_updated.model_dump()}
    )

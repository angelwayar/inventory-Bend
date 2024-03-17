from typing import List
from datetime import datetime

from bson import ObjectId
from fastapi import UploadFile
from models.product import Product
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import ValidationError

from app.models.product import UpdateProduct
from app.utils.read_image import read_image
from app.utils.save_image import save_image
from app.utils.delete_image import delete_image

client = AsyncIOMotorClient("mongodb://127.0.0.1:27017/inventory")
# client = AsyncIOMotorClient("mongodb://mongo_db:27017/inventory")
database = client.inventory
collection = database.products

PATH = "../assets/images/"


async def get_one_product_id(id: str):
    try:
        document = await collection.find_one({"_id": ObjectId(id)})
        product = Product.from_document(document=document)

        return product
    except ValidationError as e:
        print(e.json())


async def get_all_products():
    try:
        products = []
        cursor = collection.find({}).limit(10)

        async for document in cursor:
            products.append(Product.from_document(document=document))

        return products
    except Exception as e:
        print(e.json())


async def get_one_product_by_code(code: str):
    try:
        document = await collection.find_one({"code": code})
        if document is not None:
            product = Product.from_document(document=document)
            return product
    except Exception as e:
        print(e.json())


async def create_product(product, files: List[UploadFile]):
    try:
        array_image = []

        for file in files:
            fileName = file.filename.replace(' ', '')
            path = PATH + fileName

            if len(read_image(path=path)) == 0:
                array_image.append(path)
                save_image(file, path=path)
            else:
                raise f'La imagen ya existe {file.filename}'

        product["images"] = array_image

        new_product = await collection.insert_one(product)
        document_created = await collection.find_one({"_id": new_product.inserted_id})

        return Product.from_document(document=document_created)

    except Exception as e:
        print(f"Error: {e}")
        raise e


async def update_product(id: str, data: UpdateProduct):
    try:
        product = {k: v for k, v in data.model_dump().items() if v is not None}
        await collection.update_one({"_id": ObjectId(id)}, {"$set": product})

        document = await collection.find_one({"_id": ObjectId(id)})
        product_updated = Product.from_document(document=document)

        return product_updated

    except Exception as _e:
        raise _e


async def delete_product(id: str):
    document = await collection.find_one({"_id": ObjectId(id)})

    if document:
        images = document.get("images", None)
        if (images is not None) and (len(images) > 0):
            for image in images:
                delete_image(path=image)

        await collection.delete_one({"_id": ObjectId(id)})
    else:
        return False

    return True

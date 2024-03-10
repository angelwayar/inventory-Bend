import math
from motor.motor_asyncio import AsyncIOMotorClient
from models.product import Product
from pydantic import ValidationError
from bson import ObjectId

client = AsyncIOMotorClient("mongodb://127.0.0.1:27017/inventory")
# client = AsyncIOMotorClient("mongodb://mongo_db:27017/inventory")
database = client.inventory
collection = database.products


async def get_one_product_id(id: str):
    try:
        document = await collection.find_one({"_id": ObjectId(id)})
        product =  Product.from_document(document=document)

        return product
    except ValidationError as e:
        print(e.json())

def replace_nan(value):
    return value if not math.isnan(value) else None

async def get_all_products():
    try:
        products = []
        cursor = collection.find({}).limit(10)

        async for document in cursor:
            products.append(Product.from_document(document=document))

        return products    
    except ValidationError as e:
        print(e.json())


async def create_product(product):
    new_product = await collection.insert_one(product)
    created_product = await collection.find_one({"_id": new_product.inserted_id})

    return created_product


async def update_product(id: str, product):
    await collection.update_one({"_id": id}, {"$set": product})
    document = await collection.find_one({"_id": id})

    return document


async def delete_product(id: str):
    await collection.delete_one({"_id": id})

    return True

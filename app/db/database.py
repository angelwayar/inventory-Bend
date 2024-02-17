from motor.motor_asyncio import AsyncIOMotorClient
from models.product import Product

client = AsyncIOMotorClient("mongodb://localhost")
database = client.inventorydatabase
collection = database.products


async def get_one_product_id(id):
    product = await collection.find_one({"_id": id})
    return product


async def get_all_products():
    products = []
    cursor = collection.find({})

    async for document in cursor:
        products.append(Product(**document))

    return products


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

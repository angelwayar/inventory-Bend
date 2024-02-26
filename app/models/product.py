from pydantic import BaseModel


class Product(BaseModel):
    id: str
    code: str
    supplier: str
    description: str
    year: int
    height: int
    width: int
    depth: int
    retail: int
    images: int
    brand: str

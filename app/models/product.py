import math
from typing import Annotated
from pydantic import BaseModel, BeforeValidator, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class Product(BaseModel):
    id: PyObjectId | None = None
    code: str | None = None
    supplier: str | None = None
    description: str | None = None
    year: str | None = None
    height: float | None = None
    width: float | None = None
    depth: float | None = None
    retail: int | None = None
    images: int | None = None
    brand: str | None = None

from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class Product(BaseModel):
    id: Optional[PyObjectId] = None
    code: Optional[str] = None
    supplier: Optional[str] = None
    description: Optional[str] = None
    year: Optional[str] = None
    height: Optional[float] = None
    width: Optional[float] = None
    depth: Optional[float] = None
    retail: Optional[int] = None
    images: Optional[int] = None
    brand: Optional[str] = None

    @classmethod
    def from_document(cls, document: dict) -> "Product":
        document["code"] = str(document.get("code", ""))
        document["year"] = str(document.get("year", ""))
        
        return cls(**document)

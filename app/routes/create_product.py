from fastapi import HTTPException,status
from pydantic import BaseModel, Field
from app.models.product import Product

from app.routes import router
from db.database import create_product, get_one_product_by_code

class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)

@router.post(
    "/product",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageProductNotFound}}
)
async def save_product(product: Product):
    try:
        productFound = await get_one_product_by_code(code=product.code)
        if productFound:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product al ready exists")
        
        response = await create_product(product=product.model_dump())
        return response
    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
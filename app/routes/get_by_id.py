from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from app.routes import router
from db.database import get_one_product_id

class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)


@router.get(
    "/{id}/",
    status_code=status.HTTP_200_OK,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageProductNotFound}}
)
async def get_product_by_id(id: str):
    try:
        product = await get_one_product_id(id=id)
        return product
    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
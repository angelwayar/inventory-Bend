from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from app.routes import router
from db.database import delete_product

class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)

@router.delete(
    "/{id}/",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessageProductNotFound}}
)
async def remove_product(id: str):
    try:
        response = await delete_product(id=id)
        return response
    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
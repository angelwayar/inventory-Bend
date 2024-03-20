from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from app.routes import router
from db.database import get_all_products


class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        },
    },
)
async def get_all(
        page: int = 1,
        per_page: int = 10,
):
    try:
        products = await get_all_products(per_page=per_page, page=page)
        return products
    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

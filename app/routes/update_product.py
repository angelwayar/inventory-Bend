from db.database import update_product, get_one_product_id
from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from app.models.product import UpdateProduct
from app.routes import router


class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)


@router.put(
    "/{id}/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageProductNotFound,
        }
    }
)
async def put_product(id: str, product: UpdateProduct):
    try:
        productFound = await get_one_product_id(id=id)

        if productFound is None:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product does not exists",
            )

        response = await update_product(id=id, data=product)
        return response

    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

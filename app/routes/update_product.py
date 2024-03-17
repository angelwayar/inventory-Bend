from typing import List

from db.database import get_one_product_id, update_product
from fastapi import Body, File, HTTPException, UploadFile, status
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
async def put_product(
    id: str,
    product: UpdateProduct = Body(..., json_schema_extra={"nullable": True}),
    files: List[UploadFile] = File(..., json_schema_extra={"nullable": True}),
):
    try:
        productFound = await get_one_product_id(id=id)

        if productFound is None:
            return HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product does not exists",
            )

        response = await update_product(id=id, data=product, files=files)

        return response

    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

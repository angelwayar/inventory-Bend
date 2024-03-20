from typing import List

from db.database import create_product, get_one_product_by_code
from fastapi import Body, File, HTTPException, UploadFile, status
from pydantic import BaseModel, Field

from app.models.product import ProductCreate
from app.routes import router


class ProductNotFoundError(Exception):
    message = "El producto no existe."

    def __str__(self):
        return self.message


class ErrorMessageProductNotFound(BaseModel):
    detail: str = Field(example=ProductNotFoundError.message)


@router.post(
    "/save",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_404_NOT_FOUND: {
        "model": ErrorMessageProductNotFound}}
)
async def save_product(
        product: ProductCreate = Body(...),
        files: List[UploadFile] = File(..., json_schema_extra={"nullable": True}),
):
    try:
        productFound = await get_one_product_by_code(code=product.code)
        if productFound:
            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product al ready exists")

        response = await create_product(product=product.model_dump(), files=files)
        return response
    except Exception as _e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

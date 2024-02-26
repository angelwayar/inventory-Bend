from typing import Optional
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.models.base_model import Base


class Image(Base):
    __tablename__ = 'images'

    image_path: Mapped[Optional[str]] = mapped_column(String, nullable=True)

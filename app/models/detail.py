from typing import Optional
from sqlalchemy import Integer, Float, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.models.base_model import Base




class Detail(Base):
    __tablename__ = 'details'

    description: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
    part: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)
    width: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=None)
    height: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=None)
    depth: Mapped[Optional[float]] = mapped_column(Float, nullable=True, default=None)
    age: Mapped[Optional[str]] = mapped_column(String, nullable=True, default=None)

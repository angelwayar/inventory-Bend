from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped


@as_declarative
class Base(object):
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)

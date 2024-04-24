import datetime
import time

from sqlalchemy import Boolean, Column, String, sql, Integer
from sqlalchemy.dialects.postgresql import TIMESTAMP

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)

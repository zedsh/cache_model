import datetime

from typing import Any, List

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str


class UserListSchema(BaseModel):
    data: List[UserSchema]

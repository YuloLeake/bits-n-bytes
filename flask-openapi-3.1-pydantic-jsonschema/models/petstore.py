from typing import List

from pydantic import BaseModel


class Tag(BaseModel):
    id: int
    name: str


class Category(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    name: str
    category: Category
    photos: List[str]
    tags: List[Tag]
    status: str

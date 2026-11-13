from pydantic import BaseModel, Field
from typing import Literal

class CollectionItem(BaseModel):
    id: int
    title: str
    artist: str
    year: int | None
    #Accept the values used in the frontend
    format: Literal ["CD", "Vinil"]
    #Limits the rating to be between 0 and 5, with zero meaning that the album hasnt been rated
    rating: int = Field(ge = 0, le = 5)
    favorite: bool

class User(BaseModel):
    name: str
    initials: str

class Dashboard(BaseModel):
    user: User
    items: list[CollectionItem]
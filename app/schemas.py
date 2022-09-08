from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    games: Optional[int] = None



class UserCreate(UserBase):
    id: int
    name: str
    age: int
    email: str
    games: int


class GameBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class GameCreate(GameBase):
    id: int
    name: str



class UserSchema(GameBase):
    game: list[GameBase]

class GameSchema(UserBase):
    user: list[UserBase]
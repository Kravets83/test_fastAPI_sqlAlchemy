from uuid import uuid4
from sqlalchemy import Column, String, Text, Integer, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    game = relationship("game", secondary="user-game", back_populates='game')


class Game(Base):
    __tablename__ = "game"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    name = Column(String)
    user = relationship("user", secondary="user-game", back_populates='user')

user_game = Table('user-game', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('game_id', ForeignKey('game.id'), primary_key=True),)

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

# from .config import settings




engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_APP3')
print(engine)
engine.connect()
print(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    id: Any
from typing import Any, List
from sqlalchemy.orm import joinedload

from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from . import actions, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


"""Main page"""


@app.get("/")
def index():
    return {"message": "Hello world!"}


'''User action'''

@app.get("/users", response_model=List[schemas.User], tags=["user"])
def list_user(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    users = actions.user.get_all(db=db, skip=skip, limit=limit)
    return users
#
#
# @app.post(
#     "/users", response_model=schemas.User, status_code=HTTP_201_CREATED, tags=["user"]
# )
# def create_user(*, db: Session = Depends(get_db), post_in: schemas.UserCreate) -> Any:
#     user = actions.user.create(db=db, obj_in=post_in)
#     return user
#
#
# @app.put(
#     "/users/{id}",
#     response_model=schemas.User,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["user"],
# )
# def update_user(
#         *, db: Session = Depends(get_db), id: UUID4, post_in: schemas.UserUpdate,
# ) -> Any:
#     user = actions.user.get(db=db, id=id)
#     if not user:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
#     user = actions.user.update(db=db, db_obj=user, obj_in=post_in)
#     return user
#
#
@app.get(
    "/me/{id}",
    response_model=schemas.UserSchema,
    responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
    tags=["user"],
)
def get_user(*, db: Session = Depends(get_db), id: UUID4) -> Any:
    users = db.query(User).options(joinedload(User.game)).\
        where(User.id == id).one()
    if not users:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
    return users
#
#
# @app.delete(
#     "/users/{id}",
#     response_model=schemas.User,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["user"],
# )
# def delete_user(*, db: Session = Depends(get_db), id: UUID4) -> Any:
#     user = actions.user.get(db=db, id=id)
#     if not user:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")
#     user = actions.user.remove(db=db, id=id)
#     return user


'''Game action'''


@app.get("/games", response_model=List[schemas.Game], tags=["game"])
def list_game(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    games = actions.game.get_all(db=db, skip=skip, limit=limit).options(joinedload(User.game))
    return games


# @app.post(
#     "/games", response_model=schemas.Game, status_code=HTTP_201_CREATED, tags=["game"]
# )
# def create_game(*, db: Session = Depends(get_db), post_in: schemas.GameCreate) -> Any:
#     game = actions.game.create(db=db, obj_in=post_in)
#     return game
#
#
# @app.put(
#     "/games/{id}",
#     response_model=schemas.Game,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["game"],
# )
# def update_game(
#         *, db: Session = Depends(get_db), id: UUID4, post_in: schemas.GameUpdate,
# ) -> Any:
#     game = actions.game.get(db=db, id=id)
#     if not game:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Game not found")
#     game = actions.game.update(db=db, db_obj=game, obj_in=post_in)
#     return game
#
#
# @app.get(
#     "/games/{id}",
#     response_model=schemas.Game,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["game"],
# )
# def get_game(*, db: Session = Depends(get_db), id: UUID4) -> Any:
#     game = actions.game.get(db=db, id=id)
#     if not game:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="game not found")
#     return game
#
#
# @app.delete(
#     "/games/{id}",
#     response_model=schemas.Game,
#     responses={HTTP_404_NOT_FOUND: {"model": schemas.HTTPError}},
#     tags=["game"],
# )
# def delete_game(*, db: Session = Depends(get_db), id: UUID4) -> Any:
#     game = actions.game.get(db=db, id=id)
#     if not game:
#         raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Game not found")
#     game = actions.game.remove(db=db, id=id)
#     return game

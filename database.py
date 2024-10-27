from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

from user import UserModel
from models import ModelMovies

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    UserModel.metadata.create_all(engine)
    ModelMovies.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
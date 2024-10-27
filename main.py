from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from user import UserModel
from models import ModelMovies
from random import randint
from sqlmodel import select
from schemas import UserSchema, MoviesSchema

app = FastAPI()

create_db_and_tables()

@app.post("/users")
async def create_user(user_data: UserSchema, database: SessionDep):
    user = UserModel(name=user_data.name, last_name=user_data.last_name, email=user_data.email, phone=user_data.phone)

    database.add(user)
    database.commit()
    database.refresh(user)
    return user

@app.get("/users")
async def get_users(database: SessionDep):
    statement = select(UserModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int, database: SessionDep):
    user = database.get(UserModel, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found")
    
    return user

#MOVIES******

@app.post("/movies")
async def create_movie(movie_data: MoviesSchema, database: SessionDep):
    movie = ModelMovies(name_movie=movie_data.name_movie, year_of_release=movie_data.year_of_release, duration=movie_data.duration, director=movie_data.director, clasification=movie_data.clasification, gender=movie_data.gender)

    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(ModelMovies)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movie_by_id(movie_id: int, database: SessionDep):
    movie = database.get(ModelMovies, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Movie not found")
    
    return movie

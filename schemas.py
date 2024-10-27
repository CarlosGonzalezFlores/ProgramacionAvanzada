from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str

class MoviesSchema(BaseModel):
    name_movie: str
    year_of_release: int
    duration: str
    director: str
    clasification: str
    gender: str



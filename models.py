from sqlmodel import SQLModel, Field

class ModelMovies(SQLModel, table=True):
    __tablename__ = "movies"

    id : int = Field(primary_key=True)
    name_movie: str
    year_of_release: int
    duration: str
    director: str
    clasification: str
    gender: str

    
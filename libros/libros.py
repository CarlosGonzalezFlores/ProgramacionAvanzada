from datetime import date
class libros:
    id: int
    titulo: str
    autor: str
    editorial: str
    año_publicacion: date
    precio: float

    def __init__(self, id:int, titulo:str, autor:str, editorial:str, año_publicacion:date, precio:float):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publicacion = año_publicacion
        self.precio = precio
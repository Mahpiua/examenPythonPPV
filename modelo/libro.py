from modelo.articulo import Articulo
from modelo.prestable import Prestable


class Libro (Articulo, Prestable):
    def __init__(self, *, id:int, isbn:str, **kwargs):
        self.id = id
        self.isbn = isbn
        super().__init__(**kwargs)

    @property
    def id(self):
        return self.id


    @id.setter
    def id(self, nuevo_id):
        self.id = nuevo_id

    @property
    def isbn(self):
        validar_isbn = self.isbn
        if len(validar_isbn) != 10:
            print("El ISBN debe tener 10 dígitos.")

        suma = sum(int(c) * (10 - i)
                   for i, c in enumerate(validar_isbn))
        if suma % 11 != 0:
            print("ISBN inválido.")
        return self.isbn

    @isbn.setter
    def isbn(self, ISBN):
        self.isbn = ISBN
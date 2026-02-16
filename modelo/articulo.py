import datetime
from abc import ABC

from utilidades.utilidades import formatear_titulo


class Articulo (ABC):
    def __init__(self, *, titulo:str, anio:int, fecha_adquisicion:datetime, **kwargs):
        self.titulo = titulo
        self.anio = anio
        self.fecha_adquisicion = fecha_adquisicion
        self.__init__(**kwargs)

    @property
    def titulo(self):
        return formatear_titulo(self.titulo)

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.titulo = formatear_titulo(nuevo_titulo)

    @property
    def anio(self):
        actual = datetime.now().year
        if not (1500 <= self.anio <= actual):
            print("El año debe estar entre 1500 y el actual.")
        return self.anio

    @anio.setter
    def anio(self, nuevo_anio):
        self.anio = nuevo_anio

    @property
    def fecha_adquisicion(self):
        return self.fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, nueva_fec_adq):
        self.fecha_adquisicion = nueva_fec_adq


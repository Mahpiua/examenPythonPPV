from abc import ABC
from datetime import date


class Prestable(ABC):
    def __init__(self, *, num_max_dias:int = 31, prestado:bool = False, num_usuario:int = None, fecha_prestamo:date, tiempo_excedido:int, **kwargs):
        self.num_max_dias = num_max_dias
        self.prestado = prestado
        self.num_usuario = num_usuario
        self.fecha_prestamo = fecha_prestamo
        self.tiempo_excedido = tiempo_excedido
        self.__init__(**kwargs)

    @property
    def num_max_dias(self):
        return self.num_max_dias

    @property
    def prestado(self):
        return self.prestado

    #@prestado.setter
    #def prestado(self):

    @property
    def num_usuario(self):
        return self.num_usuario

    @num_usuario.setter
    def num_usuario(self, nuevo_usuario):
        self.num_usuario = nuevo_usuario

    @property
    def fecha_prestamo(self):
        return self.fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, nueva_fec_pres):
        self.fecha_prestamo = nueva_fec_pres

    @property
    def tiempo_excedido(self):
        hoy = date.today()
        diferencia = abs((hoy - fecha_bd).days)
        return self.tiempo_excedido

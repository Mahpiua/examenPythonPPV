from modelo.database import *


def crear_libro (id, isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo):
    conect = iniciar_conexion()
    cursor = conect.cursor()
    cursor.execute(INSERT_CREAR_LIBRO, (id, isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo))
    conect.commit()
    conect.close()


def mostrar_libros():
    conect = iniciar_conexion()
    cursor = conect.cursor()
    cursor.execute(SELECT_LIBROS)
    resultados = cursor.fetchall()
    conect.close()
    return resultados

def buscar_items(**kwargs):
    conect = iniciar_conexion()
    cursor = conect.cursor()
    cursor.execute(SELECT_ITEMS_LIBRO, **kwargs)
    resultados = cursor.fetchall()
    conect.close()
    return resultados

def editar_libro(isbn:int):
    conect = iniciar_conexion()
    cursor = conect.cursor()
    cursor.execute(EDITAR_LIBRO, isbn)
    conect.close()

def eliminar_libro(isbn:int):
    conect = iniciar_conexion()
    cursor = conect.cursor()
    cursor.execute(ELIMINAR_LIBRO, isbn)
    conect.close()
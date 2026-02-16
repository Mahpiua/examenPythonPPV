import sqlite3

def iniciar_conexion():
    return sqlite3.connect("biblioteca.db")

def crear_bd():
    #Creamos la conexion
    conexion = iniciar_conexion()

    #Creamos el cursor
    cursor = conexion.cursor()

    #Creamos las tablas
    cursor.execute("""CREATE TABLE IF NOT EXISTS libros (
                        id                INTEGER PRIMARY KEY AUTOINCREMENT,
                        isbn              TEXT    NOT NULL UNIQUE CHECK(length(isbn) = 10),
                        titulo            TEXT    NOT NULL,
                        anio              INTEGER NOT NULL CHECK(anio BETWEEN 1500 AND 2026),
                        fecha_adquisicion DATE    NOT NULL,
                        prestado          INTEGER NOT NULL DEFAULT 0 CHECK(prestado IN (0, 1)),
                        numero_usuario    INTEGER,
                        fecha_prestamo    DATE
                        );"""
                   )

    #Se realiza la conexion
    conexion.commit()

    #Cerramos la conexion
    conexion.close()

def iniciar_carga():

    # Creamos la conexion
    conexion = iniciar_conexion()

    # Creamos el cursor
    cursor = conexion.cursor()

    # Insert inicial
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0306406152', 'El Quijote De La Mancha', 1605, '2023-03-15', 0, NULL, NULL);")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0140157514', 'Cien Años De Soledad', 1967, '2023-05-20', 1, 1001, '2026-02-10');")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0143034901', 'La Sombra Del Viento', 2001, '2023-07-10', 0, NULL, NULL);")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0451524934', '1984', 1949, '2022-11-01', 1, 1002, '2025-12-01');")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0156012197', 'El Principito', 1943, '2024-01-20', 0, NULL, NULL);")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0394752848', 'Rayuela', 1963, '2023-09-05', 1, 1003, '2025-11-15');")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0553273914', 'La Casa De Los Espiritus', 1982, '2024-06-12', 0, NULL, NULL);")
    cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo)"
                   "VALUES ('0802130305', 'Ficciones', 1944, '2024-03-28', 1, 1004, '2026-02-05');")

    # Se realiza la conexion
    conexion.commit()

    # Cerramos la conexion
    conexion.close()


#Definicion sentencia INSERT INTO
INSERT_CREAR_LIBRO = 'INSERT INTO libros (id, isbn, titulo, anio, fecha_adquisicion, prestado, numero_usuario, fecha_prestamo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'

#Realizamos las consultas
SELECT_LIBROS = 'SELECT * FROM libros'
SELECT_ITEMS_LIBRO = 'SELECT **kwargs FROM libros'

#Update
EDITAR_LIBRO = ('UPDATE libros'
                'SET '
                'WHERE id = id')

#Delete
ELIMINAR_LIBRO = 'DELETE FROM libros WHERE isbn = ?'


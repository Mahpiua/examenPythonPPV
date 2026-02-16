import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox

from controlador.controlador_libros import *


# Se crean las tablas
crear_bd()

# Se inicializan los datos
iniciar_carga()

ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("800x400")

# Creamos el árbol
tree = ttk.Treeview(height=10, columns = ('#1','#2','#3','#4','#5','#6','#7'))
tree.grid(row=8, column=0, columnspan=4, sticky="nsew")
tree.heading('#0', text="ID", anchor = tk.CENTER)
tree.heading('#1', text="ISBN", anchor = tk.CENTER)
tree.heading('#2', text="Título", anchor = tk.CENTER)
tree.heading('#3', text="Año", anchor = tk.CENTER)
tree.heading('#4', text="Fecha_Adquisicion", anchor = tk.CENTER)
tree.heading('#5', text="Prestado", anchor = tk.CENTER)
tree.heading('#6', text="Numero_Usuario", anchor = tk.CENTER)
tree.heading('#7', text="Fecha_prestamo", anchor = tk.CENTER)
tree.pack(fill="both", expand=True)

# Mostramos los datos
for libro in mostrar_libros():
    tree.insert("", 0, text=libro[0], values=(libro[1], libro[2], libro[3], libro[4], libro[5], libro[6], libro[7]))

def abrir_formulario_libro():
    form = tk.Toplevel(ventana)
    form.title("Nuevo Libro")
    form.geometry("300x300")

    # Campos
    tk.Label(form, text="ID").pack()
    entry_id = tk.Entry(form)
    entry_id.pack()

    tk.Label(form, text="ISBN").pack()
    entry_isbn = tk.Entry(form)
    entry_isbn.pack()

    tk.Label(form, text="Título").pack()
    entry_titulo = tk.Entry(form)
    entry_titulo.pack()

    tk.Label(form, text="Año").pack()
    entry_anio = tk.Entry(form)
    entry_anio.pack()

    tk.Label(form, text="Fecha Adquisición (YYYY-MM-DD)").pack()
    entry_fecha = tk.Entry(form)
    entry_fecha.pack()

    prestado_var = tk.BooleanVar()
    tk.Checkbutton(form, text="Prestado", variable=prestado_var).pack()

    tk.Label(form, text="Numero Usuario").pack()
    entry_num_usuario = tk.Entry(form)
    entry_num_usuario.pack()

    tk.Label(form, text="Fecha Préstamo").pack()
    entry_fec_pres = tk.Entry(form)
    entry_fec_pres.pack()

    # Botón guardar
    tk.Button(
        form,
        text="Guardar",
        command=lambda: crear_libro(
            form,
            entry_isbn.get(),
            entry_titulo.get())
    ).pack(pady=10)

#Boton añadir libro
boton_add = tk.Button(ventana, text="Añadir libro", command=abrir_formulario_libro)
boton_add.pack(padx=10, pady=10, side="left")

#Boton editar libro
boton_update = tk.Button(ventana, text="Editar libro", command=abrir_formulario_libro)
boton_update.pack(padx=10, pady=10, side="left")

#Boton eliminar libro
boton_delete = tk.Button(ventana, text="Eliminar libro", command=abrir_formulario_libro)
boton_delete.pack(padx=10, pady=10, side="left")

#Boton exportar csv
boton_exportar = tk.Button(ventana, text="Exportar csv", command=abrir_formulario_libro)
boton_exportar.pack(padx=10, pady=10, side="left")


def guardar():

    crear_libro(
        int(libro[0].get()),
        libro[1].get(),
        libro[2].get(),
        int(libro[3].get()),
        date(libro[4].get()),
        int(libro[5].get()),
        int(libro[6].get()),
        date(libro[7].get())
    )
    messagebox.showinfo("Éxito", "Libro guardado")
    refrescar_treeview()


def refrescar_treeview():
    for item in tree.get_children():
        tree.delete(item)

    for libro in mostrar_libros():
        tree.insert("", tk.END, text=libro[0], values=libro[1:])

ventana.mainloop()
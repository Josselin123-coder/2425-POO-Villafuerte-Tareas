import tkinter as tk
from tkinter import messagebox

# Creamos el metodo para agregar una nueva tarea
def agregar_tarea():
    tarea = entrada.get()  # Obtenemos la tarea desde el campo de entrada
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Añadimos la tarea a la lista
        entrada.delete(0, tk.END)  # Limpiamos el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")  # Mostramos una advertencia si el campo está vacío

# Creamos el metodo para marcar una tarea como completada
def marcar_completada():
    indice_tarea_seleccionada = lista_tareas.curselection()  # Obtenemos la tarea seleccionada
    if indice_tarea_seleccionada:
        tarea = lista_tareas.get(indice_tarea_seleccionada)  # Obtenemos el texto de la tarea
        lista_tareas.delete(indice_tarea_seleccionada)  # Eliminamos la tarea de la lista
        lista_tareas.insert(tk.END, f"[COMPLETADA] {tarea}")  # Añadimos la tarea como completada
    else:
        messagebox.showinfo("Información", "Por favor, selecciona una tarea para marcar como completada.")  # Mostramos un mensaje informativo

# Creamos el metodo para eliminar una tarea
def eliminar_tarea():
    indice_tarea_seleccionada = lista_tareas.curselection()  # Obtenemos la tarea seleccionada
    if indice_tarea_seleccionada:
        lista_tareas.delete(indice_tarea_seleccionada)  # Eliminamos la tarea de la lista
    else:
        messagebox.showinfo("Información", "Por favor, selecciona una tarea para eliminar.")  # Mostramos un mensaje informativo

# Creamos el metodo para añadir tareas al presionar Enter
def agregar_tarea_al_presionar_enter(evento):
    agregar_tarea()

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")  # Título de la ventana

# Campo de entrada para escribir nuevas tareas
entrada = tk.Entry(ventana, width=40)  # Configuramos el tamaño del campo de entrada
entrada.pack(pady=10)  # Espaciado entre elementos

# Botón para añadir una tarea
boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

# Botón para marcar como completada
boton_marcar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_marcar.pack(pady=5)

# Botón para eliminar una tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Listbox para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)  # Configuramos el tamaño del Listbox
lista_tareas.pack(pady=10)

# Permitir añadir tareas con la tecla Enter
entrada.bind("<Return>", agregar_tarea_al_presionar_enter)

# Ejecutar la aplicación
ventana.mainloop()

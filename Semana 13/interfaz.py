import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Datos")
        self.root.geometry("400x300")

        # Etiqueta de Instrucción
        self.label = tk.Label(root, text="Ingrese un dato:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Campo de Texto
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.agregar_dato, font=("Arial", 12))
        self.add_button.pack(pady=5)

        # Lista de Datos
        self.listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
        self.listbox.pack(pady=5)

        # Contador de elementos
        self.counter_label = tk.Label(root, text="Elementos: 0", font=("Arial", 10))
        self.counter_label.pack(pady=5)

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.limpiar_lista, font=("Arial", 12))
        self.clear_button.pack(pady=5)

    def actualizar_contador(self):
        count = self.listbox.size()
        self.counter_label.config(text=f"Elementos: {count}")

    def agregar_dato(self):
        dato = self.entry.get()
        if dato:
            self.listbox.insert(tk.END, dato)
            self.entry.delete(0, tk.END)
            self.actualizar_contador()
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío.")

    def limpiar_lista(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
            self.actualizar_contador()
        else:
            self.listbox.delete(0, tk.END)
        self.actualizar_contador()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()

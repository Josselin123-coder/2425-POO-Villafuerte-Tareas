import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
        messagebox.showinfo("Tarea añadida", f"¡La tarea '{task}' se añadió correctamente!")

def complete_task(event=None):
    sel = tasks.curselection()
    if sel:
        task = tasks.get(sel)
        tasks.itemconfig(sel, fg="gray")
        tasks.selection_clear(0, tk.END)
        messagebox.showinfo("Tarea completada", f"¡Has marcado la tarea '{task}' como completada!")

def delete_task(event=None):
    sel = tasks.curselection()
    if sel:
        task = tasks.get(sel)
        tasks.delete(sel)
        messagebox.showinfo("Tarea eliminada", f"¡La tarea '{task}' fue eliminada!")

def clear_all():
    tasks.delete(0, tk.END)
    messagebox.showinfo("Lista limpia", "¡Todas las tareas han sido eliminadas!")

root = tk.Tk()
root.title("Gestor de Tareas Dinámico")
root.geometry("400x300")
root.bind("<Escape>", lambda e: root.destroy())

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)
entry.bind("<Return>", add_task)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Añadir Tarea", command=add_task, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Completar Tarea", command=complete_task, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Eliminar Tarea", command=delete_task, bg="#F44336", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Limpiar Todo", command=clear_all, bg="#9E9E9E", fg="white").pack(side=tk.LEFT, padx=5)

tasks = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
tasks.pack(fill=tk.BOTH, expand=True, pady=10)
tasks.bind("<Delete>", delete_task)
tasks.bind("c", complete_task)

root.mainloop()
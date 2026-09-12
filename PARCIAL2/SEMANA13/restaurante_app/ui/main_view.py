import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.controller = controller
        self.servicio = controller.servicio
        self._build()

    def _build(self):
        self.columnconfigure(0, weight=1)
        header = ttk.Frame(self, padding=10)
        header.grid(sticky="ew")
        ttk.Label(header, text="Panel Principal - Restaurante", font=(None, 14)).grid(column=0, row=0, sticky="w")

        btns = ttk.Frame(self, padding=10)
        btns.grid(sticky="w")
        ttk.Button(btns, text="Productos", command=self.mostrar_productos).grid(column=0, row=0, padx=6)
        ttk.Button(btns, text="Usuarios", command=self.mostrar_usuarios).grid(column=1, row=0, padx=6)
        ttk.Button(btns, text="Ventas (pendiente)", command=self.ventas_pendiente).grid(column=2, row=0, padx=6)
        ttk.Button(btns, text="Cerrar sesión", command=self.controller.show_login_view).grid(column=3, row=0, padx=6)

        self.panel = ttk.Frame(self, padding=10)
        self.panel.grid(sticky="nsew")
        self.panel.columnconfigure(0, weight=1)

        self.text = tk.Text(self.panel, height=15, wrap="word")
        self.text.grid(sticky="nsew")

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()
        self.text.delete("1.0", tk.END)
        if not productos:
            self.text.insert(tk.END, "No hay productos cargados.\n")
            return
        for p in productos:
            self.text.insert(tk.END, f"ID: {p.id} - {p.nombre} | Precio: ${p.precio} | Cantidad: {p.cantidad}\n")

    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()
        self.text.delete("1.0", tk.END)
        if not usuarios:
            self.text.insert(tk.END, "No hay usuarios cargados.\n")
            return
        for u in usuarios:
            self.text.insert(tk.END, f"Usuario: {u.username} - Nombre: {u.nombre}\n")

    def ventas_pendiente(self):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "Funcionalidad Ventas: pendiente de implementación gráfica.\n")

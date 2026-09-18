import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.controller = controller
        self.servicio = controller.servicio
        self._build()

    def _build(self):
        self.columnconfigure(1, weight=1)
        header = ttk.Frame(self, padding=10)
        header.grid(row=0, column=0, columnspan=2, sticky="ew")
        ttk.Label(header, text="Panel Principal - Restaurante", font=(None, 14)).pack(side="left")
        ttk.Button(header, text="Cerrar sesión", command=self.controller.show_login_view).pack(side="right")

        nav = ttk.Frame(self, padding=10)
        nav.grid(row=1, column=0, sticky="ns")
        ttk.Button(nav, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=4)
        ttk.Button(nav, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=4)

        self.panel = ttk.Frame(self, padding=10)
        self.panel.grid(row=1, column=1, sticky="nsew")
        self.panel.columnconfigure(0, weight=1)

        self.mensaje = ttk.Label(self.panel, text="", foreground="red")
        self.mensaje.grid(row=0, column=0, sticky="w")

    def _clear_panel(self):
        for child in self.panel.winfo_children():
            child.destroy()
        self.mensaje = ttk.Label(self.panel, text="", foreground="red")
        self.mensaje.grid(row=0, column=0, sticky="w")

    def mostrar_usuarios(self):
        self._clear_panel()
        usuarios = self.servicio.listar_usuarios()
        text = tk.Text(self.panel, height=15, wrap="word")
        text.grid(sticky="nsew")
        if not usuarios:
            text.insert(tk.END, "No hay usuarios cargados.\n")
            return
        for u in usuarios:
            text.insert(tk.END, f"Usuario: {u.username} - Nombre: {u.nombre}\n")

    def mostrar_productos(self):
        self._clear_panel()
        frm = ttk.Frame(self.panel)
        frm.grid(sticky="nw")

        ttk.Label(frm, text="ID (para consultar/actualizar/eliminar):").grid(row=0, column=0, sticky="w")
        self.id_entry = ttk.Entry(frm)
        self.id_entry.grid(row=0, column=1, sticky="ew")

        ttk.Label(frm, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(frm)
        self.nombre_entry.grid(row=1, column=1, sticky="ew")

        ttk.Label(frm, text="Precio:").grid(row=2, column=0, sticky="w")
        self.precio_entry = ttk.Entry(frm)
        self.precio_entry.grid(row=2, column=1, sticky="ew")

        ttk.Label(frm, text="Cantidad:").grid(row=3, column=0, sticky="w")
        self.cantidad_entry = ttk.Entry(frm)
        self.cantidad_entry.grid(row=3, column=1, sticky="ew")

        btns = ttk.Frame(frm)
        btns.grid(row=4, column=0, columnspan=2, pady=(8,0))
        ttk.Button(btns, text="Registrar", command=self._registrar_producto).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Cargar/Consultar", command=self._cargar_producto).grid(row=0, column=1, padx=4)
        ttk.Button(btns, text="Actualizar", command=self._actualizar_producto).grid(row=0, column=2, padx=4)
        ttk.Button(btns, text="Eliminar", command=self._eliminar_producto).grid(row=0, column=3, padx=4)
        ttk.Button(btns, text="Listar Todos", command=self._listar_productos).grid(row=0, column=4, padx=4)

        self.tree = ttk.Treeview(self.panel, columns=("id","nombre","precio","cantidad"), show="headings")
        for col, width in [("id",50),("nombre",200),("precio",80),("cantidad",80)]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=width)
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(10,0))
        self.panel.rowconfigure(1, weight=1)
        self._listar_productos()

    def _set_mensaje(self, text, color="red"):
        self.mensaje.config(text=text, foreground=color)

    def _listar_productos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        productos = self.servicio.listar_productos()
        for p in productos:
            self.tree.insert("", tk.END, values=(p.id, p.nombre, p.precio, p.cantidad))

    def _registrar_producto(self):
        nombre = self.nombre_entry.get().strip()
        precio = self.precio_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        try:
            nuevo = self.servicio.agregar_producto(nombre, precio, cantidad)
            self._set_mensaje(f"Producto registrado ID {nuevo.id}", "green")
            self._listar_productos()
            self.nombre_entry.delete(0, tk.END); self.precio_entry.delete(0, tk.END); self.cantidad_entry.delete(0, tk.END)
        except Exception as e:
            self._set_mensaje(str(e), "red")

    def _cargar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para consultar", "red"); return
        p = self.servicio.obtener_producto(pid)
        if not p:
            self._set_mensaje("Producto no encontrado", "red"); return
        self.nombre_entry.delete(0, tk.END); self.nombre_entry.insert(0, p.nombre)
        self.precio_entry.delete(0, tk.END); self.precio_entry.insert(0, str(p.precio))
        self.cantidad_entry.delete(0, tk.END); self.cantidad_entry.insert(0, str(p.cantidad))
        self._set_mensaje(f"Producto cargado ID {p.id}", "green")

    def _actualizar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para actualizar", "red"); return
        nombre = self.nombre_entry.get().strip()
        precio = self.precio_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        try:
            updated = self.servicio.actualizar_producto(pid, nombre=nombre, precio=precio, cantidad=cantidad)
            self._set_mensaje(f"Producto actualizado ID {updated.id}", "green")
            self._listar_productos()
        except Exception as e:
            self._set_mensaje(str(e), "red")

    def _eliminar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para eliminar", "red"); return
        try:
            self.servicio.eliminar_producto(pid)
            self._set_mensaje(f"Producto eliminado ID {pid}", "green")
            self._listar_productos()
        except Exception as e:
            self._set_mensaje(str(e), "red")

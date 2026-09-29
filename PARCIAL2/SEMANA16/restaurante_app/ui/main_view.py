import tkinter as tk
from tkinter import messagebox, ttk


class MainView(ttk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.controller = controller
        self.servicio = controller.servicio
        self.usuario_actual = None
        self._build()

    def configurar_usuario_actual(self, usuario):
        self.usuario_actual = usuario
        self._actualizar_header()
        if self.usuario_actual and self.usuario_actual.rol != "Administrador":
            if hasattr(self, 'usuarios_btn'):
                self.usuarios_btn.config(state="disabled")
        elif hasattr(self, 'usuarios_btn'):
            self.usuarios_btn.config(state="normal")

    def _build(self):
        self.columnconfigure(1, weight=1)
        header = ttk.Frame(self, padding=10)
        header.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.header_label = ttk.Label(header, text="Panel Principal - Restaurante", font=(None, 14, "bold"))
        self.header_label.pack(side="left")
        ttk.Button(header, text="Cerrar sesión", command=self.controller.show_login_view).pack(side="right")

        nav = ttk.Frame(self, padding=10)
        nav.grid(row=1, column=0, sticky="ns")
        ttk.Button(nav, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=4)
        self.usuarios_btn = ttk.Button(nav, text="Usuarios", command=self.mostrar_usuarios)
        self.usuarios_btn.pack(fill="x", pady=4)
        ttk.Button(nav, text="Ventas", command=self.mostrar_ventas).pack(fill="x", pady=4)

        self.panel = ttk.Frame(self, padding=10)
        self.panel.grid(row=1, column=1, sticky="nsew")
        self.panel.columnconfigure(0, weight=1)

        self.mensaje = ttk.Label(self.panel, text="", foreground="red")
        self.mensaje.grid(row=0, column=0, sticky="w")

        self.bind_all("<Return>", self._on_enter_global)
        self.bind_all("<Escape>", self._on_escape_global)
        self._actualizar_header()
        self.mostrar_productos()

    def _actualizar_header(self):
        usuario = self.usuario_actual.username if self.usuario_actual else "Invitado"
        rol = self.usuario_actual.rol if self.usuario_actual else "-"
        self.header_label.config(text=f"Panel Principal - Restaurante | {usuario} ({rol})")

    def _clear_panel(self):
        for child in self.panel.winfo_children():
            child.destroy()
        self.mensaje = ttk.Label(self.panel, text="", foreground="red")
        self.mensaje.grid(row=0, column=0, sticky="w")

    def _set_mensaje(self, text, color="red"):
        self.mensaje.config(text=text, foreground=color)

    def mostrar_usuarios(self):
        if self.usuario_actual is None or self.usuario_actual.rol != "Administrador":
            self._set_mensaje("Solo el usuario Administrador puede gestionar usuarios.", "red")
            return

        self._clear_panel()
        self.panel.columnconfigure(0, weight=1)
        self.panel.rowconfigure(1, weight=1)

        form = ttk.LabelFrame(self.panel, text="Administración de usuarios")
        form.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="ID:").grid(row=0, column=0, sticky="w", padx=8, pady=6)
        self.usuario_id_var = tk.StringVar()
        self.usuario_id_entry = ttk.Entry(form, textvariable=self.usuario_id_var, state="readonly")
        self.usuario_id_entry.grid(row=0, column=1, sticky="ew", padx=8, pady=6)

        ttk.Label(form, text="Nombre:").grid(row=1, column=0, sticky="w", padx=8, pady=6)
        self.usuario_nombre_entry = ttk.Entry(form)
        self.usuario_nombre_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=6)

        ttk.Label(form, text="Usuario:").grid(row=2, column=0, sticky="w", padx=8, pady=6)
        self.usuario_username_entry = ttk.Entry(form)
        self.usuario_username_entry.grid(row=2, column=1, sticky="ew", padx=8, pady=6)

        ttk.Label(form, text="Contraseña:").grid(row=3, column=0, sticky="w", padx=8, pady=6)
        self.usuario_password_entry = ttk.Entry(form, show="*")
        self.usuario_password_entry.grid(row=3, column=1, sticky="ew", padx=8, pady=6)

        ttk.Label(form, text="Rol:").grid(row=4, column=0, sticky="w", padx=8, pady=6)
        self.usuario_rol_combo = ttk.Combobox(form, values=["Administrador", "Empleado", "Cliente"], state="readonly")
        self.usuario_rol_combo.set("Cliente")
        self.usuario_rol_combo.grid(row=4, column=1, sticky="ew", padx=8, pady=6)
        self.usuario_rol_combo.bind("<<ComboboxSelected>>", self._on_rol_seleccionado)

        btns = ttk.Frame(form)
        btns.grid(row=5, column=0, columnspan=2, pady=(8, 8), sticky="ew")
        ttk.Button(btns, text="Registrar", command=self._registrar_usuario).pack(side="left", padx=4)
        ttk.Button(btns, text="Actualizar", command=self._actualizar_usuario).pack(side="left", padx=4)
        ttk.Button(btns, text="Eliminar", command=self._eliminar_usuario).pack(side="left", padx=4)
        ttk.Button(btns, text="Limpiar", command=self._limpiar_formulario).pack(side="left", padx=4)

        self.usuarios_tree = ttk.Treeview(self.panel, columns=("id", "nombre", "usuario", "rol"), show="headings")
        self.usuarios_tree.heading("id", text="ID")
        self.usuarios_tree.heading("nombre", text="Nombre")
        self.usuarios_tree.heading("usuario", text="Usuario")
        self.usuarios_tree.heading("rol", text="Rol")
        self.usuarios_tree.column("id", width=50, anchor="center")
        self.usuarios_tree.column("nombre", width=220)
        self.usuarios_tree.column("usuario", width=180)
        self.usuarios_tree.column("rol", width=130, anchor="center")
        self.usuarios_tree.grid(row=1, column=0, sticky="nsew", pady=(0, 0))
        self.usuarios_tree.bind("<<TreeviewSelect>>", self._on_usuario_seleccionado)

        self._listar_usuarios()
        self._limpiar_formulario()

    def _on_rol_seleccionado(self, event=None):
        rol = self.usuario_rol_combo.get()
        if rol:
            self._set_mensaje(f"Rol seleccionado: {rol}", "blue")

    def _on_usuario_seleccionado(self, event=None):
        seleccion = self.usuarios_tree.selection()
        if not seleccion:
            return
        item = self.usuarios_tree.item(seleccion[0], "values")
        if not item:
            return
        usuario_id = item[0]
        usuario = self.servicio.obtener_usuario(usuario_id)
        if not usuario:
            self._set_mensaje("Usuario no encontrado en la base de datos.", "red")
            return

        self.usuario_id_var.set(str(usuario.id))
        self.usuario_nombre_entry.delete(0, tk.END)
        self.usuario_nombre_entry.insert(0, usuario.nombre)
        self.usuario_username_entry.delete(0, tk.END)
        self.usuario_username_entry.insert(0, usuario.username)
        self.usuario_password_entry.delete(0, tk.END)
        self.usuario_rol_combo.set(usuario.rol)
        self._set_mensaje(f"Usuario cargado: {usuario.username}", "green")

    def _listar_usuarios(self):
        if not hasattr(self, 'usuarios_tree'):
            return
        for item in self.usuarios_tree.get_children():
            self.usuarios_tree.delete(item)
        for usuario in self.servicio.listar_usuarios():
            self.usuarios_tree.insert("", tk.END, values=(usuario.id, usuario.nombre, usuario.username, usuario.rol))

    def _limpiar_formulario(self, event=None):
        if hasattr(self, 'usuario_id_var'):
            self.usuario_id_var.set("")
        if hasattr(self, 'usuario_nombre_entry'):
            self.usuario_nombre_entry.delete(0, tk.END)
        if hasattr(self, 'usuario_username_entry'):
            self.usuario_username_entry.delete(0, tk.END)
        if hasattr(self, 'usuario_password_entry'):
            self.usuario_password_entry.delete(0, tk.END)
        if hasattr(self, 'usuario_rol_combo'):
            self.usuario_rol_combo.set("Cliente")
        if hasattr(self, 'usuarios_tree'):
            for item in self.usuarios_tree.selection():
                self.usuarios_tree.selection_remove(item)
        self._set_mensaje("Formulario listo para una nueva operación.", "blue")

    def _on_enter_global(self, event=None):
        if hasattr(self, 'usuario_nombre_entry') and self.focus_get() in (self.usuario_nombre_entry, self.usuario_username_entry, self.usuario_password_entry, self.usuario_rol_combo):
            self._registrar_usuario()

    def _on_escape_global(self, event=None):
        if hasattr(self, 'usuario_nombre_entry'):
            self._limpiar_formulario()

    def _registrar_usuario(self):
        nombre = self.usuario_nombre_entry.get().strip()
        username = self.usuario_username_entry.get().strip()
        password = self.usuario_password_entry.get().strip()
        rol = self.usuario_rol_combo.get().strip()
        try:
            usuario = self.servicio.registrar_usuario(username, password, nombre, rol)
            self._listar_usuarios()
            self._limpiar_formulario()
            self._set_mensaje(f"Usuario registrado ID {usuario.id}", "green")
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

    def _actualizar_usuario(self):
        usuario_id = self.usuario_id_var.get().strip()
        if not usuario_id:
            self._set_mensaje("Seleccione un usuario para actualizar.", "red")
            return
        nombre = self.usuario_nombre_entry.get().strip()
        username = self.usuario_username_entry.get().strip()
        password = self.usuario_password_entry.get().strip()
        rol = self.usuario_rol_combo.get().strip()
        try:
            usuario = self.servicio.actualizar_usuario(usuario_id, username=username, password=password, nombre=nombre, rol=rol)
            self._listar_usuarios()
            self._set_mensaje(f"Usuario actualizado ID {usuario.id}", "green")
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

    def _eliminar_usuario(self):
        usuario_id = self.usuario_id_var.get().strip()
        if not usuario_id:
            self._set_mensaje("Seleccione un usuario para eliminar.", "red")
            return
        usuario = self.servicio.obtener_usuario(usuario_id)
        if not usuario:
            self._set_mensaje("Usuario no encontrado.", "red")
            return
        if self.controller.usuario_actual and usuario.id == self.controller.usuario_actual.id:
            self._set_mensaje("No puede eliminar la cuenta administrativa que está activa.", "red")
            return
        if messagebox.askyesno("Confirmar eliminación", f"¿Desea eliminar al usuario {usuario.username}?"):
            try:
                self.servicio.eliminar_usuario(usuario_id, self.controller.usuario_actual)
                self._listar_usuarios()
                self._limpiar_formulario()
                self._set_mensaje(f"Usuario eliminado ID {usuario_id}", "green")
            except Exception as exc:
                self._set_mensaje(str(exc), "red")

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
        btns.grid(row=4, column=0, columnspan=2, pady=(8, 0))
        ttk.Button(btns, text="Registrar", command=self._registrar_producto).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Cargar/Consultar", command=self._cargar_producto).grid(row=0, column=1, padx=4)
        ttk.Button(btns, text="Actualizar", command=self._actualizar_producto).grid(row=0, column=2, padx=4)
        ttk.Button(btns, text="Eliminar", command=self._eliminar_producto).grid(row=0, column=3, padx=4)
        ttk.Button(btns, text="Listar Todos", command=self._listar_productos).grid(row=0, column=4, padx=4)

        self.tree = ttk.Treeview(self.panel, columns=("id", "nombre", "precio", "cantidad"), show="headings")
        for col, width in [("id", 50), ("nombre", 200), ("precio", 80), ("cantidad", 80)]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=width)
        self.tree.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        self.panel.rowconfigure(1, weight=1)
        self._listar_productos()

    def _listar_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in self.servicio.listar_productos():
            self.tree.insert("", tk.END, values=(p.id, p.nombre, p.precio, p.cantidad))

    def _registrar_producto(self):
        nombre = self.nombre_entry.get().strip()
        precio = self.precio_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        try:
            nuevo = self.servicio.agregar_producto(nombre, precio, cantidad)
            self._set_mensaje(f"Producto registrado ID {nuevo.id}", "green")
            self._listar_productos()
            self.nombre_entry.delete(0, tk.END)
            self.precio_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

    def _cargar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para consultar", "red")
            return
        p = self.servicio.obtener_producto(pid)
        if not p:
            self._set_mensaje("Producto no encontrado", "red")
            return
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, p.nombre)
        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, str(p.precio))
        self.cantidad_entry.delete(0, tk.END)
        self.cantidad_entry.insert(0, str(p.cantidad))
        self._set_mensaje(f"Producto cargado ID {p.id}", "green")

    def _actualizar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para actualizar", "red")
            return
        nombre = self.nombre_entry.get().strip()
        precio = self.precio_entry.get().strip()
        cantidad = self.cantidad_entry.get().strip()
        try:
            updated = self.servicio.actualizar_producto(pid, nombre=nombre, precio=precio, cantidad=cantidad)
            self._set_mensaje(f"Producto actualizado ID {updated.id}", "green")
            self._listar_productos()
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

    def _eliminar_producto(self):
        pid = self.id_entry.get().strip()
        if not pid:
            self._set_mensaje("Ingrese ID para eliminar", "red")
            return
        try:
            self.servicio.eliminar_producto(pid)
            self._set_mensaje(f"Producto eliminado ID {pid}", "green")
            self._listar_productos()
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

    def mostrar_ventas(self):
        self._clear_panel()
        frm = ttk.Frame(self.panel)
        frm.grid(sticky="nw")

        ttk.Label(frm, text="Usuario:").grid(row=0, column=0, sticky="w")
        self.usuario_cb = ttk.Combobox(frm, state="readonly")
        self.usuario_cb.grid(row=0, column=1, sticky="ew")

        ttk.Label(frm, text="Producto:").grid(row=1, column=0, sticky="w")
        self.producto_cb = ttk.Combobox(frm, state="readonly")
        self.producto_cb.grid(row=1, column=1, sticky="ew")

        btns = ttk.Frame(frm)
        btns.grid(row=2, column=0, columnspan=2, pady=(8, 0))
        ttk.Button(btns, text="Registrar venta", command=self._registrar_venta).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Actualizar listado", command=self._listar_ventas).grid(row=0, column=1, padx=4)

        self.ventas_tree = ttk.Treeview(self.panel, columns=("id", "usuario", "producto", "fecha"), show="headings")
        for col, width in [("id", 50), ("usuario", 150), ("producto", 200), ("fecha", 180)]:
            self.ventas_tree.heading(col, text=col.title())
            self.ventas_tree.column(col, width=width)
        self.ventas_tree.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        self.panel.rowconfigure(1, weight=1)

        usuarios = self.servicio.listar_usuarios()
        self.usuario_cb['values'] = [u.username for u in usuarios]
        productos = self.servicio.listar_productos()
        self.producto_cb['values'] = [f"{p.id} - {p.nombre}" for p in productos]

        self._listar_ventas()

    def _listar_ventas(self):
        for item in self.ventas_tree.get_children():
            self.ventas_tree.delete(item)
        for venta in self.servicio.listar_ventas():
            producto = self.servicio.obtener_producto(venta.producto_id)
            nombre_producto = producto.nombre if producto else f"ID {venta.producto_id}"
            self.ventas_tree.insert("", tk.END, values=(venta.id, venta.username, nombre_producto, venta.fecha))

    def _registrar_venta(self):
        usuario = self.usuario_cb.get().strip()
        producto_sel = self.producto_cb.get().strip()
        if not usuario:
            self._set_mensaje("Seleccione un usuario", "red")
            return
        if not producto_sel:
            self._set_mensaje("Seleccione un producto", "red")
            return
        try:
            producto_id = int(producto_sel.split(" - ")[0])
        except Exception:
            self._set_mensaje("Producto inválido", "red")
            return
        try:
            venta = self.servicio.registrar_venta(usuario, producto_id)
            self._set_mensaje(f"Venta registrada ID {venta.id}", "green")
            self._listar_ventas()
        except Exception as exc:
            self._set_mensaje(str(exc), "red")

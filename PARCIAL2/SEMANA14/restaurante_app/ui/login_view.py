import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.controller = controller
        self.servicio = controller.servicio
        self._build()

    def _build(self):
        self.columnconfigure(0, weight=1)
        frm = ttk.Frame(self, padding=20)
        frm.grid(sticky="nsew")

        ttk.Label(frm, text="Restaurante App - Login", font=(None, 14)).grid(column=0, row=0, columnspan=2, pady=(0,10))
        ttk.Label(frm, text="Usuario:").grid(column=0, row=1, sticky="w")
        self.usuario_entry = ttk.Entry(frm)
        self.usuario_entry.grid(column=1, row=1, sticky="ew")

        ttk.Label(frm, text="Contraseña:").grid(column=0, row=2, sticky="w")
        self.password_entry = ttk.Entry(frm, show='*')
        self.password_entry.grid(column=1, row=2, sticky="ew")

        self.mensaje = ttk.Label(frm, text="", foreground="red")
        self.mensaje.grid(column=0, row=3, columnspan=2, pady=(8,0))

        login_btn = ttk.Button(frm, text="Ingresar", command=self._on_login)
        login_btn.grid(column=0, row=4, columnspan=2, pady=(12,0))

        for child in frm.winfo_children():
            child.grid_configure(padx=6, pady=6)

    def _on_login(self):
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()
        if not usuario or not password:
            self.mensaje.config(text="Ingrese usuario y contraseña")
            return
        ok = self.servicio.validar_acceso(usuario, password)
        if ok:
            self.mensaje.config(text="")
            self.usuario_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.controller.show_main_view()
        else:
            self.mensaje.config(text="Credenciales inválidas")

import os
import tkinter as tk
from tkinter import ttk

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class AppController:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = None
        self.root.title("Restaurante App - Semana 16")
        self.root.geometry("1000x650")

        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self._create_frames()
        self.show_login_view()

    def _create_frames(self):
        self.frames['login'] = LoginView(self.container, controller=self)
        self.frames['main'] = MainView(self.container, controller=self)
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_login_view(self):
        self.usuario_actual = None
        self.frames['login'].tkraise()

    def show_main_view(self):
        if hasattr(self.frames['main'], 'configurar_usuario_actual'):
            self.frames['main'].configurar_usuario_actual(self.usuario_actual)
        self.frames['main'].tkraise()


def main():
    base = os.path.dirname(__file__)
    datos_path = os.path.join(base, 'datos')
    archivo = ArchivoServicio(datos_path)
    servicio = RestauranteServicio(archivo)

    root = tk.Tk()
    app = AppController(root, servicio)
    root.mainloop()


if __name__ == '__main__':
    main()

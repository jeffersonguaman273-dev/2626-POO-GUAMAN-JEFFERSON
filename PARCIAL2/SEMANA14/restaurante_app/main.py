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
        self.root.title("Restaurante App")
        self.root.geometry("600x400")

        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self._create_frames()
        self.show_login_view()

    def _create_frames(self):
        self.frames['login'] = LoginView(self.container, controller=self)
        self.frames['main'] = MainView(self.container, controller=self)
        for f in self.frames.values():
            f.grid(row=0, column=0, sticky="nsew")

    def show_login_view(self):
        frame = self.frames['login']
        frame.tkraise()

    def show_main_view(self):
        frame = self.frames['main']
        frame.tkraise()


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

"""
Módulo mascota.py
Define la clase Mascota con sus atributos y métodos
"""


class Mascota:
    """
    Clase que representa una mascota con sus características y comportamientos.

    Atributos:
        nombre (str): El nombre de la mascota
        especie (str): La especie de la mascota (perro, gato, pajaro, etc.)
        edad (int): La edad de la mascota en años
    """

    def __init__(self, nombre, especie, edad):
        """
        Constructor de la clase Mascota.

        Args:
            nombre (str): Nombre de la mascota
            especie (str): Especie de la mascota
            edad (int): Edad de la mascota
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Método que muestra la información completa de la mascota.

        Returns:
            str: Cadena con la información formateada de la mascota
        """
        informacion = f"""
        ===== INFORMACIÓN DE LA MASCOTA =====
        Nombre: {self.nombre}
        Especie: {self.especie}
        Edad: {self.edad} años
        ====================================="""
        return informacion

    def hacer_sonido(self):
        """
        Método que simula el sonido que hace la mascota según su especie.

        Returns:
            str: El sonido que hace la mascota
        """
        sonidos = {
            "perro": "¡Guau guau!",
            "gato": "¡Miau miau!",
            "pajaro": "¡Pío pío!",
            "conejo": "¡Chíchic!",
            "vaca": "¡Muuu!",
            "cerdo": "¡Oink oink!"
        }

        # Obtener el sonido correspondiente a la especie
        # Si la especie no está en el diccionario, usa un sonido genérico
        sonido = sonidos.get(self.especie.lower(), "¡Hace un sonido!")

        return f"{self.nombre} (el {self.especie}) dice: {sonido}"


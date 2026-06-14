"""
Módulo main.py
Programa principal que demuestra el uso de la clase Mascota
"""

from mascota import Mascota


def main():
    """
    Función principal que crea objetos de la clase Mascota
    y demuestra el uso de sus métodos.
    """
    print("\n" + "="*50)
    print(" PROGRAMA DE GESTIÓN DE MASCOTAS - POO ".center(50))
    print("="*50 + "\n")

    # Crear el primer objeto Mascota
    mascota1 = Mascota("Max", "perro", 3)

    # Crear el segundo objeto Mascota
    mascota2 = Mascota("Whiskers", "gato", 2)

    # Crear un tercer objeto para demostrar más funcionalidades
    mascota3 = Mascota("Tweety", "pajaro", 1)

    # Lista de mascotas para iterar
    mascotas = [mascota1, mascota2, mascota3]

    # Mostrar información y sonidos de cada mascota
    for mascota in mascotas:
        # Mostrar información de la mascota
        print(mascota.mostrar_informacion())

        # Hacer que la mascota emita su sonido
        print(f"Sonido: {mascota.hacer_sonido()}\n")

    print("="*50)
    print(" FIN DEL PROGRAMA ".center(50))
    print("="*50 + "\n")


if __name__ == "__main__":
    main()


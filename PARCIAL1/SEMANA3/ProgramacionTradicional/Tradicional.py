"""
Programa de programación tradicional para registrar y mostrar información de una mascota.
No se usan clases ni objetos: se emplean variables, diccionarios y funciones.

Uso: ejecutar el script y responder las preguntas en pantalla.
"""

def solicitar_datos():
    """Solicita los datos de la mascota mediante teclado y devuelve un diccionario."""
    print("Ingrese los datos de la mascota:")
    nombre = input("  Nombre: ").strip()
    especie = input("  Especie (ej. Perro, Gato): ").strip()
    raza = input("  Raza: ").strip()
    edad = input("  Edad (años): ").strip()
    sexo = input("  Sexo (M/F): ").strip()
    dueno = input("  Nombre del dueño: ").strip()
    contacto = input("  Teléfono o correo del dueño: ").strip()

    mascota = {
        'nombre': nombre,
        'especie': especie,
        'raza': raza,
        'edad': edad,
        'sexo': sexo,
        'dueno': dueno,
        'contacto': contacto,
    }

    return mascota


def mostrar_mascota(mascota):
    """Muestra la información de la mascota de forma organizada."""
    print('\n' + '=' * 40)
    print('  INFORMACIÓN DE LA MASCOTA'.center(40))
    print('=' * 40)
    print(f"Nombre       : {mascota.get('nombre', '')}")
    print(f"Especie      : {mascota.get('especie', '')}")
    print(f"Raza         : {mascota.get('raza', '')}")
    print(f"Edad (años)  : {mascota.get('edad', '')}")
    print(f"Sexo         : {mascota.get('sexo', '')}")
    print('-' * 40)
    print('  DATOS DEL DUEÑO'.center(40))
    print('-' * 40)
    print(f"Dueño        : {mascota.get('dueno', '')}")
    print(f"Contacto     : {mascota.get('contacto', '')}")
    print('=' * 40 + '\n')


def main():
    # Pedir datos y mostrar
    mascota = solicitar_datos()
    mostrar_mascota(mascota)


if __name__ == '__main__':
    main()


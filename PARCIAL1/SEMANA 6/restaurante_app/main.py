"""Punto de entrada: crear objetos Platillo y Bebida, agregarlos al servicio Restaurante y mostrar información."""
import os
import sys
# Asegurar que el directorio del script esté en sys.path para que los imports de paquete funcionen
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    restaurante = Restaurante('Mi Restaurante')

    # Crear platillos
    p1 = Platillo('Lomo a la plancha', 12.50, calorias=650, tipo='principal', tiempo_preparacion=20)
    p2 = Platillo('Ensalada César', 7.25, calorias=320, tipo='entrada', tiempo_preparacion=10)

    # Crear bebidas
    b1 = Bebida('Limonada', 2.50, volumen_ml=350, tamano='mediana', tipo_bebida='jugo')
    b2 = Bebida('Cerveza Artesanal', 4.75, volumen_ml=500, tamano='grande', tipo_bebida='alcohólica')

    # Agregar al restaurante
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(b1)
    restaurante.agregar_producto(b2)

    # Mostrar información (polimorfismo en acción)
    restaurante.mostrar_productos()

    # Demostración de encapsulación y validación de precio
    print('\n-- Intento de cambiar precio a 0 (debe fallar) --')
    exito = p1.cambiar_precio(0)
    print('Cambio exitoso:', exito)
    print('Información del producto tras intento de cambio:')
    print(p1.mostrar_informacion())

    print('\n-- Cambio de precio válido --')
    exito = b1.cambiar_precio(3.00)
    print('Cambio exitoso:', exito)
    print('Información del producto actualizado:')
    print(b1.mostrar_informacion())

    # Mostrar todos los productos después de las modificaciones para ver el estado completo
    print('\n-- Productos después de las modificaciones de precio --')
    restaurante.mostrar_productos()


if __name__ == '__main__':
    main()

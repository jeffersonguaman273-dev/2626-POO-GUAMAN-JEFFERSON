import json
import os
from typing import List, Dict, Any


class ArchivoServicio:
    """Servicio responsable de leer y escribir productos en formato JSON.

    - La ruta por defecto es datos/productos.json en el mismo paquete raíz.
    - Maneja FileNotFoundError, JSONDecodeError y PermissionError de forma controlada.
    """

    def __init__(self, carpeta_datos: str = None) -> None:
        if carpeta_datos:
            self._carpeta = carpeta_datos
        else:
            raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            self._carpeta = os.path.join(raiz, "datos")
        os.makedirs(self._carpeta, exist_ok=True)
        self._ruta_productos = os.path.join(self._carpeta, "productos.json")

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        """Guarda la lista de productos (lista de diccionarios) en productos.json.

        Captura PermissionError y otras excepciones específicas para evitar cierres abruptos.
        """
        try:
            with open(self._ruta_productos, "w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            print(f"Error de permisos al guardar productos: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar productos: {e}")

    def cargar_productos(self) -> List[Dict[str, Any]]:
        """Carga y devuelve la lista de productos (cada uno como dict).

        - Si el archivo no existe devuelve lista vacía.
        - Si el JSON está inválido devuelve lista vacía y muestra mensaje.
        - Si hay problemas de permiso muestra mensaje y devuelve lista vacía.
        """
        if not os.path.exists(self._ruta_productos):
            return []
        try:
            with open(self._ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if isinstance(datos, list):
                    return datos
                # Aceptar también dict (convertir a lista de valores)
                if isinstance(datos, dict):
                    return list(datos.values())
                print("Formato de datos en JSON no esperado (debe ser lista o dict). Se ignorará.")
                return []
        except json.JSONDecodeError as e:
            print(f"El archivo productos.json no contiene JSON válido: {e}")
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer productos: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado al leer productos: {e}")
            return []

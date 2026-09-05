import json
import os
from typing import Any, Dict, List


class ArchivoServicio:
    """Servicio responsable de leer y escribir productos, usuarios y ventas en JSON."""

    def __init__(self, carpeta_datos: str = None) -> None:
        if carpeta_datos:
            self._carpeta = carpeta_datos
        else:
            raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            self._carpeta = os.path.join(raiz, "datos")
        os.makedirs(self._carpeta, exist_ok=True)
        self._ruta_productos = os.path.join(self._carpeta, "productos.json")
        self._ruta_usuarios = os.path.join(self._carpeta, "usuarios.json")
        self._ruta_ventas = os.path.join(self._carpeta, "ventas.json")

    def guardar_productos(self, productos: List[Dict[str, Any]]) -> None:
        try:
            with open(self._ruta_productos, "w", encoding="utf-8") as f:
                json.dump(productos, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            print(f"Error de permisos al guardar productos: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar productos: {e}")

    def cargar_productos(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self._ruta_productos):
            return []
        try:
            with open(self._ruta_productos, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if isinstance(datos, list):
                    return datos
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

    def guardar_usuarios(self, usuarios: List[Dict[str, Any]]) -> None:
        try:
            with open(self._ruta_usuarios, "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            print(f"Error de permisos al guardar usuarios: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar usuarios: {e}")

    def cargar_usuarios(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self._ruta_usuarios):
            return []
        try:
            with open(self._ruta_usuarios, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if isinstance(datos, list):
                    return datos
                if isinstance(datos, dict):
                    return list(datos.values())
                print("Formato de datos en JSON no esperado (debe ser lista o dict). Se ignorará.")
                return []
        except json.JSONDecodeError as e:
            print(f"El archivo usuarios.json no contiene JSON válido: {e}")
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer usuarios: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado al leer usuarios: {e}")
            return []

    def guardar_ventas(self, ventas: List[Dict[str, Any]]) -> None:
        try:
            with open(self._ruta_ventas, "w", encoding="utf-8") as f:
                json.dump(ventas, f, ensure_ascii=False, indent=2)
        except PermissionError as e:
            print(f"Error de permisos al guardar ventas: {e}")
        except Exception as e:
            print(f"Error inesperado al guardar ventas: {e}")

    def cargar_ventas(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self._ruta_ventas):
            return []
        try:
            with open(self._ruta_ventas, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if isinstance(datos, list):
                    return datos
                if isinstance(datos, dict):
                    return list(datos.values())
                print("Formato de datos en JSON no esperado (debe ser lista o dict). Se ignorará.")
                return []
        except json.JSONDecodeError as e:
            print(f"El archivo ventas.json no contiene JSON válido: {e}")
            return []
        except PermissionError as e:
            print(f"Error de permisos al leer ventas: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado al leer ventas: {e}")
            return []

from typing import List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """Servicio que administra productos y usuarios.

    - Productos se mantienen como objetos Producto en memoria y se persisten
      mediante ArchivoServicio en datos/productos.json (lista de dicts).
    - Usuarios permanecen en memoria (no persistidos en esta actividad).
    """

    def __init__(self, archivo_servicio: Optional[ArchivoServicio] = None) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._archivo = archivo_servicio if archivo_servicio is not None else ArchivoServicio()

        # Cargar productos desde el archivo (reconstruir objetos)
        self._cargar_productos_desde_archivo()

    # ---------- INTERACCIÓN CON ArchivoServicio ----------
    def _cargar_productos_desde_archivo(self) -> None:
        registros = self._archivo.cargar_productos()
        self._productos = []
        for idx, registro in enumerate(registros):
            try:
                # Se espera un dict con las claves: codigo,nombre,categoria,precio
                prod = Producto(registro["codigo"], registro["nombre"], registro["categoria"], registro["precio"])
                self._productos.append(prod)
            except KeyError as e:
                print(f"Registro #{idx} inválido: falta la clave {e}. Se omitirá.")
                continue
            except ValueError as e:
                print(f"Registro #{idx} inválido: {e}. Se omitirá.")
                continue
            except Exception as e:
                print(f"Error reconstruyendo registro #{idx}: {e}. Se omitirá.")
                continue

    def _guardar_productos_en_archivo(self) -> None:
        lista = [p.to_dict() for p in self._productos]
        self._archivo.guardar_productos(lista)

    def guardar_datos(self) -> None:
        """Método público para que main.py solicite guardar antes de salir."""
        self._guardar_productos_en_archivo()

    # ---------- PRODUCTOS ----------
    def producto_existe(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return any(p.codigo == codigo for p in self._productos)

    def registrar_producto(self, producto: Producto) -> bool:
        if self.producto_existe(producto.codigo):
            return False
        self._productos.append(producto)
        # Guardar inmediatamente
        self._guardar_productos_en_archivo()
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                             categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        if nombre is not None:
            producto.nombre = nombre.strip()
        if categoria is not None:
            producto.categoria = categoria.strip()
        if precio is not None:
            try:
                producto.precio = float(precio)
            except (TypeError, ValueError):
                raise ValueError("Precio inválido")
        self._guardar_productos_en_archivo()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        for i, p in enumerate(self._productos):
            if p.codigo == codigo:
                del self._productos[i]
                self._guardar_productos_en_archivo()
                return True
        return False

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def obtener_categorias(self) -> Set[str]:
        return set(p.categoria for p in self._productos)

    # ---------- USUARIOS (en memoria) ----------
    def usuario_existe(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(u.identificacion == identificacion for u in self._usuarios)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.usuario_existe(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

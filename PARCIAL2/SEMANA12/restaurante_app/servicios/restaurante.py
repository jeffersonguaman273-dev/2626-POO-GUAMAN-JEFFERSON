from typing import Dict, List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """Servicio que administra productos, usuarios y ventas con índices auxiliares."""

    def __init__(self, archivo_servicio: Optional[ArchivoServicio] = None) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []

        self._productos_por_codigo: Dict[str, Producto] = {}
        self._usuarios_por_identificacion: Dict[str, Usuario] = {}
        self._ventas_por_usuario: Dict[str, List[Venta]] = {}

        self._archivo = archivo_servicio if archivo_servicio is not None else ArchivoServicio()

        self._cargar_productos_desde_archivo()
        self._cargar_usuarios_desde_archivo()
        self._cargar_ventas_desde_archivo()
        self._reconstruir_indices()

    def _reconstruir_indices(self) -> None:
        self._productos_por_codigo = {producto.codigo: producto for producto in self._productos}
        self._usuarios_por_identificacion = {usuario.identificacion: usuario for usuario in self._usuarios}
        self._ventas_por_usuario = {}
        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(venta.usuario_id, []).append(venta)

    def _cargar_productos_desde_archivo(self) -> None:
        registros = self._archivo.cargar_productos()
        self._productos = []
        for idx, registro in enumerate(registros):
            try:
                prod = Producto(
                    registro["codigo"],
                    registro["nombre"],
                    registro["categoria"],
                    registro["precio"],
                    registro.get("stock", 0),
                )
                self._productos.append(prod)
            except KeyError as e:
                print(f"Registro #{idx} inválido: falta la clave {e}. Se omitirá.")
            except ValueError as e:
                print(f"Registro #{idx} inválido: {e}. Se omitirá.")
            except Exception as e:
                print(f"Error reconstruyendo registro #{idx}: {e}. Se omitirá.")

    def _guardar_productos_en_archivo(self) -> None:
        self._archivo.guardar_productos([p.to_dict() for p in self._productos])

    def _cargar_usuarios_desde_archivo(self) -> None:
        registros = self._archivo.cargar_usuarios()
        self._usuarios = []
        for idx, registro in enumerate(registros):
            try:
                usuario = Usuario.from_dict(registro)
                self._usuarios.append(usuario)
            except KeyError as e:
                print(f"Registro de usuario #{idx} inválido: falta la clave {e}. Se omitirá.")
            except ValueError as e:
                print(f"Registro de usuario #{idx} inválido: {e}. Se omitirá.")
            except Exception as e:
                print(f"Error reconstruyendo usuario #{idx}: {e}. Se omitirá.")

    def _guardar_usuarios_en_archivo(self) -> None:
        self._archivo.guardar_usuarios([u.to_dict() for u in self._usuarios])

    def _cargar_ventas_desde_archivo(self) -> None:
        registros = self._archivo.cargar_ventas()
        self._ventas = []
        for idx, registro in enumerate(registros):
            try:
                venta = Venta.from_dict(registro)
                self._ventas.append(venta)
            except KeyError as e:
                print(f"Registro de venta #{idx} inválido: falta la clave {e}. Se omitirá.")
            except ValueError as e:
                print(f"Registro de venta #{idx} inválido: {e}. Se omitirá.")
            except Exception as e:
                print(f"Error reconstruyendo venta #{idx}: {e}. Se omitirá.")

    def _guardar_ventas_en_archivo(self) -> None:
        self._archivo.guardar_ventas([v.to_dict() for v in self._ventas])

    def guardar_datos(self) -> None:
        self._guardar_productos_en_archivo()
        self._guardar_usuarios_en_archivo()
        self._guardar_ventas_en_archivo()

    def producto_existe(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return codigo in self._productos_por_codigo

    def registrar_producto(self, producto: Producto) -> bool:
        if self.producto_existe(producto.codigo):
            return False
        self._productos.append(producto)
        self._productos_por_codigo[producto.codigo] = producto
        self._guardar_productos_en_archivo()
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: Optional[str] = None,
        categoria: Optional[str] = None,
        precio: Optional[float] = None,
        stock: Optional[int] = None,
    ) -> bool:
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
        if stock is not None:
            try:
                s = int(stock)
            except (TypeError, ValueError):
                raise ValueError("Stock inválido")
            if s < 0:
                raise ValueError("Stock no puede ser negativo")
            producto.stock = s
        self._guardar_productos_en_archivo()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        producto = self._productos_por_codigo.get(codigo)
        if producto is None:
            return False
        self._productos = [p for p in self._productos if p.codigo != codigo]
        self._productos_por_codigo.pop(codigo, None)
        self._guardar_productos_en_archivo()
        return True

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def obtener_categorias(self) -> Set[str]:
        return {p.categoria for p in self._productos}

    def usuario_existe(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return identificacion in self._usuarios_por_identificacion

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.usuario_existe(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[usuario.identificacion] = usuario
        self._guardar_usuarios_en_archivo()
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        identificacion = identificacion.strip()
        return self._usuarios_por_identificacion.get(identificacion)

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        try:
            if cantidad <= 0 or producto.stock < cantidad:
                return False
        except Exception:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        try:
            producto.vender(cantidad)
        except ValueError:
            return False

        self._ventas.append(venta)
        self._ventas_por_usuario.setdefault(usuario.identificacion, []).append(venta)

        self._guardar_productos_en_archivo()
        self._guardar_ventas_en_archivo()
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        identificacion_usuario = identificacion_usuario.strip()
        return list(self._ventas_por_usuario.get(identificacion_usuario, []))

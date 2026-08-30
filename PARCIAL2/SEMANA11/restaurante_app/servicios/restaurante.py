from typing import List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    """Servicio que administra productos, usuarios y ventas.

    - Productos, usuarios y ventas se mantienen como objetos en memoria y
      se persisten mediante ArchivoServicio en datos/*.json
    """

    def __init__(self, archivo_servicio: Optional[ArchivoServicio] = None) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._ventas: List[Venta] = []
        self._archivo = archivo_servicio if archivo_servicio is not None else ArchivoServicio()

        # Cargar datos desde archivos
        self._cargar_productos_desde_archivo()
        self._cargar_usuarios_desde_archivo()
        self._cargar_ventas_desde_archivo()

    # ---------- INTERACCIÓN CON ArchivoServicio ----------
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

    def _cargar_usuarios_desde_archivo(self) -> None:
        registros = self._archivo.cargar_usuarios()
        self._usuarios = []
        for idx, registro in enumerate(registros):
            try:
                usr = Usuario.from_dict(registro)
                self._usuarios.append(usr)
            except KeyError as e:
                print(f"Registro de usuario #{idx} inválido: falta la clave {e}. Se omitirá.")
                continue
            except ValueError as e:
                print(f"Registro de usuario #{idx} inválido: {e}. Se omitirá.")
                continue
            except Exception as e:
                print(f"Error reconstruyendo usuario #{idx}: {e}. Se omitirá.")
                continue

    def _guardar_usuarios_en_archivo(self) -> None:
        lista = [u.to_dict() for u in self._usuarios]
        self._archivo.guardar_usuarios(lista)

    def _cargar_ventas_desde_archivo(self) -> None:
        registros = self._archivo.cargar_ventas()
        self._ventas = []
        for idx, registro in enumerate(registros):
            try:
                venta = Venta.from_dict(registro)
                self._ventas.append(venta)
            except KeyError as e:
                print(f"Registro de venta #{idx} inválido: falta la clave {e}. Se omitirá.")
                continue
            except ValueError as e:
                print(f"Registro de venta #{idx} inválido: {e}. Se omitirá.")
                continue
            except Exception as e:
                print(f"Error reconstruyendo venta #{idx}: {e}. Se omitirá.")
                continue

    def _guardar_ventas_en_archivo(self) -> None:
        lista = [v.to_dict() for v in self._ventas]
        self._archivo.guardar_ventas(lista)

    def guardar_datos(self) -> None:
        """Método público para que main.py solicite guardar antes de salir."""
        self._guardar_productos_en_archivo()
        self._guardar_usuarios_en_archivo()
        self._guardar_ventas_en_archivo()

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
                             categoria: Optional[str] = None, precio: Optional[float] = None,
                             stock: Optional[int] = None) -> bool:
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

    # ---------- USUARIOS ----------
    def usuario_existe(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(u.identificacion == identificacion for u in self._usuarios)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.usuario_existe(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        # Guardar inmediatamente
        self._guardar_usuarios_en_archivo()
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        identificacion = identificacion.strip()
        for u in self._usuarios:
            if u.identificacion == identificacion:
                return u
        return None

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

    # ---------- VENTAS ----------
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

        # Crear venta y actualizar colecciones
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        try:
            producto.vender(cantidad)
        except ValueError:
            return False
        self._ventas.append(venta)
        # Guardar cambios en ambos archivos
        self._guardar_productos_en_archivo()
        self._guardar_ventas_en_archivo()
        return True

    def ventas_por_usuario(self, identificacion_usuario: str) -> List[Venta]:
        ventas_usuario: List[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

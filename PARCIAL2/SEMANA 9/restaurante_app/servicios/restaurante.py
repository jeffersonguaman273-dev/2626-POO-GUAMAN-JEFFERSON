import json
import os
from typing import Dict, List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Servicio que administra productos y usuarios del restaurante.

    - Usa listas para colecciones dinámicas (_productos, _usuarios).
    - Persiste los datos en archivos JSON usando diccionarios (clave→valor):
      productos se guardan por código y usuarios por identificación.
    - Proporciona operaciones de registro, búsqueda, actualización, eliminación y listado.
    """

    def __init__(self, carpeta_datos: Optional[str] = None) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

        # Determinar carpeta de datos relative al paquete
        if carpeta_datos:
            self._carpeta_datos = carpeta_datos
        else:
            raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            self._carpeta_datos = os.path.join(raiz, "data")
        os.makedirs(self._carpeta_datos, exist_ok=True)

        self._ruta_productos = os.path.join(self._carpeta_datos, "productos.json")
        self._ruta_usuarios = os.path.join(self._carpeta_datos, "usuarios.json")

        # Cargar datos existentes al iniciar
        self.cargar_datos()

    # ---------- PERSISTENCIA (JSON, con dicts) ----------
    def _guardar_json(self, ruta: str, contenido: Dict) -> None:
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                json.dump(contenido, f, ensure_ascii=False, indent=2)
        except Exception:
            # En caso de error no interrumpir el flujo principal
            pass

    def _cargar_json(self, ruta: str) -> Dict:
        if not os.path.exists(ruta):
            return {}
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def guardar_datos(self) -> None:
        """Guarda productos y usuarios en archivos JSON como diccionarios.

        - productos.json: { codigo: {codigo,nombre,categoria,precio}, ... }
        - usuarios.json: { identificacion: {identificacion,nombre,correo}, ... }
        """
        productos_dict: Dict[str, Dict] = {
            p.codigo: {"codigo": p.codigo, "nombre": p.nombre, "categoria": p.categoria, "precio": p.precio}
            for p in self._productos
        }
        usuarios_dict: Dict[str, Dict] = {
            u.identificacion: {"identificacion": u.identificacion, "nombre": u.nombre, "correo": u.correo}
            for u in self._usuarios
        }
        self._guardar_json(self._ruta_productos, productos_dict)
        self._guardar_json(self._ruta_usuarios, usuarios_dict)

    def cargar_datos(self) -> None:
        """Carga productos y usuarios desde los JSON. Reconstruye objetos en las listas internas."""
        datos_productos = self._cargar_json(self._ruta_productos)
        datos_usuarios = self._cargar_json(self._ruta_usuarios)

        self._productos = []
        for codigo, info in datos_productos.items():
            try:
                prod = Producto(info.get("codigo", codigo), info.get("nombre", ""), info.get("categoria", ""), float(info.get("precio", 0)))
                self._productos.append(prod)
            except Exception:
                continue

        self._usuarios = []
        for identificacion, info in datos_usuarios.items():
            try:
                usr = Usuario(info.get("identificacion", identificacion), info.get("nombre", ""), info.get("correo", ""))
                self._usuarios.append(usr)
            except Exception:
                continue

    def migrar_desde(self, ruta_proyecto_antiguo: str) -> Dict[str, int]:
        """Migra datos desde otro proyecto restaurante_app antiguo.

        Busca archivos JSON de la forma data/productos.json y data/usuarios.json
        dentro de la ruta proporcionada. Si encuentra datos válidos en forma de
        diccionario o lista, los incorpora a las colecciones actuales evitando
        duplicados por código/identificación.

        Devuelve un resumen: {'productos_importados': n, 'usuarios_importados': m}
        """
        resumen = {"productos_importados": 0, "usuarios_importados": 0}
        carpeta_origen = os.path.join(ruta_proyecto_antiguo, "data")
        ruta_prod_og = os.path.join(carpeta_origen, "productos.json")
        ruta_usr_og = os.path.join(carpeta_origen, "usuarios.json")

        # Intentar cargar productos antiguos
        if os.path.exists(ruta_prod_og):
            datos = self._cargar_json(ruta_prod_og)
            # aceptar tanto dict {codigo: {...}} como lista [{...}, ...]
            if isinstance(datos, dict):
                for codigo, info in datos.items():
                    if not self.producto_existe(codigo):
                        try:
                            prod = Producto(info.get("codigo", codigo), info.get("nombre", ""), info.get("categoria", ""), float(info.get("precio", 0)))
                            self._productos.append(prod)
                            resumen["productos_importados"] += 1
                        except Exception:
                            continue
            elif isinstance(datos, list):
                for info in datos:
                    codigo = info.get("codigo")
                    if not codigo:
                        continue
                    if not self.producto_existe(codigo):
                        try:
                            prod = Producto(info.get("codigo"), info.get("nombre", ""), info.get("categoria", ""), float(info.get("precio", 0)))
                            self._productos.append(prod)
                            resumen["productos_importados"] += 1
                        except Exception:
                            continue

        # Intentar cargar usuarios antiguos
        if os.path.exists(ruta_usr_og):
            datos = self._cargar_json(ruta_usr_og)
            if isinstance(datos, dict):
                for identificacion, info in datos.items():
                    if not self.usuario_existe(identificacion):
                        try:
                            usr = Usuario(info.get("identificacion", identificacion), info.get("nombre", ""), info.get("correo", ""))
                            self._usuarios.append(usr)
                            resumen["usuarios_importados"] += 1
                        except Exception:
                            continue
            elif isinstance(datos, list):
                for info in datos:
                    identificacion = info.get("identificacion")
                    if not identificacion:
                        continue
                    if not self.usuario_existe(identificacion):
                        try:
                            usr = Usuario(info.get("identificacion"), info.get("nombre", ""), info.get("correo", ""))
                            self._usuarios.append(usr)
                            resumen["usuarios_importados"] += 1
                        except Exception:
                            continue

        # Guardar cambios si hubo importaciones
        if resumen["productos_importados"] or resumen["usuarios_importados"]:
            self.guardar_datos()

        return resumen

    # ---------- PRODUCTOS ----------
    def producto_existe(self, codigo: str) -> bool:
        codigo = codigo.strip()
        return any(p.codigo == codigo for p in self._productos)

    def registrar_producto(self, producto: Producto) -> bool:
        """Agrega un producto si su código no existe. Guarda cambios en disco."""
        if self.producto_existe(producto.codigo):
            return False
        self._productos.append(producto)
        self.guardar_datos()
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        codigo = codigo.strip()
        for p in self._productos:
            if p.codigo == codigo:
                return p
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                             categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        """Actualiza los campos no None del producto identificado por codigo y guarda los cambios."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        if nombre is not None:
            producto.nombre = nombre.strip()
        if categoria is not None:
            producto.categoria = categoria.strip()
        if precio is not None:
            producto.precio = float(precio)
        self.guardar_datos()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        codigo = codigo.strip()
        for i, p in enumerate(self._productos):
            if p.codigo == codigo:
                del self._productos[i]
                self.guardar_datos()
                return True
        return False

    def listar_productos(self) -> List[str]:
        return [p.mostrar_informacion() for p in self._productos]

    def obtener_categorias(self) -> Set[str]:
        """Devuelve un conjunto con las categorías únicas de los productos."""
        return set(p.categoria for p in self._productos)

    # ---------- USUARIOS ----------
    def usuario_existe(self, identificacion: str) -> bool:
        identificacion = identificacion.strip()
        return any(u.identificacion == identificacion for u in self._usuarios)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.usuario_existe(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        self.guardar_datos()
        return True

    def listar_usuarios(self) -> List[str]:
        return [u.mostrar_informacion() for u in self._usuarios]

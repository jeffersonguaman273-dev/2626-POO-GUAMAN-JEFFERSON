# 🏗️ ARQUITECTURA DEL SISTEMA

## Diagrama de Capas

```
┌────────────────────────────────────────────────────────────────┐
│                    CAPA DE PRESENTACIÓN                        │
│                         (main.py)                              │
│  • Menú interactivo                                            │
│  • Entrada del usuario (input)                                 │
│  • Mostrar resultados (print)                                  │
└────────────────────┬─────────────────────────────────────────┘
                     │
        input() → Datos ingresados
                     │
                     ↓
┌────────────────────────────────────────────────────────────────┐
│              CAPA DE SERVICIOS (LÓGICA)                        │
│               (servicios/restaurante.py)                       │
│  • Validar duplicados                                          │
│  • Registrar objetos                                           │
│  • Buscar y filtrar                                            │
│  • Calcular estadísticas                                       │
└────────────────────┬─────────────────────────────────────────┘
                     │
        Objetos creados → Almacenamiento
                     │
                     ↓
┌────────────────────────────────────────────────────────────────┐
│               CAPA DE MODELOS (DATOS)                          │
│         (modelos/producto.py, cliente.py)                      │
│  • Producto: __init__, @property, @setter                      │
│  • Cliente: @dataclass, __post_init__                          │
│  • Validación en constructores                                 │
└────────────────────────────────────────────────────────────────┘
```

---

## Flujo Completo: Entrada → Objeto → Almacenamiento → Consulta

```
┌─────────────────────────────────────────────────────────────────┐
│                    USUARIO EN CONSOLA                           │
│  Selecciona: "1. Registrar producto"                           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ↓
                ┌──────────────────────┐
                │  Ingresa datos:      │
                │  - Nombre: "Pizza"   │
                │  - Categoría: "Platos"
                │  - Precio: "14.50"   │
                └──────────┬───────────┘
                           │
                           ↓
        ┌──────────────────────────────────────┐
        │ CAPA MODELOS: Constructor Ejecutado  │
        │                                      │
        │  pizza = Producto(                   │
        │    nombre="Pizza",                   │
        │    categoria="Platos",               │
        │    precio="14.50"                    │
        │  )                                   │
        │                                      │
        │  • __init__ se ejecuta               │
        │  • Llamadas a setters:               │
        │    - @nombre.setter: valida ✓        │
        │    - @categoria.setter: valida ✓     │
        │    - @precio.setter: valida ✓        │
        │                                      │
        │  RESULTADO: ✓ Objeto creado OK       │
        └──────────────┬───────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────────────┐
        │ CAPA SERVICIOS: Registrar en Servicio
        │                                      │
        │ restaurante.registrar_producto(      │
        │   pizza                              │
        │ )                                    │
        │                                      │
        │ • Valida que no exista (sin duplicado)
        │ • Agrega a lista: self.productos.append()
        │ • RESULTADO: ✓ Registrado OK         │
        └──────────────┬───────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────────────┐
        │ CAPA PRESENTACIÓN: Mostrar Confirmación
        │                                      │
        │ ✓ Producto registrado exitosamente! │
        │ Pizza - $14.50                       │
        │ Categoría: Platos                    │
        │ Estado: ✓ Disponible                 │
        └──────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────┐
│              USUARIO CONSULTA: "2. Listar productos"            │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ↓
        ┌──────────────────────────────────────┐
        │ CAPA SERVICIOS: Listar              │
        │                                      │
        │ restaurante.listar_productos()      │
        │ → return self.productos             │
        │ → [Pizza, Hamburguesa, Ensalada...] │
        └──────────────┬───────────────────────┘
                       │
                       ↓
        ┌──────────────────────────────────────┐
        │ CAPA PRESENTACIÓN: Mostrar Lista    │
        │                                      │
        │ 1. Pizza - $14.50                   │
        │ 2. Hamburguesa - $12.99             │
        │ 3. Ensalada - $8.99                 │
        │ ...                                  │
        └──────────────────────────────────────┘
```

---

## Estructura de Clases

```
┌─────────────────────────────────────────────────────────────┐
│                    PRODUCTO                                 │
├─────────────────────────────────────────────────────────────┤
│ Atributos:                                                  │
│  _nombre: str         ← privado, acceso via @property      │
│  _categoria: str      ← privado, acceso via @property      │
│  _precio: float       ← privado, acceso via @property      │
│  _disponible: bool    ← privado, acceso via @property      │
├─────────────────────────────────────────────────────────────┤
│ Métodos:                                                    │
│  __init__()                                                 │
│  @property nombre, @setter nombre                          │
│  @property categoria, @setter categoria                    │
│  @property precio, @setter precio                          │
│  @property disponible, @setter disponible                  │
│  mostrar_informacion() → str                                │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                    CLIENTE (@dataclass)                     │
├─────────────────────────────────────────────────────────────┤
│ Atributos (generados automáticamente):                      │
│  nombre: str                                                │
│  correo: str                                                │
│  id_cliente: str                                            │
├─────────────────────────────────────────────────────────────┤
│ Métodos:                                                    │
│  __init__()  ← generado automáticamente por @dataclass     │
│  __post_init__()                                            │
│  __repr__()  ← generado automáticamente                     │
│  mostrar_informacion() → str                                │
└─────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                   RESTAURANTE (Servicio)                    │
├─────────────────────────────────────────────────────────────┤
│ Atributos:                                                  │
│  nombre_restaurante: str                                    │
│  productos: list[Producto]                                 │
│  clientes: list[Cliente]                                   │
├─────────────────────────────────────────────────────────────┤
│ Métodos CRUD PRODUCTOS:                                    │
│  registrar_producto(producto) → bool                        │
│  listar_productos() → list                                  │
│  buscar_producto_por_nombre(nombre) → Producto             │
│  buscar_productos_por_categoria(categoria) → list          │
│  actualizar_producto(...) → bool                            │
│  eliminar_producto(nombre) → bool                           │
│  obtener_productos_disponibles() → list                     │
├─────────────────────────────────────────────────────────────┤
│ Métodos CRUD CLIENTES:                                     │
│  registrar_cliente(cliente) → bool                          │
│  listar_clientes() → list                                   │
│  buscar_cliente_por_id(id) → Cliente                        │
│  buscar_cliente_por_nombre(nombre) → list                   │
│  buscar_cliente_por_correo(correo) → Cliente               │
│  eliminar_cliente(id) → bool                                │
├─────────────────────────────────────────────────────────────┤
│ Métodos INFORMACIÓN:                                       │
│  obtener_estadisticas() → dict                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Validaciones en Cascada

```
Usuario ingresa: "Pizza", "", "14.50"
                  ↓
Llama: Producto(nombre="Pizza", categoria="", precio="14.50")
       ↓
Constructor (__init__) se ejecuta
       ↓
self.nombre = "Pizza"  → Llama @nombre.setter
       ├─ Valida: not "" and strip() != ""? ✓
       └─ self._nombre = "Pizza" ✓
       ↓
self.categoria = ""  → Llama @categoria.setter
       ├─ Valida: not "" and strip() != ""? ✗
       └─ raise ValueError("❌ La categoría no puede estar vacía")
       ↓
RESULTADO: ❌ Error capturado, objeto NO se crea
           Usuario ve: "❌ La categoría no puede estar vacía"
           (objeto nunca entra al sistema)
```

---

## Secuencia de Métodos: Registrar Producto

```
1. main.py → opcion = 1
   ↓
2. registrar_producto_interactivo()
   ├─ nombre = input("Nombre: ")
   ├─ categoria = input("Categoría: ")
   ├─ precio = float(input("Precio: "))
   ↓
3. Producto(nombre, categoria, precio)
   ├─ self.nombre = nombre  → @nombre.setter valida
   ├─ self.categoria = categoria  → @categoria.setter valida
   ├─ self.precio = precio  → @precio.setter valida
   ├─ self.disponible = True  → @disponible.setter valida
   ↓
4. restaurante.registrar_producto(nuevo_producto)
   ├─ Verifica: any(p.nombre.lower() == nombre.lower() for p in self.productos)
   ├─ if duplicado: return False
   ├─ else: self.productos.append(nuevo_producto)
   ├─ return True
   ↓
5. if restaurante.registrar_producto(nuevo_producto):
   ├─ print(f"✓ Producto registrado!")
   ├─ print(nuevo_producto.mostrar_informacion())
   ↓
6. return a menú principal
```

---

## Relaciones Entre Capas

```
PRESENTACIÓN (main.py)
    │
    ├─ Imports: from modelos import Producto, Cliente
    │                from servicios import Restaurante
    │
    ├─ Crea objetos: Producto(...), Cliente(...)
    │
    ├─ Usa servicio: restaurante.registrar_producto(...)
    │
    └─ Muestra resultados: print(objeto.mostrar_informacion())
            │
            ↓
SERVICIOS (restaurante.py)
    │
    ├─ Imports: (ninguno - no importa los modelos explícitamente)
    │
    ├─ Recibe objetos: registrar_producto(producto: Producto)
    │
    ├─ Almacena en listas: self.productos.append(producto)
    │
    └─ Accede a propiedades: p.nombre, p.precio, p.disponible
            │
            ↓
MODELOS (producto.py, cliente.py)
    │
    ├─ Define clases: class Producto, @dataclass class Cliente
    │
    ├─ Implementa @property/@setter con validación
    │
    └─ Métodos de utilidad: mostrar_informacion()
```

---

## Ciclo de Vida de un Objeto Producto

```
CREACIÓN
    ↓
usuario_input() → Producto.__init__() → setters validan
    ↓
¿Válido?
    ├─ Sí → Objeto creado ✓
    ├─ No → ValueError → Usuario reingresa datos
    ↓
ALMACENAMIENTO
    ↓
restaurante.registrar_producto(producto)
    ├─ ¿Duplicado?
    ├─ Sí → return False → Usuario notificado
    ├─ No → self.productos.append(producto) → return True
    ↓
CONSULTA
    ↓
restaurante.listar_productos() o buscar()
    ├─ Itera lista de productos
    ├─ Accede propiedades via @property (no @setter)
    └─ Retorna objeto(s) encontrado(s)
    ↓
MODIFICACIÓN (optional)
    ↓
producto.nombre = "nuevo_nombre" → Usa @setter con validación
    ├─ ¿Válido?
    ├─ Sí → self._nombre = "nuevo_nombre"
    ├─ No → ValueError → Cambio rechazado
    ↓
ELIMINACIÓN (optional)
    ↓
restaurante.eliminar_producto(nombre)
    ├─ Busca en lista
    ├─ Encontrado? → self.productos.remove(producto)
    └─ Retorna True/False
    ↓
FINAL: Objeto eliminado de memoria (cuando app cierra)
```

---

## Ejemplo: Cómo Funciona @property/@setter

```
# Sin @property/@setter (Problema):
producto._precio = -50  # ¡Precio negativo permitido!
print(producto._precio)  # -50 ✗ Datos inválidos

# Con @property/@setter (Solución):
@property
def precio(self):
    return self._precio

@precio.setter
def precio(self, valor):
    if float(valor) <= 0:
        raise ValueError("❌ El precio debe ser mayor que cero")
    self._precio = float(valor)

# Ahora:
producto.precio = -50  # ← Intenta asignar
    ↓
# Automáticamente llama al @precio.setter
@precio.setter (self, -50)
    ├─ float(-50) = -50.0
    ├─ -50.0 <= 0? ✓ Sí
    ├─ raise ValueError("❌ El precio...")
    ↓
# RESULTADO: ❌ Error, no se asigna
print(producto.precio)  # Sigue siendo el anterior ✓ Datos válidos
```

---

## Archivo Modelos/__init__.py

```python
# Permite importar directamente desde paquete:
from modelos import Producto, Cliente

# En lugar de:
from modelos.producto import Producto
from modelos.cliente import Cliente
```

---

## Archivo Servicios/__init__.py

```python
# Permite importar directamente desde paquete:
from servicios import Restaurante

# En lugar de:
from servicios.restaurante import Restaurante
```

---

**Este diagrama muestra la arquitectura completa del sistema y cómo fluyen los datos a través de las capas.** 🏗️

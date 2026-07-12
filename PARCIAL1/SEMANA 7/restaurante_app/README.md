# 🍽️ Sistema de Gestión de Restaurante

**Actividad SEMANA 7 - Programación Orientada a Objetos en Python**

## 📋 Descripción General

Este proyecto implementa un **sistema completo de gestión de restaurante** que demuestra los principios fundamentales de la Programación Orientada a Objetos (POO) en Python, incluyendo:

- ✅ Constructores tradicionales (`__init__`)
- ✅ Decoradores (`@property`, `@setter`)
- ✅ Decorador `@dataclass`
- ✅ Arquitectura modular (separación por capas)
- ✅ Validación de datos y encapsulación
- ✅ Menú interactivo con entrada del usuario

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/                    # Capa de modelos (definición de datos)
│   ├── __init__.py
│   ├── producto.py            # Clase Producto (constructor + @property/@setter)
│   └── cliente.py             # Clase Cliente (@dataclass)
│
├── servicios/                  # Capa de servicios (lógica de negocio)
│   ├── __init__.py
│   └── restaurante.py         # Clase Restaurante (CRUD operations)
│
└── main.py                     # Punto de entrada (menú interactivo)
```

---

## 🎓 Conceptos OOP Demostrados

### 1. **Clase Producto** (`modelos/producto.py`)
**Demuestra**: Constructor tradicional, @property, @setter y validación

```python
# Constructor tradicional (__init__)
def __init__(self, nombre, categoria, precio, disponible=True):
    self.nombre = nombre          # Usa setter
    self.categoria = categoria    # Usa setter
    self.precio = precio          # Usa setter
    self.disponible = disponible  # Usa setter
```

**@property y @setter**: Controlan el acceso a atributos privados

```python
@property
def precio(self):
    """Obtiene el precio"""
    return self._precio

@precio.setter
def precio(self, valor):
    """Establece el precio con validación"""
    if float(valor) <= 0:
        raise ValueError("El precio debe ser mayor que cero")
    self._precio = float(valor)
```

**Validaciones implementadas**:
- ✓ Nombre no vacío
- ✓ Categoría no vacía
- ✓ Precio > 0
- ✓ Disponibilidad booleana

---

### 2. **Clase Cliente** (`modelos/cliente.py`)
**Demuestra**: Decorador @dataclass y post-inicialización

```python
from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    
    def __post_init__(self):
        # Validaciones después de la creación automática
        if not self.nombre or self.nombre.strip() == "":
            raise ValueError("Nombre no puede estar vacío")
```

**Ventajas de @dataclass**:
- ✓ `__init__` generado automáticamente
- ✓ `__repr__` generado automáticamente
- ✓ `__eq__` generado automáticamente
- ✓ Menos código boilerplate

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)
**Demuestra**: Servicios de lógica de negocio, CRUD operations

```python
class Restaurante:
    def __init__(self, nombre_restaurante):
        self.productos = []    # Almacena objetos Producto
        self.clientes = []     # Almacena objetos Cliente
    
    # Métodos CRUD para Productos
    def registrar_producto(self, producto)      # CREATE
    def listar_productos(self)                  # READ
    def buscar_producto_por_nombre(self, nombre) # READ
    def eliminar_producto(self, nombre)         # DELETE
    
    # Métodos CRUD para Clientes
    def registrar_cliente(self, cliente)        # CREATE
    def listar_clientes(self)                   # READ
    def buscar_cliente_por_id(self, id)         # READ
    def eliminar_cliente(self, id)              # DELETE
```

---

## 🔄 Flujo de Datos: entrada → objeto → almacenamiento → consulta

### Paso 1: **Entrada del Usuario**
```
┌─────────────────────────────────┐
│ input() del usuario por consola │
│  - Nombre: "Hamburguesa"        │
│  - Categoría: "Platos Principales"
│  - Precio: "12.99"              │
└─────────────────────────────────┘
```

### Paso 2: **Constructor crea el objeto**
```
┌────────────────────────────────────┐
│ Objeto Producto creado             │
│ - Nombre: "Hamburguesa"            │
│ - Categoría: "Platos Principales"  │
│ - Precio: 12.99 (validado)         │
│ - Disponible: True (por defecto)   │
└────────────────────────────────────┘
```

### Paso 3: **Se registra en el Restaurante**
```
┌──────────────────────────────────────┐
│ restaurante.registrar_producto(obj)  │
│ self.productos.append(producto)      │
└──────────────────────────────────────┘
```

### Paso 4: **Se lista o busca**
```
┌──────────────────────────────────────┐
│ restaurante.listar_productos()       │
│ → [Hamburguesa, Pizza, Ensalada...]  │
└──────────────────────────────────────┘
```

---

## 🎮 Menú Interactivo

```
==================================================
        SISTEMA DE GESTIÓN DE RESTAURANTE
==================================================

📊 8 productos | 👥 4 clientes

==================================================
              MENÚ PRINCIPAL
==================================================

🍽️  PRODUCTOS:
  1. Registrar producto
  2. Listar productos
  3. Buscar producto
  4. Ver productos disponibles
  5. Eliminar producto

👥 CLIENTES:
  6. Registrar cliente
  7. Listar clientes
  8. Buscar cliente
  9. Eliminar cliente

📊 INFORMACIÓN:
  10. Ver estadísticas del restaurante

--------------------------------------------------
  0. Salir
==================================================
```

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos
- Python 3.7+
- No se requieren librerías externas

### Instrucciones

1. **Abre una terminal en la carpeta del proyecto**:
   ```bash
   cd restaurante_app
   ```

2. **Ejecuta el programa principal**:
   ```bash
   python main.py
   ```

3. **Interactúa con el menú**:
   - Selecciona una opción (0-10)
   - Ingresa datos cuando se solicite
   - El programa valida y almacena los datos

4. **Salir del programa**:
   - Selecciona opción `0` en el menú principal

---

## 📦 Datos de Ejemplo Pre-cargados

### Productos Iniciales
| Producto | Categoría | Precio |
|----------|-----------|--------|
| Hamburguesa Clásica | Platos Principales | $12.99 |
| Pizza Margherita | Platos Principales | $14.50 |
| Ensalada César | Ensaladas | $8.99 |
| Pasta Alfredo | Platos Principales | $13.99 |
| Café Espresso | Bebidas | $3.50 |
| Jugo Natural | Bebidas | $5.99 |
| Postre de Chocolate | Postres | $7.99 |
| Helado de Vainilla | Postres | $4.99 |

### Clientes Iniciales
| Nombre | ID | Correo |
|--------|----|----|
| Juan García | CLI001 | juan.garcia@email.com |
| María López | CLI002 | maria.lopez@email.com |
| Carlos Martínez | CLI003 | carlos.martinez@email.com |
| Ana Rodríguez | CLI004 | ana.rodriguez@email.com |

---

## ✨ Características Principales

### ✅ Validación de Datos
```python
# En Producto
- Nombre: no vacío
- Categoría: no vacía
- Precio: mayor que 0
- Disponibilidad: booleana

# En Cliente
- Nombre: no vacío
- Correo: no vacío
- ID: no vacío
```

### ✅ Búsqueda Flexible
```python
# Productos
- Por nombre (insensible a mayúsculas)
- Por categoría
- Ver disponibles

# Clientes
- Por ID
- Por nombre (búsqueda parcial)
- Por correo
```

### ✅ Estadísticas en Tiempo Real
```python
- Total de productos
- Productos disponibles
- Precio promedio
- Total de clientes
```

---

## 🎯 Objetivos de Aprendizaje

Este proyecto enseña:

1. **Constructores**: Cómo inicializar objetos con datos validados
2. **Encapsulación**: Usar @property/@setter para controlar acceso a atributos
3. **@dataclass**: Simplificar definición de clases con atributos
4. **Servicios**: Separar lógica de negocio en capas
5. **CRUD**: Operaciones básicas (Create, Read, Update, Delete)
6. **Validación**: Garantizar integridad de datos desde la entrada
7. **Modularidad**: Organizar código en carpetas y módulos
8. **Interactividad**: Integrar entrada del usuario con POO

---

## 📝 Ejemplo de Uso: Registrar Producto

```python
# USUARIO INGRESA DATOS POR CONSOLA
input: "Sushi Roll"
input: "Platos Principales"
input: "18.99"

# EL PROGRAMA CREA UN OBJETO USANDO EL CONSTRUCTOR
producto = Producto("Sushi Roll", "Platos Principales", 18.99)

# LOS SETTERS VALIDAN LOS DATOS
# Si precio <= 0 → ValueError
# Si nombre vacío → ValueError

# EL OBJETO SE REGISTRA EN EL SERVICIO
restaurante.registrar_producto(producto)

# AHORA PUEDE SER LISTADO Y BUSCADO
print(restaurante.buscar_producto_por_nombre("Sushi Roll"))
# Output: Sushi Roll - $18.99
```

---

## 🔍 Archivos Clave

| Archivo | Responsabilidad | Conceptos |
|---------|-----------------|-----------|
| `producto.py` | Define la clase Producto | `__init__`, `@property`, `@setter` |
| `cliente.py` | Define la clase Cliente | `@dataclass`, `__post_init__` |
| `restaurante.py` | Servicio CRUD | Lógica de negocio, validación |
| `main.py` | Menú interactivo | `input()`, flujo de usuario, integración |

---

## 💡 Notas Didácticas

### ¿Por qué @property y @setter?
- **Validación**: Aseguran que los datos sean válidos
- **Encapsulación**: Controlan el acceso a atributos privados
- **Flexibilidad**: Pueden cambiar la implementación sin afectar código externo

### ¿Por qué @dataclass?
- **Menos código**: No necesitas escribir `__init__`
- **Claridad**: Los atributos son explícitos y tipados
- **Eficiencia**: Es más rápido escribir y leer

### ¿Por qué arquitectura por capas?
- **Mantenibilidad**: Cambios en una capa no afectan otras
- **Testabilidad**: Cada capa puede probarse independientemente
- **Escalabilidad**: Fácil agregar nuevas funcionalidades

---

## 🏆 Requisitos Cumplidos

✅ Estructura modular (modelos, servicios, main)
✅ Clase Producto con `__init__`, `@property`, `@setter`
✅ Clase Cliente con `@dataclass`
✅ Clase Restaurante con métodos CRUD
✅ Menú interactivo desde consola
✅ Validación de datos
✅ Datos de ejemplo pre-cargados
✅ Búsqueda flexible
✅ Nombres descriptivos en snake_case
✅ Comentarios explicativos
✅ Sin código quemado, todo basado en entrada de usuario
✅ Importaciones correctas entre módulos

---

## 📚 Recursos Adicionales

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Decorators in Python](https://docs.python.org/3/glossary.html#term-decorator)
- [Dataclasses Module](https://docs.python.org/3/library/dataclasses.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

**Desarrollado para la SEMANA 7 - Programación Orientada a Objetos**

*Autor: Estudiante de POO*
*Fecha: 2026*

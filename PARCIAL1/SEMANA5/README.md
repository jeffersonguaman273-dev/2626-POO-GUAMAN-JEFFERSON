# Sistema de Gestión de Restaurante - POO

## Descripción

Sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El proyecto demuestra la aplicación de conceptos fundamentales como clases, objetos, atributos, métodos, importaciones modulares y tipos de datos estructurados.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Componentes

### 1. Módulo `modelos/`

#### `producto.py`
Clase que representa un producto disponible en el restaurante.

**Atributos:**
- `id` (int): Identificador único del producto
- `nombre` (str): Nombre descriptivo del producto
- `descripcion` (str): Descripción detallada
- `precio` (float): Precio del producto
- `disponible` (bool): Estado de disponibilidad
- `categoria` (str): Categoría del producto

**Métodos principales:**
- `__init__()`: Constructor con inicialización de atributos
- `__str__()`: Representación textual del producto
- `obtener_detalles()`: Información completa del producto
- `cambiar_disponibilidad()`: Modifica el estado de disponibilidad
- `aplicar_descuento()`: Calcula precio con descuento

#### `cliente.py`
Clase que representa un cliente registrado en el sistema.

**Atributos:**
- `id` (int): Identificador único del cliente
- `nombre` (str): Nombre completo del cliente
- `email` (str): Correo electrónico
- `telefono` (str): Número de contacto
- `es_miembro` (bool): Estado de membresía
- `historial_pedidos` (list): Lista de pedidos realizados

**Métodos principales:**
- `__init__()`: Constructor con inicialización de atributos
- `__str__()`: Representación textual del cliente
- `obtener_detalles()`: Información completa del cliente
- `agregar_pedido()`: Registra un nuevo pedido
- `obtener_total_pedidos()`: Cantidad de pedidos
- `suscribir_a_membresia()`: Activa membresía
- `cancelar_membresia()`: Desactiva membresía

### 2. Módulo `servicios/`

#### `restaurante.py`
Clase que administra el sistema completo del restaurante.

**Atributos:**
- `nombre` (str): Nombre del restaurante
- `productos` (list): Lista de productos disponibles
- `clientes` (list): Lista de clientes registrados

**Métodos principales:**
- `__init__()`: Constructor del restaurante
- `agregar_producto()`: Agrega productos al catálogo
- `agregar_cliente()`: Registra nuevos clientes
- `buscar_producto_por_id()`: Búsqueda de producto por ID
- `buscar_cliente_por_id()`: Búsqueda de cliente por ID
- `buscar_productos_por_categoria()`: Filtrado por categoría
- `obtener_productos_disponibles()`: Productos listos para venta
- `obtener_clientes_miembros()`: Clientes con membresía
- `calcular_promedio_precios()`: Promedio de precios
- `mostrar_informacion()`: Visualización organizada del sistema
- `mostrar_detalles_completos()`: Información detallada de todos

### 3. Punto de Entrada

#### `main.py`
Archivo principal que demuestra el uso del sistema.

**Funcionalidades:**
- Crea instancias de productos y clientes
- Agrega los objetos al restaurante
- Registra pedidos de clientes
- Muestra la información del sistema de forma organizada

## Principios Aplicados

### Convenciones de Nombres
- **PascalCase** para nombres de clases: `Producto`, `Cliente`, `Restaurante`
- **snake_case** para variables, atributos y métodos: `nombre_producto`, `es_miembro`, `agregar_producto()`

### Tipos de Datos
- **Básicos:** str, int, float, bool
- **Compuestos:** list (para almacenar productos, clientes y pedidos)

### Anotaciones de Tipo
Se utilizan anotaciones de tipo para mejorar la legibilidad y permitir mejor detección de errores:
```python
nombre: str
precio: float
disponible: bool
historial_pedidos: list
```

### Constructores y Métodos Especiales
- Método `__init__()` para inicialización de objetos
- Método `__str__()` para representación textual

### Modularidad
- Separación de responsabilidades en diferentes módulos
- Importaciones correctas entre módulos
- Uso de `__init__.py` para crear paquetes

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```

El programa mostrará:
1. Creación de productos con sus detalles
2. Creación de clientes con sus información
3. Información completa y organizada del restaurante
4. Estadísticas sobre productos y clientes

## Ejemplo de Salida

```
============================================================
CREANDO PRODUCTOS DEL RESTAURANTE
============================================================

Producto 1: [ID: 1] Ensalada César ($8.50) - Ensaladas - ✓ Disponible
...

============================================================
INFORMACIÓN COMPLETA DEL RESTAURANTE
============================================================

📋 PRODUCTOS (4 total)
──────────────────────────────────────────────────────────
  [ID: 1] Ensalada César ($8.50) - Ensaladas - ✓ Disponible
  ...
```

## Requisitos Cumplidos

✅ Estructura modular con carpetas organizadas  
✅ Clases con constructores `__init__()`  
✅ Método especial `__str__()` para representación textual  
✅ Tipos de datos básicos: str, int, float, bool  
✅ Listas como tipo de dato compuesto  
✅ Anotaciones de tipo en atributos y parámetros  
✅ Identificadores descriptivos en snake_case y PascalCase  
✅ Importaciones correctas entre módulos  
✅ Comentarios explicativos del código  
✅ Métodos para gestión y consulta de información  
✅ Mínimo 2 objetos de cada modelo creados  
✅ Información mostrada de forma organizada en consola  

## Notas Importantes

- El código no copia literalmente el ejemplo de biblioteca
- No utiliza interfaces gráficas ni menús interactivos
- Enfatiza en la comprensión de POO y modularidad
- Usa identificadores claros y significativos
- Incluye métodos adicionales para extensibilidad futura


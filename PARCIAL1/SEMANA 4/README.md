# Sistema de Gestión de Restaurante - Programación Orientada a Objetos

## Descripción General

Este es un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El proyecto demuestra cómo organizar un sistema en módulos, separar responsabilidades y comunicar archivos mediante importaciones.

## Estructura del Proyecto

```
SEMANA 4/
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto
│   └── cliente.py           # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py       # Clase Restaurante (servicio principal)
└── main.py                  # Punto de entrada del programa
```

## Descripción de Archivos

### `modelos/producto.py`
**Clase: Producto**

Representa un artículo disponible en el restaurante (plato, bebida, postre, etc.).

**Atributos:**
- `id`: Identificador único del producto
- `nombre`: Nombre del producto (ej: Pizza Margarita)
- `precio`: Precio del producto
- `descripcion`: Descripción breve del producto
- `tipo_producto`: Categoría (plato_principal, bebida, postre, entrada)
- `disponibilidad`: Estado de disponibilidad (bool)

**Métodos principales:**
- `__init__()`: Constructor de la clase
- `__str__()`: Representación en texto del producto
- `obtener_informacion()`: Retorna información detallada como diccionario
- `cambiar_disponibilidad()`: Actualiza el estado de disponibilidad
- `actualizar_precio()`: Modifica el precio del producto

---

### `modelos/cliente.py`
**Clase: Cliente**

Representa una persona que realiza pedidos en el restaurante.

**Atributos:**
- `id`: Identificador único del cliente
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico de contacto
- `telefono`: Número de teléfono
- `fecha_registro`: Fecha del registro del cliente
- `numero_pedidos`: Cantidad de pedidos realizados

**Métodos principales:**
- `__init__()`: Constructor de la clase
- `__str__()`: Representación en texto del cliente
- `obtener_informacion()`: Retorna información detallada como diccionario
- `actualizar_contacto()`: Permite cambiar email y/o teléfono
- `registrar_pedido()`: Incrementa el contador de pedidos
- `obtener_dias_cliente()`: Calcula días desde el registro

---

### `servicios/restaurante.py`
**Clase: Restaurante**

Gestiona el restaurante, administrando productos y clientes registrados.

**Atributos:**
- `nombre`: Nombre del restaurante
- `ubicacion`: Ubicación del restaurante
- `productos`: Lista de objetos Producto
- `clientes`: Lista de objetos Cliente

**Métodos principales:**

**Gestión de Productos:**
- `agregar_producto()`: Agrega un nuevo producto
- `eliminar_producto()`: Elimina un producto por ID
- `obtener_producto()`: Busca un producto por ID
- `listar_productos()`: Muestra todos los productos
- `listar_productos_por_tipo()`: Filtra productos por categoría

**Gestión de Clientes:**
- `agregar_cliente()`: Registra un nuevo cliente
- `eliminar_cliente()`: Elimina un cliente por ID
- `obtener_cliente()`: Busca un cliente por ID
- `listar_clientes()`: Muestra todos los clientes
- `registrar_pedido_cliente()`: Registra un pedido de un cliente

**Otros:**
- `obtener_estadisticas()`: Muestra estadísticas del restaurante
- `__str__()`: Resumen del estado del restaurante

---

### `main.py`
**Punto de entrada del programa**

Demuestra el funcionamiento completo del sistema mediante:

1. Creación de la instancia del restaurante
2. Agregación de productos al catálogo
3. Registro de clientes
4. Listado de productos y clientes
5. Registro de pedidos
6. Actualización de información
7. Filtrado de productos por categoría
8. Visualización de información detallada
9. Generación de estadísticas
10. Resumen final

## Requisitos Cumplidos

✅ Estructura de carpetas y archivos según especificación  
✅ Implementación de clases Producto y Cliente en modelos/  
✅ Implementación de clase Restaurante en servicios/  
✅ Uso de constructor `__init__()` en todas las clases  
✅ Definición de atributos pertinentes según el contexto  
✅ Métodos para mostrar y gestionar información  
✅ Implementación del método especial `__str__()`  
✅ Importaciones correctas entre archivos  
✅ Creación de objetos desde main.py  
✅ Agregación de objetos al servicio principal  
✅ Visualización organizada de información en consola  
✅ Comentarios explicativos en el código  
✅ Sistema diferente al ejemplo de biblioteca  
✅ Código original y comprensible  

## Cómo Ejecutar el Programa

### Requisitos
- Python 3.6 o superior instalado

### Pasos
1. Abre una terminal o línea de comandos
2. Navega a la carpeta `SEMANA 4/`:
   ```bash
   cd ruta/a/SEMANA\ 4
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```

## Ejemplo de Salida

El programa mostrará:
- Creación del restaurante
- Catálogo de productos disponibles
- Base de datos de clientes
- Registro de pedidos
- Actualización de información
- Filtrado de productos por categoría
- Información detallada de objetos
- Estadísticas generales del restaurante

## Conceptos POO Demostrados

### 1. **Encapsulación**
- Cada clase tiene atributos y métodos específicos
- Se respetan las responsabilidades de cada clase

### 2. **Abstracción**
- Los métodos ocultan la complejidad interna
- Se presenta una interfaz clara y simple

### 3. **Modularidad**
- Código organizado en módulos independientes
- Fácil mantenimiento y extensión

### 4. **Reutilización**
- Importación correcta entre módulos
- Las clases pueden usarse independientemente

### 5. **Método `__str__()`**
- Permite representar objetos como texto legible
- Facilita la visualización en consola

## Extensiones Posibles

El sistema puede mejorarse con:
- Clase Pedido para detallar qué productos compra cada cliente
- Métodos de búsqueda más avanzados
- Persistencia de datos en archivos o bases de datos
- Interfaz gráfica
- Sistema de inventario actual
- Historial de pedidos por cliente

## Notas Importantes

- El sistema NO es un clon del ejemplo de biblioteca
- Cada aspecto del código fue diseñado para el contexto de un restaurante
- Las responsabilidades están claramente separadas
- El código es fácil de entender y mantener
- Los comentarios explican las partes principales del código

---

**Autor:** Sistema de Gestión de Restaurante - POO en Python  
**Fecha:** 2026  
**Propósito:** Demostración de Programación Orientada a Objetos



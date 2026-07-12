# 📚 GUÍA DIDÁCTICA: Entendiendo los Principios OOP

## Introducción

Esta guía te ayudará a entender **cómo funciona el sistema de restaurante** y qué conceptos OOP se demuestran en cada parte del código.

---

## 1️⃣ EL CONSTRUCTOR: Transformando entrada en objeto

### ¿Qué es?
Un **constructor** es un método especial que se ejecuta cuando creas un objeto. En Python se llama `__init__`.

### Ejemplo en nuestro sistema

**Usuario ingresa datos por consola:**
```
Nombre del producto: Hamburguesa
Categoría: Platos Principales
Precio: 12.99
```

**El constructor crea el objeto:**
```python
# En main.py
nombre = input("Nombre del producto: ")        # "Hamburguesa"
categoria = input("Categoría: ")                # "Platos Principales"
precio = float(input("Precio ($): "))           # 12.99

# AQUÍ OCURRE LA MAGIA: El constructor se ejecuta
nuevo_producto = Producto(nombre, categoria, precio)
#                         ↓       ↓         ↓
#                    Pasan al __init__
```

**Dentro del constructor (producto.py):**
```python
def __init__(self, nombre, categoria, precio, disponible=True):
    # El constructor crea atributos privados usando setters
    self.nombre = nombre           # Usa el setter @nombre.setter
    self.categoria = categoria     # Usa el setter @categoria.setter
    self.precio = precio           # Usa el setter @precio.setter
    self.disponible = disponible   # Usa el setter @disponible.setter
    
    # Cada setter valida los datos
    # Si algo está mal, lanza un ValueError
```

### ¿Por qué es importante?
- ✅ **Garantiza validación**: Los datos se validan al crear el objeto
- ✅ **Estado consistente**: El objeto nunca nace en un estado inválido
- ✅ **Menos errores**: Atrapamos problemas ANTES de almacenar

---

## 2️⃣ @property y @setter: Control de acceso

### ¿Qué son?
Los **decoradores @property y @setter** permiten:
- Acceder a atributos como si fueran variables normales
- Validar datos antes de almacenarlos
- Cambiar la implementación sin romper código externo

### Analogía del mundo real

Imagina un **banco con un cajero**:

```
❌ SIN @property (Acceso directo):
dinero = 1000
dinero = -500  ← ¡El banco permite dinero negativo!

✅ CON @property y @setter (Control):
cajero.depositar(-500)  ← El cajero valida: "¡No puedo depositar negativo!"
```

### Ejemplo en nuestro código

**Acceso sin validación (MAL):**
```python
producto._precio = -50  # ¡Precio negativo! Desastre.
```

**Acceso CON validación (BIEN):**
```python
# En producto.py
@property
def precio(self):
    """Lectura: retorna el valor"""
    return self._precio

@precio.setter
def precio(self, valor):
    """Escritura: valida antes de almacenar"""
    try:
        precio_float = float(valor)
        if precio_float <= 0:
            raise ValueError("❌ El precio debe ser mayor que cero")
        self._precio = precio_float
    except (TypeError, ValueError):
        raise ValueError("❌ El precio debe ser un número válido")
```

**Usando el @property/@setter:**
```python
# Usuario intenta crear producto
producto = Producto("Pizza", "Platos", -50)
# ↓
# El __init__ llama: self.precio = -50
# ↓
# Se ejecuta: @precio.setter
# ↓
# Validación: if precio_float <= 0 → raise ValueError
# ↓
# RESULTADO: ❌ Error capturado, objeto no se crea
```

### Los tres atributos validados

```python
# NOMBRE: No puede estar vacío
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, valor):
    if not valor or valor.strip() == "":
        raise ValueError("❌ El nombre no puede estar vacío")
    self._nombre = valor.strip()

# Uso:
producto.nombre = ""     # ❌ Error
producto.nombre = "Pizza"  # ✅ OK

# CATEGORÍA: No puede estar vacía
@property
def categoria(self):
    return self._categoria

@categoria.setter
def categoria(self, valor):
    if not valor or valor.strip() == "":
        raise ValueError("❌ La categoría no puede estar vacía")
    self._categoria = valor.strip()

# PRECIO: Debe ser mayor que 0
@property
def precio(self):
    return self._precio

@precio.setter
def precio(self, valor):
    if float(valor) <= 0:
        raise ValueError("❌ El precio debe ser mayor que cero")
    self._precio = float(valor)

# Uso:
producto.precio = 0      # ❌ Error
producto.precio = -10    # ❌ Error
producto.precio = 19.99  # ✅ OK
```

---

## 3️⃣ @dataclass: Simplificando clases

### ¿Qué es?
**@dataclass** es un decorador que genera automáticamente:
- `__init__`: Constructor
- `__repr__`: Representación en string
- `__eq__`: Comparación entre objetos

### Comparación: Con vs Sin @dataclass

**SIN @dataclass (muchas líneas):**
```python
class Cliente:
    def __init__(self, nombre, correo, id_cliente):
        self.nombre = nombre
        self.correo = correo
        self.id_cliente = id_cliente
    
    def __repr__(self):
        return f"Cliente('{self.nombre}', '{self.correo}', '{self.id_cliente}')"
    
    def __eq__(self, otro):
        if not isinstance(otro, Cliente):
            return False
        return (self.nombre == otro.nombre and 
                self.correo == otro.correo and 
                self.id_cliente == otro.id_cliente)
```

**CON @dataclass (muy simple):**
```python
from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
```

### Con `__post_init__` para validación

```python
@dataclass
class Cliente:
    nombre: str
    correo: str
    id_cliente: str
    
    def __post_init__(self):
        # Se ejecuta automáticamente DESPUÉS de __init__
        # Perfecta para validaciones
        if not self.nombre or self.nombre.strip() == "":
            raise ValueError("Nombre no puede estar vacío")
        if not self.correo or self.correo.strip() == "":
            raise ValueError("Correo no puede estar vacío")
```

### Flujo de ejecución

```
1. @dataclass genera automáticamente __init__
    ↓
2. Se ejecuta __init__ con los parámetros
    ↓
3. Se llama automáticamente __post_init__
    ↓
4. Aquí validamos los datos
```

---

## 4️⃣ SERVICIOS: Lógica de negocio centralizada

### ¿Qué es?
Un **servicio** es una clase que administra operaciones sobre múltiples objetos.

En nuestro caso: La clase **Restaurante** administra listas de productos y clientes.

### Analogy: Biblioteca

```
Libros = Productos
Miembros = Clientes
Bibliotecario = Restaurante (servicio)

El bibliotecario sabe:
- Cuántos libros hay
- Dónde están
- Quién los pidió prestado
- Cómo buscar un libro específico
```

### Operaciones CRUD

**C**reate - Crear (registrar)
```python
def registrar_producto(self, producto):
    if any(p.nombre.lower() == producto.nombre.lower() for p in self.productos):
        return False  # Ya existe
    self.productos.append(producto)  # Agregar a la lista
    return True
```

**R**ead - Leer (listar/buscar)
```python
def listar_productos(self):
    return self.productos  # Retorna todos

def buscar_producto_por_nombre(self, nombre):
    for producto in self.productos:
        if producto.nombre.lower() == nombre.lower():
            return producto  # Retorna el encontrado
    return None  # No encontrado
```

**U**pdate - Actualizar
```python
def actualizar_producto(self, nombre_antiguo, nombre_nuevo=None):
    producto = self.buscar_producto_por_nombre(nombre_antiguo)
    if producto:
        if nombre_nuevo:
            producto.nombre = nombre_nuevo  # Usa el setter
        return True
    return False
```

**D**elete - Eliminar
```python
def eliminar_producto(self, nombre):
    producto = self.buscar_producto_por_nombre(nombre)
    if producto:
        self.productos.remove(producto)
        return True
    return False
```

### ¿Por qué centralizar en un servicio?

```
SIN SERVICIO (Caos):
main.py
├── productos_list = []
├── clientes_list = []
└── Todo el código mezclado

✅ CON SERVICIO (Organizado):
main.py
└── restaurante = Restaurante()
    ├── self.productos (lista controlada)
    ├── self.clientes (lista controlada)
    └── Métodos para gestionar ambas listas
```

---

## 5️⃣ ARQUITECTURA POR CAPAS: Modularidad

### ¿Qué es?
Separar el código en **capas**:
- **Capa de modelos**: Define QUÉ son los datos
- **Capa de servicios**: Define CÓMO se manipulan
- **Capa de presentación**: Interfaz con el usuario (main.py)

### Flujo de datos

```
┌─────────────────────────────────────────┐
│  CAPA DE PRESENTACIÓN (main.py)         │
│  - Menú interactivo                     │
│  - input() del usuario                  │
│  - Mostrar resultados                   │
└──────────────┬──────────────────────────┘
               │ Datos ingresados
               ↓
┌─────────────────────────────────────────┐
│  CAPA DE SERVICIOS (restaurante.py)     │
│  - Validar datos                        │
│  - Registrar objetos                    │
│  - Buscar y listar                      │
└──────────────┬──────────────────────────┘
               │ Objetos creados
               ↓
┌─────────────────────────────────────────┐
│  CAPA DE MODELOS (producto.py, cliente.py)
│  - Definir atributos                    │
│  - Validar en constructores             │
│  - Control con @property/@setter        │
└─────────────────────────────────────────┘
```

### Ejemplo real de la arquitectura

```python
# USUARIO INGRESA DATOS EN main.py
nombre = input("Nombre del producto: ")  # "Hamburguesa"

# ↓ CAPA DE PRESENTACIÓN CREA OBJETO (llama capa de modelos)
nuevo_producto = Producto(nombre, "Platos", 12.99)
#                ↓↓↓ VA A CAPA DE MODELOS

# En producto.py (CAPA DE MODELOS):
def __init__(self, nombre, categoria, precio):
    self.nombre = nombre  # Validación via @setter

# ↓ CAPA DE PRESENTACIÓN REGISTRA (llama capa de servicios)
restaurante.registrar_producto(nuevo_producto)
#↓↓↓ VA A CAPA DE SERVICIOS

# En restaurante.py (CAPA DE SERVICIOS):
def registrar_producto(self, producto):
    self.productos.append(producto)

# ↓ CAPA DE PRESENTACIÓN MUESTRA RESULTADO
print(f"✓ Producto registrado: {nuevo_producto}")
```

### ¿Por qué es importante?

```
❌ TODO EN MAIN.PY (Caos):
- 500 líneas de código
- Difícil de leer
- Cambios riesgosos
- Imposible reutilizar

✅ CON CAPAS (Orden):
- Cada archivo tiene una responsabilidad clara
- Código reutilizable
- Fácil de mantener
- Fácil de testear
```

---

## 6️⃣ FLUJO COMPLETO: Usuario → Objeto → Almacenamiento → Consulta

### Paso a Paso

#### PASO 1: Usuario selecciona opción en main.py
```python
opcion = 1  # Registrar producto
```

#### PASO 2: Se solicita información al usuario
```python
nombre = input("Nombre del producto: ")        # "Pizza Margherita"
categoria = input("Categoría: ")                # "Platos Principales"
precio = float(input("Precio ($): "))           # 14.50
```

#### PASO 3: Se crea objeto usando CONSTRUCTOR
```python
nuevo_producto = Producto(nombre, categoria, precio)
# ↓ Llamadas automáticas a setters:
#   - nombre setter: valida "Pizza Margherita" ✅
#   - categoria setter: valida "Platos Principales" ✅
#   - precio setter: valida 14.50 > 0 ✅
# ↓
# RESULTADO: Objeto creado exitosamente
```

#### PASO 4: Se registra en el SERVICIO
```python
restaurante.registrar_producto(nuevo_producto)
# ↓
# En restaurante.py:
#   - Verifica que no exista (no duplicados)
#   - Agrega a la lista: self.productos.append(nuevo_producto)
```

#### PASO 5: Usuario ve confirmación
```
✓ Producto registrado exitosamente!
Producto: Pizza Margherita
Categoría: Platos Principales
Precio: $14.50
Estado: ✓ Disponible
```

#### PASO 6: Usuario lista productos
```python
opcion = 2  # Listar productos
```

#### PASO 7: Se CONSULTA el servicio
```python
productos = restaurante.listar_productos()
# ↓ Retorna: [Pizza Margherita, Hamburguesa, Ensalada, ...]
```

#### PASO 8: Se muestran resultados
```
📋 LISTA DE PRODUCTOS
1. Pizza Margherita - $14.50
   Categoría: Platos Principales | Disponible: ✓
2. Hamburguesa Clásica - $12.99
   Categoría: Platos Principales | Disponible: ✓
...
```

---

## 🎯 Resumen de Conceptos

| Concepto | Propósito | Ejemplo |
|----------|----------|---------|
| **__init__** | Inicializar objeto con validación | `Producto("Pizza", "Platos", 14.50)` |
| **@property** | Leer atributo privado | `producto.precio` |
| **@setter** | Escribir con validación | `producto.precio = 15.00` |
| **@dataclass** | Generar __init__ automáticamente | `@dataclass class Cliente` |
| **Servicio** | Centralizar CRUD operations | `Restaurante.registrar_producto()` |
| **Arquitectura capas** | Separar responsabilidades | modelos, servicios, main |

---

## 💭 Preguntas de Auto-Evaluación

✅ ¿Entiendo qué hace `__init__`?
✅ ¿Puedo explicar por qué usamos @property/@setter?
✅ ¿Sé cuándo usar @dataclass vs constructor tradicional?
✅ ¿Entiendo qué es un servicio?
✅ ¿Puedo dibujar el flujo: entrada → objeto → almacenamiento?
✅ ¿Sé por qué separamos en capas?

Si respondiste "sí" a todas, **¡entiendes los conceptos OOP!** 🎉

---

## 🚀 Próximos Pasos

Ahora que entiendes cómo funciona el sistema:

1. **Modifica el código**: Agrega más validaciones
2. **Extiende el sistema**: Agrega nueva funcionalidad (órdenes, pedidos)
3. **Mejora la UI**: Haz el menú más bonito con colores
4. **Prueba casos edge**: ¿Qué pasa si ingresamos datos inválidos?
5. **Aprende persistencia**: Guarda los datos en archivos JSON o CSV

---

**¡Éxito en tu aprendizaje de POO!** 🎓

*Recuerda: La POO se trata de pensar en objetos, no en funciones.*

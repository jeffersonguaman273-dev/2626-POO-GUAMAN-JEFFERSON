# 🚀 INICIO RÁPIDO: Sistema de Gestión de Restaurante

## ⚡ 5 pasos para empezar (30 segundos)

### Paso 1: Abre la terminal
```bash
cd c:\Users\USER\UEA\2626-POO-GUAMAN-JEFFERSON\PARCIAL1\SEMANA\ 7\restaurante_app
```

### Paso 2: Ejecuta el programa
```bash
python main.py
```

### Paso 3: Selecciona opción del menú
Verás esto:
```
==================================================
        SISTEMA DE GESTIÓN DE RESTAURANTE
==================================================

📊 8 productos | 👥 4 clientes

1. Registrar producto
2. Listar productos
3. Buscar producto
...
0. Salir

Selecciona una opción [0-10]: _
```

### Paso 4: Ingresa un número (0-10)
Por ejemplo: `2` para listar productos

### Paso 5: Presiona Enter
¡Verás los resultados!

---

## 🎮 Opciones del Menú Explicadas

| Opción | Descripción | Ejemplo |
|--------|-----------|---------|
| **1** | Registrar nuevo producto | Ingresa: "Sushi", "Platos", "18.99" |
| **2** | Ver lista completa de productos | Muestra: Pizza, Hamburguesa, Ensalada... |
| **3** | Buscar producto por nombre | Ingresa: "Pizza" → Encuentra Pizza Margherita |
| **4** | Ver solo productos disponibles | Muestra solo items con ✓ |
| **5** | Eliminar producto | Ingresa: "Pizza" → Eliminada |
| **6** | Registrar nuevo cliente | Ingresa: "Pedro", "pedro@email.com", "CLI005" |
| **7** | Ver lista de clientes | Muestra todos los clientes registrados |
| **8** | Buscar cliente | Por ID, nombre o correo |
| **9** | Eliminar cliente | Ingresa ID del cliente a eliminar |
| **10** | Ver estadísticas | Total productos, precio promedio, total clientes |
| **0** | Salir | Cierra el programa |

---

## 📝 Ejemplo Paso a Paso: Registrar Producto

```
Selecciona una opción [0-10]: 1

--------------------------------------------------
📝 REGISTRAR NUEVO PRODUCTO
--------------------------------------------------
Nombre del producto: Tacos
Categoría (ej: Bebida, Plato Principal, Postre): Platos Principales
Precio ($): 10.50

✓ Producto registrado exitosamente!
  Producto: Tacos
  Categoría: Platos Principales
  Precio: $10.50
  Estado: ✓ Disponible

✓ Presiona Enter para continuar...
```

---

## 📊 Datos de Ejemplo

**Ya cargados al iniciar:**

### Productos (8):
1. Hamburguesa Clásica - $12.99
2. Pizza Margherita - $14.50
3. Ensalada César - $8.99
4. Pasta Alfredo - $13.99
5. Café Espresso - $3.50
6. Jugo Natural - $5.99
7. Postre de Chocolate - $7.99
8. Helado de Vainilla - $4.99

### Clientes (4):
1. Juan García (CLI001)
2. María López (CLI002)
3. Carlos Martínez (CLI003)
4. Ana Rodríguez (CLI004)

---

## 🔍 Tipos de Búsqueda

### Buscar Producto
```
Opción 3 → Ingresa "Pizza"
Resultado: Encuentra "Pizza Margherita"
```

Nota: Búsqueda insensible a mayúsculas (funciona: "pizza", "PIZZA", "PiZzA")

### Buscar Cliente - Opción 1: Por ID
```
Ingresa ID: CLI001
Resultado: Juan García
```

### Buscar Cliente - Opción 2: Por Nombre
```
Ingresa nombre: María
Resultado: María López (CLI002)
```

### Buscar Cliente - Opción 3: Por Correo
```
Ingresa correo: carlos@email.com
Resultado: Carlos Martínez
```

---

## 🎓 Ver Ejemplos Automáticos

Si prefieres VER el sistema funcionando sin interactuar:

```bash
python ejemplo_uso.py
```

Esto ejecutará 7 ejemplos demostrando:
1. ✓ Crear objetos con constructores
2. ✓ Usar @property y @setter
3. ✓ Operaciones CRUD (Create, Read, Update, Delete)
4. ✓ Búsquedas avanzadas
5. ✓ Gestionar clientes
6. ✓ Ver estadísticas
7. ✓ Validaciones en acción

---

## ⚠️ Errores Comunes y Soluciones

### Error: "No se encuentra main.py"
**Solución**: Asegúrate de estar en la carpeta correcta
```bash
cd c:\Users\USER\UEA\2626-POO-GUAMAN-JEFFERSON\PARCIAL1\SEMANA\ 7\restaurante_app
```

### Error: "ModuleNotFoundError: No module named 'modelos'"
**Solución**: Ejecuta desde la carpeta de restaurante_app, no desde subcarpetas

### Error: "El precio debe ser mayor que cero"
**Solución**: Ingresa un precio válido (>0). Ej: 19.99, no 0 o -10

### Error: "El nombre no puede estar vacío"
**Solución**: Ingresa un nombre. No dejes el campo en blanco

---

## 💡 Tips Útiles

### Tip 1: Busca sin importar mayúsculas
```
Ingresa: "cafe" (minúsculas)
Ingresa: "CAFE" (mayúsculas)
Ingresa: "CaFe" (mixto)
→ Todos encuentran "Café Espresso"
```

### Tip 2: Las validaciones protegen tus datos
```
Intenta: Precio = -50
Sistema: ❌ Error - precio debe ser > 0
→ Tus datos permanecen válidos
```

### Tip 3: No hay duplicados
```
Intenta: Registrar "Pizza Margherita" dos veces
Sistema: ❌ Error - "Pizza Margherita" ya existe
→ Solo una versión en el sistema
```

### Tip 4: Ver estadísticas para resumen rápido
```
Opción 10 → Ver estadísticas
Muestra: Total productos, disponibles, precio promedio, total clientes
```

---

## 📚 Documentación Disponible

Si necesitas ENTENDER cómo funciona todo:

1. **README.md** - Descripción general completa
2. **GUIA_DIDACTICA.md** - Conceptos OOP explicados
3. **INSTRUCCIONES.txt** - Manual de referencia
4. **ARQUITECTURA.md** - Diagramas del sistema
5. **RESUMEN_EJECUTIVO.md** - Resumen del proyecto

---

## 🔧 Requisitos del Sistema

- **Python**: 3.7 o superior
- **Sistema Operativo**: Windows, Mac, Linux
- **Dependencias externas**: ¡NINGUNA! (Solo Python puro)

---

## ✅ Checklist: ¿Todo funcionando?

- [ ] Abro terminal en carpeta restaurante_app
- [ ] Ejecuto `python main.py`
- [ ] Veo el menú interactivo
- [ ] Selecciono opción 2 (Listar productos)
- [ ] Veo lista de 8 productos
- [ ] Selecciono opción 7 (Listar clientes)
- [ ] Veo lista de 4 clientes
- [ ] Selecciono opción 1 (Registrar producto)
- [ ] Ingreso datos y se registra sin errores
- [ ] Selecciono opción 0 (Salir) y cierra

¡Si marcaste todos = **Sistema funcionando correctamente!** ✨

---

## 🎯 Próximas Acciones

### Para Estudiantes
1. Lee **GUIA_DIDACTICA.md** para entender los conceptos
2. Estudia el código en cada archivo Python
3. Modifica datos de ejemplo
4. Intenta agregar nuevas funcionalidades

### Para Docentes
1. Revisa la estructura modular
2. Verifica que cumple todos los requisitos
3. Examina las validaciones implementadas
4. Usa como material de enseñanza

---

## 📞 Soporte Rápido

**P: ¿Cómo cierro la aplicación?**
R: Selecciona opción 0 (Salir) en el menú

**P: ¿Dónde se guardan los datos?**
R: En memoria mientras ejecutas. Se pierden al cerrar (intencional para esta práctica)

**P: ¿Puedo tener dos clientes con mismo correo?**
R: No, pero puedes actualizar el correo de un cliente existente

**P: ¿El sistema distingue mayúsculas en búsqueda?**
R: No, la búsqueda es insensible a mayúsculas (mejor UX)

**P: ¿Puedo registrar cliente sin correo?**
R: No, es requerido. La validación lo impide.

---

## 🎉 ¡Listo para Comenzar!

```bash
cd restaurante_app
python main.py
```

**¡Que disfrutes usando el Sistema de Gestión de Restaurante!** 🍽️

---

**SEMANA 7 - Programación Orientada a Objetos**

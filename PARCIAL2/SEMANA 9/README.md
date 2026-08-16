# Sistema restaurante_app — Semana 9

Autor: Jefferson Guaman

Descripción breve

Proyecto de consola que administra productos y usuarios de un restaurante. Mantiene separación entre modelos, servicios y el punto de entrada (main.py). Esta versión incorpora el uso funcional de las estructuras de datos principales de Python: list, tuple, dict y set.

Estructura del proyecto

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Responsabilidad de componentes

- modelos/producto.py: clase Producto (codigo, nombre, categoria, precio) y método mostrar_informacion().
- modelos/usuario.py: clase Usuario (identificacion, nombre, correo) y método mostrar_informacion().
- servicios/restaurante.py: clase Restaurante que administra colecciones y operaciones sobre productos y usuarios.
- main.py: menú interactivo y coordinación de la interacción por consola.

Uso de estructuras de datos

- list: Las colecciones dinámicas de productos y usuarios se modelan con listas (self._productos y self._usuarios) dentro de Restaurante. Permiten agregar, eliminar y recorrer elementos.
- tuple: MENU_OPCIONES en main.py es una tupla que representa el conjunto estable de opciones del menú durante la ejecución.
- dict: El diccionario "acciones" en main.py asocia la clave (número de opción) con la función que ejecuta esa acción, siguiendo la relación clave→valor.
- set: El método obtener_categorias() de Restaurante devuelve un conjunto de categorías únicas para presentar sin duplicados.

Persistencia

- Los datos de productos y usuarios se archivan en formato JSON dentro de la carpeta `data/` del paquete: `data/productos.json` y `data/usuarios.json`.
- Cada archivo almacena un diccionario (estructura clave→valor) donde la clave es el identificador (código de producto o identificación de usuario) y el valor es otro diccionario con los campos del registro. Esto facilita la carga y reconstrucción de objetos al iniciar el programa.

Ejecución

Desde la carpeta `PARCIAL2\SEMANA 9` ejecutar:

```powershell
cd .\restaurante_app
python .\main.py
```

Reflexión

Seleccionar la estructura de datos adecuada mejora la claridad y eficiencia. Las listas permiten colecciones dinámicas ordenadas; las tuplas representan datos inmutables/estables; los diccionarios mapean claves a valores para despacho rápido; los conjuntos eliminan duplicados cuando interesa la unicidad. Esta versión hace uso real de cada una de estas estructuras para cumplir requisitos funcionales del sistema.

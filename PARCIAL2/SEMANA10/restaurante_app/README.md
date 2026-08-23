Nombre: Jefferson Guaman

Sistema: restaurante_app (Semana 10) — Persistencia JSON de productos

Descripción
Este proyecto administra productos y usuarios de un restaurante desde la línea de comandos. En la entrega de la Semana 10 se añadió persistencia de productos mediante un archivo JSON (datos/productos.json). Durante la ejecución el sistema sigue trabajando con objetos de la clase Producto; el archivo se usa solo para guardar y recuperar datos entre sesiones.

Estructura del proyecto
restaurante_app/
├── datos/
│   └── productos.json        # Archivo de persistencia (lista de objetos)
├── modelos/
│   ├── __init__.py
│   ├── producto.py           # Clase Producto, validaciones y to_dict()
│   └── usuario.py            # Clase Usuario (no persistida en esta versión)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py   # Lectura y escritura de datos/productos.json
│   └── restaurante.py        # Lógica del dominio: gestionar productos y usuarios
└── main.py                   # Interfaz por consola y coordinación de carga/guardado

Responsabilidad de los componentes
- modelos/producto.py: mantiene la clase Producto con validaciones (codigo, nombre, categoria no vacíos; precio >= 0) y el método to_dict() para serializar.
- modelos/usuario.py: clase Usuario; los usuarios permanecen en memoria (no se persisten en esta actividad).
- servicios/archivo_servicio.py: centraliza la persistencia. Usa with open(..., encoding='utf-8'), json.load() y json.dump(). Devuelve siempre una lista de registros (lista de dicts).
- servicios/restaurante.py: administra la colección de objetos Producto en memoria, reconstruyéndolos desde los registros recuperados por ArchivoServicio. Pide a ArchivoServicio guardar la colección cuando se registran, actualizan o eliminan productos.
- main.py: punto de entrada; construye los servicios, carga productos al iniciar, coordina el menú y solicita guardar al salir.

Formato de productos.json
Se almacena una lista de objetos; cada producto es un objeto con las claves:
- codigo (str), nombre (str), categoria (str), precio (number)
Ejemplo:
[
  {"codigo": "P001", "nombre": "Ceviche", "categoria": "Mar", "precio": 25.0},
  {"codigo": "P002", "nombre": "Lomo Saltado", "categoria": "Carne", "precio": 30.5}
]

Flujo de carga (inicio)
1. main.py crea ArchivoServicio y Restaurante.
2. Restaurante solicita a ArchivoServicio la lista de registros.
3. Para cada registro válido se instancia Producto(registro["codigo"], registro["nombre"], registro["categoria"], registro["precio"]).
4. Registros con claves faltantes (KeyError) o datos inválidos (ValueError) se omiten con mensaje, sin detener la aplicación.

Flujo de guardado (modificación)
- Al registrar, actualizar o eliminar un producto exitosamente, Restaurante convierte los objetos a diccionarios (Producto.to_dict()) y llama a ArchivoServicio.guardar_productos() para actualizar datos/productos.json.
- Al salir, main.py invoca Restaurante.guardar_datos() como medida adicional.

Manejo de excepciones controladas
- FileNotFoundError: si productos.json no existe, ArchivoServicio.cargar_productos() devuelve lista vacía y la aplicación inicia normalmente.
- json.JSONDecodeError: si el archivo existe pero no contiene JSON válido, se informa y se ignoran los datos (se inicia con colección vacía).
- PermissionError: al leer/escribir, se muestra mensaje de error y la aplicación continúa sin bloquearse.
- KeyError/ValueError: al reconstruir productos desde registros defectuosos, se omiten dichos registros y se informa al usuario.
Evitar capturas genéricas que silencien errores: cada excepción relevante es manejada y comunicada.

Ejecución
1. Abrir una terminal en la carpeta restaurante_app
2. Ejecutar: python main.py
3. Usar el menú para registrar, buscar, actualizar, eliminar o listar productos y usuarios.

Comprobación de persistencia (pasos mínimos sugeridos)
1. Ejecutar python main.py.
2. Registrar uno o más productos desde el menú.
3. Verificar que datos/productos.json contiene los registros agregados.
4. Salir con la opción 9 (se guarda antes de salir).
5. Ejecutar nuevamente python main.py y listar productos: los productos previamente guardados deben aparecer.
6. Actualizar o eliminar un producto, salir y volver a iniciar para confirmar que el cambio persiste.

Notas finales
- La persistencia implementada esta semana aplica únicamente a productos; no se persisten usuarios.
- La clase Producto conserva sus validaciones: no se reemplazan objetos por diccionarios en la lógica del sistema.
- Cualquier incidencia con el archivo de datos se comunica por consola; el sistema evita fallos catastróficos.

Contacto
Alumno: Jefferson Guaman
Repositorio: (subir proyecto en un repositorio público y pegar aquí la URL)
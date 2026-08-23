Nombre: Jefferson Guaman

Sistema: restaurante_app (Semana 10)

Descripción breve:
Este proyecto administra productos y usuarios de un restaurante desde la línea de comandos. En la Semana 10 se incorporó persistencia de productos mediante un archivo JSON ubicado en datos/productos.json.

Estructura del proyecto:
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py

Flujo de carga y guardado:
- Al iniciar, main.py crea ArchivoServicio y Restaurante; Restaurante solicita a ArchivoServicio la carga de registros.
- Cada registro recuperado se intenta convertir en un objeto Producto; los registros defectuosos se omiten con un mensaje.
- Al registrar/actualizar/eliminar un producto, Restaurante guarda inmediatamente la lista actualizada llamando a ArchivoServicio.
- Al salir, main.py solicita guardar_datos() por si hay cambios pendientes.

Manejo de excepciones controladas:
- FileNotFoundError: si no existe datos/productos.json, la aplicación inicia con colección vacía.
- json.JSONDecodeError: si el archivo no contiene JSON válido, se informa y se ignoran los datos.
- PermissionError: al leer/escribir, se informa el error y la aplicación continúa.
- KeyError/ValueError: al reconstruir productos, los registros incompletos o con datos inválidos se omiten y se informa.

Ejecución:
- Ejecutar desde la carpeta restaurante_app:
  python main.py

Prueba mínima de persistencia realizada:
1. Ejecutar main.py.
2. Registrar productos mediante el menú.
3. Verificar que datos/productos.json contiene los productos (lista de objetos).
4. Cerrar la aplicación (opción 9 para guardar y salir).
5. Volver a ejecutar main.py y listar productos para confirmar que se recuperaron.
6. Actualizar o eliminar un producto y verificar que el cambio se ve en el archivo y persiste tras reiniciar.

Notas:
- Solo los productos se persisten en esta versión; los usuarios permanecen en memoria.
- La clase Producto conserva validaciones y un método to_dict para la conversión a JSON.

Nombre: Jefferon Guaman (actualizar con su nombre completo)

Descripción:
Evolución de restaurante_app — Semana 11. Se agregó la entidad Venta, manejo de stock en Producto, persistencia JSON para productos, usuarios y ventas, y la operación de venta que relaciona Usuario + Producto -> Venta.

Estructura:
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py (vacío o paquete)
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

Responsabilidades clave:
- Producto: mantiene stock y puede venderse (método vender).
- Usuario: representación y conversión a/desde dict.
- Venta: relación usuario-producto-cantidad, persistible en JSON.
- Restaurante: lógica de negocio (registro, búsqueda, venta, consultas) y coordinación de persistencia.
- ArchivoServicio: lectura/escritura de productos.json, usuarios.json y ventas.json con manejo de excepciones específicas.

Funcionamiento del stock:
- El atributo stock en Producto siempre es entero >= 0.
- Antes de finalizar una venta se valida que la cantidad solicitada sea >0 y que exista stock suficiente.
- Al vender se registra una Venta y se decrementa el stock; luego se guardan productos.json y ventas.json.

Persistencia:
- Productos, usuarios y ventas se guardan en archivos JSON dentro de datos/.
- Al iniciar la aplicación se reconstruyen los objetos a partir de los JSON.
- Se controlan FileNotFoundError (se inician colecciones vacías), JSONDecodeError y PermissionError.

Ejecución:
- Ejecutar python main.py desde el directorio restaurante_app.
- Usar las opciones del menú para registrar usuarios, productos, realizar ventas y consultar ventas por usuario.

Pruebas realizadas (ejemplo):
1. Registrar usuario U1.
2. Registrar producto P1 con stock 5.
3. Vender 2 unidades de P1 por U1 -> stock queda 3, venta guardada en ventas.json.
4. Intentar vender 10 unidades -> rechazado, datos no modificados.
5. Cerrar programa y re-ejecutar -> productos, usuarios y ventas recuperados desde JSON.

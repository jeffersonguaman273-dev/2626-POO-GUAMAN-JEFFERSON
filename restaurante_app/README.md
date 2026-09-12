Restaurante App - Versión base gráfica

Propósito

Proyecto base adaptado desde el ejemplo docente de Semana 13. Debe servir como esqueleto para incorporar progresivamente las funcionalidades del restaurante mediante una interfaz Tkinter.

Estructura

restaurante_app/
├── datos/ (JSON con datos de ejemplo)
│   ├── productos.json
│   └── usuarios.json
├── modelos/ (clases de dominio)
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/ (acceso a archivos y lógica de negocio)
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/ (vistas Tkinter)
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py (punto de entrada)
└── README.md

Flujo de la aplicación

1. Ejecutar main.py desde la carpeta restaurante_app: python main.py
2. Aparece la pantalla de Login
3. Ingresar usuario y contraseña (ejemplo: admin / admin123)
4. Al validar, se muestra la vista principal donde se pueden ver Productos y Usuarios cargados desde JSON
5. Cerrar sesión vuelve al login

Notas

- Las vistas piden información al RestauranteServicio; no leen directamente los archivos JSON.
- La funcionalidad de Ventas está marcada como pendiente para implementaciones futuras.

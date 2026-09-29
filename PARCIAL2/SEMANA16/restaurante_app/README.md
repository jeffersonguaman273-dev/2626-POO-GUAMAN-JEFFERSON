Semana 16 - Restaurante App

En esta versión se evoluciona la aplicación desarrollada en semanas anteriores y se fortalece la gestión de usuarios mediante eventos de interfaz, validaciones de negocio y persistencia estructurada.

Objetivo de la semana:
- Mantener la navegación, productos y ventas ya desarrolladas.
- Añadir la gestión de usuarios con roles y CRUD básico.
- Evidenciar el flujo de interacción: usuario -> evento -> bind() -> callback -> servicio -> persistencia -> respuesta visual.
- Reforzar la separación entre interfaz, modelo y servicio.

Estructura principal:
- datos/: productos.json, usuarios.json, ventas.json
- modelos/: producto.py, usuario.py, venta.py
- servicios/: archivo_servicio.py, restaurante_servicio.py
- ui/: login_view.py, main_view.py
- assets/: logo.svg, icono_usuarios.svg
- main.py

Qué se implementó:
- Modelo Usuario con atributos id, username, password, nombre y rol.
- Roles permitidos: Administrador, Empleado y Cliente.
- RestauranteServicio con validaciones para login, registro, actualización, eliminación y persistencia en usuarios.json.
- Gestión administrativa de usuarios solo para el Administrador.
- Treeview con columnas ID, nombre, usuario y rol.
- Evento <<TreeviewSelect>> para cargar el usuario elegido en el formulario.
- Combobox para seleccionar el rol con <<ComboboxSelected>>.
- Atajos de teclado: <Return> para registrar desde el formulario y <Escape> para limpiar el estado.
- Botones con command= para Registrar, Actualizar, Eliminar y Limpiar.
- Confirmación previa antes de eliminar un usuario y bloqueo de la cuenta administrativa activa.

Eventos demostrados:
- Treeview -> <<TreeviewSelect>> -> bind() -> callback -> carga datos en formulario.
- Teclado -> <Return> -> callback -> registrar usuario.
- Teclado -> <Escape> -> callback -> limpiar formulario y selección.
- Combobox -> <<ComboboxSelected>> -> callback -> cambiar rol y mostrar respuesta visual.
- Botones -> command= -> callback -> registrar, actualizar, eliminar o limpiar.

Ejecución:
1. Abrir la carpeta PARCIAL2/SEMANA16/restaurante_app.
2. Ejecutar: python main.py
3. Usar la cuenta administrativa inicial: usuario admin / contraseña admin123
4. Desde la vista principal, ingresar a Usuarios si el rol es Administrador.

Notas:
- El proyecto conserva la arquitectura modular desarrollada en semanas anteriores.
- La lógica de negocio y la persistencia se mantienen en RestauranteServicio, no en la interfaz.
- Los usuarios se guardan en datos/usuarios.json y se cargan al reiniciar la aplicación.

# restaurante_app - Semana 12

Aplicación de restaurante con optimización de búsquedas por colecciones.

## Descripción
La aplicación conserva la lógica funcional desarrollada en la Semana 11 para registrar usuarios, productos, ventas y controlar el stock. La mejora de esta semana se centra en optimizar búsquedas y validaciones frecuentes mediante estructuras auxiliares en memoria.

## Colecciones utilizadas
- Listas: almacenan los objetos principales (`_productos`, `_usuarios`, `_ventas`) para persistencia, recorrido y listado.
- Diccionarios: indexan búsquedas por código de producto, identificación de usuario y ventas por usuario.
- Set: genera categorías únicas de productos sin duplicados.

## Operaciones mejoradas
- `buscar_producto(codigo)` ya no recorre toda la lista de productos.
- `usuario_existe(identificacion)` y `buscar_usuario(identificacion)` usan índices por clave.
- `ventas_por_usuario(identificacion)` consulta la colección por usuario sin recorrer todas las ventas.
- Los índices se reconstruyen al iniciar el programa y se mantienen sincronizados durante cambios.

## Ejecución
```bash
cd restaurante_app
python main.py
```

## Pruebas principales
1. Cargar datos iniciales desde `datos/*.json`.
2. Buscar un producto por código.
3. Buscar un usuario por identificación.
4. Consultar ventas de un usuario.
5. Registrar una venta y verificar que el stock se actualiza.
6. Cerrar y volver a ejecutar la app para comprobar que los datos y los índices se reconstruyen correctamente.

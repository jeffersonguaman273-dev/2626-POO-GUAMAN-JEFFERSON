# Sistema restaurante_app — Semana 8

Proyecto de ejemplo para demostrar diseño orientado a objetos y principios SOLID (adaptados al contexto de un restaurante).

Estructura:

- `modelos/` — contiene las clases de dominio: `Producto`, `Bebida` y `Cliente`.
- `servicios/` — contiene la clase `Restaurante` que administra colecciones y operaciones.
- `main.py` — punto de entrada con un menú interactivo por consola.

Características principales:

- `Producto` define datos comunes y `mostrar_informacion()`.
- `Bebida` hereda de `Producto` y sobrescribe `mostrar_informacion()` añadiendo atributos propios.
- `Restaurante` administra una sola colección de productos (que puede contener `Producto` y `Bebida`) y otra de clientes.
- Validaciones para evitar códigos de producto duplicados y identificaciones de cliente repetidas.

Uso:

Ejecutar `main.py` desde la carpeta `restaurante_app`:

```powershell
# situarse en la carpeta .../restaurante_app
python .\main.py
```

El menú permite registrar productos, bebidas y clientes, y listar los elementos registrados.


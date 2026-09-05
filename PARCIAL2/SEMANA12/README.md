# Semana 12 - Optimización con colecciones

Este proyecto conserva la aplicación de restaurante desarrollada en la Semana 11 y aplica mejoras de rendimiento mediante índices en memoria.

## Mejoras realizadas
- Se mantienen las listas principales de productos, usuarios y ventas para almacenamiento, recorrido y persistencia JSON.
- Se agregan diccionarios auxiliares para búsquedas rápidas por clave única:
  - `productos_por_codigo`
  - `usuarios_por_identificacion`
  - `ventas_por_usuario`
- Se optimiza la consulta de ventas por usuario sin recorrer toda la lista de ventas en cada consulta.
- Se usa `set` para categorías únicas, evitando duplicados y permitiendo validaciones rápidas de pertenencia.
- Los índices se reconstruyen al inicio a partir de los datos leídos desde JSON y se mantienen sincronizados cuando se registran, actualizan o eliminan objetos.

## Estructura
```text
PARCIAL2/SEMANA12/
├── README.md
└── restaurante_app/
    ├── datos/
    │   ├── productos.json
    │   ├── usuarios.json
    │   └── ventas.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── usuario.py
    │   └── venta.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante.py
    ├── main.py
    └── README.md
```

## Ejecución
```bash
cd PARCIAL2/SEMANA12/restaurante_app
python main.py
```

## Pruebas principales realizadas
- Carga de usuarios, productos y ventas desde JSON.
- Búsqueda de producto por código.
- Búsqueda de usuario por identificación.
- Consulta de ventas por usuario.
- Venta de producto con actualización automática de stock.
- Verificación de coherencia de índices tras modificaciones.
- Reinicio del programa y comprobación de reconstrucción desde JSON.

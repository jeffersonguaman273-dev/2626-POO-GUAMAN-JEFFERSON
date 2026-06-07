# Explicación del código en `Tareasemana2.py`

Este archivo explica paso a paso el código de `Tareasemana2.py`. Está pensado para quien aprende Programación Orientada a Objetos (POO) y usa Python por primera vez.

## Resumen

El programa define una clase llamada `CuentaBancaria` que representa una cuenta bancaria real. La clase tiene atributos para el titular, el número de cuenta y el saldo, y métodos para depositar, retirar, transferir y mostrar el saldo. Al final del archivo hay una función `demo()` que crea dos cuentas y muestra operaciones de ejemplo.

## Conceptos de POO usados

- Clase: `CuentaBancaria` es la plantilla que describe cómo es una cuenta.
- Objeto / instancia: `cuenta1` y `cuenta2` son instancias de la clase `CuentaBancaria`.
- Atributos: variables que pertenecen a cada objeto (por ejemplo, `titular`, `numero_cuenta`, `saldo`).
- Métodos: funciones asociadas a la clase que definen el comportamiento (por ejemplo, `depositar`, `retirar`).
- Encapsulación básica: los atributos están en el objeto y se acceden/modifican mediante métodos.

## Estructura del código (línea a línea — explicación simplificada)

1. Definición de la clase:

```python
class CuentaBancaria:
    def __init__(self, titular: str, numero_cuenta: str, saldo: float = 0.0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = float(saldo)
```

- `class CuentaBancaria:` inicia la definición de la clase.
- `__init__` es el constructor; se ejecuta cuando creas una nueva cuenta. Los parámetros que recibe permiten inicializar los atributos.
- `self` es la referencia al objeto actual (como `this` en otros lenguajes).

2. Método `depositar`:

```python
    def depositar(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que 0.")
        self.saldo += cantidad
```

- Verifica que la cantidad sea positiva; si no, lanza un error (`ValueError`).
- Suma la cantidad al `saldo` de la cuenta.

3. Método `retirar`:

```python
    def retirar(self, cantidad: float) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad
```

- Valida que la cantidad sea positiva y que haya saldo suficiente.
- Resta la cantidad del saldo.

4. Método `transferir`:

```python
    def transferir(self, otra_cuenta: 'CuentaBancaria', cantidad: float) -> None:
        if not isinstance(otra_cuenta, CuentaBancaria):
            raise TypeError("Destino inválido para la transferencia.")
        self.retirar(cantidad)
        otra_cuenta.depositar(cantidad)
```

- Verifica que el destino sea otra instancia de `CuentaBancaria`.
- Usa `retirar` en la cuenta origen y `depositar` en la cuenta destino.
- Aprovecha métodos ya escritos para mantener código limpio y evitar duplicación.

5. Método `mostrar_saldo` y `__str__`:

- `mostrar_saldo` devuelve el saldo actual (útil si quieres usar el valor en código en vez de imprimirlo).
- `__str__` define cómo se muestra la cuenta cuando haces `print(cuenta)`.

6. Función `demo()` y bloque de ejecución:

- `demo()` crea dos cuentas con saldos iniciales, realiza depósitos, retiros y una transferencia, e imprime el estado antes y después.
- El bloque `if __name__ == "__main__": demo()` hace que la demostración solo se ejecute si corres el archivo directamente (no cuando lo importas como módulo).

## Cómo ejecutar el programa

Abre una terminal en la carpeta raíz del proyecto (donde está `PARCIAL1`) y ejecuta:

```bash
python PARCIAL1/SEMANA2/Tareasemana2.py
```

Verás la impresión del estado inicial, las operaciones y el estado final de las cuentas.

## Manejo de errores

- El código utiliza `ValueError` para entradas inválidas (por ejemplo, depositar o retirar cantidades negativas) y `TypeError` si intentas transferir a un objeto que no sea una `CuentaBancaria`.
- Cuando aprendas sobre `try/except`, podrás capturar esos errores para mostrar mensajes amigables o tomar decisiones en tiempo de ejecución.

## Sugerencias para practicar (pasos siguientes)

- Añade validaciones adicionales (por ejemplo, límite máximo de retiro o comisiones).
- Implementa historial de transacciones (guardar cada operación en una lista dentro del objeto).
- Crea una interfaz simple por consola que permita al usuario elegir acciones (depósito, retiro, transferencia) en tiempo real.

---

Si quieres, puedo ejecutar el script ahora para mostrar la salida por consola y, opcionalmente, añadir ejemplos adicionales o ejercicios prácticos en el mismo archivo MD.
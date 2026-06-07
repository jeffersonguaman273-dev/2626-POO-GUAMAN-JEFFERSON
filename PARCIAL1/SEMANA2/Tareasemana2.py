class CuentaBancaria:
	def __init__(self, titular: str, numero_cuenta: str, saldo: float = 0.0):
		self.titular = titular
		self.numero_cuenta = numero_cuenta
		self.saldo = float(saldo)

	def depositar(self, cantidad: float) -> None:
		if cantidad <= 0:
			raise ValueError("La cantidad a depositar debe ser mayor que 0.")
		self.saldo += cantidad

	def retirar(self, cantidad: float) -> None:
		if cantidad <= 0:
			raise ValueError("La cantidad a retirar debe ser mayor que 0.")
		if cantidad > self.saldo:
			raise ValueError("Saldo insuficiente para realizar el retiro.")
		self.saldo -= cantidad

	def transferir(self, otra_cuenta: 'CuentaBancaria', cantidad: float) -> None:
		if not isinstance(otra_cuenta, CuentaBancaria):
			raise TypeError("Destino inválido para la transferencia.")
		self.retirar(cantidad)
		otra_cuenta.depositar(cantidad)

	def mostrar_saldo(self) -> float:
		return self.saldo

	def __str__(self) -> str:
		return f"Cuenta({self.numero_cuenta}) - Titular: {self.titular} - Saldo: {self.saldo:.2f}"


def demo():
	# Crear dos cuentas
	cuenta1 = CuentaBancaria(titular="Juan Pérez", numero_cuenta="ES1234567890", saldo=500.0)
	cuenta2 = CuentaBancaria(titular="María López", numero_cuenta="ES0987654321", saldo=150.0)

	print("Estado inicial:")
	print(cuenta1)
	print(cuenta2)

	# Operaciones
	print("\nDepositando 200 en la cuenta 1...")
	cuenta1.depositar(200)
	print(cuenta1)

	print("\nRetirando 50 de la cuenta 2...")
	try:
		cuenta2.retirar(50)
	except ValueError as e:
		print("Error:", e)
	print(cuenta2)

	print("\nTransfiriendo 300 de la cuenta 1 a la cuenta 2...")
	try:
		cuenta1.transferir(cuenta2, 300)
	except ValueError as e:
		print("Error en transferencia:", e)

	print("\nEstado final:")
	print(cuenta1)
	print(cuenta2)


if __name__ == "__main__":
	demo()


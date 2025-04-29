class Tarjeta:
  def __init__(self, saldo):
    self.saldo = saldo

  def recargar(self, cantidad):
    self.saldo += cantidad
    print(f"Saldo recargado. Nuevo saldo: {self.saldo}")
    return

  def descontar(self, cantidad):
    if self.saldo >= cantidad:
      self.saldo -= cantidad
    else:
      print("Saldo insuficiente.")

  def consultar_saldo(self):
    return self.saldo

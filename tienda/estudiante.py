class Estudiante:
  def __init__(self, nombre, grado, tarjeta):
    self.nombre = nombre
    self.grado = grado
    self.tarjeta = tarjeta

  def comprar(self, dulce, cantidad):
    total = dulce.precio * cantidad
    if self.tarjeta.consultar_saldo() >= total:
      self.tarjeta.descontar(total)
      dulce.reducir_cantidad(cantidad)
      return f"{self.nombre} compró {cantidad} {dulce.nombre}(s)."
    else:
      return "Saldo insuficiente."

  def recargar_saldo(self, cantidad):
    self.saldo += cantidad
    return f"Saldo recargado. Nuevo saldo: ${self.saldo}"
  
  def __str__(self):
    return f"{self.nombre} - Grado: {self.grado} - Saldo: ${self.saldo}"

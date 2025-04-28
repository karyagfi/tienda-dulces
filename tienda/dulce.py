class Dulce:
  def __init__(self, nombre, precio, cantidad, sabor):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    self.sabor = sabor

  def actualizar_precio(self, nuevo_precio):
    self.precio = nuevo_precio

  def actualizar_cantidad(self, nueva_cantidad):
    self.cantidad = nueva_cantidad

  def reducir_cantidad(self, cantidad_vendida):
    if cantidad_vendida <= self.cantidad:
      self.cantidad -= cantidad_vendida
      return  cantidad_vendida
    else:
      print(f"No hay suficiente {self.nombre} en inventario.")
      return 

  def disponible(self):
    return self.cantidad > 0
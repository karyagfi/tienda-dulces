class Venta:
  def __init__(self):
    self.productos = []

  def agregar_producto(self, dulce, cantidad):
    self.productos.append((dulce.nombre, dulce.precio, cantidad))

  def calcular_total(self):
    total = 0
    for nombre, precio, cantidad in self.productos:
      total += precio * cantidad
    return total

  def mostrar_venta(self):
    for producto in self.productos:
      nombre, precio, cantidad = producto
      print(f"Producto: {nombre}")
      print(f"Cantidad: {cantidad} | Precio por unidad: ${precio}")

    print(f"Total: {self.calcular_total()}")

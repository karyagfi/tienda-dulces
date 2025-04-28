from tienda.venta import Venta

class Tienda:
  def __init__(self):
    self.inventario = []
    self.estudiantes = []
    self.ventas_diarias = []

  def agregar_dulce(self, dulce):
    self.inventario.append(dulce)

  def buscar_dulce(self, nombre):
    for dulce in self.inventario:
      if dulce.nombre.lower() == nombre.lower():
        return dulce
    return 
  
  def registrar_venta(self, estudiante, dulce, cantidad):
    total = dulce.precio * cantidad
    estudiante.tarjeta.saldo -= total
    dulce.cantidad -= cantidad
    venta = Venta()
    venta.agregar_producto(dulce, cantidad)
    self.ventas_diarias.append(venta)
    return estudiante.comprar(dulce, cantidad)

  def calcular_ganancias_diarias(self):
    total = 0
    for venta in self.ventas_diarias:
      total += venta.calcular_total()
    return total
  
  def verificar_stock_bajo(self):
    stock_bajo = []
    for dulce in self.inventario:
      if dulce.cantidad < 5:
        stock_bajo.append(dulce.nombre)
    return stock_bajo  

  def mostrar_inventario(self):
    for dulce in self.inventario:
      print(f"Nombre: {dulce.nombre}, Precio: {dulce.precio}, Cantidad: {dulce.cantidad}, Sabor: {dulce.sabor}")  

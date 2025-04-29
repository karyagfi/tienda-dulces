from tienda.dulce import Dulce
from tienda.estudiante import Estudiante
from tienda.tienda import Tienda
from tienda.tarjeta import Tarjeta

tienda = Tienda()

tienda.agregar_dulce(Dulce("Chocolates", 20, 50, "Chocolate"))
tienda.agregar_dulce(Dulce("Gomitas", 10, 30, "Fresa"))
tienda.agregar_dulce(Dulce("Chicles", 5, 100, "Menta"))

estudiante1 = Estudiante("Juan Perez", "Cuarto", Tarjeta(100))
estudiante2 = Estudiante("Maria Lopez", "Quinto", Tarjeta(50))

tienda.estudiantes.append(estudiante1)
tienda.estudiantes.append(estudiante2)

print("Inventario actual:")
tienda.mostrar_inventario()

dulce = tienda.buscar_dulce("Chocolates")
print(tienda.registrar_venta(estudiante1, dulce, 10))

dulce = tienda.buscar_dulce("Gomitas")
print(tienda.registrar_venta(estudiante2, dulce, 3))

print("\nInventario después de la compra:")
tienda.mostrar_inventario()

print(f"\nGanancias diarias: ${tienda.calcular_ganancias_diarias()}")

print("\nDulces con stock bajo:")
print(tienda.verificar_stock_bajo())

estudiante1.tarjeta.recargar(400)
print(estudiante1.tarjeta.consultar_saldo())
print(estudiante2.tarjeta.consultar_saldo())
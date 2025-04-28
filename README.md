# Ejercicio 2: Sistema para una Tienda de Dulces

## Enunciado

Vamos a diseñar un sistema para una pequeña tienda de dulces de la escuela. La tienda vende diferentes tipos de dulces como chocolates, gomitas, paletas y chicles. Cada dulce tiene un **nombre**, **precio**, **sabor** y **cantidad disponible**.

Los estudiantes pueden comprar dulces usando su **tarjeta de estudiante**, que tiene un **saldo** que pueden recargar. Cada estudiante tiene su **nombre**, **grado** y **saldo disponible**.

La tienda necesita llevar un registro de las ventas diarias, controlar el inventario y saber cuáles son los dulces más vendidos.

El sistema debe permitir:
- Agregar nuevos dulces al inventario
- Actualizar precios y cantidades
- Registrar ventas a estudiantes
- Recargar saldo de las tarjetas de estudiantes
- Mostrar los dulces más populares
- Calcular las ganancias diarias
- Alertar cuando un dulce se está agotando

La tienda solo funciona durante el recreo, por lo que el sistema debe ser rápido y sencillo de usar.

---

## Sustantivos

- **sistema**
- **tienda**
- **dulce**
- **chocolates**
- **gomitas**
- **paletas**
- **chicles**
- **nombre**
- **precio**
- **sabor**
- **cantidad**
- **estudiante**
- **tarjeta**
- **saldo**
- **grado**
- **venta**
- **inventario**

---

## Verbos

- **diseñar**
- **vende**
- **tiene**
- **comprar**
- **usando**
- **llevar**
- **controlar**
- **saber**
- **permitir**
- **debe**
- **necesita**
- **agregar** (dulce)
- **actualizar** (precio y cantidad)
- **recargar** (saldo)
- **mostrar** (dulces populares)
- **calcular** (ganancias)
- **alertar** (dulces agotados)
- **registrar** (venta)
- **funciona**
- **ser**
- **usar**

---

## CLASES

| **CLASE**      | **ATRIBUTOS**                               | **MÉTODOS**                                              |
|----------------|---------------------------------------------|----------------------------------------------------------|
| **Dulce**      | nombre, precio, cantidad, sabor             | actualizar precio, actualizar cantidad, reducir cantidad, disponible |
| **Estudiante** | nombre, grado, tarjeta                      | comprar, recargar tarjeta                                |
| **Venta**      | productos, total                            | calcular total, agregar producto, mostrar venta          |
| **Tarjeta**    | saldo                                       | recargar, descontar, consultar saldo                     |
| **Tienda**     | inventario, estudiantes, ventas diarias     | agregar dulce, buscar dulce, registrar venta, calcular ganancias diarias, mostrar dulces populares, verificar stock bajo |
---
```mermaid
classDiagram
    Tienda "1" --> "*" Dulce : tiene varios
    Tienda "1" --> "*" Estudiante : tiene varios
    Tienda "1" --> "*" Venta : tiene varias

    Estudiante "1" --> "1" Tarjeta : tiene una
    Estudiante "1" --> "*" Venta : realiza varias

    Venta "1" --> "*" Dulce : contiene varios
    Venta "1" --> "1" Estudiante : es realizada por

    Dulce "1" --> "*" Venta : se incluye en varias

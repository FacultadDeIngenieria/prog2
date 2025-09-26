---
title: Ejercicios adicionales - Parcial 1
layout: practice
permalink: /additional-practice/parcial-1
---

# Ejercicios adicionales - Parcial 1

A continuación encontrarás una serie de ejercicios pensados para practicar Programación Orientada a Objetos en Java. Cada enunciado describe un problema que deberás modelar utilizando clases, objetos, encapsulamiento, recursividad y testing.

## Ejercicio 1 – Biblioteca Digital

### Instructions

Una biblioteca de barrio decidió informatizar el registro de sus libros y préstamos. Actualmente, cualquier persona que se haga socia puede retirar libros si están disponibles, y devolverlos cuando ya no los necesite. La biblioteca también quiere llevar un control de cuántos libros prestados tiene en un momento dado.

Debes modelar el sistema para que permita:

* Registrar socios.
* Manejar el estado de los libros (prestados o no).
* Permitir que un socio pida prestado y devuelva libros.
* Calcular el total de libros prestados mediante recursividad.
* Escribir al menos 2 tests que prueben el correcto funcionamiento de métodos distintos.

### Examples

* Un socio pide prestado un libro disponible → el libro queda marcado como prestado.
* Un socio devuelve un libro → el libro vuelve a estar disponible.
* El sistema consulta el total de libros prestados y devuelve el número correcto.

## Ejercicio 2 – Tienda de Mascotas

### Instructions

Una tienda de mascotas vende diferentes animales (perros, gatos, hámsters, etc.) cada una con un precio diferente calculado sobre un precio base de 10.000,00 pesos. Cada mascota puede estar disponible para la venta o ya haber sido vendida. Los clientes que llegan a la tienda pueden comprar una mascota, siempre que no esté vendida. El dueño de la tienda quiere saber en cualquier momento cuántas mascotas se vendieron en total.

Los perros tienen un costo adicional por el mantenimiento de la tienda de mascotas, de un 20% el precio base por mascota. (20% de 10.000,00 = 2.000,00)

Los gatos están a mitad de precio de una mascota normal porque la tienda tiene demasiados.

Los Hamster valen un 10% de lo que sale una mascota normal, porque no requieren mucho mantenimiento.

Debes modelar el sistema para que permita:

* Registrar clientes.
* Manejar las mascotas de diferentes especies en venta y sus estados.
* Registrar la compra de mascotas por parte de los clientes.
* Calcular el total de mascotas vendidas con un método recursivo.
* Calcular el monto total en pesos de las ventas de mascotas.
* Escribir al menos 2 tests para verificar el correcto funcionamiento de métodos distintos.

### Examples

* Un cliente compra un perro → el perro pasa a estado "vendido".
* El sistema consulta el total de mascotas vendidas y devuelve el número correcto.

# Ejercicio 3 – Plataforma de Cursos Online

### Instructions

Una plataforma de educación en línea quiere administrar las inscripciones de sus estudiantes. Cada curso, que puede ser online o presencial tiene un cupo máximo de inscriptos. Los estudiantes pueden anotarse en cursos mientras aún haya lugar. La plataforma también quiere conocer el número total de inscripciones hechas, calculado con un método recursivo.

Los cursos online, permiten que cualquier estudiante inscrito reciba automaticamente el certificado.

Los cursos presenciales, requiren que el estudiante haya asistido a todas las clases para poder generar el certificado.

Debes modelar el sistema para que permita:

* Registrar estudiantes.
* Crear cursos y controlar el cupo.
* Permitir la inscripción de estudiantes en cursos.
* Generar un certificado para los estudiantes que completan un curso.
* Organizar cursos en distintas categorías.
* Calcular de manera recursiva la cantidad total de inscripciones en la plataforma.
* Escribir al menos 2 tests que validen métodos distintos.

# Ejercicio 4 – Cine

### Instructions

Un cine quiere registrar funciones, vender entradas y controlar el total de entradas vendidas. Los clientes pueden comprar entradas y se debe calcular recursivamente el total de ventas.

Debes modelar el sistema para que permita:

* Registrar clientes.
* Crear funciones de cine.
* Vender entradas a los clientes.
* Calcular el total de entradas vendidas usando un método recursivo.
* Escribir al menos 2 tests para validar métodos distintos.


# Ejercicio 5 – Supermercado

### Instructions

Un supermercado quiere registrar compras de clientes, manejar productos (que pueden ser perecederos o no perecederos) y calcular ingresos totales. Debe contar los productos distintos vendidos con un método recursivo.

Los productos perecederos, si se venden despues de su fecha de vencimiento, el precio baja un 50%.

Los productos perecederos, se se venden más de 5 unidades de ese producto, aplica un 10% de descuento por la cantidad comprada. Ejemplo: Si compras 10 unidades de un producto, el precio final es 90% del precio original. Si compras 15 unidades, el precio final es 85% del precio original. Si compras 20 unidades, el precio final es 80% del precio original.

Debes modelar el sistema para que permita:

* Registrar clientes y productos.
* Crear compras y agregarlas al historial.
* Calcular el ingreso total de todas las compras.
* Contar productos distintos vendidos usando recursión.
* Escribir al menos 2 tests que verifiquen métodos distintos.

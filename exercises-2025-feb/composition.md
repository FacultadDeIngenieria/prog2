---
title: Composición
layout: practice
permalink: /exercises/composition
---

## Ejercicio 1
Implemente la clase Triangle, que debe estar compuesta por Rectas, que a su vez
están compuesta por puntos. Debe contar con los siguientes métodos:

- area()
- perimeter()
- isIsoceles()
- isScalane()
- isEquilateral()

Indique: ¿Que tipo de agregación tiene la clase Triángulo con sus componentes?

## Ejercicio 2
Implemente la clase PhoneBill, que permite registrar movimientos de una cuenta de
teléfonos. A medida que se realizan consumos, estos se van registrando y permiten luego
imprimir por pantalla los movimientos, permite además consultar el saldo de la cuenta. Además,
existe la posibilidad de ajustar el precio del segundo en cualquier momento.

## Ejercicio 3
Implemente el método **equals()** de todas las clases definidas en la guía anterior.

# Trabajo Práctico 2 - Ejercicio 3 - TDD
[Ejercicio 3](https://classroom.github.com/a/INbuKXvT)

Desarrollar un sistema de gestion de cuentas bancarias,
en Java y siguiendo las practicas de TDD.

## Requerimientos

### Crear una cuenta
- Crear una cuenta la crea con un saldo inicial de 0.

### Depositar en una cuenta
- Realizar un deposito en la cuenta incrementa el saldo.
- Realizar un deposito negativo no se permite.
- Realizar un deposito en una cuenta no existente no se permite.


### Retirar de una cuenta
- Realizar un retiro en la cuenta disminuye el saldo.
- Realizar un retiro negativo no se permite.
- Realizar un retiro en la cuenta sin saldo no se permite.
- Realizar un retiro en una cuenta no existente no se permite.

### Transferencias
- Realizar una transferencia entre cuentas, disminuye el saldo de una y aumenta el saldo de la otra.
- Realizar una transferencia entre cuentas sin saldo no se permite.
- Realizar una transferencia entre cuentas no existentes no se permite.
- Realizar una transferencia negativa no se permite.
- Realizar una transferencia entre la misma cuenta no se permite.
- Realizar una trasnferencia entre cuentas no existentes no se permite.


## Entrega

- Seguir las buenas practicas de TDD.
- Implementar en el proceso al menos 15 tests.

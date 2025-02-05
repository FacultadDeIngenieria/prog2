---
title: Introducción a Java
layout: practice
permalink: /introduction
---

## Ejercicio 1
Diseñe e implemente la clase Point2D, el cual debe representar un punto en el espacio
cartesiano de dos dimensiones. Debe contar con los siguientes métodos:

- getDistance(Point2D point): que indique la distancia que existe entre el punto
destino.
- add(Point2D point): que devuelva un nuevo punto la suma de el punto original y
el argumento.
- getX() : devuelve la coordenada en X
- getY(): devuelve la coordenada en Y

Ayuda: Puede utilizar las siguientes funciones (más adelante veremos que son)
- Math.pow(x, y) : eleva el número x a la potencia y 
- Math.sqrt(x): devuelve la raíz cuadrada de x

## Ejercicio 2
Implemente la clase círculo, que esté definida cómo un centro y un rádio. De tal manera
que permita consultar su centro, su área e indicar su un punto está incluído en su área:

- center() : obtiene el centro del círculo
- area(): obtiene el área del círculo
- contains(Point2D point): devuelve True/False si el punto está contenido está
contenido.
- perimeter(): devuelve el perímetro del círculo.

Ayuda: Puede utilizar la constante π haciendo uso de: Math.PI

## Ejercicio 3
Implemente la clase Interval, que representa una secuencia igualmente espaciados de
números desde el comienzo (inclusive) y hasta el final(exclusive). Debe contener los siguientes
métodos:

- first() : devuelve el primer elemento del intervalo
- last() : devuelve el último elemento del intervalo
- at(int i): devuelve el i-ésimo elemento del intervalo.
- size(): devuelve la cantidad de elementos del intervalo

## Ejercicio 4
Implemente la clase Polinomio, que representa un polinomio de grado N. Que permita
setear sus coeficientes, evaluarlo para un X en particular y derivarlo.
- setCoef(a, b): donde a es el coeficiente y b es el valor
- evaluar(x): evalúa el polinomio en X y devuelve su valor
- derivar(): devuelve un nuevo Polinomio derivado.

# Trabajo Práctico - TDD
Crear proyecto en [Github Classroom](https://classroom.github.com/a/INbuKXvT)

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
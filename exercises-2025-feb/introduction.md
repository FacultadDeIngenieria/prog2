---
title: Introducción a Java
layout: practice
permalink: /exercises/introduction
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
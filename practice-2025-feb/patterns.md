---
title: Patrones de Diseño
layout: practice
permalink: /practice/patterns
---

# Clasificación de patrones
# Singleton 
# Iterator 
# MVC 

## Ejercicio 1
Implemente el patrón **Iterador** para los elementos de la colección **Interval** implementada anteriormente.

## Ejercicio 2
Implemente el patrón **Iterador** para las colecciones **ListaArreglo** y **ListaEncadenada** que se implementaron anteriormente.

## Ejercicio 3
Agregue a las clases **ListaArreglo** y **ListaEncadenada** un método sort que ordene la lista haciendo uso del **compareTo** de los elementos.

¿Qué debe debe garantizar de los elementos que se quieran ordenar?

¿Dónde corresponde implementar correctamente este método?

_No utilizar la clase Collections. Utilice el método **BubbleSort**: https://en.wikipedia.org/wiki/Bubble_sort_

## Ejercicio 4
Sobrecargue el método **sort** con otro método que reciba un **Comparator** de tal forma que se pueda cambiar el criterio de ordenamiento.

## Ejercicio 5
Agregue un método **isSorted** que informe si la colección está ordenada o no.

## Ejercicio 6
Sobrecargue el método **isSorted** para indicar si la colección está ordenada bajo un criterio **Comparator** dado.
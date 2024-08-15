---
title: Ejercicio adicional 1.1
layout: practice
permalink: /additional-practice/1.1
---

# Types

## Instructions

You have to solve a Second grade equation of the form **ax<sup>2</sup> + bx + c**.

For this create a class named Quadratic that creates from 3 Float numbers, each representing the coefficients a, b and c 

This class have all this behaviour:
* *roots* returns a list of numbers that represents the (x<sub>1</sub> and x<sub>2</sub>).
  * If the equation has only one real solution then it should return one root.
  * If the equation has no real solutions then return an empty List.
 <!--* Given a `float` that represent a x<sub>1</sub> *valueY* returns a `float` that is the y<sub>1</sub> -->
 <!-- * `__str__()` should return a String representing the Quadratic as a String the form `Y = A * X2 + B * X + C` -->
 <!--* Given 2 `floats` that represent the coefficients a & b, *derivation* should return a String representing the Quadratic function
derivated. --> 
<!--This String should be similar than the String returned by `__str()__` -->

<!--* Dado los parámetros (a, b) el método derivation que devolverá un String mostrando la función lineal derivada.-->


## Examples

`Quadratic(1, -5, 6).roots()` should return `( 2 , 3 )`

`Quadratic(2, 0, 0).roots()` should return `(0)`

`Quadratic(1, 2, 1).roots()` should return `(-1)`

`Quadratic(1, 1, 1).roots()` should return `()`




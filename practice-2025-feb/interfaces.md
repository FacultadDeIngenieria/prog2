---
title: Interfaces
layout: practice
permalink: /practice/interfaces
---

## Ejercicio 1
Escriba una interface Function, que implemente un único método, evaluate de tal forma
que reciba un double y retorne un double.

```java
public interface Function {
    public double evaluate(double value);
}
```

De esta forma, implemente las siguientes funciones: LinealFunction, CuadraticFunction y CompoundFunction.
Las funciones Lineal y Cuadratic deben implementar Function, lo mismo CompoundFunction. 
Una función compuesta, es aquella cuyo resultado es el argumento de la siguiente. 
For ejemplo, sean las funciones f y g, la función compuesta entre f y g, es f(g(x)).
¿Qué tipo de argumentos deberían tener el constructor de la función compuesta?
2.2: Permita que la clase Polinomio desarrollada en la práctica 1, participe de este sistema.

## Ejercicio 2
Agregue al **Interval** los siguientes métodos:
* double findFirst(Criteria evaluator)
* double[] findAll(Criteria evaluator)

**Criteria** es un Objeto que recibe un double y devuelve true o false, y el objetivo es poder
_evaluar_ los elementos sin necesidad de implementar un nuevo método para cambiar el criterio.
No sería práctico implementar un nuevo Intervalo cada vez que, por ejemplo, se quiera buscar
el primer número positivo o el tercer número consecutivo que sea par. 
Lo mismo ocurre para _findAdd_. ¿Que tipos de elementos deben estar contenidos en la lista retornada?
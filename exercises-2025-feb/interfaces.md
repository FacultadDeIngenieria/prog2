---
title: Interfaces
layout: practice
permalink: /interfaces
---

## Ejercicio 1
Explique cuales son las similitudes y las diferencias entre las interfaces y las clases
abstractas. Busque un ejemplo claro, donde tenga que usar una interface y donde tiene que
usar una clase abstracta. Se puede combinar el uso de ambas?

## Ejercicio 2
Escriba una interface Function, que implemente un único método, evaluate de tal forma
que reciba un double y retorne un double.

public interface Function {

public double evaluate(double value);
}

De esta forma, implemente las siguientes funciones: LinealFunction,
CuadraticFunction y CompoundFunction.
Las funciones Lineal y Cuadratic deben implementar Function, lo mismo
CompoundFunction. Una función compuesta, es aquella cuyo resultado es el argumento de la
siguiente. For ejemplo, sean las funciones f y g, la función compuesta entre f y g, es f(g(x)).
¿Qué tipo de argumentos deberían tener el constructor de la función compuesta?
2.2: Permita que la clase Polinomio desarrollada en la práctica 1, participe de este sistema.

## Ejercicio 3
Agregue al Ejercicio 4, de la guía 1 de Intervalo los siguientes métodos
double findFirst(Criteria evaluator)
double[] findAll(Criteria evaluator)
Donde Criteria es un Objeto que recibe un double y devuelve true o false, y el objetivo es poder
evaluar los elementos sin necesidad de implementar un nuevo método para cambiar el criterio.
No sería práctico implementar un nuevo Intervalo cada vez que por ejemplo, se quiera buscar
el primer número positivo o el primer número que tenga 5 números anteriores que sean

divisibles por 2. Lo mismo ocurre para findAdd. ¿Que tipos de elementos deben estar
contenidos en la lista retornada?

## Ejercicio 4
Modifique la jerarquía de clases de figuras implementada anteriormente para que en
lugar de utilizar herencia, utilice interfaces. ¿Es correcta esta forma de encarar la solución?
¿Cuál es el problema?

## Ejercicio 5
Implemente dos versiones de Stack, una debe utilizar cómo estructura interna un Array,
y la otra mediante Nodos encadenados. Utilice las siguiente definición:

public interface Stack {

public void push(Object element);
public Object pop();
public boolean isEmpty();
}
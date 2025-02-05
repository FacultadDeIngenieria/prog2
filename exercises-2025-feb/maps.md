---
title: Mapas
layout: practice
permalink: /exercises/maps
---

## Ejercicio 1
Una Bag es una colección de elementos desordenados, que admite repetidos. 
Implemente una colección que permita dicho funcionamiento. 
No debe guardar más de la cantidad de elementos necesarios para tal fin.

## Ejercicio 2
La función recursiva Fibonacci está definida de la siguiente forma:

fibonacci_0 = 1
fibonacci_1 = 1
fibonacci_n = fibonacci_n-1 + fibonacci_n-2


Así,
fibonacci_2 =  2
fibonacci_3 =  3
fibonacci_4 =  5

En pseudocódigo:
public int fibonacci(int n) {
if ( n == 0 || n == 1)
return 1;
return fibonacci(n-1) + fibonacci(n-2);
}

## Ejercicio 3
Utilice un mapa para no tener que recalcular el resultado de cada invocación de fibonacci.

## Ejercicio 4
Haga pruebas y responda:
1. ¿En qué casos un Mapa sigue funcionando si no se implementan ni hashCode y equals? 
2. ¿Que ocurre si el si el equals funciona correctamente, pero hashCode cambia con cada llamada? 
3. ¿Que ocurre con el mapa si el hashCode de todos los objetos siempre devuelve 1?

## Ejercicio 5
Se tiene la siguiente clase, que se puede adjuntar a la jerarquía de funciones. El objetivo es no tener que recalcular la evaluación de cada función una vez que ya se hizo.

public abstract class Function {

public abstract Object evaluate(Object[] arguments);

}

	Realice una implementación de dicha clase, para que sólo calcule el resultado de evaluar la función con dichos argumentos una única vez.

## Ejercicio 6
Un Set es una colección que no admite elementos repetidos. Se puede recorrer, pero no se puede indexar, porque sus elementos no están ordenados. Implemente una clase Set que pueda almacenar elementos, y debe permitir consultar si un elemento se encuentra, o no en el Set. ¿Que métodos deben implementar los elementos para que puedan participar del Set? Utice cómo base un HashMap. ¿Cómo debería hacerse? ¿Qué deben implementar los elementos de dicha colección?

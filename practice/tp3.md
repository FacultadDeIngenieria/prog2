---
title: Trabajo Práctico 3
layout: practice
permalink: /practice/3
---

# Trabajo Práctico 3 - Recursion

[TP 3](https://classroom.github.com/a/jpz3BNJ9)

Dado la siguiente consigna, implementar las siguientes funciones TODAS USANDO RECURSIVIDAD (Eso significa, sin usar for o while):

[//]: # (Descripción con ejemplos en Java)

## Ejercicio 1
* Método **recursive_index_of** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso
  de no encontrarse ninguna retorna el valor -1.

```java
public static int recursiveIndexOf(String target, List<String> list) {
  
}
```

## Ejercicio 2
* Método **recursive_index_of_by_index** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```java
public static int recursiveIndexOfByIndex(String target, List<String> list, int index) {
  
}
```

## Ejercicio 3
* Método **recursive_index_of_empty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```java
public static int recursiveIndexOfEmpty(List<String> list) {
  
}
```

## Ejercicio 4
* Método **recursive_put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```java
public static int recursivePut(String target, List<String> list) {
  
}
```

## Ejercicio 5
* Método **recursive_remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra y
  retorne el número de eliminaciones que ha hecho.


```java
public static int recursiveRemove(String target, List<String> list) {
  
}
```

## Ejercicio 6
* Método **recursive_sum** qie calcule la suma de los primeros `n` números naturales de forma recursiva.

```java
public static int recursiveSum(int n) {
  
}
```

## Ejercicio 7
* Método **recursive_factorial** qie calcule el factorial de un numero entero no negativo de forma recursiva.
```java
public static int recursiveFactorial(int n) {
  
}
```

## Ejercicio 8
* Método **recursive_pow** que calcule el resultado de la `base` elevado a la potencia `exponent` de forma recursiva.

```java
public static int recursivePow(int base, int exponent) {
  
}
```

## Ejercicio 9
* Método **recursive_fibonacci** que calcule el término `n` de la secuencia de Fibonacci utilizando recursividad.

```
La sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…
```

```java
public static int recursiveFibonacci(int n) {
  
}
```

## Ejercicio 10
* Método **recursive_palindrome** que verifique si una palabra es palíndromo de forma recursiva (se lee igual de izquierda a derecha que de derecha a izquierda)
```java
public static boolean recursivePalindrome(String word) {
  
}
```



[//]: # (Descripción con ejemplos en Pyton)
[//]: # (## Ejercicio 1)

[//]: # (* Método **recursive_index_of** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso)

[//]: # (  de no encontrarse ninguna retorna el valor -1.)

[//]: # ()
[//]: # (```python)

[//]: # (from typing import List)

[//]: # (colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

[//]: # ()
[//]: # (print&#40;recursive_index_of&#40;"Black", colors&#41;&#41;)

[//]: # (#imprime: 3)

[//]: # (print&#40;recursive_index_of&#40;"Blue", colors&#41;&#41;)

[//]: # (#imprime: -1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 2)

[//]: # (* Método **recursive_index_of_by_index** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir)

[//]: # (  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.)

[//]: # ()
[//]: # (```python)

[//]: # (from typing import List)

[//]: # (colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

[//]: # ()
[//]: # (print&#40;recursive_index_of_by_index&#40;"Black", colors, 1&#41;&#41;)

[//]: # (#imprime: 3)

[//]: # (print&#40;recursive_index_of_by_index&#40;"Black", colors, 4&#41;&#41;)

[//]: # (#imprime: 6)

[//]: # (print&#40;recursive_index_of_by_index&#40;"Green", colors, 2&#41;&#41;)

[//]: # (#imprime: -1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 3)

[//]: # (* Método **recursive_index_of_empty** que retorne el índice del primer lugar “vacío” &#40;igual a ""&#41; en una lista de Strings. De no encontrar ninguno que retorne -1.)

[//]: # ()
[//]: # (```python)

[//]: # (from typing import List)

[//]: # (colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

[//]: # ()
[//]: # (print&#40;recursive_index_of_empty&#40;colors&#41;&#41;)

[//]: # (#imprime: -1)

[//]: # ()
[//]: # (colors: List[str] = ["Red", "Green", "", "", "Pink", "", "Black"])

[//]: # (print&#40;recursive_index_of_empty&#40;colors&#41;&#41;)

[//]: # (#imprime: 2)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 4)

[//]: # (* Método **recursive_put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne)

[//]: # (  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.)

[//]: # ()
[//]: # (```python)

[//]: # (from typing import List)

[//]: # ()
[//]: # (colors: List[str] = ["Red", "Green", "", "", "Pink", "", "Black"])

[//]: # (print&#40;recursive_put&#40;"Blue", colors&#41;&#41;)

[//]: # (#imprime: 2)

[//]: # ()
[//]: # (colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

[//]: # (print&#40;recursive_put&#40;"Blue", colors&#41;&#41;)

[//]: # (#imprime: -1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 5)

[//]: # (* Método **recursive_remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra y)

[//]: # (  retorne el número de eliminaciones que ha hecho.)

[//]: # ()
[//]: # ()
[//]: # (```python)

[//]: # (from typing import List)

[//]: # (colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"])

[//]: # ()
[//]: # (print&#40;recursive_remove&#40;"Black", colors&#41;&#41;)

[//]: # (#imprime: 2)

[//]: # (print&#40;recursive_remove&#40;"Blue", colors&#41;&#41;)

[//]: # (#imprime: 0)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 6)

[//]: # (* Método **recursive_sum** qie calcule la suma de los primeros `n` números naturales de forma recursiva.)

[//]: # ()
[//]: # (```python)

[//]: # (recursive_sum&#40;4&#41; # devuelve 10)

[//]: # (recursive_sum&#40;1&#41; # devuelve 1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 7)

[//]: # (* Método **recursive_factorial** qie calcule el factorial de un numero entero no negativo de forma recursiva.)

[//]: # (```python)

[//]: # (recursive_factorial&#40;5&#41; # devuelve 120)

[//]: # (recursive_factorial&#40;0&#41; # devuelve 1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 8)

[//]: # (* Método **recursive_pow** que calcule el resultado de la `base` elevado a la potencia `exponent` de forma recursiva.)

[//]: # ()
[//]: # (```python)

[//]: # (recursive_pow&#40;2, 3&#41; # devuelve 8)

[//]: # (recursive_pow&#40;5, 0&#41; # devuelve 1)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 9)

[//]: # (* Método **recursive_fibonacci** que calcule el término `n` de la secuencia de Fibonacci utilizando recursividad.)

[//]: # ()
[//]: # (```)

[//]: # (La sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…)

[//]: # (```)

[//]: # ()
[//]: # (```python)

[//]: # (recursive_fibonacci&#40;7&#41;  # devuelve 13)

[//]: # (recursive_fibonacci&#40;0&#41; # devuelve 0)

[//]: # (```)

[//]: # ()
[//]: # (## Ejercicio 10)

[//]: # (* Método **recursive_palindrome** que verifique si una palabra es palíndromo de forma recursiva &#40;se lee igual de izquierda a derecha que de derecha a izquierda&#41;)

[//]: # (```python)

[//]: # (recursive_palindrome&#40;"neuquen"&#41; # devuelve True)

[//]: # (recursive_palindrome&#40;"python"&#41; # devuelve False# prog-2-python-tp)

[//]: # (```)

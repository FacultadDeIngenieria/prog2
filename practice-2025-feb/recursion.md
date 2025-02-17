---
title: Recursividad
layout: practice
permalink: /practice/recursion
---

## Ejercicio 1
Método **recursiveIndexOf** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. 
En caso de no encontrarse ninguna retorna el valor -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(recursiveIndexOf("Black", colors)); // imprime: 3
System.out.println(recursiveIndexOf("Blue", colors)); // imprime: -1
```

## Ejercicio 2
Método **recursiveIndexOfByIndex** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, 
a partir de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(recursiveIndexOfByIndex("Black", colors, 1)); // imprime: 3
System.out.println(recursiveIndexOfByIndex("Black", colors, 4)); // imprime: 6
System.out.println(recursiveIndexOfByIndex("Green", colors, 2)); // imprime: -1
```

## Ejercicio 3
Método **recursiveIndexOfEmpty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. 
De no encontrar ninguno que retorne -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");
System.out.println(recursiveIndexOfEmpty(colors)); // imprime: -1

List<String> colors2 = Arrays.asList("Red", "Green", "", "", "Pink", "", "Black");
System.out.println(recursiveIndexOfEmpty(colors2)); // imprime: 2
```

## Ejercicio 4
Método **recursivePut**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne
el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "", "", "Pink", "", "Black");
System.out.println(recursivePut("Blue", colors)); // imprime: 2

List<String> colors2 = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");
System.out.println(recursivePut("Blue", colors2)); // imprime: -1
```

## Ejercicio 5
Método **recursiveRemove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra y
retorne el número de eliminaciones que ha hecho.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black")
        
System.out.println(recursiveRemove("Black", colors)); // imprime: 2
System.out.println(recursiveRemove("Blue", colors)); // imprime: 0
```

## Ejercicio 6
Método **recursiveSum** qie calcule la suma de los primeros `n` números naturales de forma recursiva.

```java
recursiveSum(4); // devuelve 10
recursiveSum(1); // devuelve 1
```

## Ejercicio 7
Método **recursiveFactorial** qie calcule el factorial de un numero entero no negativo de forma recursiva.

```java
recursiveFactorial(5); // devuelve 120
recursiveFactorial(0); // devuelve 1
```

## Ejercicio 8
Método **recursivePow** que calcule el resultado de la `base` elevado a la potencia `exponent` de forma recursiva.

```java
recursivePow(2, 3); // devuelve 8
recursivePow(5, 0); // devuelve 1
```

## Ejercicio 9
Método **recursiveFibonacci** que calcule el término `n` de la secuencia de Fibonacci utilizando recursividad.

_La sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…_

```java
recursiveFibonacci(7); // devuelve 13
recursiveFibonacci(0); // devuelve 0
```

## Ejercicio 10
Método **recursivePalindrome** que verifique si una palabra es palíndromo de forma recursiva (se lee igual de izquierda a derecha que de derecha a izquierda)

```java
recursivePalindrome("neuquen"); // devuelve True
recursivePalindrome("python"); // devuelve False
```
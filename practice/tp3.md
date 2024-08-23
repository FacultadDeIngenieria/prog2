# TP3

[github](https://classroom.github.com/a/3vHTo3t4)

---
title: Práctica 9
layout: practice
permalink: /practice/9
---

# Trabajo Práctico 9

Dado la siguiente consigna, implementar las siguientes funciones TODAS USANDO RECURSIVIDAD (Eso significa, sin usar for o while):

## Ejercicio 1
* Método **recursive_index_of** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso
  de no encontrarse ninguna retorna el valor -1.

```python
from typing import List
colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(recursive_index_of("Black", colors))
#imprime: 3
print(recursive_index_of("Blue", colors))
#imprime: -1
```

## Ejercicio 2
* Método **recursive_index_of_by_index** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```python
from typing import List
colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(recursive_index_of_by_index("Black", colors, 1))
#imprime: 3
print(recursive_index_of_by_index("Black", colors, 4))
#imprime: 6
print(recursive_index_of_by_index("Green", colors, 2))
#imprime: -1
```

## Ejercicio 3
* Método **recursive_index_of_empty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```python
from typing import List
colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(recursive_index_of_empty(colors))
#imprime: -1

colors: List[str] = ["Red", "Green", "", "", "Pink", "", "Black"]
print(recursive_index_of_empty(colors))
#imprime: 2
```

## Ejercicio 4
* Método **recursive_put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío que encuentre y retorne
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```python
from typing import List

colors: List[str] = ["Red", "Green", "", "", "Pink", "", "Black"]
print(recursive_put("Blue", colors))
#imprime: 2

colors: List[str] = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(recursive_put("Blue", colors))
#imprime: -1
```

## Ejercicio 5
* Método **recursive_remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra y
  retorne el número de eliminaciones que ha hecho.


```python
from typing import List
colors: List[str = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]

print(recursive_remove("Black", colors))
#imprime: 2
print(recursive_remove("Blue", colors))
#imprime: 0
```

## Ejercicio 6
* Método **recursive_sum** qie calcule la suma de los primeros `n` números naturales de forma recursiva.

```python
recursive_sum(4) # devuelve 10
recursive_sum(1) # devuelve 1
```

## Ejercicio 7
* Método **recursive_factorial** qie calcule el factorial de un numero entero no negativo de forma recursiva.
```python
recursive_factorial(5) # devuelve 120
recursive_factorial(0) # devuelve 1
```

## Ejercicio 8
* Método **recursive_pow** que calcule el resultado de la `base` elevado a la potencia `exponent` de forma recursiva.

```python
recursive_pow(2, 3) # devuelve 8
recursive_pow(5, 0) # devuelve 1
```

## Ejercicio 9
* Método **recursive_fibonacci** que calcule el término `n` de la secuencia de Fibonacci utilizando recursividad.

```
La sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597…
```

```python
recursive_fibonacci(7)  # devuelve 13
recursive_fibonacci(0) # devuelve 0
```

## Ejercicio 10
* Método **recursive_palindrome** que verifique si una palabra es palíndromo de forma recursiva (se lee igual de izquierda a derecha que de derecha a izquierda)
```python
recursive_palindrome("neuquen") # devuelve True
recursive_palindrome("python") # devuelve False# prog-2-python-tp
```
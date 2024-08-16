---
title: Trabajo Práctico 2
layout: practice
permalink: /practice/2
---

# Trabajo Práctico 2

## Completar el trabajo práctico en GitHub Classroom

# Trabajo Práctico 2 - Ejercicio 1 - MyPy
[Ejercicio 1](https://classroom.github.com/a/Z3DLfOeP)

## 1.1 maximums.py

Completar la función `max_of_two` agregándole los tipos correctos en el argumento de la función y en cada variable

```python
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest
```

Ejemplos:
```python
max_of_two(5,4) # Retorna: 5

max_of_two(-2,-3) # Retorna: -2

max_of_two(0,0) # Retorna: 0
```


## 1.2 maximums.py
Escribir la funcion `max_of_three` con su implementación y también los tipos correctos en el argumento de la función y en cada variable

```python
def max_of_three(x, y, z):
"""Given x, y and z, that are 3 numbers, return the biggest number of the three."""
return "ANSWER HERE" # Remove this line and implement
```

Ejemplos:
```python
max_of_three(5,4,7) # Retorna: 7

max_of_three(-2,-3,-1) # Retorna: -1

max_of_three(0,0,0) # Retorna: 0
```

## 1.3 leap_year.py

Escribir la función `is_leap_year` que pida al usuario ingresar una año.
Se debe imprimir en pantalla el mensaje "El año $año es $es_bisiesto" con los valores adecuados.
Por último la función debe retornar el valor booleando True si es un año biciesto y False en caso de que no lo sea


Un año es bisiesto cuanto es divisible por cuatro, a menos que sea un año centenario.
En ese caso sólo es bisiesto si también es divisible por 400.

Ejemplos:
```
> Ingrese un año: 2000 # Número 2000 Ingresado por el usuario
# Se imprime luego
El año 2000 es bisiesto
# Retorna
> True
```
```
> Ingrese un año: 2001  # Número 2001 Ingresado por el usuario
# Se imprime luego
El año 2001 no es bisiesto
# Retorna
> False
```

# Trabajo Práctico 2 - Ejercicio 2 - Java Collections
[Ejercicio 2](TODO)

# Trabajo Práctico 2 - Ejercicio 3 - TDD
[Ejercicio 3](TODO)
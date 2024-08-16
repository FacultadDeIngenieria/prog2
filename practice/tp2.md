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
[Ejercicio 2](https://classroom.github.com/a/O7JasqRO)

## 2.1 Lists

Dado la siguiente consigna, implementar las siguientes funciones:
* Función **index_of** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso
  de no encontrarse ninguna retorna el valor -1.

```java
List<String> colors = List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(indexOf("Black", colors));
// imprime: 3
System.out.println(indexOf("Blue", colors));
// imprime: -1
```

* Función **index_of_by_index** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```java
List<String> colors = List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(indexOfByIndex("Black", colors, 1));
// imprime: 3
System.out.println(indexOfByIndex("Black", colors, 4));
// imprime: 6
System.out.println(indexOfByIndex("Green", colors, 2));
// imprime: -1
```

* Función **index_of_empty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```java
List<String> colors1 = List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");
System.out.println(indexOfEmpty(colors1));
// imprime: -1

List<String> colors2 = List.of("Red", "Green", "", "", "Pink", "", "Black");
System.out.println(indexOfEmpty(colors2));
// imprime: 2
```

* Función **put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío (igual a "") que encuentre y retorne
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```java
List<String> colors1 = new ArrayList<>(List.of("Red", "Green", "", "", "Pink", "", "Black"));
System.out.println(put("Blue", colors1));
// imprime: 2

List<String> colors2 = new ArrayList<>(List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(put("Blue", colors2));
// imprime: -1
```

* Función **remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra (lo cambia a "") y
  retorne el número de eliminaciones que ha hecho.


```java
List<String> colors1 = new ArrayList<>(List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(remove("Black", colors1));
// imprime: 2

List<String> colors2 = new ArrayList<>(List.of("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(remove("Blue", colors2));
// imprime: 0
```

## 2.2 Sets

Clasificar Cócteles y Mocktails.
El evento incluirá tanto cócteles como "mocktails" - bebidas mezcladas sin alcohol.
Necesitas asegurarte de que las bebidas "mocktail" sean verdaderamente no alcohólicas y que los cócteles realmente incluyan alcohol.

Implementa la función `check_drinks` que tome el nombre de una bebida y una lista de ingredientes.
La función debería devolver el nombre de la bebida seguido de "Mocktail" si la bebida no tiene ingredientes alcohólicos, y el nombre de la bebida seguido de "Cocktail" si la bebida incluye alcohol.
Para los propósitos de este ejercicio, los cócteles solo incluirán alcoholes del set ALCOHOLS en sets_categories_data.py:

```java
System.out.println(checkDrinks("Honeydew Cucumber", Arrays.asList("honeydew", "coconut water", "mint leaves", "lime juice", "salt", "english cucumber")));
// Imprime: Honeydew Cucumber Mocktail

System.out.println(checkDrinks("Shirley Tonic", Arrays.asList("cinnamon stick", "scotch", "whole cloves", "ginger", "pomegranate juice", "sugar", "club soda")));
// Imprime: Shirley Tonic Cocktail
```

## 2.3 Maps

En este ejercicio, administrarás un sistema de inventario.

El inventario debe estar organizado por el nombre del artículo y debe llevar un seguimiento del número de artículos disponibles.

Tendrás que gestionar la adición de artículos a un inventario. Cada vez que un artículo aparezca en una lista dada, aumenta la cantidad del artículo en `1` en el inventario. Luego, tendrás que gestionar la eliminación de artículos de un inventario.

Para finalizar, tendrás que implementar una función que devuelva todos los pares clave-valor en un inventario como una lista de `tuplas`.

### 2.3.1. Crear un inventario basado en una lista

Implementa la función `create_inventory` que crea un "inventario" a partir de una lista de artículos. Debe devolver un `dict` que contenga cada nombre de artículo emparejado con su cantidad respectiva.

```python
>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
{"coal":1, "wood":2, "diamond":3}
```

### 2.3.2. Añadir artículos a partir de una lista a un diccionario existente

Implementa la función `add_items` que agrega una lista de artículos a un inventario:

```python
>>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
{"coal":2, "wood":2, "iron":1}
```

### 2.3.3. Decrementar artículos del inventario

Implementa la función `decrement_items` que toma una `lista` de artículos. La función debe restar uno de la cantidad disponible en el inventario por cada vez que un artículo aparezca en la `lista`:

```python
>>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
```
Las cantidades de los artículos en el inventario no deben caer por debajo de 0. Si la cantidad de veces que un artículo aparece en la lista excede la cantidad disponible, la cantidad listada para ese artículo debe permanecer en 0 y las solicitudes adicionales para eliminar cantidades deben ser ignoradas.

```python
>>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}
```

### 2.3.4. Eliminar por completo un artículo del inventario

Implementa la función `remove_item` que elimina un artículo y su cantidad completamente de un inventario:

```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
{"wood":1, "diamond":2}
```
Si el artículo no se encuentra en el inventario, la función debe devolver el inventario original sin cambios.
```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
{"coal":2, "wood":1, "diamond":2}
```

### 2.3.5. Devolver el contenido del inventario

Implementa la función `list_inventory` que toma un inventario y devuelve una lista de tuplas `(artículo, cantidad)`. La lista solo debe incluir los artículos disponibles (con una cantidad mayor a cero):

```python
>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
```

# Trabajo Práctico 2 - Ejercicio 3 - TDD
[Ejercicio 3 - fixed](https://classroom.github.com/a/INbuKXvT)

Desarrollar un sistema de gestion de cuentas bancarias,
en Java y siguiendo las practicas de TDD.

## Requerimientos

### Crear una cuenta
- Crear una cuenta la crea con un saldo inicial de 0.

### Depositar en una cuenta
- Realizar un deposito en la cuenta incrementa el saldo.
- Realizar un deposito negativo no se permite.
- Realizar un deposito en una cuenta no existente no se permite.


### Retirar de una cuenta
- Realizar un retiro en la cuenta disminuye el saldo.
- Realizar un retiro negativo no se permite.
- Realizar un retiro en la cuenta sin saldo no se permite.
- Realizar un retiro en una cuenta no existente no se permite.

### Transferencias
- Realizar una transferencia entre cuentas, disminuye el saldo de una y aumenta el saldo de la otra.
- Realizar una transferencia entre cuentas sin saldo no se permite.
- Realizar una transferencia entre cuentas no existentes no se permite.
- Realizar una transferencia negativa no se permite.
- Realizar una transferencia entre la misma cuenta no se permite.
- Realizar una trasnferencia entre cuentas no existentes no se permite.


## Entrega

- Seguir las buenas practicas de TDD.
- Implementar en el proceso al menos 15 tests.

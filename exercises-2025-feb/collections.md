---
title: Collections
layout: practice
permalink: /collections
---

# Trabajo Práctico 2 - Ejercicio 2 - Java Collections
[Ejercicio 2 Fixed](https://classroom.github.com/a/D8FP7CVi)

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
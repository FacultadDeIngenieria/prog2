---
title: Collections
layout: practice
permalink: /practice/collections
---

**Entrega opcional**: crear proyecto en [Github Classroom](https://classroom.github.com/a/D8FP7CVi)

# Ejercicio 1: Lists

a. Implementar una función **indexOf** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings. En caso
  de no encontrarse ninguna retorna el valor -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(indexOf("Black", colors)); // imprime: 3
System.out.println(indexOf("Blue", colors)); // imprime: -1
```

b. Implementar una función **indexOfByIndex** que retorne el índice de la primera ocurrencia de un String dentro de una lista de Strings, a partir
  de un índice dado, incluido en la búsqueda. En caso de no encontrarse ninguna coincidencia retorna el valor -1.

```java
List<String> colors = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");

System.out.println(indexOfByIndex("Black", colors, 1)); // imprime: 3
System.out.println(indexOfByIndex("Black", colors, 4)); // imprime: 6
System.out.println(indexOfByIndex("Green", colors, 2)); // imprime: -1
```

c. Implementar una función **indexOfEmpty** que retorne el índice del primer lugar “vacío” (igual a "") en una lista de Strings. De no encontrar ninguno que retorne -1.

```java
List<String> colors1 = Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black");
System.out.println(indexOfEmpty(colors1)); // imprime: -1

List<String> colors2 = Arrays.asList("Red", "Green", "", "", "Pink", "", "Black");
System.out.println(indexOfEmpty(colors2)); // imprime: 2
```

d. Implementar una función **put**, que dado un String y una lista de Strings lo coloque en el primer lugar vacío (igual a "") que encuentre y retorne
  el índice en donde lo colocó. De no haber ningún lugar vacío debe retornar -1.

```java
List<String> colors1 = new ArrayList<>(Arrays.asList("Red", "Green", "", "", "Pink", "", "Black"));
System.out.println(put("Blue", colors1)); // imprime: 2

List<String> colors2 = new ArrayList<>(Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(put("Blue", colors2)); // imprime: -1
```

e. Implementar una función **remove** que dado un String y una lista de Strings, busque el string, lo elimine si lo encuentra (lo cambia a "") y
  retorne el número de eliminaciones que ha hecho.


```java
List<String> colors1 = new ArrayList<>(Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(remove("Black", colors1)); // imprime: 2

List<String> colors2 = new ArrayList<>(Arrays.asList("Red", "Green", "White", "Black", "Pink", "Yellow", "Black"));
System.out.println(remove("Blue", colors2)); // imprime: 0
```


# Ejercicio 2: Sets

Clasificar Cócteles y Mocktails.
El evento incluirá tanto cócteles como "mocktails" - bebidas mezcladas sin alcohol.
Necesitas asegurarte de que las bebidas "mocktail" sean verdaderamente no alcohólicas y que los cócteles realmente incluyan alcohol.

Implementa la función **checkDrinks** que tome el nombre de una bebida y una lista de ingredientes.
La función debería devolver el nombre de la bebida seguido de "Mocktail" si la bebida no tiene ingredientes alcohólicos, y el nombre de la bebida seguido de "Cocktail" si la bebida incluye alcohol.
Para los propósitos de este ejercicio, los cócteles solo incluirán alcoholes del set `ALCOHOLS` a continuación:

```java
private static final Set<String> ALCOHOLS = new HashSet<>(Arrays.asList("whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch", "vodka",
        "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco","aperol", "brandy", "mezcal",
        "triple sec", "coffee liqueur", "almond liqueur", "champagne", "orange curacao", "rum"));

// Imprime: Honeydew Cucumber Mocktail
System.out.println(checkDrinks("Honeydew Cucumber", Arrays.asList("honeydew", "coconut water", "mint leaves", "lime juice", "salt", "english cucumber")));

// Imprime: Shirley Tonic Cocktail
System.out.println(checkDrinks("Shirley Tonic", Arrays.asList("cinnamon stick", "scotch", "whole cloves", "ginger", "pomegranate juice", "sugar", "club soda")));
```

# Ejercicio 3: Maps

En este ejercicio, administrarás un sistema de **inventario**.

El inventario debe estar organizado por el nombre del artículo y debe llevar un seguimiento del número de artículos disponibles.

Tendrás que gestionar la adición de artículos a un inventario. Cada vez que un artículo aparezca en una lista dada, aumenta la cantidad del artículo en `1` en el inventario. Luego, tendrás que gestionar la eliminación de artículos de un inventario.

Para finalizar, tendrás que implementar una función que devuelva todos los pares clave-valor en un inventario como una lista de `tuplas`.

### 3.1. Crear un inventario basado en una lista

Implementa la función `createInventory` que crea un "inventario" a partir de una lista de artículos. Debe devolver un `diccionario` que contenga cada nombre de artículo emparejado con su cantidad respectiva.

```java
public Map<String, Integer> createInventory(List<String> items)
```

### 3.2. Añadir artículos a partir de una lista a un diccionario existente

Implementa la función `addItems` que agrega una lista de artículos a un inventario:

```java
    public Map<String, Integer> addItems(Map<String, Integer> inventory, List<String> items) {
```

### 3.3. Decrementar artículos del inventario

Implementa la función `decrementItems` que toma una `lista` de artículos. La función debe restar uno de la cantidad disponible en el inventario por cada vez que un artículo aparezca en la `lista`:

```java
    public Map<String, Integer> decrementItems(Map<String, Integer> inventory, List<String> items) {
```
Las cantidades de los artículos en el inventario no deben caer por debajo de 0. Si la cantidad de veces que un artículo aparece en la lista excede la cantidad disponible, la cantidad listada para ese artículo debe permanecer en 0 y las solicitudes adicionales para eliminar cantidades deben ser ignoradas.


### 3.4. Eliminar por completo un artículo del inventario

Implementa la función `removeItem` que elimina un artículo y su cantidad completamente de un inventario:

```java
    public Map<String, Integer> removeItem(Map<String, Integer> inventory, String item) {
```
Si el artículo no se encuentra en el inventario, la función debe devolver el inventario original sin cambios.

### 3.5. Devolver el contenido del inventario

Implementa la función `listInventory` que toma un inventario y devuelve una lista de tuplas `(artículo, cantidad)`. La lista solo debe incluir los artículos disponibles (con una cantidad mayor a cero):

```java
    public List<Map.Entry<String, Integer>> listInventory(Map<String, Integer> inventory) {
```
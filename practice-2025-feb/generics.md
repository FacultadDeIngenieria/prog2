---
title: Generics
layout: practice
permalink: /practice/generics
---

## Ejercicio 1
Implementar la clase **Bag** que guarda una colección de objetos genéricos **T**, incluso repetidos. 
Pero ésta, no debe guardar más de un referencia del objeto en la misma. 
De esta forma, la colección utiliza la menor cantidad de memoria posible. 
Para la implementación se debe cumplir con la siguiente interfaz:

```java
public interface IBag<T> {
    
    // Agrega un objeto a la bolsa
    public void add(T object);

    //Informa cuantas copias hay del objeto pasado como parámetro
    public int count(T object);

    // Elimina un elemento, solo una ocurrencia del mismo
    public void remove(T object);

    // Eliminar un elemento, todas sus ocurrencias
    public void removeAllOccurences(T object);

    // Informa el tamaño total de la colección
    public int size();

    // Informa si la bolsa está vacía
    public boolean isEmpty();

    // Devuelve un Set con los objetos sin repeticiones y 
    // filtrados de acuerdo al criterio suministrado
    public Set<T> getElementsUniqueAndFiltered(Filter filter);
}
```

## Ejercicio 2
Implementar la clase **Filter** que se encarga de filtrar los elementos de la colección.
Desarrollar diferentes filtros que apliquen distintos criterios de filtrado. 
Por ejemplo, realice la clase **FilterBoolean**, **FilterGreaterThan** y **FilterEquals**

## Ejercicio 3
Implementar la clase **Tupla<K, V>** que representa una tupla de dos elementos, uno de tipo **K** y otro de tipo **V**.
Realice las operaciones necesarias para poder comparar dos tuplas, que se puedan almacenar en una colección y realizar consultas.

## Ejercicio 4
Crea una clase Diccionario<K, V> que utilice una lista de Tupla<K, V>.
Implementa métodos en Diccionario<K, V> para agregar pares clave-valor y buscar valores por clave.

[//]: # (## Ejercicios adicionales)

[//]: # ()
[//]: # (### Adicional 1)

[//]: # (A stack is a container that stores objects in a manner indicated by its name —)

[//]: # (in a vertical stack where only the object at the top of the stack is accessible. It)

[//]: # (works rather like a sprung stack of plates in a cafeteria. Only the top plate is)

[//]: # (at counter level and, therefore, is the only one you can access. When you add)

[//]: # (a plate to the stack, the existing plates are pushed down so the new plate is)

[//]: # (now the one that you can access. Define a generic Stack<> type with a)

[//]: # (method push&#40;&#41; that adds the object that is passed as an argument to the top of)

[//]: # (the stack, and with a method pop&#40;&#41; that removes and returns the object that is)

[//]: # (currently at the top of the stack. The pop&#40;&#41; method should return null when)

[//]: # (the stack is empty. Demonstrate the operation of your Stack<>)

[//]: # (implementation by storing and retrieving 10 strings and 10 Double objects in)

[//]: # (stacks of a suit- able type.)

[//]: # ()
[//]: # (### Adicional 2)

[//]: # (Implement and demonstrate a listAll&#40;&#41; method in the Stack<> class definition that will list the objects in the stack.)

[//]: # ()
[//]: # (### Adicional 3)

[//]: # (Modify your Stack<> type to make it serializable. )

[//]: # (Demonstrate that this is the case by creating a Stack<String> object and adding 10 strings to it, )

[//]: # (then serializing and deserializing the Stack<String> object, and listing the contents of the deserialized stack.)
---
title: Generics
layout: practice
permalink: /practice/generics
---

## Ejercicio 1
Implementar la clase **Bag<T>** que guarda una colección de objetos genéricos **T**, incluso repetidos. 
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
    public Set<T> getElementsUniqueAndFiltered(Filter<T> filter);
}
```

Implementar la clase **Filter<T>** que se encarga de filtrar los elementos de tipo **T** en la colección.
Desarrollar los filtros **FilterEquals<T>** y **FilterGreaterThan<T>** que apliquen distintos criterios de filtrado.

## Ejercicio 2
Implementar la clase **Tupla<K, V>** que representa una tupla de dos elementos, uno de tipo **K** (key) y otro de tipo **V** (value).
Realice las operaciones necesarias para poder comparar dos tuplas, que se puedan almacenar en una colección y realizar consultas.

## Ejercicio 3
Crea una clase Diccionario<K, V> que utilice una lista de Tupla<K, V>.
Implementa métodos en Diccionario<K, V> para agregar pares clave-valor y buscar valores por clave.

## Ejercicio 4
Diseñanar un sistema en el cual se optimicen las lecturas de los elementos más accedidos. 
Para esto, se debe utilizar un Cache, que es una memoria pequeña pero rápida. 
Se pide realizar una implementación LimitedCache de la interface Cache. 
De tal forma, que cuando el cache se llene, y se desee agregar un nuevo par, se elimine el menos consultado.

```java
public interface Cache <K, V> {

    // Agrega un par Clave-Valor
    public void add(K key, V value);
    
    //Devuelve el valor almacenado
    public V get(K key);
    
    //Devuelve el tamaño del cache
    public int size();
}
```

```java
public class TestCache {

    @Test
    public void testCache() {
        Cache<String, String> cache = new LimitedCache<>(2);
        cache.add("Hola", "mundo");
        cache.add("Soy", "Diego");

        assertEquals("Diego", cache.get("Soy"));
        //Cuando llamo a cache.get("Soy") estoy haciendo que "Diego" sea el último valor consultado

        cache.add("Como", "Estan"); //Se elimina "mundo" por ser el valor menos consultado y se agrega "Estan" en su lugar
        assertNull(cache.get("Hola")); // Tira null porque "Hola" se borró del cache
    }
}
```


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
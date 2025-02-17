---
title: Excepciones
layout: practice
permalink: /practice/exceptions
---

Las excepciones surgen cómo mecanismo para realizar control de errores. En lenguajes más sencillos es común devolver datos por fuera del universo de respuestas posibles. 

Por ejemplo, una función que devuelve el índice de un elemento en un array, podría devolver -1, un valor inválido, para señalar que no existe dicho índice. Pero esto tiene un límite, no siempre se puede recurrir a este sistema. 

Considere el caso donde a una colección se le pide el elemento 11, pero la colección llega hasta el 10. ¿Que se devuelve? Si se devuelve null, un objeto válido, pero nulo, se podría llegar a confundir que dicho objeto es realmente parte de la colección.

## Ejercicio 1
Existen dos grandes tipos en Java, las “**unchecked**” y las “**checked**”. 

Las primeras son los tipos de excepciones que surgen sobre en errores de _funcionamiento interno y de programación_. 
Por ejemplo, **IndexOutOfBoundsException**, que ocurre cuando se accede a un array por fuera de sus límites (y cualquier otra colección). 
O por ejemplo **ClassCastException** cuando se hace un casteo incorrecto. 
Estas heredan de **RuntimeException** y _no es necesario declarar que se lanzan, ni atraparlas_. 

Las otras, que heredan directamente de **Exception** son _errores recuperables_, es decir, que se puede hacer algo al respecto. 
Por ejemplo, en el caso de que no se encuentre un archivo, se le puede pedir al usuario que ingrese una nueva ruta para dicho archivo.

Clasifique de que tipo debe ser cada excepción

- Método no implementado
- Corrupción de Memoria, al levantar una Clase en memoria.
- Conexión caída, al buscar un recurso en la red.
- Permisos Insuficientes, al querer acceder a recursos del sistema.
- Stack Vacío, al hacer pop de un stack vacío.
- Formato de número inválido, al pedirle al usuario la edad.

## Ejercicio 2
Implemente en los siguientes ejercicio el uso de excepciones en los casos que crea indicados:
* **Interval**: si no se encuentra ningún valor con el criterio indicado en ```findFirst(Criteria criteria)```, si el índice buscado no existe en ```at(int i)```.
* **Cuentas Bancarias**: si no se encuentra la cuenta bancaria, si el monto es insuficiente, si el monto es negativo.
* **Hotel**: si no se encuentra la habitación, si la habitación ya está ocupada en la fecha pedida, si las fechas de check-in y check-out son incorrectas (ej. check-out antes de check-in).

Argumente si las excepciones implementadas deberían ser “**checked**” o “**unchecked**”.

## Ejercicio 3
Indique cual es el resultado de ejecutar el siguiente código:

```java
public class Ej3 {

    private static final String nombreDeArchivo = "cuidadoConElEquals";
    private static int count = 0;
    private static int[] array = {0, 1};
    
    public static void main(String[] args) {
    
          try {
              try {
                  try {
                      String fileName = "cuidadoCon";
                      fileOpen(fileName + "El" + "Equals");
                      System.out.println("Archivo 1 abierto correctamente");
                  } catch (FileNotFoundException e) {
                      System.out.println("Catching FileNotFoundException: " + e.getMessage());
                  } finally {
                      System.out.println("En 1 Finally");
                      fileOpen(nombreDeArchivo);
                      System.out.println("Archivo 2 Abirto Correctamente");
                  }
              } finally {
                  System.out.println("En 2 Finally");
                  fileOpen("otroArchivo");
              }
          } catch (IOException e) {
              System.out.println("Catching IOException: " + e.getMessage());
          } catch (Exception e) {
              System.out.println("Catching Exception: " + e.getMessage());
          }
    
          System.out.println("Fin!");
    }
    
    
    private static void fileOpen(String fileName) throws IOException {
        System.out.println("FileOpen: " + array[count]);
        count++;
        if (fileName == nombreDeArchivo) {
            throw new FileNotFoundException("Archivo no encontrado");
        } else {
            throw new EOFException("Fin del Archivo");
        }
    }
}
```
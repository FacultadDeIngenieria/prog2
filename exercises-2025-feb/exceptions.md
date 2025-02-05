---
title: Excepciones
layout: practice
permalink: /exceptions
---

## Ejercicio 1
Las excepciones surgen cómo mecanismo para realizar control de errores. En lenguajes más sencillos es común devolver datos por fuera del universo de respuestas posibles. Por ejemplo, una función que devuelve el índice de un elemento en un array, podría devolver -1, un valor inválido, para señalar que no existe dicho índice. Pero esto tiene un límite, no siempre se puede recurrir a este sistema. Considere el caso donde a una colección se le pide el elemento 11, pero la colección llega hasta el 10. ¿Que se devuelve? Si se devuelve null, un objeto válido, pero nulo, se podría llegar a confundir que dicho objeto es realmente parte de la colección.

	Existen dos grandes tipos en Java, las “unchecked” y las “checked”. Las primeras son los tipos de excepciones que surgen sobre en errores de funcionamiento interno y de programación. Por ejemplo, IndexOutOfBoundsException, que ocurre cuando se accede a un array por fuera de sus límites (y cualquier otra colección). O por ejemplo ClassCastException cuando se hace un casteo incorrecto. Estas heredan de RuntimeException y no es necesario declarar que se lanzan, ni atraparlas. Las otras, que heredan directamente de Exception son errores recuperables, es decir, que se puede hacer algo al respecto. Por ejemplo, en el caso de que no se encuentre un archivo, se le puede pedir al usuario que ingrese una nueva ruta para dicho archivo.

Clasifique de que tipo debe ser cada excepción


- Método no implementado
- Corrupción de Memoria, al levantar una Clase en memoria.
- Conexión caída, al buscar un recurso en la red.
- Permisos Insuficientes, al querer acceder a recursos del sistema.
- Stack Vacío, al hacer pop de un stack vacío.
- Formato de número inválido, al pedirle al usuario la edad.

## Ejercicio 2

Cuando se pide la primera ocurrencia de un objeto de tipo Interval, si no se encuentra dicho valor, ¿Que se debería devolver? Agregue una excepción para señalizar este caso. Argumente si esta excepción debe ser “checked” o “unchecked”.


## Ejercicio 3

	Indique cual es el resultado de ejecutar el siguiente código:


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
if(fileName == nombreDeArchivo) {
throw new FileNotFoundException("Archivo no encontrado");
} else {
throw new EOFException("Fin del Archivo");
}
}




## Ejercicio 4

	Implemente en el ejercicio de Bancos de la guía 4 el uso de excepciones en los casos que crea indicado.
Para qué situaciones las ha utilizado?

---
title: Interfaces
layout: practice
permalink: /practice/interfaces
---

## Ejercicio 1
Diseñe la interfaz **Boolean** e implemente los métodos **and**, **or** y **not**.

## Ejercicio 2
Escriba una interface **Function**, que implemente un único método, evaluate de tal forma
que reciba un double y retorne un double.

```java
public interface Function {
    public double evaluate(double value);
}
```

De esta forma, implemente las siguientes funciones: **LinealFunction**, **CuadraticFunction** y **CompoundFunction**.

Una función compuesta, es aquella cuyo resultado es el argumento de la siguiente. 
Por ejemplo, sean las funciones f y g, la función compuesta entre f y g, es f(g(x)).

¿Qué tipo de argumentos deberían tener el constructor de la función compuesta?

Hacer que la clase **Polinomio** desarrollada anteriormente, participe de este sistema.

## Ejercicio 3
Agregue al **Interval** los siguientes métodos:
* double findFirst(Criteria evaluator)
* double[] findAll(Criteria evaluator)

**Criteria** es un Objeto que recibe un double y devuelve true o false, y el objetivo es poder
_evaluar_ los elementos sin necesidad de implementar un nuevo método para cambiar el criterio.
No sería práctico implementar un nuevo Intervalo cada vez que, por ejemplo, se quiera buscar
el primer número positivo o el tercer número consecutivo que sea par. 
Lo mismo ocurre para _findAdd_. ¿Que tipos de elementos deben estar contenidos en la lista retornada?

[//]: # (## Ejercicio 4)

[//]: # (Crea una interfaz llamada **Notification** que defina un método `sendNotification&#40;&#41;`. Luego, implementa esta interfaz con las siguientes clases:)

[//]: # (* **PushNotification**: Simula el envío de una notificación push. )

[//]: # (* **EmailNotification**: Simula el envío de una notificación por correo electrónico.)

[//]: # (* **SmsNotification**: Simula el envío de una notificación por mensaje SMS.)

[//]: # ()
[//]: # (Crear una clase **User** que tenga atributos como `nombre`, `email` y un booleano `hasAppInstalled` para indicar si el usuario tiene la aplicación instalada.)

[//]: # (Desde el **NotificationService** se deberá enviar al usuario una notificación push &#40;si tiene la app instalada&#41;, un SMS &#40;si tiene número de teléfono&#41;, o un correo &#40;si solo tiene email&#41;.)
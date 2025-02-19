---
title: Herencia
layout: practice
permalink: /practice/inheritance
---

## Ejercicio 1
Implemente la clase **Figure**, y sus subclases **Rectangle**, **Triangle** y **Circle**. 
Luego agregue la clase **Square** donde corresponda. Defina donde corresponda el método 
para determinar si un punto del espacio 2D está dentro de la figura:
- contains(Point2D point): devuelve True/False si el punto está contenido

Guardar todas las figuras en una **Lista**. Recorrer la estructura invocando el método **contains** 
para imprimir si un punto dado esta dentro de cada una de las figuras. 
Luego recorrer la estructura e imprimir el radio de las figuras que les corresponda tenerlo. 
Ayuda: usar la palabra clave **instanceof**.

## Ejercicio 2
Se está diseñando un sistema para la **Universidad**, la cual, obviamente cuenta con
Alumnos, Profesores, Personal administrativo, etc. Además, también hay cursos de grado y
seminarios, etc. Diseñe un modelo de clases para representar el sistema. Aplique Composición
y Herencia donde corresponde. Preguntesé:
* ¿Un Alumno es una Persona? 
* ¿Un Profesor es un Empleado? 
* ¿Un Curso tiene un Profesor?

## Ejercicio 3
Implemente la clase **Employee**, el cual poseé un sueldo base. 
Agregue el método **getSalary** el cual permite conocer el sueldo de dicho
empleado. Agregue la clase **Manager**, que también es un Empleado el cual, cobra además de
su sueldo base, un 1% extra del sueldo de sus subordinados. Agregue un método
**addEmployee** de tal forma de poder agregar subordinados.

## Ejercicio 4
Diseñe un sistema para un **Hotel**. El Hotel puede tener varios tipos de habitaciones,
puede ser Estándar, Suite, o Presidencial. Cada habitación tiene su propio precio, y su propia
cantidad de posibles personas que lo pueden ocupar. Por ejemplo, la Estándar tiene un costo
de U$ 200 y puede ser ocupada por 4 personas; la Suite, U$ 300 y puede estar ocupada por 2
personas y la Presidencial U$ 600 y puede ser ocupada por 2. Además, el sistema debe permitir
un sistema de reservas. A los clientes, se les asigna una habitación y una fecha (LocalDateTime).
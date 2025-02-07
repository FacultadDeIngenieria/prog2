---
title: Trabajo Práctico Final
layout: practice
permalink: /practice/tp
---

# Tower Defense Game

## Objetivo
Aplicar y reforzar los conceptos de la Programación Orientada a Objetos y otros
conceptos aprendidos durante la materia mediante el desarrollo de un juego del estilo Tower Defence.

## Enunciado
Desarrollar en Java y utilizando cualquier biblioteca extra que el alumno crea necesaria
un juego al estilo Tower Defence. En este juego, se colocan torres al costado de un camino por
el cual, viajan enemigos los cuales son atacados por las torres para evitar que lleguen al final
del camino. Cuando un enemigo llega al extremo opuesto, se descuenta vida, la cual, cuando
llega a cero, el jugador pierde. Cuando un enemigo es eliminado, se acredita oro el cual sirve
para comprar y actualizar torres.

### Tipos de torres
* **Torre Simple**: Ataca a un único enemigo a la vez realizando un daño básico
sencillo. 
* **Torre de Área**: Ataca a N enemigos a la vez que estén cerca suyo. 
* **Cañón**: Ataca a un área en particular y daña a varios enemigos a la vez. 
* **Torre de Frío**: No daña a los enemigos, sino que simplemente les retarda la
velocidad de movimiento de ellos. 
* **Torre Eléctrica**: Daña poco a los enemigos comunes, daña mucho a los
enemigos sensibles a daños eléctricos.

### Tipos de enemigos
* **Enemigo Simple**: Tienen N puntos de vida, cuando esta vida llega a 0, el
enemigo muere. 
* **Enemigo Múltiple**: Tienen N vida, cuando esta llega a 0, se genera un enemigo
nuevo de menor calidad en su lugar. 
* **Enemigo con Escudo Eléctrico**: Tienen N vida y recibe poco daño de una torre
común, pero mucho daño de una torre eléctrica.

* El juego debe contar de al menos 5 niveles, a decisión de los alumnos, de tal forma que
aumentan en complejidad. Los enemigos son más fuertes y vienen en mayor cantidad.
* Las torres se deben poder agregar alrededor del camino de acuerdo al oro disponible
que tiene el jugador.
* Las torres de deben poder actualizar, lo cual aumentan su daño, velocidad y rango de
ataque.
* Además debe contar con un sistema de los TOP 10 jugadores, rankeados por puntaje y
mostrando la fecha de realización

## Consideraciones
* Cualquier requerimiento no especificado quedará a decisión del alumno, podrá
consultarse con la cátedra para validarlas en caso de que sea necesario. 
* Se pueden consultar entre ustedes para discutir ideas de diseño e
implementación. Pero cada trabajo debe ser propio y se evaluarán los conceptos 
de la materia en la defensa oral. Cualquier detección de plagio es sensible a 
sanciones de acuerdo lo establecido por el reglamento académico.

## Demo de ejemplo
Cómo ejemplo se puede ver el juego en el siguiente link:
https://www.youtube.com/watch?v=XhUqV456MFI
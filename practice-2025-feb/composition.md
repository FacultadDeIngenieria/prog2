---
title: Composición y TDD
layout: practice
permalink: /practice/composition
---

# Composición

## Ejercicio 1
Implemente la clase **Triangle**, que debe estar compuesta por **Rectas**, que a su vez
están compuesta por **puntos**. Debe contar con los siguientes métodos:

- area()
- perimeter()
- isIsoceles()
- isScalane()
- isEquilateral()

Indique: ¿Que tipo de agregación tiene la clase Triángulo con sus componentes?

## Ejercicio 2
Implemente la clase **PhoneBill**, que permite registrar movimientos de una cuenta de
teléfonos. A medida que se realizan consumos, estos se van registrando y permiten luego
imprimir por pantalla los movimientos, permite además consultar el saldo de la cuenta. Además,
existe la posibilidad de ajustar el precio del segundo en cualquier momento.

# TDD
Test-Driven Development (TDD) is a software development approach where tests are written before the code that needs to be implemented. 

TDD is independent of the programming language, in this class we will use Java's **JUnit** to write the tests.

### Process steps
1. Write a test that fails
2. Write the minimum code to pass the test
3. Refactor the code
4. Repeat

### Why TDD?
- **Design**: TDD helps to design the software in small increments.
- **Quality**: TDD helps to ensure that the code is working as expected.
- **Documentation**: The tests are a form of documentation.
- **Confidence**: TDD gives confidence to the developers to make changes.
- **Feedback**: TDD gives immediate feedback on the code.
- **Productivity**: TDD helps to write code faster.
- **Bug detection**: TDD helps to detect bugs early in the development process.

### Example
```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyTest {

    @Test
    public void testAdd() {
        assertEquals(4, 2 + 2);
    }

    @Test
    public void testSubtract() {
        assertEquals(0, 2 - 2);
    }
}
```

## Ejercicio 3
Implemente un método que determine si un año dado es bisiesto (**Leap year**):
- A year is a leap year if it is divisible by 4
- A year is not a leap year if it is divisible by 100
- A year is a leap year if it is divisible by 400

## Ejercicio 4
Implemente **TDD** y los siguientes métodos a todas las clases definidas en las guías:
- toString()
- equals()
- compareTo()

## Ejercicio 5
Desarrollar un sistema de gestion de cuentas bancarias,
en Java siguiendo las *buenas practicas de TDD* y cumpliendo los siguientes requerimientos:

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


### Entrega opcional
- Crear proyecto en [Github Classroom](https://classroom.github.com/a/INbuKXvT)
- Implementar las practicas de TDD en el repositorio remoto para poder ver el estado de los tests.  
- Se espera poder desarrollar en el proceso al menos 15 tests.
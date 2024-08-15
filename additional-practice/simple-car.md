---
title: Ejercicio adicional 1.2
layout: practice
permalink: /additional-practice/1.2
---


Para este ejercicio, el objetivo es modelar un auto. Un auto se describe de la siguiente forma:

- Marca del auto (make)
- Modelo del auto
- Año de fabricación
- Cantidad de kilometros (odometer)

Cuando se crea un auto nuevo, siempre vienen con 0 kilometros.
Un auto ademas debera poder realizar las siguientes operaciones:

- **get_descriptive_name:** Devuelve un String en upper camel case que marque el año, marca y modelo del auto. Ejemplo: "2019 Audi A4"

- **read_odometer:** Devuelve un String que describa el kilometraje actual del auto. Ejemplo: "This car has 23 kilometers on it"

- **update_odometer:** Dado un número que representa el nuevo kilometraje total, el método deberá cambiar el total de kilometros actual si y solo si este total es mayor al total actual.

- **increment_odometer:** Dado un número que representa una cantidad de kilometros, el método debera agregarlo al total actual de kilometros del auto.

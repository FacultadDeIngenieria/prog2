---
title: Trabajo Práctico 2
layout: practice
permalink: /practice/2
---

# Trabajo Práctico 2

## Completar el trabajo práctico en GitHub Classroom
[TP 2](https://classroom.github.com/a/m8X3cbCp)

## Entrega

- Seguir las buenas practicas de TDD.
- Implementar en el proceso al menos 15 tests.

## 1. Leap Year

### Objetivo
Implementar una función que determine si un año es bisiesto siguiendo la metodología TDD.

### Especificaciones
Un año es bisiesto si cumple las siguientes reglas:
- ✅ **Es divisible por 4** → Es año bisiesto
- ❌ **Es divisible por 100** → NO es año bisiesto
- ✅ **Es divisible por 400** → Es año bisiesto (excepción a la regla anterior)

### Ejemplos
- `2000` → **Bisiesto** (divisible por 400)
- `1900` → **No bisiesto** (divisible por 100 pero no por 400)
- `2004` → **Bisiesto** (divisible por 4)
- `2001` → **No bisiesto** (no divisible por 4)

### Progresión Sugerida de Tests

#### Paso 1: Caso base
#### Paso 2: Divisible por 4
#### Paso 3: Divisible por 100
#### Paso 4: Divisible por 400
### Implementación Final

### Archivos del Ejercicio
- **Test**: `src/test/java/com/tp2/leapyear/LeapYearTest.java`
- **Implementación**: `src/main/java/com/tp2/leapyear/LeapYear.java`

---

## 2. String Calculator

### Objetivo
Implementar una calculadora que sume números contenidos en un string siguiendo TDD.

### Especificaciones
- String vacío → 0
- Un número → ese número (`"1"` → 1)
- Dos números separados por coma → suma (`"1,2"` → 3)
- Múltiples números → suma de todos (`"1,2,3"` → 6)
- Saltos de línea como delimitador → funciona (`"1\n2,3"` → 6)
- Números negativos → lanza `IllegalArgumentException`

### Ejemplos
```java
calculator.add("") → 0
calculator.add("1") → 1
calculator.add("1,2") → 3
calculator.add("1\n2,3") → 6
calculator.add("1,-2") → IllegalArgumentException
```

### Progresión Sugerida de Tests
#### Paso 1: String vacío
#### Paso 2: Un número
#### Paso 3: Dos números
#### Paso 4: Múltiples números
#### Paso 5: Saltos de línea
#### Paso 6: Números negativos (excepción)

### Archivos del Ejercicio
- **Test**: `src/test/java/com/tp2/stringcalculator/StringCalculatorTest.java`
- **Implementación**: `src/main/java/com/tp2/stringcalculator/StringCalculator.java`

---

## 3. Password Validator

### Objetivo
Implementar un validador de contraseñas con múltiples criterios siguiendo TDD.

### Especificaciones
Una contraseña válida debe cumplir **TODOS** estos criterios:
- ✅ **Mínimo 8 caracteres**
- ✅ **Al menos 1 letra mayúscula** (A-Z)
- ✅ **Al menos 1 letra minúscula** (a-z)
- ✅ **Al menos 1 número** (0-9)
- ✅ **Al menos 1 carácter especial** Definan que valores consideran, por ejemplo: !@#$%^&*()_+-=[]{}|;:,.<>?

### Ejemplos
```java
validator.isValid("abc") → false (muy corta)
validator.isValid("abcdefgh") → false (sin mayúscula, número, especial)
validator.isValid("Abcdefgh") → false (sin número, especial)
validator.isValid("Abcdefg1") → false (sin carácter especial)
validator.isValid("Abcdefg1!") → true (cumple todos los criterios)
```

### Progresión Sugerida de Tests
#### Paso 1: Longitud mínima
#### Paso 2: Letra mayúscula requerida
#### Paso 3: Letra minúscula requerida
#### Paso 4: Número requerido
#### Paso 5: Carácter especial requerido
#### Paso 6: Contraseña válida completa

### Archivos del Ejercicio
- **Test**: `src/test/java/com/tp2/password/PasswordValidatorTest.java`
- **Implementación**: `src/main/java/com/tp2/password/PasswordValidator.java`

---

## 4. Roman Numerals

### Objetivo
Implementar un conversor de números arábigos a números romanos siguiendo TDD.

### Especificaciones
Conversión de números (1-3999) a numerales romanos:
- **Símbolos básicos**: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
- **Reglas de resta**: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
- **No más de 3 símbolos consecutivos** del mismo tipo

### Ejemplos
```java
converter.convert(1) → "I"
converter.convert(4) → "IV"
converter.convert(5) → "V"
converter.convert(9) → "IX"
converter.convert(27) → "XXVII"
converter.convert(1994) → "MCMXCIV"
```

### Progresión Sugerida de Tests
#### Paso 1: Números básicos (1, 5, 10)
#### Paso 2: Casos de resta (4, 9)
#### Paso 3: Números medianos (40, 50, 90, 100)
#### Paso 4: Números grandes (400, 500, 900, 1000)
#### Paso 5: Números complejos (1994, 2023)

### Archivos del Ejercicio
- **Test**: `src/test/java/com/tp2/roman/RomanNumeralsTest.java`
- **Implementación**: `src/main/java/com/tp2/roman/RomanNumerals.java`

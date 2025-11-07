class: center, middle, inverse

# Lambda Expressions in Java (21)

---

## Agenda

1. What are Lambdas?
2. Functional Programming (mini intro)
3. Why Lambdas? (Value & impact)
4. Java Lambda Syntax
5. Functional Interfaces
6. java.util.function Primer
7. Method References
8. Streams + Lambdas
9. Scope, Captures, & Exceptions
10. Best Practices & Pitfalls
11. Exercises
12. Conclusion

---

## What are Lambdas?

**Lambda expression** = a concise function literal (anonymous function) you can treat as a value.

- You can **pass** it to methods, **return** it, **store** it in variables.
- In Java, lambdas implement **functional interfaces** (single abstract method).

```java
// (parameters) -> expression
Runnable r = () -> System.out.println("Hello");

// (parameters) -> { statements }
Comparator<String> byLen = (a, b) -> Integer.compare(a.length(), b.length());

```

---

## Functional Programming (mini intro)

Core ideas:
- Functions as values (first-class): pass, return, compose.
- Immutability & reduced shared state.
- Declarative style: tell what, not how.
- Higher-order functions (take/return functions).

Benefits: fewer side effects, clearer intent, easier concurrency & testing.

---

## Why Lambdas? (Value & impact)

- Eliminate verbose anonymous classes.
- Enable Streams (map/filter/reduce) & fluent APIs.
- Improve readability and maintainability.
- Facilitate parallelism (parallel streams) with minimal code changes.

---

## Java Lambda Syntax

```java
// Single parameter, expression body (type inference)
Consumer<String> log = msg -> System.out.println(msg);

// Multiple parameters, expression body
BiFunction<Integer, Integer, Integer> add = (x, y) -> x + y;

// Block body with return
Function<String, Integer> length = s -> { return s.length(); };

// Explicit parameter types (optional)
Predicate<String> longWord = (String s) -> s.length() > 10;

// No params
Supplier<Double> rnd = () -> Math.random();
```

Rules:
- Parameter types usually inferred.
- Use parentheses for 0 or >1 parameters.
- Use braces + return for multi-statement bodies.

---

## Functional Interfaces

A functional interface has exactly one abstract method (SAM).

```java
@FunctionalInterface
interface Formatter<T> {
    String format(T value);
}
Formatter<Integer> f = n -> "N=" + n;
```

- May contain default/static methods.
- Common built-ins in java.util.function (next slides).

---

## java.util.function — Core Types

Single-arg

- Function<T,R> — R apply(T t)
- Predicate<T> — boolean test(T t)
- Consumer<T> — void accept(T t)
- Supplier<T> — T get()
- UnaryOperator<T> — T apply(T t) (Function where T->T)


Two-arg
- BiFunction<T,U,R> — R apply(T t, U u)
- BiPredicate<T,U> — boolean test(T t, U u)
- BiConsumer<T,U> — void accept(T t, U u)
- BinaryOperator<T> — T apply(T t1, T t2)

Primitives (avoid boxing): IntPredicate, LongFunction<R>, DoubleUnaryOperator, etc.

---

## java.util.function — Composition Helpers

```java
Function<String, Integer> parse = Integer::parseInt;
Function<Integer, Integer> square = x -> x * x;

Function<String, Integer> parseThenSquare = parse.andThen(square);
Function<Integer, Integer> squareThenNegate = square.andThen(x -> -x);

Predicate<String> nonEmpty = s -> !s.isEmpty();
Predicate<String> longEnough = s -> s.length() > 5;
Predicate<String> ok = nonEmpty.and(longEnough).negate();
```

- Function#compose, andThen
- Predicate#and, or, negate
- Comparator#thenComparing

---

## Method References

Shorthand for common lambda shapes:

```java
// Static method


Function<String, Integer> parse = Integer::parseInt;

// Instance method of a particular object


PrintStream out = System.out;

Consumer<String> log = out::println;

// Instance method of an arbitrary object of a type


Function<String, String> trim = String::trim;

// Constructor reference


Supplier<List<String>> newList = ArrayList::new;

Function<Integer, int[]> newArray = int[]::new;
```

Use when it improves readability.

---

## Streams + Lambdas (Essentials)

```java
List<String> names = List.of("Ana", "Tomás", "Lucía", "Matías");

List<String> result = names.stream()
    .filter(n -> n.length() > 3)       // Predicate
    .map(String::toUpperCase)          // Function
    .sorted(Comparator.comparingInt(String::length).reversed())
    .toList();

int totalChars = names.stream()
    .mapToInt(String::length)
    .sum();
```

- Declarative pipelines: filter, map, flatMap, sorted, distinct, limit, skip
- minal ops: forEach, collect, reduce, toList, sum, findFirst, allMatch

---

## Reduce & Collect

```java
int product = List.of(2,3,4).stream()
    .reduce(1, (a, b) -> a * b);

// Collectors
Map<Integer, List<String>> byLen = names.stream()
    .collect(Collectors.groupingBy(String::length));

String joined = names.stream()
    .collect(Collectors.joining(", "));

double avgLen = names.stream()
    .collect(Collectors.averagingInt(String::length));
```

Use Collectors for grouping, partitioning, joining, statistics, mapping, etc.

---

## Conclusion
- Lambdas bring functional style to Java: concise, expressive, testable.
- Combined with functional interfaces, method references, Streams, and Optional, they unlock powerful, declarative APIs.
- Focus on clarity, immutability, and composition; measure performance and avoid overuse.
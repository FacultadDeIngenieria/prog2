class: center, middle, inverse

# Pattern Matching in Java 21

---

## Agenda

1. What is Pattern Matching?
2. Motivation and Evolution
3. Pattern Matching with `instanceof`
4. Pattern Matching with `switch`
5. Record Patterns
6. Nested and Guarded Patterns
7. Exhaustiveness and Sealed Types
8. Best Practices
9. Conclusion


---


## What is Pattern Matching?

A concise and type-safe way to **test an object’s shape and extract data** from it in one step.

Instead of:
```java
if (obj instanceof Person) {
    Person p = (Person) obj;
    ...
}
```

We can now match and bind directly:

```java
if (obj instanceof Person p) {
    System.out.println(p.name());
}
```


---


## Motivation and Evolution


•	Java 14: Preview of pattern matching for instanceof.
•	Java 16: Records introduced, enabling structural data models.
•	Java 17: Sealed classes and interfaces (foundation for exhaustive matching).
•	Java 21: Pattern matching for switch and record deconstruction finalized.

Goal:   

- Simplify conditional logic
- reduce casting boilerplate
- make switch more expressive and safe.


---


## Pattern Matching with instanceof



```java
public class InstanceOfExample {
    public static void main(String[] args) {
        Object obj = "Hello, Pattern Matching!";

        if (obj instanceof String s && s.length() > 5) {
            System.out.println("String length: " + s.length());
        } else if (obj instanceof Number n) {
            System.out.println("Number: " + n.doubleValue());
        } else {
            System.out.println("Unknown type");
        }
    }
}
```

✅ Binds a variable (s, n) automatically on success.
✅ Safe, readable, and eliminates manual casts.



---



## Pattern Matching with switch

```java
static String formatObject(Object obj) {
    return switch (obj) {
        case null -> "null value";
        case Integer i -> "Integer: " + i;
        case String s -> "String of length " + s.length();
        case Boolean b -> "Boolean: " + b;
        default -> "Unknown type";
    };
}

public static void main(String[] args) {
    
    System.out.println(formatObject("Hello"));
    
    System.out.println(formatObject(42));
    
    System.out.println(formatObject(true));
    
}
```

- ✅ Each case can have a pattern variable.
- ✅ null can be matched directly.
- ✅ Type safety verified at compile time.
- 
---

## Record Patterns

Records *naturally* work with pattern matching to destructure components.


```java
record Point(int x, int y) {}

static String describe(Point p) {
    return switch (p) {
        case Point(int x, int y) when x == y -> "Diagonal point: " + x;
        case Point(int x, int y) -> "Point at (" + x + ", " + y + ")";
        default -> "Not a point";
    };
}

public static void main(String[] args) {
    System.out.println(describe(new Point(3, 3)));
    System.out.println(describe(new Point(2, 5)));
}
```
✅ Deconstructs record fields directly in the pattern.
✅ Guard (when) adds conditional logic.



---



## Nested Record Patterns

Patterns can be nested to deconstruct complex data models.


```java
record Address(String city, String country) {}
record Person(String name, int age, Address address) {}

static String describePerson(Person p) {
    return switch (p) {
        case Person(String n, int a, Address(String c, String _)) when a < 18 ->
            n + " is a minor from " + c;
        case Person(String n, int a, Address(String c, String _)) ->
            n + " is an adult from " + c;
    };
}
```

✅ Fully deconstructs nested records in one expression.
✅ Guards provide fine-grained control.



---



## Exhaustiveness and Sealed Types

Sealed hierarchies ensure all cases are handled safely.

```java
sealed interface Shape permits Circle, Rectangle, Square {}

record Circle(double r) implements Shape {}
record Rectangle(double w, double h) implements Shape {}
record Square(double a) implements Shape {}

static double area(Shape s) {
    return switch (s) {
        case Circle c -> Math.PI * c.r() * c.r();
        case Rectangle r -> r.w() * r.h();
        case Square q -> q.a() * q.a();
    };
}
```

✅ The compiler verifies all permitted subtypes are covered.
✅ No default needed when exhaustive.



---



## Guarded Patterns (when)

Guards refine matches with conditions.

```java
static String describeNumber(Number n) {
    return switch (n) {
        case Integer i when i > 0 -> "Positive integer";
        case Integer i when i < 0 -> "Negative integer";
        case Double d when d.isNaN() -> "NaN double";
        case null -> "Null value";
        default -> "Other number";
    };
}
```
✅ Clean separation between pattern shape and condition.
✅ Prevents deep nested if-else chains.



---



## Advanced Example

```java
sealed interface Event permits Login, Logout, Error {}

record Login(String user) implements Event {}

record Logout(String user) implements Event {}

record Error(int code, String message) implements Event {}

static String handle(Event e) {
    return switch (e) {
        case Login(String u) -> "User " + u + " logged in.";
        
        case Logout(String u) -> "User " + u + " logged out.";
        
        case Error(int c, String m) when c >= 500 ->
                "Server error " + c + ": " + m;
        
        case Error(int c, String m) ->
                "Client error " + c + ": " + m;
    };
}
```

✅ Combines record deconstruction, sealing, and guards.

---

## Best Practices

•	Prefer sealed hierarchies for exhaustive safety.
•	Keep switch expressions pure—avoid side effects.
•	Use guards (when) for additional conditions.
•	Avoid default unless necessary (it breaks exhaustiveness).
•	Model data with records for natural pattern deconstruction.
•	Use type patterns (instanceof) for small, isolated checks.



---



## Common Pitfalls

•	Forgetting default in non-sealed hierarchies causes compilation errors.
•	Shadowing variable names inside patterns.
•	Overusing nested patterns → readability issues.
•	Confusing runtime type checks with compile-time patterns (generics).



---



## Conclusion
•	Pattern Matching in Java 21 is concise, safe, and expressive.
•	Works seamlessly with records, sealed types, and switch.
•	Encourages functional, declarative style over imperative casting logic.
•	A key step toward a more modern, pattern-oriented Java.


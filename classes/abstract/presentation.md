
# Abstract Classes and Inheritance in Java

---

## Abstract Class

An **abstract class** in Java is a class that cannot be instantiated on its own and is meant to be subclassed.

- It is used to represent an **incomplete concept**.
- Contains one or more **abstract methods** (methods without implementation).
- Can also contain fully implemented methods.

### Example:
```java
abstract class Animal {
  // Abstract method
  public abstract void sound();

  // Regular method
  public void sleep() {
    System.out.println("This animal is sleeping");
  }
}
```

---

## Abstract Methods

An **abstract method** is a method that is declared but does not have a body.

- Subclasses that extend an abstract class must provide implementations for all abstract methods.

### Example:
```java
abstract class Animal {
  public abstract void sound();
}

class Dog extends Animal {
  public void sound() {
    System.out.println("Bark");
  }
}
```

---

## Inheritance

**Inheritance** is a mechanism where one class acquires the properties and behaviors of another class.

- **`extends`** keyword is used to inherit from a class.
- Subclasses inherit fields and methods from the parent class.
- Subclasses can override methods to provide specific functionality.

### Example:
```java
class Dog extends Animal {
  public void sound() {
    System.out.println("Bark");
  }
}
```

---

## When to Use Abstract Classes?

- When you want to share **common code** among related classes.
- When classes share **common behavior** but should also enforce **specific implementations**.

### Example:
```java
abstract class Shape {
  public abstract double area();
}

class Circle extends Shape {
  private double radius;

  public Circle(double radius) {
    this.radius = radius;
  }

  public double area() {
    return Math.PI * radius * radius;
  }
}
```

---

## Example: Real-world Scenario

### Vehicle Example:
You could create an abstract class `Vehicle` that has an abstract method `move()`.

- **Car** and **Bicycle** can extend `Vehicle`, each providing its own implementation of `move()`.
  
```java
abstract class Vehicle {
  public abstract void move();
}

class Car extends Vehicle {
  public void move() {
    System.out.println("The car drives on roads.");
  }
}

class Bicycle extends Vehicle {
  public void move() {
    System.out.println("The bicycle is pedaled on paths.");
  }
}
```

---

## Constructors in Abstract Classes

- **Abstract classes** can have constructors, even though you cannot instantiate them directly.
- These constructors are called when a **subclass** is instantiated.
- They are used to initialize fields that are common to all subclasses.

### Example:
```java
abstract class Animal {
  String name;

  // Constructor for the abstract class
  public Animal(String name) {
    this.name = name;
  }

  public abstract void sound();
}

class Dog extends Animal {
  public Dog(String name) {
    super(name);  // Calling the abstract class constructor
  }

  public void sound() {
    System.out.println(name + " says: Bark");
  }
}


---

## Benefits of Using Abstract Classes

- Provides a common base for multiple subclasses.
- Helps in **code reusability** by sharing methods among related classes.
- Enforces a **contract** for subclasses, ensuring certain methods are always implemented.

---

### Conclusion

Abstract classes and inheritance provide a powerful way to structure and organize your code by defining common behavior and enforcing structure. Abstract classes help in designing clear, reusable, and maintainable code.


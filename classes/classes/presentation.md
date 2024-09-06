class: center, middle, inverse

# Classes

---

## Class

Blueprint for building objects of the same type.

*Classes* describe *instances* by listing the **attributes** they will have and the **behaviors** they share.

#### Composed by
- **State**: a set of attributes that describe the object.
- **Behavior**: 
  - Defines a contract/protocol for how to interact through its messages that can receive (method signature).
  - How it will react and change its internal state, and what information it will make visible to the outside world (getters & setters).

.center[![Model]({{site.baseurl}}/classes/classes/class_model.png)]


---

## Object construction & lifecycle

.center[![Lifecycle]({{site.baseurl}}/classes/classes/lifecycle.png)]

---

## Access modifiers

### Methods
It is not good for all methods to be public.

Some should be private, so that behavior can also be hidden from the outside.

### State
As a general rule, all components of an object should be private. Otherwise, it breaks the _Encapsulation_ rule.

However, sometimes for efficiency reasons, a member can be made visible externally, but it must be **final**.

---

## Access modifiers in Java

**public**: It is visible from the entire program.
```java 
public void deposit(float amount)
public final int cbu;     // account.cbu 
```

**private**: Only accessible from the same class.
```java 
private void validate();
private float balance;
```

**protected**: Only accessible from classes in the same package or subclasses.
```java 
protected void setName(String name)    // student.setName("Diego")
protected String name;                 // student.name 
```

**package (defalut)**: Only accessible from the same package but not subclasses in other packages.
```java 
protected void setName(String name)    // student.setName("Diego")
protected String name;                 // student.name 
```

## Access modifiers in Python

By default, all the variables and methods in a Python class are public.

Make age private and salary as protected by prefixing double and single underscores respectively.
```python 
class Employee:

   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)
 
```

---

## Variables

### Instance variables
- They contain the state of an object
- They are only visible to the object that contains them 
- They cannot be modified from the outside
- They can only be accessed through the object's methods

### Class variables
- They maintain the internal state of the class 
- They are only visible to instances of the class 
- They can only be modified by instances of the class, or by class methods.

---

## Methods

### Instance methods
Modify objects belonging to a class only.

The change is only visible to the object in question.

### Class methods
They can receive messages and the change is visible to all member objects of that class.

_new_ is an example of a class method.

---

## Instance vs Class Example

```java
public class Bill {
    
    private static double secondCost = 1.0;
    private String phone;
    private Entry[] entries;

    public Bill(String aPhone) {
        phone = aPhone;
        entries = new Entry[50];
    }
    
    public static double getCostPerSecond() { 
        return secondCost; 
    }
    
    public static void setCost(double cost) { 
        secondCost = cost; 
    }
    
    public void register(String destination, int seconds) {
        int free = nextFree();
        if (free == -1) {
            throw new RuntimeException("No hay más lugar...");
        }
        this.entries[free] = 
                new Entry(destination, seconds, seconds * getCostPerSecond());
    }
}
```

---

## Composition

Objects can be composed not only by _primitive types_ provided but also be by other objects.

We think of it as something "part of" another thing relationship.

The container object is called an _Aggregate_. The contained objects are called _components or parts._

.center[![Example]({{site.baseurl}}/classes/classes/aggregation_examples.png)]

---

## Composition

### Weak Aggregation
- The component lifecycle is independent of the aggregate object. 
- i.e. classroom and chair: can have zero, one, or several chairs. 
- Relationship: “has a”

### Strong Aggregation
- The component's life cycle is related to that of the aggregate. 
- i.e. Cellular and antenna: no sense without antenna 
- Relationship: “it is a”

.center[![Aggregations]({{site.baseurl}}/classes/classes/aggregations.png)]

---

## Composition Example

```java
public class Triangle {
    
    public Rect ab;
    public Rect bc;
    public Rect ac;
    
    public Triangle(Point2D a, Point2D b, Point2D c) {
        ab = new Rect(a, b);
        bc = new Rect(b, c);
        ac = new Rect(a, c);
    }
    
    public double perimeter() { 
        return ab.length() + bc.length() + ac.length(); 
    }
    
    public double area() {
        double s = perimeter() / 2 ;
        return Math.sqrt(s*(ab.length()-s)*(bc.length()-s)*(s-ac.length()));
    }
}
```

---

## Equals

### Built-in data types 

Use a space in memory, so the **==** operator compares each element in the memory it represents.

```java
public class Main {
    public boolean equals(int a, int b) {
        return a == b;
    }
}
```

### Non-built-in data types

Use the **equals** method.

All classes implement it.

If not defined, it compares memory addresses.

---

## Equals example

### Non-built-in data types

```java
public class Book {
    private String title;
    private Author author;
    private int year;
    
    public boolean equals(Object o) {
        if (o == this) { 
            return true; 
        }
        
        if (o == null) { 
            return false; 
        }
        
        if (!o.getClass().equals(Book.class)) { 
            return false; 
        }
        
        Book aBook = (Book) o;
        
        return aBook.year == year && 
                aBook.title.equals(title) && 
                aBook.author.equals(author);
    }
}
```

---

## Equals example test

### Non-built-in data types

```java
public class Main {
    public static void main(String[] args) {
        
        Book a = new Book("Juan Cortaba Manzanas", new Author("Juan Martín"), 2010);
        Book b = new Book("Juan Cortaba Manzanas", new Author("Juan Martín"), 2010);
        
        
        System.out.println(a.equals(b)); //True
      
        System.out.println(a == b); //False
    }
}
```

---

## Overloading

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.

You can reuse the name of a method, so that it is easier to understand.

For example, it would be nice if adding an integer to a complex number was just as readable as adding a complex number to another complex number.

```java
public Complex add(Complex complex)
public Complex add(Integer integer)

public Complex addComplex(Complex complex);
public Complex addInt(int i);
```

A Constructor is a method too, and therefore can be overloaded in order to provide more than one way to initialize an object.

```java
public Complex(float real, float imaginary);
public Complex(float real);  //imaginary = 0
```

### In Python
When working with languages that can discriminate data types at compile-time, selecting among the alternatives can occur at compile-time.

Python is a dynamically typed language, so the concept of overloading simply does not apply to it.

However, we can create such alternative functions at run-time with _multimethods or multiple dispatch._

---

## Design patterns

A design pattern is a solution to a recurring problem. 

The goal is to provide a standardized solution to a recurring problem.

### Singleton
There are cases where there is only one instance of an object in the system. 

For example:
- Runtime, the class that represents the Java virtual machine
- The application we are building
- The graphical environment

However, this pattern should not be overused, as it makes the code
completely coupled with itself, making it difficult to maintain and test.

**How would you do it?**

---

### Singleton

A class variable of the type that is the Singleton is defined and the constructor is declared
**private**.

In this way, the user is not allowed to create a _new instance_ without control.

```java
public class Application {
  
    private StudentDataBase studentDatabase;
    private static Application instance;
    
    public static Application getInstance() {
        if(instance == null) {
            instance = new Application();
        }
        return instance;
    }
    
    private Application() {
        
        StudentDataBase.getInstance();
        
        Runtime.getRuntime();
    }
}
```

---

## Bonus

### KISS: Keep It Short & Simple
- It helps in solving problem quickly. 
- Since solution is simple, it helps in maintaining code. 
- It provides flexibility to modify or refactor code. 
- It provides solution of complex problems in fewer lines of code. 
- At the end it delivers high-quality code.

### DRY: Don't Repeat Yourself
- Reuse your code and never duplicate it.
- Follow naming conventions and assign clear names of a method, variable, class and objects etc. 
- Write code in appropriate layers, locations and services.

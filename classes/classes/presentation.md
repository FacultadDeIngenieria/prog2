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

## Lifecycle

.center[![Lifecycle]({{site.baseurl}}/classes/classes/lifecycle.png)]

---

## Access modifiers 

### Methods
- It is not good for all methods to be public.
- Some should be private, so that behavior can also be hidden from the outside.

### State
- As a general rule, all components of an object should be private. Otherwise, it breaks the _Encapsulation_ rule.
- However, sometimes for efficiency reasons, a member can be made visible externally, but it must be **final**.

---

## Access modifiers

### public
It is visible from the entire program.
```java 
public void deposit(float amount)

public final int cbu;     // account.cbu 
```

### private 
Only accessible from the same class.
```java 
private void validate();

private float balance;
```

### protected
Only accessible from classes in the same package or subclasses.
```java 
protected void setName(String name)    // student.setName("Diego")

protected String name;                 // student.name 
```

### package (defalut)
Only accessible from the same package but not subclasses in other packages.
```java 
protected void setName(String name)    // student.setName("Diego")

protected String name;                 // student.name 
```


---

## Overloading

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

public Interval(float first, float last, float step);
public Interval(float first, float last);   //step = 1
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

```java
// example
```

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
        this.entries[free] = new Entry(destination, seconds, seconds * getCostPerSecond());
    }
}
```

---

## Composition

Objects can be composed not only by _primitive types_ provided but also be by other objects.

We think of it as something "part of" another thing relationship.

The container object is called an _Aggregate_. The contained objects are called _components or parts._

### Weak Aggregation
- The component lifecycle is independent of the aggregate object. 
- i.e. classroom and chair: a classroom can have zero, one, or several chairs. 
- Relationship: “has a”

### Strong Aggregation
- The component's life cycle is related to that of the aggregate. 
- i.e. Cellular and antenna: no sense without antenna 
- Relationship: “it is a”

.center[![Lifecycle]({{site.baseurl}}/classes/classes/aggregations.png)]

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

Built-in data types use a space in memory, so the == operator compares each element in the memory it represents.

```java
public class Main {
    public boolean equals(int a, int b) {
        return a == b;
    }
}
```

---

## Equals

Non-built-ins data types use the _equals_ method. 

All classes implement it. 

If not defined, it compares memory addresses.

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

public class Main {
    public static void main(String[] args) {
        Book a = new Book("Juan Cortaba Manzanas", new Author("Juan Martín"), 2010);
        Book b = new Book("Juan Cortaba Manzanas", new Author("Juan Martín"), 2010);
        
        System.out.println(a.equals(b)); //True
        System.out.println(a == b); //False
    }
}
```
class: center, middle, inverse

# Object-Oriented Programming (OOP)

---

## Agenda

1. What is Object-Oriented Programming?
2. History
3. Classes in Python
4. Classes in Java
5. Characteristics
6. Principles
7. Conclusion

---

## What is Object-Oriented Programming?

A programming paradigm based on the use of "objects," which can contain data and code.

Objects interact with one another through methods, allowing for a modular approach to programming.

This paradigm contrasts with procedural programming, which focuses on functions and sequences of operations.

---

## What are Objects ?

Instances of "classes," which define their structure and behavior.

Each object can hold its own unique data and utilize the methods defined by its class to manipulate that data.

This allows for the creation of complex data models and interactions within a program.

---

## What is the purpose ?

To facilitate code organization and improve reusability.

By encapsulating data and methods within objects, developers can build modular components that can be reused across different parts of a program or in different projects.

This approach also helps in managing and maintaining large codebases more effectively.

---

## History

- **1960s:** The OOP concept emerged with Simula 67, the first object-oriented language.
- **1980s:** Languages like Smalltalk popularized OOP, followed by C++.
- **1990s and 2000s:** Java and C# dominate object-oriented development.
- **Present:** OOP remains one of the most widely used paradigms.

---

## Defining Classes in Python

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name : str = name
        self.age : int = age
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

In Python, the **__init__** method is a special method used for initializing a new instance of a class.
It is called constructor method, and it does not return anything. Instead, it initializes the attributes of the instance and sets up the object.

---

## Instantiating Classes in Python

```python
# Instantiation of Person
person1 : Person = Person(name="Alice", age=30)

# Using the greet method
greeting : str = person1.greet()
print(greeting)
```

**person1 = Person(name="Alice", age=30)** creates a new instance of the Person class.


**greeting = person1.greet()** calls the greet method on the **person1** instance.


This method returns a string with the person's name and age, which is then stored in the greeting variable.
---

## Defining Classes in Java

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String greet() {
        return "Hello, my name is " + name + " and I am " + age + " years old.";
    }
}
```

**private String name;**: This line declares a private instance variable name of type String. The **private** keyword restricts access to this variable from outside the class.

**private int age;**: Similarly, this line declares a private instance variable age of type int.

**public Person(String name, int age)**: This is the constructor of the Person class. It has the same name as the class and is used to initialize new objects of that class.

---

## Defining Classes in Java

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String greet() {
        return "Hello, my name is " + name + " and I am " + age + " years old.";
    }
}
```


The constructor takes two parameters: **name** (a String) and **age** (an int).

Inside the constructor, **this.name = name;** assigns the value of the parameter name to the instance variable **name**.

Similarly, **this.age = age;** assigns the value of the parameter age to the instance variable **age**.

---

## Instantiating Classes in Java

```java
public class Main {
    public static void main(String[] args) {
        // Instantiation of Person
        Person person1 = new Person("Alice", 30);

        // Using the greet method
        String greeting = person1.greet();
        System.out.println(greeting);
    }
}
```
**new Person("Alice", 30)**: This creates a new **Person** object using the constructor. The name is set to "Alice" and age is set to 30.


**Person person1**: This declares a variable **person1** of type **Person** and assigns the newly created Person object to it.

**person1.greet()**: Calls the **greet** method on the **person1** object, which returns a greeting message.

---

[//]: # ()
[//]: # (## Characteristics - Encapsulation)

[//]: # ()
[//]: # (Grouping data and methods that operate on it.)

[//]: # ()
[//]: # (**Data Hiding:** Encapsulation hides the internal state of an object from the outside world.)

[//]: # (Only specific methods are exposed to interact with the object's data, which helps maintain control over how the data is accessed or modified.)

[//]: # ()
[//]: # (**Controlled Access:** Encapsulation provides a controlled way to access and modify the object's data.)

[//]: # (This is typically achieved through getter and setter methods.)

[//]: # ()
[//]: # (**Increased Flexibility:** By hiding implementation details, encapsulation allows the internal implementation of a class to be changed without affecting the classes that use it.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Characteristics - Encapsulation - Example)

[//]: # ()
[//]: # (```python)

[//]: # (class Person:)

[//]: # (    def __init__&#40;self, name, age&#41;:)

[//]: # (        self.__name = name  # private attribute)

[//]: # (        self.__age = age    # private attribute)

[//]: # ()
[//]: # (    # Public method to access private attribute)

[//]: # (    def get_name&#40;self&#41;:)

[//]: # (        return self.__name)

[//]: # ()
[//]: # (    # Public method to modify private attribute)

[//]: # (    def set_name&#40;self, name&#41;:)

[//]: # (        self.__name = name)

[//]: # ()
[//]: # (    # Public method to access private attribute)

[//]: # (    def get_age&#40;self&#41;:)

[//]: # (        return self.__age)

[//]: # ()
[//]: # (    # Public method to modify private attribute)

[//]: # (    def set_age&#40;self, age&#41;:)

[//]: # (        if age > 0:)

[//]: # (            self.__age = age)

[//]: # (        else:)

[//]: # (            print&#40;"Invalid age"&#41;)

[//]: # ()
[//]: # (# Usage)

[//]: # (person = Person&#40;"John Doe", 30&#41;)

[//]: # (print&#40;person.get_name&#40;&#41;&#41;  # Access private attribute through a public method - "John Doe")

[//]: # (print&#40;person.get_age&#40;&#41;&#41;   # Access private attribute through a public method - 30)

[//]: # (person.set_age&#40;31&#41;        # Modify private attribute through a public method -)

[//]: # (print&#40;person.get_age&#40;&#41;&#41;   # Verify the change                                - 31)

[//]: # ()
[//]: # (```)

[//]: # (---)

[//]: # (## Characteristics - Abstraction)

[//]: # ()
[//]: # (Hiding internal details and exposing functionalities.)

[//]: # ()
[//]: # (---)

[//]: # (## Characteristics - Inheritance)

[//]: # ()
[//]: # (Ability to create new classes based on existing ones.)

[//]: # ()
[//]: # ()
[//]: # (---)

[//]: # (## Characteristics - Polymorphism)

[//]: # ()
[//]: # (Ability of an object to take multiple forms.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Principles - S.O.L.I.D.)

[//]: # (    )
[//]: # (* **S**: Single Responsibility Principle)

[//]: # (* **O**: Open/Closed Principle)

[//]: # (* **L**: Liskov Substitution Principle)

[//]: # (* **I**: Interface Segregation Principle)

[//]: # (* **D**: Dependency Inversion Principle)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Principles - S.O.L.I.D. - Single Responsibility Principle)

[//]: # (**Example:** Suppose you have a class Invoice.)

[//]: # (It should only handle tasks related to invoicing, like calculating total amounts.)

[//]: # (If it also handles printing or saving the invoice to a database, that would violate this principle.)

[//]: # (Instead, create separate classes like InvoicePrinter and InvoiceRepository.)

[//]: # (```python)

[//]: # (class Invoice:)

[//]: # (    def calculate_total&#40;self&#41;:)

[//]: # (        # Calculate total amount)

[//]: # (        pass)

[//]: # ()
[//]: # (class InvoicePrinter:)

[//]: # (    def print_invoice&#40;self, invoice: Invoice&#41;:)

[//]: # (        # Print the invoice)

[//]: # (        pass)

[//]: # ()
[//]: # (class InvoiceRepository:)

[//]: # (    def save_to_database&#40;self, invoice: Invoice&#41;:)

[//]: # (        # Save the invoice to the database)

[//]: # (        pass)

[//]: # (```)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Principles - S.O.L.I.D. - Open/Closed Principle)

[//]: # ()
[//]: # (**Example:** A PaymentProcessor class should be open to extension but closed to modification.)

[//]: # (If you need to add new payment methods, you should extend the class without modifying existing code.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Principles - DRY)

[//]: # ()
[//]: # (**&#40;Don't Repeat Yourself&#41;:** Avoid code duplication.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Principles - KISS)

[//]: # ()
[//]: # (**&#40;Keep It Simple, Stupid&#41;:** Keep the code simple and straightforward.)

[//]: # ()
[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Conclusion)

[//]: # ()
[//]: # (- Object-Oriented Programming is an essential paradigm in modern development.)

[//]: # (- It facilitates the creation of modular, reusable, and maintainable code.)

[//]: # (- Understanding OOP is key for any developer.)
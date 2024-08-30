class: center, middle, inverse

# Object-Oriented Programming (OOP)

---

## Agenda

1. What is Object-Oriented Programming?

2. History
   
3. Classes in Python

4. Classes in Java

5. Principles

6. Conclusion

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

In Python, the **__ init __** method is a special method used for initializing a new instance of a class.
It is called constructor method, and it does not return anything. Instead, it initializes the attributes of the instance and sets up the object.

Inside the constructor, **self.name : str = name;** assigns the value of the parameter name to the instance variable **name**.
Similarly, **self.age : int = age;** assigns the value of the parameter age to the instance variable **age**.

---

## Instantiating Classes in Python

```python
# Instantiation of Person
matias : Person = Person(name="Matias", age=29)

# Using the greet method
greeting : str = matias.greet()
print(greeting)
```

**matias = Person(name="Matias", age=29)** creates a new instance of the Person class.


**greeting = matias.greet()** calls the greet method on the **matias** instance.


This method returns a string with the person's name and age, which is then stored in the greeting variable.

---

## Defining Classes in Java

```java
public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String greet() {
        return "Hello, my name is " + name + " and I am " + age + " years old.";
    }
}
```

**String name;**: and **int age;** declares two instance variables, name of type String and age of type int.

**public Person(String name, int age)**: This is the constructor of the Person class. It has the same name as the class and is used to initialize new objects of that class.

Inside the constructor, **this.name = name;** assigns the value of the parameter name to the instance variable **name**.
Similarly, **this.age = age;** assigns the value of the parameter age to the instance variable **age**.

---

## Instantiating Classes in Java

```java
public class Main {
    public static void main(String[] args) {
        // Instantiation of Person
        Person tomas = new Person("Tomás", 18);

        // Using the greet method
        String greeting = tomas.greet();
        System.out.println(greeting);
    }
}
```
**new Person("Tomás", 18)**: This creates a new **Person** object using the constructor. The name is set to "Tomás" and age is set to 18.

**Person tomas**: This declares a variable **tomas** of type **Person** and assigns the newly created Person object to it.

**tomas.greet()**: Calls the **greet** method on the **tomas** object, which returns a greeting message.

---


## Principles:

   1. Inheritance
   
   2. Encapsulation

   3. Abstraction

   4. Polymorphism

---

## Principles - Encapsulation

Grouping data and methods that operate on it.

Encapsulation hides the internal state of an object from the outside world.
Only specific methods are exposed to interact with the object's data, which helps maintain control over how the data is accessed or modified.

This is typically achieved through getter and setter methods.

By hiding implementation details, encapsulation allows the internal implementation of a class to be changed without affecting the classes that use it.

---

## Principles - Encapsulation - Class Example

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name  # private attribute
        self.__age: int = age    # private attribute

    # Public method to access private attribute
    def get_name(self) -> str:
        return self.__name

    # Public method to modify private attribute
    def set_name(self, name) -> None:
        self.__name: str = name

    # Public method to access private attribute
    def get_age(self) -> int:
        return self.__age

    # Public method to modify private attribute
    def set_age(self, age) -> None:
        if age > 0:
            self.__age: int = age
        else:
            print("Invalid age")
```

---

## Principles - Encapsulation - Usage Example

```python
person: Person = Person("John Doe", 30)
print(person.get_name())  # Access private attribute through a public method - "John Doe"
print(person.get_age())   # Access private attribute through a public method - 30
person.set_age(31)        # Modify private attribute through a public method -
print(person.get_age())   # Verify the change                                - 31
```

**Private Attributes:** The attributes **__name** and **__age** are private ( in Python this is indicated by the double underscores **__** )
This means they cannot be accessed directly from outside the class.

**Getter and Setter Methods:** The class provides **get_name**, **set_name**, **get_age**, and **set_age** methods to access and modify the private attributes.
These methods ensure that the data is validated before any changes are made (e.g., age cannot be negative).

---

## Principles - Inheritance - Base Class


Ability to create new classes based on existing ones.

This allows a new class to inherit properties and methods from an existing class. This promotes code reuse and helps in creating a hierarchical relationship between classes.

```python
class Animal:
    def __init__(self, name: str, species: str) -> None:
        self.name: str = name
        self.species: str = species

    def make_sound(self) -> str:
        return "Some generic sound"

    def describe(self) -> str:
        return f"{self.name} is a {self.species}"
```
**Animal** is a Base Class that contains attributes name and species and methods like **make_sound()** and **describe()**.
 This class provides basic functionality common to all animals.

---

## Principles - Inheritance - Subclasses

```python
class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name, "Dog")
        self.breed: str = breed

    def make_sound(self) -> str:
        return "Woof!"

    def fetch(self) -> str:
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, "Cat")
        self.color: str = color

    def make_sound(self) -> str:
        return "Meow!"

    def climb(self) -> str:
        return f"{self.name} is climbing a tree"

```
**Dog** is a subclass that inherits from **Animal**. It overrides the **make_sound()** method and adds a new attribute **breed** and a new method **fetch()**.
**Cat** subclass inherits from **Animal**, overrides the **make_sound()** method, and adds a new attribute **color** and a new method **climb()**.

---

## Principles - Abstraction - Example

Hiding internal details and exposing functionalities.
It allows you to define a common interface for a set of related objects without exposing the underlying complexities.

```python
# Pseudocode
class Animal():
    def make_sound():
        pass

```

**Animal** class is an abstract base class.

It contains an abstract method **make_sound()**, which means that any subclass must implement this method.

---

## Principles - Abstraction - Example

```python
# Pseudocode
class Dog(Animal):
    def make_sound():
        return "Woof!"

class Cat(Animal):
    def make_sound():
        return "Meow!"

```
Both **Dog** and **Cat** are concrete classes and inherit from Animal and implement the **make_sound()** method. Each class provides its specific implementation.

---

## Principles - Polymorphism

Objects of different classes can be treated as objects of a common superclass. It enables the same method to behave differently based on the object calling it.

In simpler terms, polymorphism means "many shapes," and it allows methods to do different things based on the object they're acting upon.

```python
# Including Animal, Dog and Cat classes.
class Bird(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, "Bird")
        self.color: str = color

    def make_sound(self) -> str:
        return "Chirp!"

# Outside these Animal classes. Example usage:
def animal_sound(animal: Animal) -> str:
    print(f"{animal.describe()} It says: {animal.make_sound()}")
 
animals : List[Animal]= [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    animal_sound(animal)
```
---

## Conclusion


- Object-Oriented Programming is an essential paradigm in modern development.

- It facilitates the creation of modular, reusable, and maintainable code.

- Understanding OOP is key for any developer.
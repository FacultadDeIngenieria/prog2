class: center, middle, inverse

# Object-Oriented Programming (OOP)

---

## Agenda

1. What is Object-Oriented Programming?

2. History

3. Classes in Java

4. Principles

5. Conclusion

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

<!---
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
-->


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

   1. Encapsulation
   
   2. Inheritance

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

```java
public class Person {
    
    // Atributos privados
    private String name;
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters
    public String getName() {
        return name;
    }
    public int getAge() {
        return age;
    }

    // Setter para age con validación
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        } else {
            System.out.println("Invalid age");
        }
    }
}
```

[//]: # (```python)

[//]: # (class Person:)

[//]: # (    def __init__&#40;self, name: str, age: int&#41; -> None:)

[//]: # (        self.__name: str = name  # private attribute)

[//]: # (        self.__age: int = age    # private attribute)

[//]: # ()
[//]: # (    # Public method to access private attribute)

[//]: # (    def get_name&#40;self&#41; -> str:)

[//]: # (        return self.__name)

[//]: # ()
[//]: # (    # Public method to modify private attribute)

[//]: # (    def set_name&#40;self, name&#41; -> None:)

[//]: # (        self.__name: str = name)

[//]: # ()
[//]: # (    # Public method to access private attribute)

[//]: # (    def get_age&#40;self&#41; -> int:)

[//]: # (        return self.__age)

[//]: # ()
[//]: # (    # Public method to modify private attribute)

[//]: # (    def set_age&#40;self, age&#41; -> None:)

[//]: # (        if age > 0:)

[//]: # (            self.__age: int = age)

[//]: # (        else:)

[//]: # (            print&#40;"Invalid age"&#41;)

[//]: # (```)

---

## Principles - Encapsulation - Usage Example

```java
public class Main {
    public static void main(String[] args) {
        // Crear objeto Person
        Person person = new Person("John Doe", 30);

        // Acceder a los atributos privados a través de getters
        System.out.println(person.getName()); // "John Doe"
        System.out.println(person.getAge());  // 30

        // Modificar atributos privados a través de setters
        person.setAge(31);

        // Verificar el cambio
        System.out.println(person.getAge());  // 31
    }
}
```

**Private Attributes:** The attributes **name** and **age** are private
This means they cannot be accessed directly from outside the class.

**Getter and Setter Methods:** The class provides **getName**, **setName**, **getAge**, and **setAge** methods to access and modify the private attributes.
These methods ensure that the data is validated before any changes are made (e.g., age cannot be negative).

---

[//]: # (```python)

[//]: # (person: Person = Person&#40;"John Doe", 30&#41;)

[//]: # (print&#40;person.get_name&#40;&#41;&#41;  # Access private attribute through a public method - "John Doe")

[//]: # (print&#40;person.get_age&#40;&#41;&#41;   # Access private attribute through a public method - 30)

[//]: # (person.set_age&#40;31&#41;        # Modify private attribute through a public method -)

[//]: # (print&#40;person.get_age&#40;&#41;&#41;   # Verify the change                                - 31)

[//]: # (```)

[//]: # (**Private Attributes:** The attributes **__name** and **__age** are private &#40; in Python this is indicated by the double underscores **__** &#41;)

[//]: # (This means they cannot be accessed directly from outside the class.)

[//]: # ()
[//]: # (**Getter and Setter Methods:** The class provides **get_name**, **set_name**, **get_age**, and **set_age** methods to access and modify the private attributes.)

[//]: # (These methods ensure that the data is validated before any changes are made &#40;e.g., age cannot be negative&#41;.)

---

## Principles - Inheritance - Base Class


Ability to create new classes based on existing ones.

This allows a new class to inherit properties and methods from an existing class. This promotes code reuse and helps in creating a hierarchical relationship between classes.

```java
public class Animal {
    
    // Attributes
    protected String name;
    protected String species;

    // Constructor
    public Animal(String name, String species) {
        this.name = name;
        this.species = species;
    }

    // Method
    public String makeSound() {
        return "Some generic sound";
    }

    // Method
    public String describe() {
        return name + " is a " + species;
    }
}
```

**Animal** is a Base Class that contains attributes name and species and methods like **makeSound()** and **describe()**.
This class provides basic functionality common to all animals.

[//]: # (```python)

[//]: # (class Animal:)

[//]: # (    def __init__&#40;self, name: str, species: str&#41; -> None:)

[//]: # (        self.name: str = name)

[//]: # (        self.species: str = species)

[//]: # ()
[//]: # (    def make_sound&#40;self&#41; -> str:)

[//]: # (        return "Some generic sound")

[//]: # ()
[//]: # (    def describe&#40;self&#41; -> str:)

[//]: # (        return f"{self.name} is a {self.species}")

[//]: # (```)

---

## Principles - Inheritance - Subclasses

```java
// Subclass Dog
public class Dog extends Animal {
    
    private String breed;

    public Dog(String name, String breed) {
        super(name, "Dog"); // Call the Animal constructor
        this.breed = breed;
    }

    @Override
    public String makeSound() {
        return "Woof!";
    }

    public String fetch() {
        return name + " is fetching the ball";
    }
}

// Subclass Cat
public class Cat extends Animal {
    
    private String color;

    public Cat(String name, String color) {
        super(name, "Cat"); // Call the Animal constructor
        this.color = color;
    }

    @Override
    public String makeSound() {
        return "Meow!";
    }

    public String climb() {
        return name + " is climbing a tree";
    }
}
```

---

## Principles - Inheritance - Subclasses

```java
// Subclass Cat
public class Cat extends Animal {
    
    private String color;

    public Cat(String name, String color) {
        super(name, "Cat"); // Call the Animal constructor
        this.color = color;
    }

    @Override
    public String makeSound() {
        return "Meow!";
    }

    public String climb() {
        return name + " is climbing a tree";
    }
}
```

**Dog** is a subclass that inherits from **Animal**. It overrides the **makeSound()** method and adds a new attribute **breed** and a new method **fetch()**.
**Cat** subclass inherits from **Animal**, overrides the **makeSound()** method, and adds a new attribute **color** and a new method **climb()**.

---

[//]: # (```python)

[//]: # (class Dog&#40;Animal&#41;:)

[//]: # (    def __init__&#40;self, name: str, breed: str&#41; -> None:)

[//]: # (        super&#40;&#41;.__init__&#40;name, "Dog"&#41;)

[//]: # (        self.breed: str = breed)

[//]: # ()
[//]: # (    def make_sound&#40;self&#41; -> str:)

[//]: # (        return "Woof!")

[//]: # ()
[//]: # (    def fetch&#40;self&#41; -> str:)

[//]: # (        return f"{self.name} is fetching the ball")

[//]: # ()
[//]: # (class Cat&#40;Animal&#41;:)

[//]: # (    def __init__&#40;self, name: str, color: str&#41; -> None:)

[//]: # (        super&#40;&#41;.__init__&#40;name, "Cat"&#41;)

[//]: # (        self.color: str = color)

[//]: # ()
[//]: # (    def make_sound&#40;self&#41; -> str:)

[//]: # (        return "Meow!")

[//]: # ()
[//]: # (    def climb&#40;self&#41; -> str:)

[//]: # (        return f"{self.name} is climbing a tree")

[//]: # (```)

---

## Principles - Abstraction - Example

Hiding internal details and exposing functionalities.
It allows you to define a common interface for a set of related objects without exposing the underlying complexities.

```java
// Abstract base class
public abstract class Animal {
    
    // Abstract method (no implementation here)
    public abstract String makeSound();
}
```

**Animal** class is an abstract base class.

It contains an abstract method **makeSound()**, which means that any subclass must implement this method.

---

[//]: # (```python)

[//]: # (# Pseudocode)

[//]: # (class Animal&#40;&#41;:)

[//]: # (    def make_sound&#40;&#41;:)

[//]: # (        pass)

[//]: # (```)

---

## Principles - Abstraction - Example

```java
// Subclass Dog
public class Dog extends Animal { 
    
    @Override
    public String makeSound() {
        return "Woof!";
    }
}

// Subclass Cat
public class Cat extends Animal { 
    
    @Override 
    public String makeSound() {
        return "Meow!";
    }
}
```

Both **Dog** and **Cat** are concrete classes and inherit from Animal and implement the **makeSound()** method. 
Each class provides its specific implementation.

[//]: # (```python)

[//]: # (# Pseudocode)

[//]: # (class Dog&#40;Animal&#41;:)

[//]: # (    def make_sound&#40;&#41;:)

[//]: # (        return "Woof!")

[//]: # ()
[//]: # (class Cat&#40;Animal&#41;:)

[//]: # (    def make_sound&#40;&#41;:)

[//]: # (        return "Meow!")

[//]: # (```)

---

## Principles - Polymorphism

Objects of different classes can be treated as objects of a common superclass. It enables the same method to behave differently based on the object calling it.

In simpler terms, polymorphism means "many shapes," and it allows methods to do different things based on the object they're acting upon.

```java
public class Bird extends Animal {
    
    private String color;

    public Bird(String name, String color) {
        super(name, "Bird");
        this.color = color;
    }

    @Override
    public String makeSound() {
        return "Chirp!";
    }
}
```

[//]: # (```python)

[//]: # (# Including Animal, Dog and Cat classes.)

[//]: # (class Bird&#40;Animal&#41;:)

[//]: # (    def __init__&#40;self, name: str, color: str&#41; -> None:)

[//]: # (        super&#40;&#41;.__init__&#40;name, "Bird"&#41;)

[//]: # (        self.color: str = color)

[//]: # ()
[//]: # (    def make_sound&#40;self&#41; -> str:)

[//]: # (        return "Chirp!")

[//]: # ()
[//]: # (# Outside these Animal classes. Example usage:)

[//]: # (def animal_sound&#40;animal: Animal&#41; -> str:)

[//]: # (    print&#40;f"{animal.describe&#40;&#41;} It says: {animal.make_sound&#40;&#41;}"&#41;)

[//]: # ( )
[//]: # (animals : List[Animal]= [Dog&#40;"Buddy"&#41;, Cat&#40;"Whiskers"&#41;, Bird&#40;"Tweety"&#41;])

[//]: # ()
[//]: # (for animal in animals:)

[//]: # (    animal_sound&#40;animal&#41;)

[//]: # (```)

---

## Principles - Polymorphism - Example

```java
public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog("Buddy");
        Animal myCat = new Cat("Whiskers");
        Animal myBird = new Bird("Tweety");

        Lists<Animal> animals = new ArrayList<>();
        animals.add(myDog);
        animals.add(myCat);
        animals.add(myBird);
        
        for (Animal animal : animals) {
            System.out.println(animal.describe() + " It says: " + animal.makeSound());
        }
    }
}
```

---

## Conclusion


- Object-Oriented Programming is an essential paradigm in modern development.

- It facilitates the creation of modular, reusable, and maintainable code.

- Understanding OOP is key for any developer.
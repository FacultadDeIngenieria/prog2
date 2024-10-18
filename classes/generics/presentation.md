class: center, middle, inverse

# Generics

---

## Generics

It is a class or interface that has a parameterized type.

Instead of using an _Object Type_, use a _Variable Type_: S, T, U, V or the desired parameter.

It cannot be used in _class methods_ or _class variables_. 

The parameter can be any type of Object, but not built-ins.

```java
public class Box<T> {
    //...
}
```

```java
public class List<E> {
    //...
}
```

```java
public interface Map<K, V> {
    //...
}
```

Why don't we want to have a list of each type? or a list of _Object_?

---

## Example
```java
public class Box<T> {
    
    private T element;
    
    public Box(T element) {
        this.element = element;
    }
    
    public void setElement(T element) {
        this.element = element;
    }
    public T getElement() {
        return element;
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        
        //If your declared Type is String, 
        //You can only pass a String or subclass of String as an argument
        Box<String> box = new Box<String>("Hello");
        
        //It is not necessary to cast, because getElement returns String
        String msg = box.getElement();
        box.setElement("World!");
    }
}
```

---

## Type Safety

The compiler checks types on assignments:
  - Casting is avoided 
  - Elements must be of the indicated type

```java
public class Main {
    public static void main(String[] args) {
        
        Box<String> boxString = new Box<String>("Hello");
        Box<Integer> boxInteger = new Box<Integer>(1);
        
        String msg = boxString.getElement(); //OK
        String msg2 = boxInteger.getElement(); //Error
        boxInteger.setElement("String"); //Error
        
        //When executed, the generic type disappears
        System.out.println(boxString.getClass().equals(boxInteger.getClass())); //True
        
        //Since all instances belong to the same class, this cannot be done
        if(boxInteger instanceof Box<Integer>) {
            //...
        }
    }
}
```

---

## Inheritance

Generic types can be inherited

```java
public class SubClass<T> extends SuperClass<T> {
    //...
}
```

```java
public class SubClass extends SuperClass<String> {
    //...
}

```

---

## Polymorphism

The same goes for interfaces.

However, the generic type is limited with _bounded types_:

```java
public interface Integrable<T extends Number> {
    //...
}
```

```java
public class Box<T extends Serializable> {
    //...
}
```

```java
public class Box<T extends Number & Iterable & Cloneable> {
    //...
}
```

---

## Warning!
String is a subclass of Object... but Box<String> is not a subclass of Box<Object>

```java
public class Example {
    public static void main(String[] args) {
        Box<String> boxString = new Box<String>("String"); //Ok
        Box<Object> boxObject = boxString; //Error!

        //Another example ------------------------------
        List<Teacher> teachers = new ArrayList<>();
        calculateSalaries(teachers); //Error
        calculateSalaries((List<Employee>) teachers); //Error
    }
    public double calculateSalaries(List<Employee> employees) {
        double salaries = 0;
        for (Employee e : employees) {
            salaries += e.getSalary();
        }
        return salaries;
    }
}
```
                
```java
public class Employee {
    public double getSalary() {...}
}

public class Teacher extends Employee {
}
```

---

## Wildcard

You can use **?** when the type is not needed.

```java
public class Example {

    public void printList(List<?> elementos) {

        System.out.print("[");

        for (Object e : elementos) {
            System.out.print(e);
        }

        System.out.print("]");
    }

    public static void main(String[] args) {
        
        List<Teachers> teachers = new ArrayList<>();
        printList(teachers);
    }
}
```

---

## Extended Wildcard

```java
public class Example {

    public double calculateSalaries(List<? extends Employee> employees) {
        double salaries = 0;
        for(Employee e: employees) {
            salaries += e.getSalary();
        }
        return salaries;
    }
    

    public static void main(String[] args) {
        
        List<Teachers> teachers = new ArrayList<>();
        calculateSalaries(teachers);
    }
}
```

---

## Generic Methods

```java
public <T> void doSomething(T element) {
    //...
}
```

```java
public <T> void remove(T[] array, T element) {
    ...
}
```

```java
public <T> void remove(T[] array, T element) {
    ...
}
```

### Multiple Generic Types

```java
public <T, U, V> void example(T t, U u, V v) {
    ...
}
```

```java
public <T, U, V> T example(T t, U u, V v) {
    ...
    return t;
}
```

---

## Collections

Collections are a fundamental part of Java API. 

They provide mechanisms for holding and storing various types of objects. 

There are several types, each with its own interface and implementation.

### Examples
- ArrayList<T>
- LinkedList<T>
- HashSet<T>
- TreeSet<T>
- HashMap<K, V>
- TreeMap<K, V>

Each of these implements Collection<T>, in such a way that they guarantee minimum methods, such as adding, removing, size, etc.

---

## Collections

In addition, there is a class to work with collections in a generic way.

### Examples
- Collections.EMPTY_LIST: it is an empty list. 

- Collections.sort(List<T> collection, {comparator}) : orders the list. 

- Collections.unmodificableList(List<?> list) : returns a list that throws errors when you want to modify it.

- Collections.syncronizedSet(Set<?> set): returns a set that cannot be modified concurrently.

- Collections.swap(List<?> list, int i, int j);

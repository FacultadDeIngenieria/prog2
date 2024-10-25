class: center, middle, inverse

# Exceptions

---

## Exceptions

They indicate the occurrence of an unexpected event.

When an exception occurs within a method, it creates an object that contains information about the exception,
such as the name and description of the exception and the state of the program when the exception occurred.

Major reasons why an exception occurs:
- Invalid user input 
- Code errors 
- Out of bound 
- Null reference 
- Arithmetic errors (divide by zero)
- Database errors
- Opening an unavailable file
- Loss of network connection
- Physical limitations (out-of-disk memory)


### Real-life comparison.
Imagine that we order a product online, but while en-route, there’s a failure in delivery. A good company can handle this problem and gracefully re-route our package so that it still arrives on time.

Likewise, in Java, the code can experience errors while executing our instructions. Good exception handling can handle errors and gracefully re-route the program to give the user still a positive experience.

---

## Syntax
```java
try {
    //Code that can throw an exception
} catch (Throwable e) { //← Type of exception to handle
    //Exception handling
}
finally {
    //Is always executed, whether or not an error occurs
}
```

```java
public void dangerousMethod() {
    if (...) {
        throw new AnException(“Exception Message”);
    }
}
```

---

## Hierarchy

Exceptions are just Java objects with all of them extending from Throwable

There are three main categories of exceptional conditions:

- **Checked exceptions**: data/procedures/code errors (Exception)
- **Unchecked exceptions**: programming errors (Runtime Exceptions) 
- **Errors**: java errors, don't handle.

.center[![Model]({{site.baseurl}}/classes/exceptions/exception-hierarchy.png)]

---

## Checked Exceptions

Checked exceptions are exceptions that the Java compiler requires us to handle. We have to either declaratively throw the exception up the call stack, or we have to handle it ourselves. More on both of these in a moment.

- They are recoverable errors or errors that are not related to programming
- They are exceptions that inherit from Exception (but not from RuntimeException)

```java
public void processFile(String fileName) {
    try {
        FileReader reader = new FileReader(new File(fileName));
        //process file
        reader.close();
        
    } catch(FileNotFoundExcepcion e) {
        System.out.println(“No se encontró el archivo : “ + fileName);
            
    } catch(IOException e) {
        //Do something more
    }
}
```

If exceptions are not caught, it must be declared in the method, that the exception can be thrown.

```java
public void processFile(String fileName) throws IOException {
    FileReader reader = new FileReader(new File(fileName));
    //process file
        
    reader.close();
}
```

---

## Unchecked Exceptions
Unchecked exceptions are exceptions that the Java compiler does not require us to handle.

These are exceptions that are produced by a programming error, or are not recoverable. 
They should not be caught, and do not need to be caught. They inherit from RuntimeException.

Examples:
- IndexOutOfBoundsException
- OperationNotSupportedException  
- InvalidArgumentException
- NullPointerException
- ClassCastException

```java
```

---

## Errors

Errors represent serious and usually irrecoverable conditions like a library incompatibility, infinite recursion, or memory leaks.

```java
```

---

## Finally Block examples

```java
public static void main(String[] args) {
    try {
        System.out.println("Before dangerous code");
        somethingDangerous();
        System.out.println("It does not get executed");
        
    } catch (Exception e) {
        System.out.println("Catch: " + e.getMessage());
        
    } finally {
        System.out.println("Always get executed");
    }
}

private static void somethingDangerous() {
    throw new RuntimeException("Error!");
}
```

Prints:
```
Before dangerous code
Catch: Error!
Always get executed
```

---

## Finally Block example 2

```java
public static void main(String[] args) {
    System.out.println("Before testCode()");
    testCode();
    System.out.println("After testCode()");
}

private static void testCode() {
    try {
        System.out.println("Before Return");
        return;
        
    } finally {
        System.out.println("Finally...");
    }
}
```

Prints:
```
Before testCode()
Before Return
Finally...
After testCode()
```

---

## Custom Exceptions

Errors represent serious and usually irrecoverable conditions like a library incompatibility, infinite recursion, or memory leaks.

```java
public MyException extends Exception {
    
    public MyException() {
    }
    
    public MyException(String message) {
        super(message);
    }
}
```

```java
public MyException extends RuntimeException {
}
```

---

## Rules

- When reporting that a method throws an exception, it should be as general as possible, but within the framework being discussed. i.e IOException 
- Do not catch Throwable 
- In a “layered” system, catch exceptions, log them, and rethrow them, wrapping the caught one with the new one, onion style.

1. Presentation 
2. Application 
3. Persistence

```java
catch(AplicationException e) {
    throw new PresentationException(e);
}
```

```java
catch(PersistenceException e) {
    throw new AplicationException(e);
}
```

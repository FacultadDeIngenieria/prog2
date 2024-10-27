class: center, middle, inverse

# Exceptions

---

## Exceptions

They indicate the occurrence of an unexpected event.

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


### Real-life comparison
Imagine that we order a product online, but while en-route, there’s a failure in delivery. A good company can handle this problem and gracefully re-route our package so that it still arrives on time.

Likewise, in Java, the code can experience errors while executing our instructions. Good exception handling can handle errors and gracefully re-route the program to give the user still a positive experience.

---

## Syntax

When an exception occurs within a method, it creates an object that contains 
information about the exception, such as the name and description of the 
exception and the state of the program when the exception occurred.

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

Exceptions are just Java objects with all of them extending from Throwable.

There are three main categories of exceptional conditions:

- **Checked exceptions**: data/procedures/code errors (Exception)
- **Unchecked exceptions**: programming errors (Runtime Exceptions) 
- **Errors**: java errors, don't handle! (i.e. OutOfMemoryError)

.center[![Model]({{site.baseurl}}/classes/exceptions/exception-hierarchy.png)]

---

## Checked Exceptions

Checked exceptions are situational errors that Java _requires us to handle_. 

- They are recoverable errors that are not related to programming
- They are exceptions that inherit from Exception
- Throw them when we can reasonably expect the caller of our method to be able to recover.

```java
public void processFile(String fileName) {
    try {
        FileReader reader = new FileReader(new File(fileName));
        //process file
        reader.close();
    } catch(FileNotFoundExcepcion e) {
        System.out.println(“Didn't find the file' : “ + fileName);
    } catch(IOException e) {
        //Do something more
    }
}
```
If exceptions are not caught, it must be declared in the method that the exception can be thrown.
```java
public void processFile(String fileName) throws IOException {
    FileReader reader = new FileReader(new File(fileName));
    //process file
    reader.close();
}
```

---

## Unchecked Exceptions
Unchecked exceptions are usage errors that Java compiler _does not require us to handle_.

- These are exceptions that are produced by a programming error, or are not recoverable. 
- They should not be caught, and do not need to be caught. 
- They inherit from RuntimeException.

Examples:
- IndexOutOfBoundsException
- OperationNotSupportedException  
- InvalidArgumentException
- NullPointerException
- ClassCastException

---

## Errors

Errors represent serious and usually irrecoverable conditions like a library incompatibility, infinite recursion, or memory leaks.

It’d be weird for us to handle, instantiate or extend Errors. 

Usually, we want these to propagate all the way up.

Examples:
- StackOverflowError
- OutOfMemoryError

---

## Example

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

## Multiple catch blocks

- Multiple catches give us the chance to handle each exception differently.
- Remember to place them higher in the list of catches.
- When we’re catching IOException, all of its subclasses are also handled (FileNotFoundException).
- When we know that the way we handle errors is going to be the same, 
  you can catch multiple exceptions in the same block.

```java
public int getPlayerScore(String playerFile) {
    try (Scanner contents = new Scanner(new File(playerFile))) {
        return Integer.parseInt(contents.nextLine());
    } catch (IOException e) {
        logger.warn("Player file wouldn't load!", e);
        return 0;
    } catch (NumberFormatException e) {
        logger.warn("Player file was corrupted!", e);
        return 0;
    } catch (TimeoutException | ConnectionException e) {
        logger.warn("Failed to load score!", e);
        return 0;
    }
}
```

---

## Custom Exceptions

We can create Exceptions inside our domain in order to be able to handle it separately and to hold our own information, such as the name of the user of our app. 

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

- When reporting that a method throws an exception, it should be as general as possible, but within the framework being discussed. 
  i.e. IOException
- Do not catch Throwable 
- In a “layered” system, catch exceptions, log them, and rethrow them, wrapping the caught one with the new one. Onion style:
  1. Presentation 
  2. Application 
  3. Persistence


```java
catch(PersistenceException e) {
    throw new AplicationException(e);
}
```

```java
catch(AplicationException e) {
    throw new PresentationException(e);
}
```


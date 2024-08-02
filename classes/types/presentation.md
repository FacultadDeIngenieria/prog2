class: center, middle, inverse

# Types
Definition of types and examples in Python and Java

---


# Definition

```
A type is a description of a set of values and a set of
allowed operations on those values.
```

<div style="page-break-after: always;"></div>

---

# Integer Numbers

## Examples

- `10`
- `-5`
- `0`


---


# Integer Numbers
## Python

```python
# int
my_variable = 10
my_variable = -5
my_variable = 0
```

## Java

```java
// int
int myVariable = 10;
int myVariable = -5;
int myVariable = 0;
```

---

# Real Numbers

## Examples

- `3.14`
- `-0.5`
- `0.0`

---

# Real Numbers

## Python

```python
# float
my_variable = 3.14
my_variable = -0.5
my_variable = 0.0
```

## Java

```java
// double
double myVariable = 3.14;
double myVariable = -0.5;
double myVariable = 0.0;
```

---

# Strings

## Examples

- `"Hello"`
- `"World"`
- `"Hello, World!"`

---

# Strings

## Python

```python
# str
my_variable = "Hello"
my_variable = "World"
my_variable = "Hello, World!"
```

## Java

```java
// String
String myVariable = "Hello";
String myVariable = "World";
String myVariable = "Hello, World!";
```

---

# Booleans

## Examples

- `True`
- `False`

---

# Booleans

## Python

```python
# bool
my_variable = True
my_variable = False
```

## Java

```java
// boolean
boolean myVariable = true;
boolean myVariable = false;
```

---

# Lists

## Examples

- `[1, 2, 3]`
- `["a", "b", "c"]`
- `[True, False, True]`

---

# Lists

## Python

```python
# list
my_variable = [1, 2, 3]
my_variable = ["a", "b", "c"]
my_variable = [True, False, True]
```

## Java

```java
// Array
int[] myVariable = {1, 2, 3};
String[] myVariable = {"a", "b", "c"};
boolean[] myVariable = {true, false, true};

// List
List<Integer> myVariable = Arrays.asList(1, 2, 3);
List<String> myVariable = Arrays.asList("a", "b", "c");
List<Boolean> myVariable = Arrays.asList(true, false, true);
```

---

# Interpreter vs Compiler


![Interpreter vs Compiler](diff-compiler.jpeg)

---


# Interpreter vs Compiler

- A Compiler reads the source code and translates it to machine code for later execution.
- An interpreter reads the source code and executes it 'on the fly'.
- And.. oh yes.. there are 'semicompiled' languages that translate the code to an intermediate, machine neutral,
code (bytecode). i.e.: Java or C#


---

# Interpreter vs Compiler

Example: Python

```python
# my_script.py
print("Hello, World!")
```

```shell
$ python my_script.py
> hello, World!
```

---

# Interpreter vs Compiler

Example: Java

```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```shell
$ javac HelloWorld.java
$ java HelloWorld
> hello, World!
```

---

# Type Systems

- Static Typing
- Dynamic Typing


---

# Type Systems
## Static Typing

The types of the variables are known at compile time. So the compiler 
can verify that they are used consistently

---

# Type Systems
## Dynamic Typing

The types of the variables are known only at runtime. They are not tied to the
variables, so they can change depending on the current execution flow.

---

# Type Systems, Compilers and Interpreters

- Static Typing is usually associated with compiled languages

_They nearly always have static typing. Because machine codes have different instructions for different
types  . (i.e.: add vs fadd). So the compiler needs to know the type to translate it in an efficient way._

- Dynamic Typing is usually associated with interpreted languages

_In most of the cases they have dynamic typing because it's simpler to check the type of the variable 
while executing that having to do a full analysis before interpreting._

---

# Type Systems
## Pros and Cons

### Dynamic Typing
-  Code is more consice.
- It's simpler to write functions that work over different types
- OK for small, not critical code

### Static Typing
- Code is better documented, and easier to understand by others
- More errors detected earlier in development.
- IDEs can help you to detect functions and methods
- Fewer errors at runtime and in shipped code.
- Allows for compiler optimisation which yields faster code.

_we can compare java and python to see this_
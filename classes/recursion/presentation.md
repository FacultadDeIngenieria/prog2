class: center, middle, inverse

# Recursion

---

# Agenda

1. Basic Concept of Recursion
2. Dividing a problem
3. Identifying the Base Case and Recursive Case
4. Visualizing the Process
   * Execution Stack for Recursion
   * Call diagram
5. Common Problems
6. Practical Example
7. Recursion vs Iteration

.center[![Factorial]({{site.baseurl}}/classes/recursion/recursion_complete.png)]

---

# 1. Basic Concept of Recursion
   Recursion is a method where a function calls itself to solve a smaller problem of the same nature.
   
   - **Example:** Use a basic example such as calculating the factorial (`n!`), where `n! = n * (n-1)!` and `0! = 1`.

---
## Python example:
```python
def factorial(n):
    if n == 0:
        return 1 # Base case
    else:
        return n * factorial(n-1) # Recursive call

num = 5  # We could use an input here too!
print(f"The factorial of {num} is {factorial(num)}") # Should print 120
```
---

## Java example:
```java
public class Factorial {
    public static int factorial(int n) {
        if (n == 0) {
            return 1; // Base case
        }
        return n * factorial(n - 1); // Recursive call
    }

    public static void main(String[] args) {
        System.out.println(factorial(5)); // Should print 120
    }
}
```
---

# 2. Dividing a problem

- Problems (in life and also in computer science) can often seem big and scary
- The essence of thinking recursively goes like this:

    - Many problems are too complex to solve in one step. By dividing the problem into smaller pieces, each sub-problem becomes easier to manage and solve.
  
    - In recursion, each sub-problem is a smaller instance of the original problem. This self-similarity allows the same function to be applied repeatedly, reducing the need for multiple functions to solve similar problems.
  
    - Specifically, solving the same problem on a simplified or smaller input.
  
    - But if the solution to every smaller problem in a recursive algorithm depended on a solution to an even smaller algorithm
  
    - *What is going to happen?*

---

- It becomes clear that this process **would never end**
  .center[![Factorial]({{site.baseurl}}/classes/recursion/recursion_without_base_condition.jpg)]

---

# 3. Identifying the Base Case and Recursive Case
- So, to properly handle this recursive issue, a base case is always necessary, where a problem of sufficient simplicity can be solved by itself, without reliance on any other thing being dealt with.

.center[![Factorial]({{site.baseurl}}/classes/recursion/base_recursive_case.png)]

- **Base Case:** The importance of the base case is to avoid infinite recursions.
- **Recursive Case:** How the function approaches the base case with each recursive call.

---

# 4. Visualizing the Process

## a. Execution Stack for Recursion

The Execution Stack is a data structure where function calls are stored in the order they are invoked.
- **LIFO (Last In, First Out):** The Stack operates as LIFO, meaning the last element in is the first one out.


- **Step-by-Step in the Stack:**
  Following up with the factorial example: 
    - `factorial(3)` calls `factorial(2)` and so on until reaching the base case `factorial(0)`.
    - Then, the calls are resolved in reverse order.

```
Step 1:                Step 2:               Step 3:               Step 4:
|              |        |              |      |              |      | factorial(0) |
|              |        |              |      | factorial(1) |      | factorial(1) |
|              |        | factorial(2) |      | factorial(2) |      | factorial(2) |
| factorial(3) |        | factorial(3) |      | factorial(3) |      | factorial(3) |

```
---

# 4. Visualizing the Process
## b. Call diagram

.center[![Factorial]({{site.baseurl}}/classes/recursion/factorial.png)]

---
## 5. Common Problems
   - **Stack Overflow:** What happens if the base case is incorrectly defined or missing?
       - In recursion, each time a function calls itself, a new frame is added to the call stack. If the recursion is too deep or if the base case is missing or incorrect, the stack can grow too large, leading to a stack overflow error. 
   - **Efficiency:** Recursion can be elegant and straightforward, but it can also be inefficient, especially in terms of time and space complexity.
       - Each recursive call adds a frame to the call stack, consuming memory. Additionally, some recursive solutions may involve redundant calculations, leading to higher time complexity.

---
## 6. Practical Example
   - **Fibonacci:** Calculation of the nth Fibonacci number.

```java
public class Fibonacci {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n; // Base cases
        }
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive call
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(6)); // Should print 8
    }
}
```
---

## 7. Recursion vs Iteration
Think the algorithm to sum the first `n` natural numbers both recursively and iteratively, and how we can explain these approaches step by step.

## Problem
We want to calculate the sum of the first `n` natural numbers, i.e., `1 + 2 + 3 + ... + n`.

---

## Recursive Approach

```java
public class SumRecursive {
    public static int sum(int n) {
        if (n == 1) {
            return 1; // Base case
        }
        return n + sum(n - 1); // Recursive call
    }

    public static void main(String[] args) {
        int result = sum(5);
        System.out.println("Recursive Result: " + result);
    }
}
```

---
## Iterative Approach

```java
public class SumIterative {
    public static int sum(int n) {
        int total = 0;
        for (int i = 1; i <= n; i++) {
            total += i; // Iterative sum
        }
        return total;
    }

    public static void main(String[] args) {
        int result = sum(5);
        System.out.println("Iterative Result: " + result);
    }
}
```

---

## Comparison and Discussion

- **Efficiency:** The iterative approach generally uses less memory because it doesn’t need to stack recursive calls.
- **Use Cases:** 
    - Some problems are naturally recursive in their structure, meaning the solution directly follows a recursive pattern. Others can be broken down into smaller subproblems, each of which is a smaller instance of the original problem
    - Problems that involve repeating a process a fixed number of times or where each step is dependent only on the previous step are better suited to iteration.

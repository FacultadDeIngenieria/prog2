class: center, middle, inverse

# Introducción a la Programación I

Recursion

---

# Agenda

- Recursion

.center[![Factorial]({{site.baseurl}}/presentation/recursion/recursion_complete.png)]

---

# Helping Santa - Iteratively

- Have you ever wondered how Christmas presents are delivered? 
- Let's believe Santa Claus has a list of houses he loops through. 
- He goes to a house, drops off the presents, eats the cookies and milk, and moves on to the next house on the list. 
- Since this algorithm for delivering presents is based on an explicit loop construction, it is called an iterative algorithm.

.center[![Factorial]({{site.baseurl}}/presentation/recursion/santa_claus_it.webp)]

```python
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)
```
```
>>> deliver_presents_iteratively()
Delivering presents to Eric's house
Delivering presents to Kenny's house
Delivering presents to Kyle's house
Delivering presents to Stan's house
```

---

# Helping Santa - Recursively

- At his age, Santa shouldn’t have to deliver all the presents by himself
- Let's propose an algorithm with which he can divide the work of delivering presents among his elves:

1. Appoint an elf and give all the work to him
2. Assign titles and responsibilities to the elves based on the number of houses for which they are responsible:
  - Greater than 1 (> 1): he is a manager and can appoint two elves and divide his work among them
  - Equal to 1 (= 1): he is a worker and has to deliver the presents to the house assigned to him

.center[![Factorial]({{site.baseurl}}/presentation/recursion/santa_claus_rec.png)]

---

# Recursion - Dividing a problem

- Problems (in life and also in computer science) can often seem big and scary
- The essence of thinking recursively goes like this:
  - You have one problem, so brake it down into smaller forms of itself, to find a more efficient solution
  - One of the aspects of using recursion is that a major part of the solution lies in solving this “smaller” version of the problem 
  - Specifically, solving the same one on a simplified or smaller input.
  - But if the solution to every smaller problem in a recursive algorithm depended on a solution to an even smaller algorithm
  - *What is going to happen?*

---

# Recursion - Base / recursive case

- It becomes clear that this process **would never end**
- So, to properly handle this recursive issue, a base case is always necessary, where a problem of sufficient simplicity can be solved by itself, without reliance on any other thing being dealt with.

.center[![Factorial]({{site.baseurl}}/presentation/recursion/base_recursive_case.png)]

- This Base Case is also known as the first part of the function and is what prevents the algorithm from running forever. 
- The second part is more interesting and is known as the Recursive Step.

---

# Helping Santa - Recursively

```python
houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work 
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
```

```
>>> deliver_presents_recursively(houses)
Delivering presents to Eric's house
Delivering presents to Kenny's house
Delivering presents to Kyle's house
Delivering presents to Stan's house
``` 

---

# A little bit like the movie Inception

.center[![Factorial]({{site.baseurl}}/presentation/recursion/inception.jpg)]

---

# Recursion

- Programming technique in which a function calls itself to solve a problem.
- Such methods are called recursive functions.
- Many problems can be solved only with recursion.
- Others can be solved better with it.

.center[![Factorial]({{site.baseurl}}/presentation/recursion/fixing_problems.webp)]

---

# Recursion - Example

- Example: integer factorial calculation.
    - 0! = 1
    - 1! = 1 \* 0!
    - 2! = 2 \* 1! \* 0!
    - 3! = 3 \* 2 \* 1! \* 0!
    - ...

---

# Recursion - Example

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = 3  # We could use an input here too!
print(f"The factorial of {num} is {factorial(num)}")
```

---

# Recursion - Example

- To show it graphically:

.center[![Factorial]({{site.baseurl}}/presentation/recursion/factorial.png)]

---
# Maintaining State

When dealing with recursive functions, keep in mind that each recursive call has its own execution context, so to maintain state during recursion you have to either:
 - Thread the state through each recursive call so that the current state is part of the current call’s execution context
Keep the state in global scope
 - A demonstration should make things clearer. Let’s calculate 1 + 2 + 3 ⋅⋅⋅⋅ + 10 using recursion. The state that we have to maintain is (current number we are adding, accumulated sum till now).

Here’s how you do that by threading it through each recursive call (i.e. passing the updated current state to each recursive call as arguments):
```python
def sum_recursive(current_number, accumulated_sum):
    # Base case: return the final state
    if current_number == 11:
        return accumulated_sum
    # Recursive case: thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)
```
---
# Maintaining State

Here’s how you maintain the state by keeping it in global scope:
```python
# Global mutable state
current_number = 1
accumulated_sum = 0

def sum_recursive():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()
```
It is better threading the state through each recursive call.

<!-- --- -->
<!-- # Resources -->
<!-- - [Thinking Recursively in Python
](https://realpython.com/python-thinking-recursively/) #Same as this presentation... -->
<!-- - [Why Inception reminds us of recursion](https://wewrite.taleas.io/2018/11/14/why-inception-reminds-us-of-recursion/)  # Not available anymore -->

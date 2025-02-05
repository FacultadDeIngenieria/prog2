## Introduction

> 1.Write a function which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

**Hints** : Consider use the `range(begin, end)` 

---
> 2.With a given integral number n, write a function to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).

Example
```python
> dictionary(8)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```
---

> 3.Write a function which takes 2 digits, n, m as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
```python
> matrix(3, 5)
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
```

---

> 4.Write a function that accepts a sequence of whitespace separated words as input and returns the words after removing all duplicate words

```python
> remove_duplicates(["hello",  "world",  "again", "world", "hello"])
["hello",  "world",  "again"]
```

---

> 5.Write a function, which will find all such numbers between `n` and `m` (both included) such that each digit of the number is an even number.

---

> 6.Write a function that accepts a sentence and calculate the number of letters and digits, returning them as a tuple.

```python
count_letters_and_digits("hello world! 123")
(10, 3)
```
---

> 7.Write a function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

```python
> f(9)
11106
```

---
> 8.Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

```python
> square_odds(1,2,3,4,5,6,7,8,9)
1,3,5,7,9
```
---

> 9.A website requires the users to input username and password to register. Write a function to check the validity of password input by users.
Following are the criteria for checking the password:

* At least 1 letter between [a-z]
* At least 1 number between [0-9]
* At least 1 letter between [A-Z]
* At least 1 character from [$#@]
* Minimum length of password: `6`
* Maximum length of password: `12`

```python
> check_password("ABd1234@1")
True
> check_password("2We3345")
False
```
---

> 10.A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
> Create a function that given a list of tuples `[(direction, steps)]` returns the distance moved. 


```python
> distance([("UP", 5), ("LEFT", 2), ("DOWN", 2), ("RIGHT", 6)])
5
```
---

> 11.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

```python
> c = Circle(2)
c.area()
12.5664
```

---

> 12.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

```python
> r = Rectangle(2, 4)
r.area()
8
```
---

> 13.Add checks for negative values to exercises 11 & 12, (raise an exception)

---

> 14.Write a function to generate all sentences given a list of subject a list of verbs and a list of objects.
>

```python
> sentences(["I", "You"], ["Play", "Love"], ["Hockey","Football"])
["I Play Hockey", "I Play Football", "I Love Hockey", .....]
```

---

> 15.By using list comprehension, please write a function to print the list after removing the elements in even positions

```python
> remove_evens([12,24,35,70,88,120,155])
[12,35,88,155]
```

---

> 16.By using list comprehension, please write a function generate a `n x m x o` 3D array with each element being 0.

```python
> array3d(3, 3, 2)
[[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]
```
---

> 17.Write a function to solve a classic ancient Chinese puzzle: 
> We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
> Return `None` if no solutions are found
**Hint** Iterate all possible solutions.

```python
> solve(35, 94)
(23, 12)
> solve(35, 48)
None
> solve(23, 50)
(21, 2)
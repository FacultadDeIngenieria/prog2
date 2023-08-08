# Matrix Operations

## Instructions

You have to implement some operations over **Matrices**

### Part 1 - Matrix multiplication 

Given 2 Matrices represented as `List[List[float]]` You have to multiply them and return the result.

If **A** has dimensions **m × n** and **B** has dimensions **n x p**.

Then the product **C = A x B** has dimensions **m x p**.

Where C<sub>i,j</sub> = Sum of each element of the row A<sub>i</sub> by each element of the column B<sub>j</sub>.

![See](matrixmultiplication.jpeg)

Example 1:

```python

Matrix([[1, 2, 3],
        [4, 5, 6]]).multiply(Matrix([[1, 2],[3, 4],[5, 6]]))
```

Should return:
```python
[[22 , 28],
 [49, 64]]
```
Example 2:
```python
matrix = Matrix([[1, 2, 3],
                [4, 5, 6]])
matrix.dimensions()

```
should return

```python
[2,3]
```      
          

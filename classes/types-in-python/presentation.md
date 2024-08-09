class: center, middle, inverse

# Types in python
Definition of types and examples in Python with MyPy

---

# Typing variables

## Int

```python
# int
my_variable: int = 10
my_variable: int = -5
```

---

# Typing variables

## Float

```python
# float
my_variable: float = 3.14
my_variable: float = -0.5
```

---

# Typing variables

## String

```python
# str
my_variable: str = "Hello"
my_variable: str = 'World'
```

---

# Typing variables

## Boolean

```python
# bool
my_variable: bool = True
my_variable: bool = False
```

---

# Typing variables

## List

```python
# list
import List from typing
my_variable: List[int] = [1, 2, 3]
my_variable: List[int] = ["Hello", "World"]
```


---

# Typing variables

## Tuple

```python
# tuple
import Tuple from typing
my_variable: Tuple[int, str] = (1, "Hello")
my_variable: Tuple[int, str] = (1, 2)
```

---

# Typing variables

## Dict

```python
# dict
import Dict from typing
my_variable: Dict[str, int] = {"key": 1}
my_variable: Dict[int, str] = {1: "key"}
```

---

# Typing variables

## Set

```python
# set
import Set from typing
my_variable: Set[int] = {1, 2, 3}
my_variable: Set[str] = {"Hello", "World"}
```


# Typing variables

## How to use mypy

```bash
mypy my_file.py
```

---

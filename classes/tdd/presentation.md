class: center, middle, inverse


# TDD
Test-Driven Development (TDD) is a software development approach where tests are written
before the code that needs to be implemented. It is a practice derived from Extreme Programming (XP)
and is widely used in Agile methodologies.

TDD is independent of the programming language. We will use Java and Python in this class as examples for it.

---

# TDD in a nutshell

1. Write a test that fails
2. Write the minimum code to pass the test
3. Refactor the code
4. Repeat

---

# Why TDD?

- **Design**: TDD helps to design the software in small increments.
- **Quality**: TDD helps to ensure that the code is working as expected.
- **Documentation**: The tests are a form of documentation.
- **Confidence**: TDD gives confidence to the developers to make changes.
- **Feedback**: TDD gives immediate feedback on the code.
- **Productivity**: TDD helps to write code faster.
- **Bug detection**: TDD helps to detect bugs early in the development process.

---

# TDD in Python

In Python, we can use the `unittest` module to write tests. The `unittest` module is part of the Python standard library.

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()
```

---

# TDD in Java

In Java, we can use JUnit to write tests. JUnit is a popular testing framework for Java.

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyTest {

    @Test
    public void testAdd() {
        assertEquals(4, 2 + 2);
    }

    @Test
    public void testSubtract() {
        assertEquals(0, 2 - 2);
    }
}
```

---

# TDD in practice

## Example: Leap year

Let's implement a simple leap year using TDD.

1. Write a failing test

---

# WAIT
What tests should we write?

---

# TDD in practice

## Example: Leap year

Specifications:
    
    - A year is a leap year if it is divisible by 4
    - A year is not a leap year if it is divisible by 100
    - A year is a leap year if it is divisible by 400
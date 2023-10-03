# Simple xor encryption

## Instructions
 
The **exclusive or** (operator `^`) has the property that if it is applied twice you get the original value back

So for example:
```python
> 11 ^ 3
8
> 8 ^ 3
11
```

Using this property you can develop a simple encryption algorithm.

### 1. Create a function to encrypt a string using a single char as a key 

The char has to be 'xor-ed' to each of the string chars

So for example:
```python
> encrypt_with_char("Hello", "x")
"0\x1d\x14\x14\x17"
> encrypt_with_char("0\x1d\x14\x14\x17", "x")
"Hello"
```

### 2. Create a function to encrypt a string based on a string as the key

You should use each character of the key in sequence, repeating it if necessary

So to encrypt the string `"Hello World"` with the key `"secret"`
you should repeat the key as this: `secretsecre`

```python
'H' ^ 's'
'e' ^ 'e'
'l' ^ 'c'
'l' ^ 'r'
'o' ^ 'e'
' ' ^ 't'
'W' ^ 's'
'o' ^ 'e'
'r' ^ 'c'
'l' ^ 'r'
'd' ^ 'e'
```

For example:
```python
> e = encrypt("What a wonderful World!", "badkey")
> e
"5\t\x05\x1fE\x18B\x16\x0b\x05\x01\x1c\x10\x07\x11\x07E.\r\x13\x08\x0fD"
> encrypt("e", "badkey")
"What a wonderful World!"
```

## How to xor characters ?

The xor operator works with `int`s. 

So you can do things like: `11 ^ 3` that gives the result `8`.

(Notice `11` is `1011` in binary and 3 is `0011`, so `0111` xor `0011` is `0100` -> 8)

But the xor operator does **not** work with characters.

So you need to convert the character to its code (an `int`) using the `ord` function:

For example:
```python
> ord('A')
65
> ord('B')
66
> ord('a')
97
```

Then after doing the `xor` you get an `int` to convert it back to a char you use the `chr` function:

```python
> chr(65)
'A'
> chr(97)
'a'
```
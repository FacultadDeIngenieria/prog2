---
title: Generics
layout: practice
permalink: /exercises/generics
---

## Ejercicio 1
A stack is a container that stores objects in a manner indicated by its name —
in a vertical stack where only the object at the top of the stack is accessible. It
works rather like a sprung stack of plates in a cafeteria. Only the top plate is
at counter level and, therefore, is the only one you can access. When you add
a plate to the stack, the existing plates are pushed down so the new plate is
now the one that you can access. Define a generic Stack<> type with a
method push() that adds the object that is passed as an argument to the top of
the stack, and with a method pop() that removes and returns the object that is
currently at the top of the stack. The pop() method should return null when
the stack is empty. Demonstrate the operation of your Stack<>
implementation by storing and retrieving 10 strings and 10 Double objects in
stacks of a suit- able type.

## Ejercicio 2
Implement and demonstrate a listAll() method in the Stack<> class definition that will list the objects in the stack.

## Ejercicio 3
Modify your Stack<> type to make it serializable. 
Demonstrate that this is the case by creating a Stack<String> object and adding 10 strings to it, 
then serializing and deserializing the Stack<String> object, and listing the contents of the deserialized stack.
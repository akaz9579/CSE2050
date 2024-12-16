# Pratice: Exam 1 Coding

You will have to hand-write code during lecture for the summative coding assessments in this course (the coding exams). Below are some example problems from each module.

## Mod 01 - Python Foundations

Write a function `has_same_letters(word1, word2)` that returns `True` if every letter in `word1` also appears in `word2` and vice-versa. Note that they do not have to have the same *count* of each letter, as long as they have the same letters.

### Examples

```python
>>> has_same_letters("reheat", "theater")
True
>>> has_same_letters("reheat", "there")
False
```

### Work
Code:
```python
def has_same_letters(word1, word2):
    return set(word1) == set(word2)
```

Running time: $O(max(n1, n2))$ where `n1` and `n2` are the lengths of `word1` and `word2`, respectively; or $O(n1 + n2)$ where `n1` and `n2` are the lengths of `word1` and `word2`, respectively.

\pagebreak

## Mod 02 - Object-Oriented Programming

Write code to implement the following class diagram. Make sure to add `init` methods with the appropriate parameters where appropriate.

### Examples

![Class diagram to be implemented. Note that `name`, `sound`, `species`, and `is_good_boy` are instance variables.](./images/AnimalClassDiagram.png)

### Work

Code: 
```python
class Animal:
    def __init__(self, name, sound, species):
        self.name = name
        self.sound = sound
        self.species = species

class Dog(Animal):
    def __init__(self, name, sound, species, is_good_boy):
        super().__init__(name, sound, species)
        self.is_good_boy = is_good_boy

class Cat(Animal):
    pass
```

\pagebreak

## Mod 03 - Running Time Analysis and Test-Driven Development

Write a function `time_func(func, *args)` that takes as input a function and a tuple of arguments, runs that function 10 times, and returns the *minimum time requried* for function to complete.

### Examples
```python
>>> def double(x):
        return x*2

>>> time_func(double, ('hello'))
0.00005
```

### Work

Code:
```python
import time
def time_func(func, *args):
    t_min = float('inf')

    for _ in range(10):
        start = time.time()
        func(*args)
        t_trial = time.time() - start
        
        if t_trial < t_min:
            t_min = t_trial

    return t_min
```

Write a suite of unittests for the Stack ADT. You can assume the stack provides typical methods for `push`, `pop`, `len`, and `peek`, and that it should raise an `IndexError` if you try to pop from an empty stack.

```python
from stack import Stack
import unittest

class TestStack(unittest.TestCase):
    def test_init(self):
        s = Stack()
        self.assertEqual(len(s), 0)
    
    def test_push_five(self):
        s = Stack()
        n = 5

        for i in range(n):
            s.push(i)
            self.assertEqual(len(s), i)
            self.assertEqual(s.peek(), i)

    def test_pushfive_popfive(self):
        s = Stack()
        n = 5

        for i in range(n):
            s.push(i)

        for i in range(n):
            self.assertEqual(len(s), n-i)
            self.assertEqual(s.peek(), n-1-i)
            self.assertEqual(s.pop(), n-1-i)

    def test_popempty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

unittest.main()
```

\pagebreak

# Mod 04 - Linear ADTs and Data Structures

Implement `add_last` in the `LinkedList` below. Note that you should *only* add code to the method `add_last` - do not create any other methods or add any other attributes to the class.

### Work

Code:
```python
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def __len__(self):
        return self._len

    def add_last(self, data):
        """Your work here"""
        if len(self) == 0:
            self._head = Node(data)
        
        else:
            node = self._head
            while node.link is not None:
                node = node.link
            
            node.link = Node(data)
        
        self._len += 1
```

Running Time: $O(n)$
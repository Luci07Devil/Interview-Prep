### Magic Methods
    Certainly! In Python, **magic methods** (also known as **dunder methods**) are special methods that start and end with double underscores (`__`). These methods are not meant to be directly invoked by you; instead, they are called internally by the class in response to certain actions. Here are some common magic methods in Python:

1. `__init__(self, ...)`: The constructor method, called when an object is created.
2. `__del__(self)`: The destructor method, called when an object is about to be destroyed.
3. `__call__(self, ...)`: Allows an object to be called like a function.
4. `__str__(self)`: Returns a human-readable string representation of the object (used by `str()`).
5. `__repr__(self)`: Returns an unambiguous string representation of the object (used by `repr()`).
6. `__len__(self)`: Returns the length of the object (used by `len()`).
7. `__getitem__(self, key)`: Enables indexing (used by square brackets `[]`).
8. `__setitem__(self, key, value)`: Enables assignment to an index (used by square brackets `[]`).
9. `__iter__(self)`: Allows iteration over the object (used by `for` loops).
10. `__next__(self)`: Used in conjunction with `__iter__` for custom iterators.
11. `__add__(self, other)`: Defines behavior for the `+` operator.
12. `__sub__(self, other)`: Defines behavior for the `-` operator.
13. `__mul__(self, other)`: Defines behavior for the `*` operator.
14. `__divmod__(self, other)`: Defines behavior for the `//` operator.
15. `__eq__(self, other)`: Defines behavior for equality comparison (`==`).### Magic Methods
    Certainly! In Python, **magic methods** (also known as **dunder methods**) are special methods that start and end with double underscores (`__`). These methods are not meant to be directly invoked by you; instead, they are called internally by the class in response to certain actions. Here are some common magic methods in Python:

    1. `__init__(self, ...)`: The constructor method, called when an object is created.
    2. `__del__(self)`: The destructor method, called when an object is about to be destroyed.
    3. `__call__(self, ...)`: Allows an object to be called like a function.
    4. `__str__(self)`: Returns a human-readable string representation of the object (used by `str()`).
    5. `__repr__(self)`: Returns an unambiguous string representation of the object (used by `repr()`).
    6. `__len__(self)`: Returns the length of the object (used by `len()`).
    7. `__getitem__(self, key)`: Enables indexing (used by square brackets `[]`).
    8. `__setitem__(self, key, value)`: Enables assignment to an index (used by square brackets `[]`).
    9. `__iter__(self)`: Allows iteration over the object (used by `for` loops).
    10. `__next__(self)`: Used in conjunction with `__iter__` for custom iterators.
    11. `__add__(self, other)`: Defines behavior for the `+` operator.
    12. `__sub__(self, other)`: Defines behavior for the `-` operator.
    13. `__mul__(self, other)`: Defines behavior for the `*` operator.
    14. `__divmod__(self, other)`: Defines behavior for the `//` operator.
    15. `__eq__(self, other)`: Defines behavior for equality comparison (`==`).
    16. `__ne__(self, other)`: Defines behavior for inequality comparison (`!=`).
    17. `__lt__(self, other)`: Defines behavior for less than comparison (`<`).
    18. `__le__(self, other)`: Defines behavior for less than or equal comparison (`<=`).
    19. `__gt__(self, other)`: Defines behavior for greater than comparison (`>`).
    20. `__ge__(self, other)`: Defines behavior for greater than or equal comparison (`>=`).

	To explore the magic methods inherited by a specific class, you can use the 'dir()' function.
	For instance, calling `dir(int)` will list all the attributes and methods defined in the `int` class.

16. `__ne__(self, other)`: Defines behavior for inequality comparison (`!=`).
17. `__lt__(self, other)`: Defines behavior for less than comparison (`<`).
18. `__le__(self, other)`: Defines behavior for less than or equal comparison (`<=`).
19. `__gt__(self, other)`: Defines behavior for greater than comparison (`>`).
20. `__ge__(self, other)`: Defines behavior for greater than or equal comparison (`>=`).

These are just a few examples, and there are many more magic methods available. To explore the magic methods inherited by a specific class, you can use the `dir()` function. For instance, calling `dir(int)` will list all the attributes and methods defined in the `int` class. Similarly, other programming languages like PHP also have their own set of magic methods.

Feel free to ask if you'd like more information about any specific magic method! 😊

Source: Conversation with Copilot, 6/2/2024
(1) Magic or Dunder Methods in Python - TutorialsTeacher.com. https://www.tutorialsteacher.com/python/magic-methods-in-python.
(2) PHP: Magic Methods - Manual. https://www.php.net/manual/en/language.oop5.magic.php.
(3) The Magic Methods in Python - AskPython. https://www.askpython.com/python/oops/magic-methods.
(4) Python Dunder Methods Cheat Sheet - Finxter. https://blog.finxter.com/python-dunder-methods-cheat-sheet/.

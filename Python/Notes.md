### Magic Methods
* Certainly! In Python, **magic methods** (also known as **dunder methods**) are special methods that start and end with double underscores (`__`).
* These methods are not meant to be directly invoked by you; 
* Instead, they are called internally by the class in response to certain actions. 

Here are some common magic methods in Python:

* `__init__(self, ...)`: The constructor method, called when an object is created.
* `__del__(self)`: The destructor method, called when an object is about to be destroyed.
* `__call__(self, ...)`: Allows an object to be called like a function.
* `__str__(self)`: Returns a human-readable string representation of the object (used by `str()`).
* `__repr__(self)`: Returns an unambiguous string representation of the object (used by `repr()`).
* `__len__(self)`: Returns the length of the object (used by `len()`).
* `__getitem__(self, key)`: Enables indexing (used by square brackets `[]`).
* `__setitem__(self, key, value)`: Enables assignment to an index (used by square brackets `[]`).
* `__iter__(self)`: Allows iteration over the object (used by `for` loops).
* `__next__(self)`: Used in conjunction with `__iter__` for custom iterators.
* `__add__(self, other)`: Defines behavior for the `+` operator.
* `__sub__(self, other)`: Defines behavior for the `-` operator.
* `__mul__(self, other)`: Defines behavior for the `*` operator.
* `__divmod__(self, other)`: Defines behavior for the `//` operator.
* `__eq__(self, other)`: Defines behavior for equality comparison (`==`).
* `__ne__(self, other)`: Defines behavior for inequality comparison (`!=`).
* `__lt__(self, other)`: Defines behavior for less than comparison (`<`).
* `__le__(self, other)`: Defines behavior for less than or equal comparison (`<=`).
* `__gt__(self, other)`: Defines behavior for greater than comparison (`>`).
* `__ge__(self, other)`: Defines behavior for greater than or equal comparison (`>=`).

To explore the magic methods inherited by a specific class, you can use the 'dir()' function.
For instance, calling `dir(int)` will list all the attributes and methods defined in the `int` class.

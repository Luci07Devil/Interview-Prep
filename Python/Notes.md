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

### Built-in Exceptions in Python

In Python, all exceptions must be instances of a class that derives from `BaseException`. Below are some of the commonly used built-in exceptions:

1. **`BaseException`**: The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.
2. **`SystemExit`**: Raised when the `sys.exit()` function is called.
3. **`KeyboardInterrupt`**: Raised when the user interrupts the execution (usually by pressing Ctrl+C).
4. **`GeneratorExit`**: Raised when a generator or coroutine is closed.
5. **`Exception`**: The base class for all non-system-exiting exceptions. User-defined exceptions should inherit from this class.
6. **`StopIteration`**: Raised by the `next()` function to signal the end of an iterator.
7. **`StopAsyncIteration`**: Raised by asynchronous iterators to signal the end of an iteration.
8. **`ArithmeticError`**: The base class for arithmetic-related exceptions.
    - **`ZeroDivisionError`**: Raised when dividing by zero.
    - **`FloatingPointError`**: Raised for floating-point arithmetic errors.
    - **`OverflowError`**: Raised when an arithmetic operation exceeds the limits of the data type.
9. **`AssertionError`**: Raised when an `assert` statement fails.
10. **`AttributeError`**: Raised when an attribute reference or assignment fails.
11. **`BufferError`**: Raised when a buffer-related operation fails.
12. **`LookupError`**: The base class for indexing and key-related exceptions.
    - **`IndexError`**: Raised when an index is out of range.
    - **`KeyError`**: Raised when a dictionary key is not found.
13. **`MemoryError`**: Raised when an operation runs out of memory.
14. **`NameError`**: Raised when a local or global name is not found.
15. **`OSError`**: The base class for operating system-related exceptions.
    - **`FileNotFoundError`**: Raised when a file or directory is not found.
    - **`PermissionError`**: Raised when permission is denied.
16. **`TypeError`**: Raised when an operation or function is applied to an object of inappropriate type.
17. **`ValueError`**: Raised when an operation or function receives an argument of the correct type but an inappropriate value.
18. **`RuntimeError`**: The base class for runtime-related exceptions.
    - **`RecursionError`**: Raised when maximum recursion depth is exceeded.
19. **`ImportError`**: Raised when an import statement fails.
20. **`ModuleNotFoundError`**: Raised when a module is not found.
21. **`SyntaxError`**: Raised when there is a syntax error in the code.
22. **`IndentationError`**: Raised when indentation is incorrect.
23. **`TabError`**: Raised when indentation contains mixed tabs and spaces.
24. **`SystemError`**: Raised when an internal error occurs in the Python interpreter.
25. **`SystemWarning`**: Base class for warnings related to the Python interpreter.
26. **`UserWarning`**: Base class for user-defined warnings.
27. **`DeprecationWarning`**: Base class for warnings about deprecated features.
28. **`PendingDeprecationWarning`**: Base class for warnings about features that will be deprecated in the future.
29. **`RuntimeWarning`**: Base class for runtime-related warnings.

Remember that these are just some of the built-in exceptions. You can find more details in the official Python documentation.


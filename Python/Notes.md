### Magic Methods (Dunder Methods)

In Python, special methods are also called magic methods or dunder methods.
These methods have names that start and end with double underscores (`__`).
They provide custom behavior for various operations and are automatically called by Python.
These methods are not meant to be directly invoked by you; 
Instead, they are called internally by the class in response to certain actions. 

Here are some commonly used magic methods:

1. **`__init__()`**: Initializes an object.
2. **`__str__()`**: Provides a user-friendly string representation of an object.
3. **`__repr__()`**: Provides a developer-friendly string representation of an object.
4. **`__add__()`**: Handles addition (`+`) between objects.
5. **`__sub__()`**: Handles subtraction (`-`) between objects.
6. **`__mul__()`**: Handles multiplication (`*`) between objects.
7. **`__divmod__()`**: Handles division and remainder (`//`) between objects.
8. **`__eq__()`**: Handles equality (`==`) comparison.
9. **`__lt__()`**: Handles less than (`<`) comparison.
10. **`__gt__()`**: Handles greater than (`>`) comparison.
11. **`__len__()`**: Returns the length of an object (used for sequences).
12. **`__getitem__()`**: Retrieves an item from an object (used for indexing).
13. **`__setitem__()`**: Sets an item in an object (used for assignment).
14. **`__delitem__()`**: Deletes an item from an object.
15. **`__iter__()`**: Creates an iterator for an object.
16. **`__next__()`**: Retrieves the next value from an iterator.
17. **`__enter__()`** and **`__exit__()`**: Used for context management (with statements).

There are many more magic methods available. For a complete reference, check the official Python documentation.
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


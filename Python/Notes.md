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

### Inheritance

There are different types of inheritance in Python:

1. **Single Inheritance**:
   - In single inheritance, a derived class inherits properties from a single parent class. This enables code reusability and allows you to add new features to existing code.
   - Example:
     ```python
     class Parent:
         def func1(self):
             print("This function is in the parent class.")

     class Child(Parent):
         def func2(self):
             print("This function is in the child class.")

     # Usage
     obj = Child()
     obj.func1()  # Output: This function is in the parent class.
     obj.func2()  # Output: This function is in the child class.
     ```

2. **Multiple Inheritance**:
   - In multiple inheritance, a class can be derived from more than one base class. All features of the base classes are inherited into the derived class.
   - Example:
     ```python
     class Mother:
         def mother(self):
             print(self.mothername)

     class Father:
         def father(self):
             print(self.fathername)

     class Son(Mother, Father):
         def parents(self):
             print("Father:", self.fathername)
             print("Mother:", self.mothername)

     s1 = Son()
     s1.fathername = "RAM"
     s1.mothername = "SITA"
     s1.parents()  # Output: Father: RAM, Mother: SITA
     ```

3. **Multilevel Inheritance**:
   - In multilevel inheritance, features of the base class and the derived class are further inherited into a new derived class. It's similar to a relationship representing a child and a grandfather.
   - Example:
     ```python
     class Grandfather:
         def __init__(self, grandfathername):
             self.grandfathername = grandfathername

     class Father(Grandfather):
         def __init__(self, fathername, grandfathername):
             self.fathername = fathername
             Grandfather.__init__(self, grandfathername)

     class Son(Father):
         def __init__(self, sonname, fathername, grandfathername):
             self.sonname = sonname
             Father.__init__(self, fathername, grandfathername)

         def print_name(self):
             print("Grandfather name:", self.grandfathername)
             print("Father name:", self.fathername)
             print("Son name:", self.sonname)

     s1 = Son("Prince", "Rampal", "Lal mani")
     print(s1.grandfathername)  # Output: Lal mani
     s1.print_name()
     # Output:
     # Grandfather name: Lal mani
     # Father name: Rampal
     # Son name: Prince
     ```

4. **Hierarchical Inheritance**:
   - In hierarchical inheritance, more than one derived class is created from a single base class. Each child class inherits from the same parent class.
   - Example:
     ```python
     class Parent:
         def func1(self):
             print("This function is in the parent class.")

     class Child1(Parent):
         def func2(self):
             print("This function is in child 1.")

     class Child2(Parent):
         def func3(self):
             print("This function is in child 2.")

     object1 = Child1()
     object2 = Child2()
     object1.func1()  # Output: This function is in the parent class.
     object1.func2()  # Output: This function is in child 1.
     object2.func1()  # Output: This function is in the parent class.
     object2.func3()  # Output: This function is in child 2.
     ```
   
5. **Hybrid Inheritance**:
   - Hybrid inheritance is a combination of any of the above types. It involves multiple inheritance patterns in a single program.

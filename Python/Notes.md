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

### Types of Methods in Python
There are **three main types of methods** that you can use in your classes.

1. **Instance Methods**:
   - These methods are associated with an **object** of a class.
   - They can **access and modify instance-specific data** (attributes) within the object.
   - The first parameter of an instance method is **`self`**, which refers to the instance itself.
   - Example:
     ```python
     class Student:
         def __init__(self, name, age):
             self.name = name
             self.age = age

         def birthday(self):
             self.age += 1
             return f"{self.name} has now turned {self.age}.\n" \
                    f"{self.no_of_students - 1} students of his class have sent Birthday gifts."

     student1 = Student("Chan", 13)
     print(student1.birthday())
     ```
     Output:
     ```
     Chan has now turned 14.
     9 students of his class have sent Birthday gifts.
     ```

2. **Class Methods**:
   - These methods are **associated with the class itself**, rather than individual instances.
   - They can **access and modify class-level data** (class attributes).
   - The first parameter of a class method is **`cls`**, which refers to the class.
   - Example:
     ```python
     class Student:
         no_of_students = 10

         @classmethod
         def get_total_students(cls):
             return cls.no_of_students

     print(Student.get_total_students())  # Output: 10
     ```

3. **Static Methods**:
   - These methods are **not tied to any specific instance or class**.
   - They are like regular functions but are defined inside a class for organization.
   - They **don't have access to instance-specific or class-level data**.
   - Example:
     ```python
     class MathUtils:
         @staticmethod
         def add(a, b):
             return a + b

     result = MathUtils.add(5, 3)
     print(f"Result of addition: {result}")  # Output: Result of addition: 8
     ```

## Abstraction in Python

Abstraction involves separating the essential features or behaviors of an object from the specific implementation details.
It provides a high-level view of an object, focusing on what it does rather than how it does it.
In Python, abstraction is achieved through the use of **abstract classes** and **interfaces**.

1. **Abstract Classes**:
   - An abstract class can be considered a blueprint for other classes.
   - It defines a set of methods that must be implemented by any child classes derived from the abstract class.
   - Abstract classes cannot be instantiated directly; they serve as a common interface for related classes.
   - Example of an abstract class with an abstract method:
     ```python
     from abc import ABC, abstractmethod

     class Polygon(ABC):
         @abstractmethod
         def noofsides(self):
             pass
     ```

2. **Abstract Methods**:
   - An abstract method is a method declared in an abstract class but without an implementation.
   - Subclasses must provide concrete implementations for abstract methods.
   - Example of a subclass implementing the abstract method:
     ```python
     class Triangle(Polygon):
         def noofsides(self):
             print("I have 3 sides")
     ```

3. **Data Abstraction**:
   - Data abstraction hides complex implementation details and shows only essential information to users.
   - It allows us to define common attributes and behaviors that can be shared among multiple classes.
   - Example of data abstraction using an abstract base class:
     ```python
     class Animal(ABC):
         @abstractmethod
         def move(self):
             pass

     class Dog(Animal):
         def move(self):
             print("Dog walks on four legs")

     class Bird(Animal):
         def move(self):
             print("Bird flies in the sky")
     ```

4. **Benefits of Abstraction**:
   - Promotes code organization and modularity.
   - Reduces redundancy by defining common functionality in one place.
   - Provides a clear structure for derived classes to follow.

### Access Modifiers in Python

Access modifiers determine the accessibility of class members (variables and methods) from outside the class. 
Access modifiers ontrol the visibility of data members and methods within a class.
Python uses underscores (`_`) to specify access control for specific data members and member functions. 
Here are the three types of access modifiers:

1. **Public Access Modifier**:
   - Members declared as public are easily accessible from any part of the program.
   - By default, all data members and member functions of a class are public.
   - Example:
     ```python
     class Geek:
         def __init__(self, name, age):
             self.geekName = name  # Public data member
             self.geekAge = age

         def displayAge(self):  # Public member function
             print("Age:", self.geekAge)

     obj = Geek("R2J", 20)
     print("Name:", obj.geekName)
     obj.displayAge()
     ```
   - Output:
     ```
     Name: R2J
     Age: 20
     ```

2. **Protected Access Modifier**:
   - Members declared as protected are accessible only within the class and its subclasses (derived classes).
   - To declare a protected data member, prefix it with a single underscore (`_`).
   - Example:
     ```python
     class Student:
         def __init__(self, name, roll, branch):
             self._name = name  # Protected data member
             self._roll = roll
             self._branch = branch

         def _displayRollAndBranch(self):  # Protected member function
             print("Roll:", self._roll)
             print("Branch:", self._branch)

     class Geek(Student):
         def displayDetails(self):
             print("Name:", self._name)
             self._displayRollAndBranch()

     obj = Geek("R2J", 1706256, "Information Technology")
     obj.displayDetails()
     ```
   - Output:
     ```
     Name: R2J
     Roll: 1706256
     Branch: Information Technology
     ```

3. **Private Access Modifier**:
   - Members declared as private are accessible only within the class.
   - To declare a private data member, prefix it with a double underscore (`__`).
   - Note that Python name mangling changes the name of private members to `_classname__member`.
   - Example:
     ```python
     class BankAccount:
         def __init__(self, balance):
             self.__balance = balance  # Private data member

         def get_balance(self):  # Public getter method
             return self.__balance

         def set_balance(self, new_balance):  # Public setter method
             self.__balance = new_balance

     obj = BankAccount(1000)
     print("Initial balance:", obj.get_balance())
     obj.set_balance(1500)
     print("Updated balance:", obj.get_balance())
     ```
   - Output:
     ```
     Initial balance: 1000
     Updated balance: 1500
     ```
## Decorators in Python

Decorators are a very useful feature in Python. 
They allow you to wrap another function to extend its behavior dynamically.
Decorators are a powerful tool that allows you to modify the behavior of functions or classes without permanently altering them.
Here are some key concepts related to decorators:

1. **First-Class Objects**:
   - In Python, functions are considered first-class objects. This means that functions can be:
     - Stored in variables.
     - Passed as arguments to other functions.
     - Returned from other functions.
     - Stored in data structures like lists or hash tables.

   Example:
   ```python
   def shout(text):
       return text.upper()

   yell = shout
   print(yell('Hello'))  # Output: HELLO
   ```

2. **Passing Functions as Arguments**:
   - You can pass functions as arguments to other functions.
   - The passed function can then be called inside the receiving function.

   Example:
   ```python
   def greet(func):
       greeting = func("Hi, I am created by a function passed as an argument.")
       print(greeting)

   greet(shout)  # Output: HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
   ```

3. **Returning Functions from Another Function**:
   - You can create a function inside another function and return the inner function.
   - This is useful for creating closures.

   Example:
   ```python
   def create_adder(x):
       def adder(y):
           return x + y
       return adder

   add_15 = create_adder(15)
   print(add_15(10))  # Output: 25
   ```

4. **Syntax for Decorators**:
   - Decorators use the `@decorator_name` syntax.
   - A decorator is a callable function that wraps another function and adds some code before and/or after calling the original function.

   Example:
   ```python
   @gfg_decorator
   def hello_decorator():
       print("Gfg")
   ```

   This is equivalent to:
   ```python
   def hello_decorator():
       print("Gfg")

   hello_decorator = gfg_decorator(hello_decorator)
   ```

5. **Creating a Decorator**:
   - A decorator function takes another function as an argument.
   - It defines a wrapper function inside it, which executes code before and after calling the original function.

   Example:
   ```python
   def hello_decorator(func):
       def wrapper():
           print("Before function call")
           func()
           print("After function call")
       return wrapper

   @hello_decorator
   def say_hello():
       print("Hello!")

   say_hello()
   # Output:
   # Before function call
   # Hello!
   # After function call
   ```

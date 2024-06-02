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
Decorators are powerful tools that allow you to modify the behavior of functions or classes. 
They enhance code reusability, readability, and maintainability.

## Types of Decorators in Python

1. **Function Decorators:**
   - **Function decorators** are the most commonly used type. They are applied to regular functions.
   - A decorator is a higher-order function that takes another function as an argument and returns a modified version of it.
   - Example of a simple function decorator:
     ```python
     def make_pretty(func):
         def inner():
             print("I got decorated")
             func()
         return inner

     def ordinary():
         print("I am ordinary")

     decorated_ordinary = make_pretty(ordinary)
     decorated_ordinary()  # Output: "I got decorated" followed by "I am ordinary"
     ```

2. **Class Decorators:**
   - **Class decorators** are applied to classes and modify their behavior.
   - They can add or remove properties, methods, or attributes from a class.
   - Example of a class decorator:
     ```python
     def my_class_decorator(cls):
         cls.new_attribute = "Added by decorator"
         return cls

     @my_class_decorator
     class MyClass:
         def __init__(self):
             self.name = "MyClass"

     obj = MyClass()
     print(obj.name)  # Output: "MyClass"
     print(obj.new_attribute)  # Output: "Added by decorator"
     ```

3. **Method Decorators:**
   - **Method decorators** modify the behavior of class methods.
   - They can be used to add functionality or change the behavior of specific methods.
   - Example of a method decorator:
     ```python
     def uppercase_decorator(func):
         def wrapper(*args, **kwargs):
             result = func(*args, **kwargs)
             return result.upper()
         return wrapper

     class TextManipulator:
         @uppercase_decorator
         def capitalize(self, text):
             return text.capitalize()

     tm = TextManipulator()
     print(tm.capitalize("hello"))  # Output: "HELLO"
     ```

4. **Property Decorators:**
   - **Property decorators** allow you to define getter, setter, and deleter methods for class properties.
   - They provide a clean way to access and modify attributes.
   - Example of a property decorator:
     ```python
     class Circle:
         def __init__(self, radius):
             self._radius = radius

         @property
         def radius(self):
             return self._radius

         @radius.setter
         def radius(self, value):
             if value >= 0:
                 self._radius = value
             else:
                 raise ValueError("Radius must be non-negative")

     circle = Circle(radius=5)
     print(circle.radius)  # Output: 5
     circle.radius = 7
     print(circle.radius)  # Output: 7
     ```

Decorators are a powerful feature in Python that allow you to modify functions, classes, and properties. 

## Polymorphism

Polymorphism is a fundamental concept in programming that allows a single type entity (such as a method, operator, or object) to represent different types in different scenarios.
It enhances flexibility and makes code more generic and reusable.

##### Examples of Polymorphism:

1. **Operator Polymorphism:**
   - The `+` operator is used extensively in Python programs. However, it does not have a single usage.
   - For integer data types, the `+` operator performs arithmetic addition.
     ```python
     num1 = 1
     num2 = 2
     print(num1 + num2)  # Outputs 3
     ```
   - For string data types, the `+` operator performs concatenation.
     ```python
     str1 = "Python"
     str2 = "Programming"
     print(str1 + " " + str2)  # Outputs "Python Programming"
     ```

2. **Function Polymorphism:**
   - The `len()` function is compatible with multiple data types in Python.
   - It can work with strings, lists, tuples, sets, and dictionaries.
     ```python
     print(len("Programiz"))  # Outputs 9
     print(len(["Python", "Java", "C"]))  # Outputs 3
     print(len({"Name": "John", "Address": "Nepal"}))  # Outputs 2
     ```

3. **Class Polymorphism:**
   - In object-oriented programming, we can use polymorphism while creating class methods.
   - Different classes can have methods with the same name.
   - For example, consider two classes: `Cat` and `Dog`.
     ```python
     class Cat:
         def info(self):
             print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
         def make_sound(self):
             print("Meow")

     class Dog:
         def info(self):
             print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
         def make_sound(self):
             print("Bark")

     cat1 = Cat("Kitty", 2.5)
     dog1 = Dog("Fluffy", 4)

     for animal in (cat1, dog1):
         animal.make_sound()
         animal.info()
     ```
   - Output:
     ```
     Meow
     I am a cat. My name is Kitty. I am 2.5 years old.
     Meow
     Bark
     I am a dog. My name is Fluffy. I am 4 years old.
     ```

Polymorphism allows us to write more generic and reusable code, treating different objects uniformly.
Whether it's through operators, functions, or class methods, polymorphism enhances the flexibility and adaptability of our Python programs.

Polymorphism refers to the ability of different objects or classes to respond to the same method name in a way that is specific to their individual types.
It allows you to write code that can work with objects of various classes in a consistent and predictable manner, thereby enhancing code flexibility and reusability.

1. **Function Polymorphism**:
    - In Python, polymorphism is often seen with functions or methods that can be executed on different objects.
    - For example, consider the `len()` function:
        - For strings, `len()` returns the number of characters.
        - For tuples, it returns the number of items.
        - For dictionaries, it returns the number of key/value pairs¹.

2. **Class Polymorphism**:
    - Polymorphism is also used in class methods, where multiple classes can have the same method name.
    - Let's say we have three classes: `Car`, `Boat`, and `Plane`, each with a `move()` method:
        ```python
        class Car:
            def move(self):
                print("Drive!")

        class Boat:
            def move(self):
                print("Sail!")

        class Plane:
            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang")
        boat1 = Boat("Ibiza", "Touring 20")
        plane1 = Plane("Boeing", "747")

        for x in (car1, boat1, plane1):
            x.move()
        ```
        - Because of polymorphism, we can execute the same `move()` method for all three classes¹.

3. **Inheritance and Class Polymorphism**:
    - When we have child classes with the same method name, we can still use polymorphism.
    - Suppose we create a parent class called `Vehicle` and make `Car`, `Boat`, and `Plane` child classes of `Vehicle`:
        ```python
        class Vehicle:
            def move(self):
                print("Move!")

        class Car(Vehicle):
            pass

        class Boat(Vehicle):
            def move(self):
                print("Sail!")

        class Plane(Vehicle):
            def move(self):
                print("Fly!")

        car1 = Car("Ford", "Mustang")
        boat1 = Boat("Ibiza", "Touring 20")
        plane1 = Plane("Boeing", "747")

        for x in (car1, boat1, plane1):
            print(x.brand)
            print(x.model)
            x.move()
        ```
        - The child classes inherit properties and methods from the parent class.
        - The `Boat` and `Plane` classes override the `move()` method, demonstrating polymorphism¹.

4. **Benefits of Polymorphism**:
    - Simplifies interactions between objects.
    - Increases code flexibility and maintainability.
    - Allows for more elegant and concise code.

## Difference between **compile-time polymorphism** (also known as **static polymorphism**) and **runtime polymorphism** (also known as **dynamic polymorphism**):

#### Compile-Time Polymorphism (Static Polymorphism)

1. **Definition**:
   - Compile-time polymorphism occurs during the compilation phase of a program.
   - It is resolved at compile time based on the type information available.
   - The decision about which method or function to call is made before the program runs.

2. **Examples**:
   - **Function Overloading**:
     - In languages like C++ or Java, you can define multiple functions with the same name but different parameter lists.
     - The appropriate function to call is determined based on the number and types of arguments during compilation.
   - **Operator Overloading**:
     - You can redefine the behavior of operators (e.g., `+`, `-`, `*`) for custom classes.
     - The compiler resolves the correct operator implementation based on the operands' types.

3. **Advantages**:
   - Efficiency: Compile-time polymorphism results in faster execution because method resolution happens at compile time.
   - Early Error Detection: Issues related to method signatures or operator usage are caught during compilation.

#### Runtime Polymorphism (Dynamic Polymorphism)

1. **Definition**:
   - Runtime polymorphism occurs during program execution.
   - It is resolved dynamically based on the actual type of the object.
   - The decision about which method or function to call is made at runtime.

2. **Examples**:
   - **Method Overriding**:
     - Inheritance allows you to override methods in derived classes.
     - The method to call is determined based on the actual object type at runtime.
   - **Virtual Functions (C++)**:
     - In C++, you can declare a function as `virtual`.
     - The correct method implementation is chosen based on the object type during runtime.

3. **Advantages**:
   - Flexibility: Runtime polymorphism allows for more flexible and extensible code.
   - Late Binding: The method resolution happens dynamically, allowing for dynamic dispatch.

#### Summary

- **Compile-time polymorphism** is resolved at compile time based on type information, while **runtime polymorphism** is resolved dynamically during program execution.
- Both types of polymorphism have their use cases, and understanding when to use each is essential for writing efficient and maintainable code.

Certainly! Operator overloading in Python allows you to redefine the behavior of certain operators for user-defined types. You can change how operators work based on the context. Let's dive into the details of overloading arithmetic operators:

## Operator Overloading in Python

In Python, you can overload various arithmetic operators by defining special methods in your class. These methods have double underscores (e.g., `__add__`, `__sub__`, etc.) and allow you to customize the behavior of operators. Here are some commonly used arithmetic operators and their corresponding special methods:

1. **Addition (`+`)**:
   - To overload the `+` operator, implement the `__add__()` method in your class.
   - Example:
     ```python
     class Point:
         def __init__(self, x=0, y=0):
             self.x = x
             self.y = y
         def __add__(self, other):
             x = self.x + other.x
             y = self.y + other.y
             return Point(x, y)
     p1 = Point(1, 2)
     p2 = Point(2, 3)
     print(p1 + p2)  # Output: (3, 5)
     ```

2. **Subtraction (`-`)**:
   - Implement the `__sub__()` method to overload the `-` operator.

3. **Multiplication (`*`)**:
   - Implement the `__mul__()` method to overload the `*` operator.

4. **Power (`**`)**:
   - Implement the `__pow__()` method to overload the `**` operator.

5. **Division (`/`)**:
   - Implement the `__truediv__()` method to overload the `/` operator.

6. **Floor Division (`//`)**:
   - Implement the `__floordiv__()` method to overload the `//` operator.

7. **Remainder (Modulo) (`%`)**:
   - Implement the `__mod__()` method to overload the `%` operator.

8. **Bitwise Left Shift (`<<`)**:
   - Implement the `__lshift__()` method to overload the `<<` operator.

9. **Bitwise Right Shift (`>>`)**:
   - Implement the `__rshift__()` method to overload the `>>` operator.

10. **Bitwise AND (`&`)**:
    - Implement the `__and__()` method to overload the `&` operator.

11. **Bitwise OR (`|`)**:
    - Implement the `__or__()` method to overload the `|` operator.

12. **Bitwise XOR (`^`)**:
    - Implement the `__xor__()` method to overload the `^` operator.

## Operator Overloading for Comparison Operators in Python

Operator overloading allows you to redefine the behavior of built-in operators for user-defined classes.
When you overload comparison operators, you customize how instances of your class are compared using operators like `<`, `<=`, `>`, `>=`, `==`, and `!=`.

##### Available Comparison Operators

1. **Less Than (`<`) Operator (`__lt__`)**:
   - Method: `__lt__(self, other)`
   - Description: Defines behavior for the less than operator (`<`). It is automatically invoked when you use the `<` operator with instances of your class.
   - Example:
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age

         def __lt__(self, other):
             return self.age < other.age

     p1 = Person("Alice", 20)
     p2 = Person("Bob", 30)
     print(p1 < p2)  # Output: True
     ```

2. **Less Than or Equal To (`<=`) Operator (`__le__`)**:
   - Method: `__le__(self, other)`
   - Description: Defines behavior for the less than or equal to operator (`<=`).
   - Example:
     ```python
     # Similar to the Person class example above
     ```

3. **Greater Than (`>`) Operator (`__gt__`)**:
   - Method: `__gt__(self, other)`
   - Description: Defines behavior for the greater than operator (`>`).
   - Example:
     ```python
     # Similar to the Person class example above
     ```

4. **Greater Than or Equal To (`>=`) Operator (`__ge__`)**:
   - Method: `__ge__(self, other)`
   - Description: Defines behavior for the greater than or equal to operator (`>=`).
   - Example:
     ```python
     # Similar to the Person class example above
     ```

5. **Equal To (`==`) Operator (`__eq__`)**:
   - Method: `__eq__(self, other)`
   - Description: Defines behavior for the equal to operator (`==`).
   - Example:
     ```python
     # Similar to the Person class example above
     ```

6. **Not Equal To (`!=`) Operator (`__ne__`)**:
   - Method: `__ne__(self, other)`
   - Description: Defines behavior for the not equal to operator (`!=`).
   - Example:
     ```python
     # Similar to the Person class example above
     ```

## How It Works

- Whenever you use a comparison operator (e.g., `p1 < p2`), Python automatically calls the corresponding magic method (e.g., `p1.__lt__(p2)`).
- By changing the code inside these magic methods, you can give extra meaning to the comparison operators.

## Concepts of Polymorphism

1. **Function Polymorphism**:
    - Functions or methods can behave differently based on the data types they operate on.
    - Example: The `len()` function can work with strings, lists, tuples, sets, and dictionaries, returning specific information about each type¹.

2. **Class Polymorphism**:
    - In OOP, polymorphism is often seen in class methods.
    - Child classes can override methods inherited from parent classes, providing specific implementations.
    - Example: Consider a base class `Animal` with a method `make_sound()`. Subclasses like `Cat` and `Dog` can override this method to produce different sounds⁵.

#### Method Overloading

Method overloading involves defining multiple methods with the **same name** but **different parameters** within the same class. However, Python does not natively support method overloading. Instead, we can simulate it by defining methods with varying parameters and selectively using the appropriate one based on the arguments provided.

##### Example of Simulated Method Overloading

```python
def add(datatype, *args):
    if datatype == 'int':
        result = 0
    elif datatype == 'str':
        result = ''
    
    for x in args:
        result += x
    
    print(result)

# Usage
add('int', 5, 6)  # Output: 11
add('str', 'Hello', 'World')  # Output: HelloWorld
```

In this example, the `add()` function behaves differently based on the data type provided as the first argument.

#### Method Overriding

Method overriding is a form of **runtime polymorphism**. It occurs when a child class provides a specific implementation for a method that is already defined in its parent class. The child class effectively overrides the behavior of the parent class method.

##### Example of Method Overriding

```python
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

# Usage
cat = Cat()
dog = Dog()

cat.make_sound()  # Output: Meow
dog.make_sound()  # Output: Bark
```

In this example:
- The `Cat` and `Dog` classes override the `make_sound()` method inherited from the `Animal` class.
- When we create instances of `Cat` and `Dog`, their specific `make_sound()` implementations are called⁵.

#### Inheritance

Inheritance is a fundamental concept in OOP. It allows a child class (subclass) to inherit properties and methods from a parent class (superclass). In Python, we achieve inheritance using the `class ChildClassName(ParentClassName)` syntax.

##### Example of Inheritance

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"I am a {self.brand}")

class Car(Vehicle):
    def drive(self):
        print("Vroom!")

class Boat(Vehicle):
    def sail(self):
        print("Sailing smoothly!")

# Usage
my_car = Car("Toyota")
my_boat = Boat("Yacht")

my_car.info()  # Output: I am a Toyota
my_boat.info()  # Output: I am a Yacht
my_car.drive()  # Output: Vroom!
my_boat.sail()  # Output: Sailing smoothly!
```

In this example:
- `Car` and `Boat` inherit the `info()` method from the `Vehicle` class.
- They also have additional methods specific to their types⁵.

##### 1. Polymorphism with Class Methods

Consider two classes, `Dog` and `Cat`, each with a method named `speak`. Despite having different implementations, we can use them interchangeably:

```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

# Usage
dog_instance = Dog()
cat_instance = Cat()

dog_instance.speak()  # Output: Woof!
cat_instance.speak()  # Output: Meow!
```

In this example, both `Dog` and `Cat` have a `speak` method, but they behave differently. Polymorphism allows us to treat them uniformly, regardless of their specific class.

##### 2. Polymorphism with Inheritance

In Python, polymorphism lets us define methods in child classes that have the same name as methods in the parent class. When a child class inherits methods from the parent class, we can modify or override those methods to better suit the child class's behavior:

```python
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most birds can fly, but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

# Usage
bird_instance = Bird()
sparrow_instance = Sparrow()
ostrich_instance = Ostrich()

bird_instance.intro()
bird_instance.flight()

sparrow_instance.intro()
sparrow_instance.flight()

ostrich_instance.intro()
ostrich_instance.flight()
```

In this example, `Sparrow` and `Ostrich` override the `flight` method inherited from `Bird`. Polymorphism allows us to call the same method name on different bird instances, even though their behavior varies.

##### 3. Polymorphism with a Function and Objects

We can create functions that accept any object, allowing for dynamic polymorphism. Python checks the object type at runtime and calls the correct method:

```python
def describe_animal(animal):
    animal.intro()
    animal.flight()

# Usage
describe_animal(sparrow_instance)  # Calls Sparrow's methods
describe_animal(ostrich_instance)  # Calls Ostrich's methods
```

In this example, the `describe_animal` function works with different bird instances, demonstrating polymorphism.

## Virtual Functions in Python

1. **What are Virtual Functions?**
   - Virtual functions are a fundamental concept in object-oriented programming (OOP).
   - They allow a derived class to override a method from its base class.
   - The method to call is determined dynamically at runtime based on the actual type of the object.

2. **How Python Handles Virtual Functions: Duck Typing**
   - Python doesn't have explicit keywords like `virtual` or `override` as in languages like C++.
   - Instead, Python relies on **duck typing**.
   - Duck typing means that if an object behaves like a certain type (quacks like a duck), it is treated as that type.
   - In Python, all methods are essentially "virtual" because they are resolved dynamically based on the runtime type of the object¹.

3. **Example: Implementing Virtual Functions in Python**
   - Consider the following example with an `Animal` base class and its derived classes `Cat` and `Dog`:
     ```python
     class Animal:
         def speak(self):
             print("Animal makes a sound")

     class Cat(Animal):
         def speak(self):
             print("Meow")

     class Dog(Animal):
         def speak(self):
             print("Woof")

     my_pets = [Dog(), Cat(), Dog()]
     for pet in my_pets:
         pet.speak()
     ```
     Output:
     ```
     Woof
     Meow
     Woof
     ```
   - Here, the `speak()` method behaves differently for each derived class, demonstrating dynamic method resolution¹.

4. **Abstract Base Classes (ABCs) and `abstractmethod`**
   - Python provides the `abc` module for creating abstract base classes.
   - An abstract base class defines a contract that derived classes must follow.
   - The `abstractmethod` decorator marks a method as abstract, ensuring that any subclass must override it.
   - While Python doesn't have true compile-time errors, using `abstractmethod` helps catch missing implementations during class definition (before instantiation)⁷.

5. **Summary**
   - In Python, all methods are effectively virtual due to duck typing.
   - Use abstract base classes and `abstractmethod` to enforce method overrides.
   - When designing modules or frameworks, consider using abstract methods to self-document requirements for subclassing.


## Passing Functions as Arguments in Python

### 1. First-Class Functions
In Python, functions are considered **first-class objects**. This means that you can treat them like any other object, such as integers, strings, or lists. Specifically, you can:
- Assign functions to variables.
- Pass functions as arguments to other functions.
- Return functions from other functions.

##### Example
Let's start with a basic example. Suppose we have two functions: `shout(text)` and `whisper(text)`. The `shout` function converts the input text to uppercase, while `whisper` converts it to lowercase. We can pass these functions as arguments to another function:

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)

# Example usage
greet(shout)   # Output: HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
greet(whisper) # Output: hi, i am created by a function passed as an argument.
```

In this example:
- The `greet` function takes another function (`func`) as an argument.
- We call `greet(shout)` and `greet(whisper)` to demonstrate how the same `greet` function behaves differently based on the function passed to it.

### 2. Decorators (Wrapper Functions)
Decorators allow us to modify the behavior of a function without permanently changing it. They are often used for tasks like logging, timing, or authentication. Here's a simple decorator example:

```python
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1

def function_to_be_used():
    print("This is inside the function!!")

# Applying the decorator
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()
# Output:
# Hello, this is before function execution
# This is inside the function!!
# This is after function execution
```

In this example:
- `hello_decorator` wraps the `function_to_be_used` function.
- When we call `function_to_be_used()`, it executes the modified behavior defined in `inner1`.

### 3. Lambda Functions
Lambda functions (also known as anonymous functions) are concise functions with a single expression. They can be used as arguments too. Here's an example:

```python
square = lambda x: x * x
cube = lambda func: func ** 3

print("Square of 2 is:", square(2))
print("The cube of", square(2), "is", cube(square(2)))
# Output:
# Square of 2 is: 4
# The cube of 4 is 64
```

In this example:
- We define a lambda function `square` that squares its input.
- The `cube` function takes another function (`func`) and computes its cube.

## Passing functions as arguments in Python has several real-world use cases.

1. **Higher-Order Functions:**
   - Functions that accept other functions as arguments are called **higher-order functions**. These functions allow you to create more flexible and reusable code.
   - Real-world examples:
     - Sorting algorithms (e.g., `sorted()`) can take a custom comparison function as an argument.
     - Map and filter operations (e.g., `map()`, `filter()`) apply a given function to each element of a collection.
     - Event handling in GUI libraries (e.g., Tkinter) where callback functions are passed as arguments.

2. **Decorators (Wrapper Functions):**
   - Decorators allow you to modify the behavior of a function without permanently changing it.
   - Real-world examples:
     - Logging: You can create a decorator to log function calls, execution time, or other relevant information.
     - Authentication: Decorators can be used to check user authentication before executing certain functions.
     - Caching: Decorators can cache expensive function results to improve performance.

3. **Lambda Functions:**
   - Lambda functions (anonymous functions) are concise and can be used as arguments.
   - Real-world examples:
     - Sorting with custom keys: You can pass a lambda function to `sorted()` to sort based on specific criteria.
     - Callbacks in event-driven programming: Lambda functions are often used for event handlers.
     - Functional programming: Lambda functions are common in functional programming paradigms.

4. **Currying:**
   - Currying is when you break down a function that takes multiple arguments into a series of functions, each taking only one argument.
   - Real-world examples:
     - Mathematical operations: Currying allows you to partially apply arguments to a function.
     - Configurable functions: Curried functions can be used to create specialized versions of a generic function.

Remember that these concepts enhance code readability, maintainability, and reusability.

Certainly! Besides **currying**, there are several other interesting concepts and techniques in Python that enhance code flexibility and maintainability. Let's explore a few of them:

1. **Partial Functions:**
   - A **partial function** is a way to fix a certain number of arguments of a function and generate a new function with fewer arguments.
   - It's similar to currying, but instead of creating a chain of single-argument functions, you create a new function with some arguments pre-set.
   - Python's `functools.partial` allows you to create partial functions.
   - Example:
     ```python
     from functools import partial

     def multiply(a, b):
         return a * b

     double = partial(multiply, b=2)
     print(double(5))  # Output: 10
     ```

2. **Lambda Functions (Anonymous Functions):**
   - Lambda functions are concise, one-liner functions that can be used wherever function objects are required.
   - They are often used for small tasks or as arguments to higher-order functions.
   - Example:
     ```python
     square = lambda x: x ** 2
     print(square(3))  # Output: 9
     ```

3. **Default Parameters:**
   - You can set default values for function parameters. If an argument is not provided, the default value is used.
   - Useful for creating more flexible functions.
   - Example:
     ```python
     def greet(name="Guest"):
         return f"Hello, {name}!"

     print(greet())       # Output: Hello, Guest!
     print(greet("Alice"))  # Output: Hello, Alice!
     ```

4. **Higher-Order Functions:**
   - These are functions that take other functions as arguments or return functions.
   - Useful for creating reusable and modular code.
   - Examples:
     - `map()`, `filter()`, and `reduce()` functions.
     - Callback functions in event handling.

5. **Generator Functions:**
   - Generator functions use the `yield` keyword to produce a sequence of values lazily.
   - They are memory-efficient and allow you to iterate over large data without loading it all into memory.
   - Example:
     ```python
     def fibonacci():
         a, b = 0, 1
         while True:
             yield a
             a, b = b, a + b

     fib_gen = fibonacci()
     for _ in range(10):
         print(next(fib_gen), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
     ```

Remember that these concepts empower you to write more expressive and elegant Python code.

## `*args` and `**kwargs` in Python. 

#### 1. `*args` (Non-Keyword Arguments)
`*args` stands for "arguments" and is used to pass a variable number of non-keyworded arguments to a function. Here's how it works:

- When defining a function, you can include `*args` as one of the parameters.
- At runtime, you can pass any number of positional arguments to the function, and they will be collected into a tuple.
- Inside the function, you can iterate over this tuple and perform operations on the arguments.

##### Example:
```python
def my_sum(*args):
    """Sums up all the integers passed as arguments."""
    result = 0
    for num in args:
        result += num
    return result

# Usage
print(my_sum(1, 2, 3))  # Output: 6
print(my_sum(10, 20, 30, 40))  # Output: 100
```

In the example above, `my_sum()` accepts any number of integers and calculates their sum. The `*args` parameter allows us to handle an arbitrary number of arguments without explicitly specifying them in the function definition¹.

#### 2. `**kwargs` (Keyword Arguments)
`**kwargs` stands for "keyword arguments" and allows you to pass a variable number of keyworded arguments (i.e., named arguments) to a function. Here's how it works:

- When defining a function, you can include `**kwargs` as one of the parameters.
- At runtime, you can pass any number of keyword arguments (in the form of key-value pairs) to the function.
- Inside the function, `kwargs` becomes a dictionary containing the passed arguments.

##### Example:
```python
def print_info(**kwargs):
    """Prints information about the provided arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print_info(name="Alice", age=30, city="Wonderland")
# Output:
# name: Alice
# age: 30
# city: Wonderland
```

In this example, `print_info()` accepts any number of keyword arguments and displays their values. The `**kwargs` parameter allows us to work with a dynamic set of named arguments².

#### Difference Between `*args` and `**kwargs`
The key difference lies in how they collect and handle the arguments:
- `*args` collects positional arguments into a tuple, allowing you to work with them as a sequence.
- `**kwargs` collects keyword arguments into a dictionary, allowing you to access them by their names.

Remember:
- Use `*args` when dealing with non-keyworded arguments (e.g., numbers, strings, objects).
- Use `**kwargs` when dealing with keyworded arguments (e.g., configuration settings, options).

## Combining `*args` and `**kwargs` 
Combining `*args` and `**kwargs` in the same function allows you to create highly flexible functions that can handle various types of arguments.

1. **Using Both `*args` and `**kwargs` in a Function:**
   You can define a function that accepts both positional arguments (collected by `*args`) and keyword arguments (collected by `**kwargs`). Here's an example:

    ```python
    def example_function(*args, **kwargs):
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    # Usage
    example_function(1, 2, 3, name="Alice", age=30)
    ```

   In this example:
   - The integers `1`, `2`, and `3` are collected by `*args`.
   - The keyword arguments `name="Alice"` and `age=30` are collected by `**kwargs`.

2. **Order of Arguments:**
   - When defining a function, the named arguments (if any) come first, followed by `*args`, and finally `**kwargs`.
   - The order matters: `def my_function(a, b, *args, **kwargs)` is valid, but `def my_function(*args, a, b, **kwargs)` is not.

3. **Unpacking Iterables Using Asterisks:**
   - You can also use a single asterisk (`*`) to unpack iterables (e.g., lists, tuples) into function arguments.
   - Similarly, two asterisks (`**`) can unpack dictionaries into keyword arguments.

4. **Benefits:**
   - Combining `*args` and `**kwargs` allows your function to handle a dynamic set of arguments, making it more versatile.

## Differences between `*args` and `**kwargs` in Python:

1. **Purpose and Usage:**
   - `*args` (Non-Keyword Arguments):
     - Collects a variable number of non-keyworded arguments (positional arguments) into a tuple.
     - Useful when you want to pass an arbitrary number of arguments to a function without explicitly specifying them in the function definition.
   - `**kwargs` (Keyword Arguments):
     - Collects a variable number of keyworded arguments (named arguments) into a dictionary.
     - Useful when you want to handle named arguments dynamically within a function.

2. **Syntax:**
   - `*args`:
     - Defined using a single asterisk (`*`) before the parameter name (e.g., `def my_function(*args):`).
   - `**kwargs`:
     - Defined using a double asterisk (`**`) before the parameter name (e.g., `def my_function(**kwargs):`).

3. **Data Structure:**
   - `*args`:
     - Collects arguments as a tuple.
     - You can iterate over the tuple and perform operations on the arguments.
   - `**kwargs`:
     - Collects arguments as a dictionary.
     - You can access the arguments by their names (keys) and perform dictionary operations.

4. **Example:**
   ```python
   def example_function(*args, **kwargs):
       # Use args (tuple)
       for arg in args:
           print(arg)
       # Use kwargs (dictionary)
       for key, value in kwargs.items():
           print(f"{key}: {value}")

   # Usage
   example_function(1, 2, 3, name="Alice", age=30)
   ```

5. **Order of Arguments:**
   - When defining a function, named arguments (if any) come first, followed by `*args`, and finally `**kwargs`.
   - The order matters: `def my_function(a, b, *args, **kwargs)` is valid, but `def my_function(*args, a, b, **kwargs)` is not.

6. **Unpacking Iterables:**
   - You can use a single asterisk (`*`) to unpack iterables (e.g., lists, tuples) into function arguments.
   - Similarly, two asterisks (`**`) can unpack dictionaries into keyword arguments.

## Iterators and Iterables in Python: Run Efficient Iterations

In Python, **an iterator** is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets. Python iterators implement the iterator design pattern, which decouples the iteration algorithms from container data structures¹. Here's an elaboration on iterators and iterables:

### What Is an Iterator in Python?

An iterator represents a stream of data and provides a method to access its elements sequentially. It maintains the current position during iteration and knows how to retrieve the next element. You can create an iterator from a collection using the built-in Python function `iter()`².

### What Is the Python Iterator Protocol?

The Python iterator protocol consists of two methods:

1. `__iter__()`: This method returns the iterator object itself. It allows an object to be used as an iterable in a `for` loop.
2. `__next__()`: This method retrieves the next value from the iterator. When there are no more elements, it raises the `StopIteration` exception.

### When to Use an Iterator in Python?

You'll encounter iterators and iterables in almost all your Python programs. Here are some scenarios where iterators are useful:

1. **Efficient Data Processing**: Iterators allow you to process large datasets efficiently, as they load data lazily (one element at a time) rather than loading everything into memory.
2. **Custom Iteration Logic**: You can create custom iterators with specific behavior, such as filtering, transforming, or generating new data.
3. **Streaming Data**: When dealing with streaming data (e.g., reading from a file or a network stream), iterators are essential.

### Creating Different Types of Iterators

#### 1. Yielding the Original Data

The most straightforward iterator is one that yields the original data from a collection. For example:

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Usage:
my_list = [1, 2, 3, 4]
my_iter = MyIterator(my_list)
for item in my_iter:
    print(item)
```

#### 2. Transforming the Input Data

You can create iterators that transform the input data. For instance, applying a function to each element:

```python
class SquareIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index] ** 2
        self.index += 1
        return value

# Usage:
my_list = [1, 2, 3, 4]
squared_iter = SquareIterator(my_list)
for squared_value in squared_iter:
    print(squared_value)
```

#### 3. Generating New Data

You can create iterators that generate new data dynamically. For example, an infinite sequence of Fibonacci numbers:

```python
class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

# Usage:
fib_iter = FibonacciIterator()
for _ in range(10):
    print(next(fib_iter))
```

## Difference between an **iterable** and an **iterator** in Python:

1. **Iterable**:
   - An iterable is any Python object that can be looped over using a `for` loop.
   - It represents a collection of elements.
   - Examples of iterables include lists, tuples, dictionaries, strings, sets, and more.
   - When you use a `for` loop to iterate over an iterable, Python automatically creates an iterator behind the scenes.

2. **Iterator**:
   - An iterator is an object that implements the iterator protocol.
   - It provides a way to access elements sequentially from an iterable.
   - Iterators maintain state during iteration (e.g., the current position).
   - The two essential methods for an iterator are:
     - `__iter__()`: Returns the iterator object itself.
     - `__next__()`: Retrieves the next value from the iterator.
   - When you use a `for` loop, it calls the `__iter__()` method on the iterable to get an iterator and then repeatedly calls `__next__()` to retrieve elements.
   - Iterators are memory-efficient because they load data lazily (one element at a time) rather than loading everything into memory.

3. **Example**:
   ```python
   my_list = [1, 2, 3]
   my_iter = iter(my_list)  # Create an iterator from the list
   print(next(my_iter))     # Prints 1
   print(next(my_iter))     # Prints 2
   print(next(my_iter))     # Prints 3
   # After this point, calling next(my_iter) will raise StopIteration
   ```

An iterable is a broader concept (anything you can loop over), while an iterator is a specific object that allows you to traverse an iterable's elements sequentially.

## Lazy Evaluation in Python

Lazy evaluation refers to cases when Python doesn't work out the values of an expression immediately.
Instead, the values are returned at the point when they're required in the program.
It can also be referred to as **call-by-need**¹.

#### Eager vs. Lazy Evaluation

Python evaluates expressions in two main ways:

1. **Eager evaluation**: In eager evaluation, Python computes the value of an expression as soon as it encounters it. Examples of expressions that are evaluated eagerly include arithmetic operations, function calls, and list literals. For instance:

    ```python
    # Eager evaluation examples
    result1 = 5 + 10
    result2 = random.randint(1, 10)
    numbers = [2, 4, 6, 8, 10]
    ```

    In the above examples, Python immediately evaluates the expressions and assigns the results to the corresponding variables.

2. **Lazy evaluation**: Lazy evaluation, on the other hand, defers the computation of an expression until its value is actually needed. Lazy evaluation is particularly useful when dealing with large data sets or potentially infinite sequences. Some examples of lazy evaluation in Python include:

    - **Generators**: Generators produce values on-the-fly as you iterate over them. They don't compute all values upfront, which saves memory. For example, the `range()` function returns a lazy iterable that generates values only when requested⁵.

    - **Generator expressions**: Similar to list comprehensions, generator expressions create lazy iterators. They allow you to define a sequence without creating an entire list in memory. For instance:

        ```python
        squares_generator = (i * i for i in range(5))
        ```

    - **Short-circuit evaluation**: Logical operators like `and` and `or` use lazy evaluation. If the first operand determines the result, Python doesn't evaluate the second operand unnecessarily.

    - **File reading operations**: When reading large files, Python reads data lazily, fetching only the necessary portions as requested.

#### Advantages of Lazy Evaluation
1. **Memory efficiency**: Lazy evaluation avoids loading all data into memory at once. It generates values on-the-fly, which is crucial for large datasets.
2. **Performance optimization**: By computing values only when needed, lazy evaluation reduces unnecessary calculations and improves performance.
3. **Infinite data structures**: Lazy evaluation allows you to work with potentially infinite sequences (e.g., an infinite stream of prime numbers).
#### Disadvantages of Lazy Evaluation
1. **Complexity**: Lazy evaluation can make code harder to reason about, especially when dealing with complex dependencies between expressions.
2. **Order of evaluation**: The order in which expressions are evaluated may not always be intuitive, leading to unexpected behavior.

# Short Circuiting in Python

**Short-circuiting** refers to the behavior where the evaluation of a boolean expression stops as soon as the overall truth value can be determined.
This optimization technique avoids unnecessary computations and improves performance. Let's explore short-circuiting in detail:
**Short-Circuiting**: When Python evaluates a logical expression, it stops its evaluation if the result is already known.
This means that certain parts of the expression are not computed because they won't affect the final outcome¹.

### Short-Circuiting Techniques

#### 1. Short-Circuiting with Boolean Operators

- **`or` Operator**:
    - When evaluating an `or` expression, Python checks the first statement. If it is `True`, the second statement is not evaluated, and the result is based on the first value.
    - Example:

    ```python
    x = 5
    y = 10
    if x > 6 or y < 20:
        print('OK')
    ```

    Output: `OK`

- **`and` Operator**:
    - For an `and` expression, Python checks if the first statement is `False`. If it is, the whole expression must be `False`, so it returns that value. Otherwise, it evaluates the second statement and returns the value.
    - An expression containing `and` or `or` stops execution when the truth value has been determined. Evaluation occurs from left to right.

#### 2. Short-Circuiting in `all()` and `any()` Functions

- The built-in functions `all()` and `any()` also support short-circuiting:
    - `all()`: Evaluates each element of a sequence in order until finding a result that allows an early exit.
    - `any()`: Stops evaluation as soon as a `True` value is encountered.
    - Example:

    ```python
    def check(i):
        print("geeks")
        return i

    print(all(check(i) for i in [1, 1, 0, 0, 3]))  # Output: False
    print(any(check(i) for i in [0, 0, 0, 1, 3]))  # Output: True
    ```

#### 3. Short-Circuiting in Conditional Operators

- Conditional operators (`>`, `<`, etc.) also follow short-circuiting:
    - If the result of an expression is already known, further execution is skipped.
    - Example:

    ```python
    def check(i):
        print("geeks")
        return i

    print(10 > 11 > check(3))  # Output: False
    print(10 < 11 > check(3))  # Output: True
    print(10 < 11 > check(12))  # Output: False
    ```

#### 4. Short-Circuiting in a Ladder of `if`, `elif`, `elif`, ... `else` Statements

- When there is a sequence (a "ladder") of `if` and one or more `elif` statements, none of the conditions after the first `True` condition are evaluated.
- Example:

    ```python
    a = 10
    b = 20
    c = 30

    def printreturn(l):
        print(l)
        return l

    if a == 11:
        print("a == 11")
    elif b == 20 and c == 30:
        print("b == 20 and c == 30")
    elif b == a + a and 0 < len(printreturn("This was evaluated")):
        print("b == a + a")
    ```

    Output: `b == 20 and c == 30`


==What is PEP 8 and why is it important?

PEP 8 is important because it documents the style guidelines for python code.

==Python is an interpreted language? Explain.

It means python code is executed line by line.  Source code is first converted into bytecode line by line and then executed on python virtual machine.


==What is the difference between compiled and interpreted language?

A compiled language is converted into machine language code using compiler and is executed by the target machine.
![[Pasted image 20240802162017.png]]

An interpreted language is not directly run by the machine. The code is run without compiling and is run by some other program.
![[Pasted image 20240802162027.png]]



Static Typed Language -- Data types are checked before execution
Dynamically Typed Language -- Data types are checked during execution


==How to print a string without new line character at the end? (as the print function adds new line character at the end by default)

print("some_string", end=" ")

![[Pasted image 20240802195223.png]]

==what is the difference between python lists and arrays?

List data structure is built into Python
Lists are mutable, can have different data types, do not need to be unique, ordered, noted by square backet

need to import array module
or numpy package for using array

Arrays



function->module->Package->directory->library



==What is a python lambda function?

- lambda functions are one liner functions. 
- dont have name specified. 
- can be used to pass to a higher order function like map,reduce,filter or any other

- lambda function can have only single statement.
- can take one or more arguments.

example -->
```python
cube = lambda x:x**3   
			 print(cube(4))
			 output >>> 64	
			 #lamda functions

#this is a function which returns a function----

def myfunc(n):

  return lambda a : a * n

  

mydoubler = myfunc(2)

mytripler = myfunc(3)

  

print(mydoubler(11)) ---> output is 22

print(mytripler(11)) --> output is 33

  
  

doubler = lambda x : 2*x

  

print(doubler(4)) --> output is 8
```

```
```



==map function


map function is a higher order function which is used to apply a particular function to each element of an iterable.


Example -->

```python

list1 = [1,2,3,4,5]

  

result = list(map(lambda x:x**3,list1))

  

print(result)
```


==Enscapsulation

Important principle of object-oriented design is encapsulation. Different components of a software system should not reveal the internal details of their respective implementations. One of the main advantages of encapsulation is that it gives one programmer freedom to implement the details of a component, without concern that other programmers will be writing code that intricately depends on those internal decisions. The only constraint on the programmer of a component is to maintain the public interface for the component, as other programmers will be writing code that depends on that interface. Encapsulation yields robustness and adaptability, for it allows the implementation details of parts of a program to change without adversely affecting other parts, thereby making it easier to fix bugs or add new functionality with relatively local changes to a component.


==Operator Overloading

Python’s built-in classes provide natural semantics for many operators. For example, the syntax a+b invokes addition for numeric types, yet concatenation for sequence types. When defining a new class, we must consider whether a syntax like a+bshould be defined when a or b is an instance of that class. By default, the + operator is undefined for a new class. However, the author of a class may provide a definition using a technique known as operator overload ing. This is done by implementing a specially named method. In particular, the +operator is overloaded by implementing a method named add ,whichtakes the right-hand operand as a parameter and which returns the result of the expres sion. That is, the syntax, a+b, is converted to a method call on object a of the form, a. add (b). Similar specially named methods exist for other operators. Table 2.1 provides a comprehensive list of such methods


==Protected and Private variables

Several object-oriented languages (e.g., Java, C++) draw a distinction for nonpublic members, allowing declarations of protected or private access modes. Members that are declared as protected are accessible to subclasses, but not to the general public, while members that are declared as private are not accessible to either. In this respect, we are using balance as if it were protected (but not private).


==Abstract Base Class and Concrete Class

In classic object-oriented terminology, we say a class is an abstract base class if its only purpose is to serve as a base class through inheritance. More formally, an abstract base class is one that cannot be directly instantiated, while a concrete class is one that can be instantiated.

==Abstract Method decorator

The second advanced technique is the use of the @abstractmethod decorator immediately before the len and getitem methods are declared. That declares these two particular methods to be abstract, meaning that we do not provide an implementation within our Sequence base class, but that we expect any concrete subclasses to support those two methods. Python enforces this expectation, by dis allowing instantiation for any subclass that does not override the abstract methods with concrete implementations



==Garbage Collection in Python

In some languages, like C and C++, the memory space for objects must be explic itly deallocated by the programmer, which is a duty often overlooked by beginning programmers and is the source of frustrating programming errors even for experi enced programmers. The designers of Python instead placed the burden of memory management entirely on the interpreter. The process of detecting “stale” objects, deallocating the space devoted to those objects, and returning the reclaimed space to the free list is known as garbage collection.





---

## 🧠 What is Polymorphism?

**Polymorphism** means **"many forms"**.

In object-oriented programming (OOP), polymorphism allows **different classes to be treated as instances of the same parent class**, and the same method name can behave **differently based on the object** calling it.

---

### 🧾 Types of Polymorphism in Python

1. **Compile-time (Static)** – Not applicable in Python (since it's dynamically typed).
    
2. **Runtime (Dynamic)** – This is what Python supports via:
    
    - Method overriding (in inheritance)
        
    - Duck typing
        

---

## ✅ Example 1: Polymorphism via Inheritance (Method Overriding)

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Using polymorphism
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
```

🎯 Here, the method `speak()` is **common**, but it behaves **differently** depending on the object (`Dog` or `Cat`). This is **runtime polymorphism**.

---

## ✅ Example 2: Duck Typing (Pythonic Polymorphism)

```python
class Duck:
    def walk(self):
        print("Duck walks like a duck")

class Robot:
    def walk(self):
        print("Robot walks like a machine")

def start_walking(entity):
    entity.walk()

duck = Duck()
robot = Robot()

start_walking(duck)   # Duck walks like a duck
start_walking(robot)  # Robot walks like a machine
```

🎯 Here, the function `start_walking()` doesn't care about the object type — if it has a `walk()` method, it works. This is **duck typing** — _"If it walks like a duck and quacks like a duck..."_

---

## ✅ Key Interview Point

> **Polymorphism** promotes flexibility and scalability in code.  
> It allows functions to use objects of different classes **interchangeably**, as long as they follow a common interface or method structure.

---

Let me know if you want real-world examples of polymorphism (e.g., in automation frameworks or REST API handlers).


**Operator overloading** means giving **custom meaning** to Python **built-in operators** (like `+`, `-`, `*`, etc.) **based on the operands' types**.

In Python, this is done by **overriding special methods** (also called **dunder methods**) in your class.

---

## 📦 Why Use It?

It helps objects behave **like built-in types**, making your code more **intuitive and readable**.

---

## ✅ Example: Overloading `+` Operator

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # This calls p1.__add__(p2)
print(p3)     # Output: (6, 8)
```

🎯 The `+` operator now **adds two `Point` objects** component-wise, thanks to the `__add__()` method.

---

## 🔧 Common Overloadable Operators

|Operator|Method|
|---|---|
|`+`|`__add__()`|
|`-`|`__sub__()`|
|`*`|`__mul__()`|
|`/`|`__truediv__()`|
|`==`|`__eq__()`|
|`!=`|`__ne__()`|
|`<`|`__lt__()`|
|`>`|`__gt__()`|
|`str()`|`__str__()`|

---

## 🎯 Interview Answer Format

> **Operator overloading** allows user-defined classes to **override Python’s built-in operator behavior** using **special methods like `__add__`, `__eq__`, etc.**
> 
> For example, in a `Point` class, we can overload `+` to add coordinates instead of throwing an error.

---

Would you like an advanced example (like overloading `==` to compare custom objects or `len()`)?
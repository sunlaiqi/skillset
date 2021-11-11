- [Python Crash Course](#python-crash-course)
- [What is Python?](#what-is-python)
- [pipenv](#pipenv)
- [Class and Object](#class-and-object)
  - [Namespace](#namespace)
  - [Scope](#scope)
  - [global/nonlocal statements](#globalnonlocal-statements)
    - [Scopes and Namespaces Example](#scopes-and-namespaces-example)
  - [Class Definition Syntax](#class-definition-syntax)
    - [Class Objects](#class-objects)
    - [Instance Objects](#instance-objects)
    - [Method Objects](#method-objects)
    - [Class and Instance Variables](#class-and-instance-variables)
    - [Name mangling](#name-mangling)
- [Command line argument parsing](#command-line-argument-parsing)
  - [Argument Parsing using sys.argv](#argument-parsing-using-sysargv)
  - [Standard Python library argparse](#standard-python-library-argparse)
    - [Quick Start](#quick-start)
    - [Positional Arguments](#positional-arguments)
    - [Optional Arguments](#optional-arguments)
    - [Multiple Input Arguments](#multiple-input-arguments)
    - [Mutually Exclusive Arguments](#mutually-exclusive-arguments)
    - [Subparsers](#subparsers)
- [Descriptor](#descriptor)
  - [What Are Python Descriptors?](#what-are-python-descriptors)
    - [Best Solution - Store In The Object](#best-solution---store-in-the-object)
  - [`__set_name__(self, owner, name)`](#__set_name__self-owner-name)
  - [Lazy Properties](#lazy-properties)
- [Generators Are Simplified Iterators](#generators-are-simplified-iterators)
  - [Generator Object](#generator-object)
    - [return vs yield](#return-vs-yield)
  - [Generator Expressions](#generator-expressions)
    - [Generator Expressions vs List Comprehensions](#generator-expressions-vs-list-comprehensions)
    - [In-line Generator Expressions](#in-line-generator-expressions)
- [Coroutines](#coroutines)
- [Iterator](#iterator)
  - [What is iterator](#what-is-iterator)
  - [Difference between iterable and iterator](#difference-between-iterable-and-iterator)
    - [How do for-in loops work in Python?](#how-do-for-in-loops-work-in-python)
  - [A Simpler Iterator Class](#a-simpler-iterator-class)
  - [A realistic example for iterable class](#a-realistic-example-for-iterable-class)
- [Metaclass](#metaclass)
  - [Defining a Class Dynamically](#defining-a-class-dynamically)
    - [Examples](#examples)
    - [Custom Metaclasses](#custom-metaclasses)
    - [Object Factory and Class Factory](#object-factory-and-class-factory)
- [Cahe - lru_cache](#cahe---lru_cache)
  - [Implementing a Cache Using a Python Dictionary](#implementing-a-cache-using-a-python-dictionary)
  - [Caching Strategies](#caching-strategies)
  - [Diving Into the Least Recently Used (LRU) Cache Strategy](#diving-into-the-least-recently-used-lru-cache-strategy)
  - [Using @lru_cache to Implement an LRU Cache in Python](#using-lru_cache-to-implement-an-lru-cache-in-python)
  - [Unpacking the Functionality of @lru_cache](#unpacking-the-functionality-of-lru_cache)
- [What is monkey patching in Python?](#what-is-monkey-patching-in-python)
- [Data Structure](#data-structure)
  - [Array Data Structures](#array-data-structures)
    - [Array](#array)
      - [Accessing Array Element](#accessing-array-element)
    - [str – Immutable Arrays of Unicode Characters](#str--immutable-arrays-of-unicode-characters)
    - [bytes – Immutable Arrays of Single Bytes](#bytes--immutable-arrays-of-single-bytes)
    - [bytearray – Mutable Arrays of Single Bytes](#bytearray--mutable-arrays-of-single-bytes)
    - [list – Mutable Dynamic Arrays](#list--mutable-dynamic-arrays)
    - [linked lists](#linked-lists)
      - [Reverse Linked List](#reverse-linked-list)
    - [tuple – Immutable Containers](#tuple--immutable-containers)
    - [collections.namedtuple – Convenient Data Objects](#collectionsnamedtuple--convenient-data-objects)
    - [typing.NamedTuple – Improved Namedtuples](#typingnamedtuple--improved-namedtuples)
  - [struct.Struct – Serialized C Structs](#structstruct--serialized-c-structs)
  - [types.SimpleNamespace – Fancy Attribute Access](#typessimplenamespace--fancy-attribute-access)
  - [Dictionaries, Maps, and Hashtables](#dictionaries-maps-and-hashtables)
    - [collections.OrderedDict – Remember the Insertion Order of Keys](#collectionsordereddict--remember-the-insertion-order-of-keys)
    - [collections.defaultdict – Return Default Values for Missing Keys](#collectionsdefaultdict--return-default-values-for-missing-keys)
    - [collections.ChainMap – Search Multiple Dictionaries as a Single Mapping](#collectionschainmap--search-multiple-dictionaries-as-a-single-mapping)
    - [types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries](#typesmappingproxytype--a-wrapper-for-making-read-only-dictionaries)
  - [set](#set)
    - [Accessing Values in a Set](#accessing-values-in-a-set)
    - [Union of Sets](#union-of-sets)
    - [Compare Sets](#compare-sets)
    - [frozenset – Immutable Sets](#frozenset--immutable-sets)
    - [collections.Counter – Multisets](#collectionscounter--multisets)
  - [Stacks (LIFOs)](#stacks-lifos)
    - [list – Simple, Built-In Stacks](#list--simple-built-in-stacks)
    - [collections.deque – Fast & Robust Stacks](#collectionsdeque--fast--robust-stacks)
    - [queue.LifoQueue – Locking Semantics for Parallel Computing](#queuelifoqueue--locking-semantics-for-parallel-computing)
  - [Queues (FIFOs)](#queues-fifos)
    - [collections.deque – Fast & Robust Queues](#collectionsdeque--fast--robust-queues)
    - [queue.Queue – Locking Semantics for Parallel Computing](#queuequeue--locking-semantics-for-parallel-computing)
    - [multiprocessing.Queue – Shared Job Queues](#multiprocessingqueue--shared-job-queues)
  - [Priority Queues](#priority-queues)
    - [list – Maintaining a Manually Sorted Queue](#list--maintaining-a-manually-sorted-queue)
    - [heapq – List-Based Binary Heaps](#heapq--list-based-binary-heaps)
    - [queue.PriorityQueue – Beautiful Priority Queues](#queuepriorityqueue--beautiful-priority-queues)


# Python Crash Course

Basically, this readme is the quick review of what I learned and read about Python. 
TO make it concise and rich enough to include necessary information. 
Following are the contents planned to be incuded.

How could Python be used?

Where to start?

Data Structure

    Numerate

Key concepts

    closure
    decorator    
    duty type
    Coroutines

Use Python as web backend

Regular expression

Debug

Coding style guide 

Tricks/tips

Best practice

System design

# What is Python?

- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. 
  - It is an interprated language without needing complilation, which makes the edit-test-debug cycle is increadibly fast.
- Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. 
- Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. 
- Python supports modules and packages, which encourages program modularity and code reuse. 
- The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.

Python is a strongly-typed and dynamically-typed language.
- Strongly-typed: Interpreter always “respects” the types of each variable.
- Dynamically-typed: “A variable is simply a value bound to a name.” 
- Execution: Python is first interpreted into bytecode (.pyc) and then compiled by a VM implementation into machine instructions. (Most commonly using C.)

Strongly-typed: `1 + ‘1’` → Error!

Dynamically-typed: `foo = [1,2,3]` ...later... `foo = ‘hello!’`

Tokens
Smallest units of any programming languages are called Tokens (Lexical Unit). Python tokens are:
- Keywords
- Identifiers (Names)
- Literals (oftern called Constant Values)
- Operators
- Punctuators


# pipenv

pipenv is a packaging tool for Python that solves some common problems associatd with the typical workflow using piv, vitrualevn and the goold old requirements.txt. In addition to addressing some common issues, it consolidates and simplifies the development process to a single command line tool.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the eveer-important Pipfile.lock, which is used to produce deterministric builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment.

The problems that Pipenv seeks to solve are multi-faceted:

- You no longer need to use `pip` and `virtualenv` separately. They work together.
- Managing a `requirements.txt` file can be problematic, so `Pipenv` uses `Pipfile` and `Pipfile.lock` to separate abstract dependency declarations from the last tested combination.
- Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
- Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.
- Give you insight into your dependency graph (e.g. `$ pipenv graph`).
- Streamline development workflow by loading `.env` files.

If you’re on MacOS, you can install Pipenv easily with Homebrew:
```bash
$ brew install pipenv
```

Basic Concepts
- A virtualenv will automatically be created, when one doesn’t exist.
- When no parameters are passed to install, all packages [packages] specified will be installed.
- To initialize a Python 3 virtual environment, run `$ pipenv --three`.
- To initialize a Python 2 virtual environment, run `$ pipenv --two`.
- Otherwise, whatever `virtualenv` defaults to will be the default.

Other Commands
- `graph` will show you a dependency graph of your installed dependencies.
- `shell` will spawn a shell with the virtualenv activated.
- `run` will run a given command from the virtualenv, with any arguments forwarded (e.g. `$ pipenv run python` or $ `pipenv run pip freeze`).
- `check` checks for security vulnerabilities and asserts that PEP 508 requirements are being met by the current environment.

# Class and Object

## Namespace

A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries. Examples of namespaces are: the set of built-in names (containing functions such as `abs()`, and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. 

Namespaces are created at different moments and have different lifetimes. 
- The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. 
- The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. 
- The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called `__main__`, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.)
- The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. 

## Scope

A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

## global/nonlocal statements
The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.

A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for deletions:the statement *del x* removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.

### Scopes and Namespaces Example
This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:
```python
def scope_test():
    def do_local():
        spam = "local spam" ## Local scope

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam" ## Enclosing scope

    def do_global():
        global spam
        spam = "global spam" ## Global scope

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
The output of the example code is:
```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
Note how the *local* assignment (which is default) didn’t change scope_test’s binding of spam. The *nonlocal* assignment changed scope_test’s binding of spam, and the *global* assignment changed the module-level binding.
You can also see that there was no previous binding for spam before the *global* assignment.

## Class Definition Syntax
**Official definition**:
A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.

```python
class ClassName: 
    <statement-1>
    .
    .
    .
    <statement-N>
```
When a class definition is left normally (via the end), a class object is created. Rememer, everything in Python is object.

### Class Objects

Class objects support two kinds of operations: attribute references and instantiation.
Attribute references use the standard syntax used for all attribute references in Python: `obj.name`. Valid attribute names are all the names that were in the class’s namespace when the class object was created. 
Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. 
```py
x = MyClass()
```
creates a new instance of the class and assigns this object to the local variable x.

### Instance Objects

The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.

### Method Objects

Instance method objects have attributes, too: `m.__self__` is the instance object with the method `m()`, and `m. __func__` is the function object corresponding to the method.

### Class and Instance Variables

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class. 
Correct design of the class should use an instance variable instead.
Each value is an object, and therefore has a class (also called its type). It is stored as `object.__class__`.

### Name mangling

In name mangling process, any identifier with two leading underscore and one trailing underscore is textually replaced with `_classname__identifier` where classname is the name of the current class. It means that any identifier of the form `__geek` (at least two leading underscores or at most one trailing underscore) is replaced with `_classname__geek`, where classname is the current class name with leading underscore(s) stripped.

```py
# Python program to demonstrate
# name mangling


class Student:
	def __init__(self, name):
		self.__name = name

	def displayName(self):
		print(self.__name)

s1 = Student("Santhosh")
s1.displayName()

# Raises an error
print(s1.__name)
```
Output
```
Santhosh
Traceback (most recent call last):
  File "/home/be691046ea08cd2db075d27186ea0493.py", line 14, in 
    print(s1.__name)
AttributeError: 'Student' object has no attribute '__name'
```
In the above example, the class variable `__name` is not accessible outside the class. **It can be accessed only within the class**. Any modification of the class variable can be done only inside the class.

**Name mangling process**

With the help of `dir()` method, we can see the name mangling process that is done to the class variable. **The name mangling process was done by the Interpreter**. The `dir()` method is used by passing the class object and it will return all valid attributes that belong to that object.

**Accessing Name Mangled variables**

The name mangling process helps to access the class variables from outside the class. The class variables can be accessed by adding `_classname` to it. The name mangling is closest to private not exactly private.

```py
# Python program to demonstrate
# name mangling


class Student:
	def __init__(self, name):
		self.__name = name

s1 = Student("Santhosh")
print(s1._Student__name)
```

**Name mangling with method overriding**

Due to name mangling, there is limited support for a valid use-case for class-private members basically to avoid name clashes of names with names defined by subclasses. This is helpful for letting subclasses override methods without breaking intraclass method calls.
Let’s look at this example and try to find out how this underscore works:
```py
# Python code to illustrate how mangling works
# With method overriding

class Map:
	def __init__(self):
		self.__geek()
		
	def geek(self):
		print("In parent class")
	
	# private copy of original geek() method
	__geek = geek	
	
class MapSubclass(Map):
		
	# provides new signature for geek() but
	# does not break __init__()
	def geek(self):		
		print("In Child class")
		
# Driver's code
obj = MapSubclass()
obj.geek()
```
Output:
```
In parent class
In Child class
```

# Command line argument parsing

## Argument Parsing using sys.argv


```python
import sys

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))
```

- You first imported the Python module `sys`, which comes with a standard installation of Python. 
- You then employed the `argv` submodule which returns the list of the arguments passed to a Python script where `argv[0]` contains the name of the Python script. 

For example, if you execute `python demo1.py abc 123`, then the program would yield -
```
Number of arguments: 3
Argument(s) passed: ['demo1.py', 'abc', '123']
```

## Standard Python library argparse 

### Quick Start

```py
# Import the library
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--name', type=str, required=True)

# Parse the argument
args = parser.parse_args()

# Print "Hello" + the user input argument
print('Hello,', args.name)
````
```bash
$ python hello.py
usage: hello.py [-h] --name NAME
hello.py: error: the following arguments are required: --name
```
### Positional Arguments

**multiply.py — Without Positional Arguments**

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int, required=True)
parser.add_argument('--y', type=int, required=True)
args = parser.parse_args()
product = args.x * args.y
print('Product:', product)
```
Output
```bash
$ python multiply.py --x 4 --y 5
Product: 20
```

**multiply_with_positional.py — With Positional Arguments**
```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help='The first value to multiply')
parser.add_argument('y', type=int, help='The second value to multiply')
args = parser.parse_args()
product = args.x * args.y
print('Product:', product)
```
Output
```bash
$ python multiply_with_positional.py 4 5
Product: 20
```
```bash
$ python multiply.py -h
usage: multiply.py [-h] x y
positional arguments:
x           The first value to multiply
y           The second value to multiply

```

### Optional Arguments

Optional arguments are useful if you want to give the user a choice to enable certain features. To add an optional argument, simply omit the `required` parameter in `add_argument()`.

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--age', type=int)
args = parser.parse_args()
if args.age:
  print(args.name, 'is', args.age, 'years old.')
else:
  print('Hello,', args.name + '!')
```
```bash
$ python optional.py 
usage: optional.py [-h] --name NAME [--age AGE]
optional.py: error: the following arguments are required: --name
```

### Multiple Input Arguments

Using the `nargs` parameter in `add_argument()`, you can specify the number (or arbitrary number) of inputs the argument should expect.
In this example named `sum.py`, the `--value` argument takes in 3 integers and will print the sum.
```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--values', type=int, nargs=3)
args = parser.parse_args()
sum = sum(args.values)
print('Sum:', sum)
```
Output
```bash
$ python sum.py --values 1 2 3
Sum: 6
```
What if you don’t want just 3 values, but any number of inputs? You can set `nargs='+'`, which will allow the argument to take in any number of values. 

### Mutually Exclusive Arguments

The method `add_mutually_exclusive_group()` adds **a group of arguments** that are mutually exclusive (cannot be used at the same time).
```py
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group() # Create a group of arguments
group.add_argument('--add', action='store_true')
group.add_argument('--subtract', action='store_true')
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()
if args.add:
  sum = args.x + args.y
  print('Sum:', sum)
elif args.subtract:
  difference = args.x - args.y
  print('Difference:', difference)
```

- By creating a group with `group = parser.add_mutually_exclusive_group()`, the user is only allowed to select one of the arguments to use. 
- In the `add_argument()` method, there is a new parameter called `action`. This is simply storing the default method if the argument is blank.

### Subparsers

Subparsers are created for subcommands in some cases. For example, git command has different subcommands, like `git checkout` and `git commit`, in which `checkout` and `commit` are subcommands.

```py
import argparse
parser = argparse.ArgumentParser()

# Create a subparser
subparser = parser.add_subparsers(dest='command') 
# Add two subparsers (subcommands) 'login' and 'register'
login = subparser.add_parser('login')
register = subparser.add_parser('register')
# Add arguments for each subparser
login.add_argument('--username', type=str, required=True)
login.add_argument('--password', type=str, required=True)
register.add_argument('--firstname', type=str, required=True)
register.add_argument('--lastname', type=str, required=True)
register.add_argument('--username', type=str, required=True)
register.add_argument('--email', type=str, required=True)
register.add_argument('--password', type=str, required=True)

args = parser.parse_args()
# Handle with different subparsers
if args.command == 'login':
  print('Logging in with username:', args.username,
  'and password:', args.password)
elif args.command == 'register':
  print('Creating username', args.username,
  'for new member', args.firstname, args.lastname,
  'with email:', args.email,
  'and password:', args.password)
```

Here, we added `subparser = parser.add_subparsers(dest='command')`. 
- This is used to create the subparser, and the `dest='command'` is used to differentiate between which argument is actually used. 
- You can see in the if statement that we distinguish between “login” and “register” with args.command.

**Login**
```bash
$ python user.py login --username D0loresh4ze --password whoismrrobot
Logging in with username: D0loresh4ze and password: whoismrrobot
```

**Register**
```bash
$ python user.py register --firstname Dolores --lastname Haze --username Doloresh4ze --email dhaze@ecorp.com --password whoismrrobot
Creating username Doloresh4ze for new member Dolores Haze with email: dhaze@ecorp.com and password: whoismrrobot
```

# Descriptor

## What Are Python Descriptors?

Descriptors are Python objects that implement a method of the **descriptor protocol**, which gives you the ability to create objects that have special behavior when they’re accessed as attributes of other objects. Here you can see the correct definition of the descriptor protocol:
```py
__get__(self, obj, type=None) -> object 
__set__(self, obj, value) -> None 
__delete__(self, obj) -> None 
__set_name__(self, owner, name)
```
- If your descriptor implements just .`__get__()`, then it’s said to be a **non-data descriptor**. 
- If it implements .`__set__() or .__delete__()`, then it’s said to be a **data descriptor**. 

Take a look at the following example, which defines a descriptor that logs something on the console when it’s accessed:
```python
# descriptors.py
class Verbose_attribute():
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None) -> object: 
        print("accessing the attribute to get the value") 
        return self.value
        
    def __set__(self, obj, value) -> None: 
        print("accessing the attribute to set the value") 
        self.value = value

class Foo():
    attribute1 = Verbose_attribute(6)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
my_foo_object.attribute1 = 5
x = my_foo_object.attribute1
print(x)
```
In the example above, `Verbose_attribute()` implements the descriptor protocol. Once it’s instantiated as an attribute of Foo, it can be considered a descriptor.

When you implement the protocol, keep these things in mind:
- `self` is the instance of the descriptor you’re writing.
- `obj` is the instance of the object your descriptor is attached to. 
- `type` is the type of the object the descriptor is attached to.
  - In `__set__()`, you don’t have the type variable, because you can only call `__set__()` on the **object**. In contrast, you can call `__get__()` on both the object and the class.

- Shared Descriptor Instance
  - Another important thing to know is that Python descriptors are instantiated just once per class. 
  - That means that every single instance of a class containing a descriptor shares that descriptor instance. 
  - This is something that you might not expect and can lead to a classic pitfall.

### Best Solution - Store In The Object

The best solution here is to simply not store values in the descriptor itself, but to store them in the object that the descriptor is attached to. Try this approach next:
```python
# descriptors4.py
class OneDigitNumericValue():
    def __init__(self, name): 
        self.name = name
    def __get__(self, obj, type=None) -> object: 
        return obj.__dict__.get(self.name) or 0
    def __set__(self, obj, value) -> None: 
        obj.__dict__[self.name] = value
class Foo():
    number = OneDigitNumericValue("number")
my_foo_object = Foo() 
my_second_foo_object = Foo()
my_foo_object.number = 3 
print(my_foo_object.number) 
print(my_second_foo_object.number)
my_third_foo_object = Foo() 
print(my_third_foo_object.number)
```

In this example, when you set a value to the number attribute of your object, the descriptor stores it in the `__dict__` attribute of the object it’s attached to using the same name of the descriptor itself.
The only problem here is that when you instantiate the descriptor you have to specify the `name` as a parameter:
```python
number = OneDigitNumericValue(“number")
```
Wouldn’t it be better to just write `number = OneDigitNumericValue()`? It might, but if you’re running a version of Python less than 3.6, then you’ll need a little bit of magic here with metaclasses and decorators. If you use Python 3.6 or higher, however, then the descriptor protocol has a new method .`__set_name__()` that does all this magic for you, as proposed in PEP 487:

## `__set_name__(self, owner, name)`

With this new method, whenever you instantiate a descriptor this method is called and the `name` parameter automatically set.
Now, try to rewrite the former example for Python 3.6 and up:
```python
# descriptors5.py
class OneDigitNumericValue():
    def __set_name__(self, owner, name): 
        self.name = name
    def __get__(self, obj, type=None) -> object: 
        return obj.__dict__.get(self.name) or 0
    def __set__(self, obj, value) -> None: 
        obj.__dict__[self.name] = value
class Foo():
    number = OneDigitNumericValue()
my_foo_object = Foo() 
my_second_foo_object = Foo()
my_foo_object.number = 3 
print(my_foo_object.number) 
print(my_second_foo_object.number)
my_third_foo_object = Foo() 
print(my_third_foo_object.number)
```

## Lazy Properties

The first and most straightforward example is lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time. Then, they load their initial value and keep that value cached for later reuse.
Consider the following example. You have a class DeepThought that contains a method meaning_of_life() that returns a value after a lot of time spent in heavy concentration:
```python
# slow_properties.py 
import random 
import time
class DeepThought:
    def meaning_of_life(self):
        time.sleep(3) 
        return 42
my_deep_thought_instance = DeepThought() 
print(my_deep_thought_instance.meaning_of_life()) 
print(my_deep_thought_instance.meaning_of_life()) 
print(my_deep_thought_instance.meaning_of_life())
```
If you run this code and try to access the method three times, then you get an answer every three seconds, which is the length of the sleep time inside the method.
Now, a lazy property can instead evaluate this method just once when it’s first executed. Then, it will cache the resulting value so that, if you need it again, you can get it in no time. You can achieve this with the use of Python descriptors:

```python
# lazy_properties.py 
import random 
import time
class LazyProperty:
    def __init__(self, function):
        self.function = function 
        self.name = function.__name__
    def __get__(self, obj, type=None) -> object: 
        obj.__dict__[self.name] = self.function(obj) 
        return obj.__dict__[self.name]

class DeepThought: 
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3) 
        return 42
my_deep_thought_instance = DeepThought() 
print(my_deep_thought_instance.meaning_of_life) 
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
```

In this example, when you use the @LazyProperty descriptor, you’re instantiating a descriptor and passing to it `meaning_of_life()`. This descriptor stores both the method and its name as instance variables.

- Since it is a non-data descriptor, when you first access the value of
the `meaning_of_life` attribute, `__get__()` is automatically called and executes `meaning_of_life()` on the `my_deep_thought_instance` object. 
The resulting value is stored in the `__dict__` attribute of the object itself. 
When you access the `meaning_of_life attribute` again, Python will use the lookup chain to find a value for that attribute inside the `__dict__` attribute, and that value will be returned immediately.

Note that this works because, in this example, you’ve only used one method `__get__()` of the descriptor protocol. You’ve also implemented a non-data descriptor. If you had implemented a data descriptor, then the trick would not have worked. 

# Generators Are Simplified Iterators

## Generator Object

A very simple generator:
```python
def repeater(value): 
    while True:
        yield value
for x in repeater('Hi'):
    print(x)

# Use next()
generator_obj = repeater('Hey')
print(next(generator_obj))
# Hey
```
As you can see, a generator is an iterator automatically without using `iter()` to convert it.

You can think generators as syntactic sugar for implementing iterators. You’ll find that for most types of iterators, writing a generator function will be easier and more readable than defining a long-winded class- based iterator.

### return vs yield

when a `return` statement is invoked inside a function, it permanently passes control back to the caller of the function. When a `yield` is invoked, it also passes control back to the caller of the function—but it only does so temporarily.

Whereas a `return` statement disposes of a function’s local state, a `yield` statement suspends the function and retains its local state.

## Generator Expressions

You see, class-based iterators and generator functions are two expressions of the same underlying design pattern.

Here’s an example:
```python
iterator = ('Hello' for i in range(3))
```

**Note**:
Once a generator expression has been consumed, it can’t be restarted or reused. So in some cases there is an advantage to using generator functions or class-based iterators.

### Generator Expressions vs List Comprehensions

```python
 >>> listcomp = ['Hello' for i in range(3)] 
 >>> genexpr = ('Hello' for i in range(3))
 >>> list(genexpr)
['Hello', 'Hello', 'Hello']
 ```

### In-line Generator Expressions

```python
for x in ('Bom dia' for i in range(3)): 
    print(x)
```

# Coroutines

Normally, functions operate on a single set of input arguments. However, a function can also be written to operate as a task that processes a sequence of inputs sent to it. This type of function is known as a `coroutine` and is created by using the `yield` statement as an expression `(yield)` as shown in this example:
```py
def print_matches(matchtext): 
  print("Looking for", matchtext)
  while True:
    line = (yield) # Get a line of text 
    if matchtext in line:
      print line
```
To use this function, you first call it, advance it to the first `(yield)`, and then start
sending data to it using `send()`. For example:

```py
>>> matcher = print_matches("python")
>>> matcher.next() # Advance to the first (yield) 
Looking for python
>>> matcher.send("Hello World")
>>> matcher.send("python is cool")
python is cool
>>> matcher.send("yow!")
>>> matcher.close() # Done with the matcher function call 
>>>
```

- A coroutine is suspended until a value is sent to it using `send()`. 
- When this happens, that value is returned by the `(yield)` expression inside the coroutine and is processed by the statements that follow. 
- Processing continues until the next `(yield)` expression is encountered — at which point the function suspends.
- This continues until the coroutine function returns or `close()` is called on it as shown in the previous example.

Coroutines are useful when writing concurrent programs based on **producer-consumer** problems where one part of a program is producing data to be consumed by another part of the program. 

# Iterator

## What is iterator

You’ll find the answers to these questions in Python’s iterator protocol: Objects that support the `__iter__` and `__next__` dunder methods automatically work with for-in loops, or the Python object is iterable.

## Difference between iterable and iterator

An object is iterable, meaning it could be iterated over by for-in loop. But it doesn't mean it is an iterator.

For example, a list is iterable but not an iterator.

```python
>>> my_list = [1, 2, 3]
>>> next(my_list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
>>> iterator = iter(my_list)
1
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
As we can see, in order to use `next()` built-in, we need to make sure the object is an iterator, usually being converted by another built-in `iter()`.

### How do for-in loops work in Python?

A simple iterator example:

```python
class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value
# Here is the iterator instance
repeater = Repeater('Hello')
for i in repeater:
    print(i)
    
# Following is what for-in is doing.
repeater = Repeater('Hello') 
iterator = repeater.__iter__() 
while True:
    item = iterator.__next__() 
    print(item)

# You can use iter to convert the object into iterator
# You can see built-in next() and iter() act the same as __next__ and __iter__
iterator = iter(repeater)
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

As you can see, the for-in was just syntactic sugar for a simple while loop:
- It first prepared the repeater object for iteration by calling its `__iter__` method. This returned the actual iterator object.
- After that, the loop repeatedly called the iterator object’s `__next__` method to retrieve values from it.

Also you can see, the calls to `__iter__` and `__next__` with could be replaced with calls to Python’s built-in functions, `iter()` and `next()`.

## A Simpler Iterator Class

Up until now, our iterator example consisted of two separate classes, `Repeater` and `RepeaterIterator`. They corresponded directly to the two phases used by Python’s iterator protocol:
First, setting up and retrieving the iterator object with an `iter()` call, and then repeatedly fetching values from it via `next()`.
```python
class Repeater:
    def __init__(self, value):
        self.value = value 
    def __iter__(self):
        return self
    def __next__(self): 
        return self.value

repeater = Repeater('Hello')

for item in repeater:
    print(item)

```

## A realistic example for iterable class
 
```python
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value 
        self.max_repeats = max_repeats 
        self.count = 0
    def __iter__(self): 
        return self
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration 
        self.count += 1
        return self.value

repeater = BoundedRepeater('Hello', 3)
for item in repeater:
    print(item)
```

# Metaclass

In general, the type of any new-style class is `type`.
The type of the built-in classes you are familiar with is also `type`.

`type` is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass.

`type` is also an instance of the `type` metaclass, so it is an instance of itself.

## Defining a Class Dynamically

You can also call type() with three arguments — `type(<name>, <bases>, <dct>)`:
- `<name>` specifies the class name. This becomes the `__name__` attribute of the class.
- `<bases>` specifies a tuple of the base classes from which the class inherits. This becomes the `__bases__` attribute of the class.
- `<dct>` specifies a namespace dictionary containing definitions for the class body. This becomes the `__dict__` attribute of the class.

Calling `type()` in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

### Examples

```python
def f(obj):
    print('attr =', obj.attr)

Foo = type('Foo', (),{
    'attr': 100,
    'attr_val': f
    })

x = Foo()
print(x.attr)
print(x.attr_val())
```
```
100
attr = 100
None???
```

### Custom Metaclasses

Consider again this well-worn example:
```py
class Foo():
  pass

foo = Foo()
```

When the interpreter encounters `Foo()`, the following occurs:
- The `__call__()` method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class is the `type` metaclass, so type’s `__call__()` method is invoked.
- That `__call__()` method in turn invokes the following:
  ```python
  __new__() 
  __init__()
  ```

In the following, a custom method called `new()` is defined and assigned as the `__new__()` method for Foo:
```python
class Foo: 
    pass

def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

Foo.__new__ = new
f = Foo()
print(f.attr)
```

Define a metaclass from `type`:
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct) 
        x.attr = 100
        return x

class Foo(metaclass=Meta):
    pass

print(Foo.attr)
```
Since `type` is a metaclass, that makes `Meta` a metaclass as well.
Delegates via `super()` to the `__new__()` method of the parent metaclass (type) to actually create a new class.
Assigns the custom attribute attr to the class, with a value of 100.
Returns the newly created class.

### Object Factory and Class Factory

In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template for the creation of classes. Metaclasses are sometimes referred to as class factories.
Compare the following two examples:
```python
# Object Factory
class Foo:
    def __init__(self):
        self.attr = 100
x = Foo()
print(x.attr)
y = Foo()
print(y.attr)

class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100
# Class Factory
class X(metaclass=Meta):
    pass
print(X.attr)
class Y(metaclass=Meta):
    pass
print(Y.attr)
```

# Cahe - lru_cache

## Implementing a Cache Using a Python Dictionary

```python
import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
```

## Caching Strategies
There’s one big problem with this cache implementation: the content of the dictionary will grow indefinitely! 
To work around this issue, you need a strategy to decide which articles should stay in memory and which should be removed. 

## Diving Into the Least Recently Used (LRU) Cache Strategy

Every time you access an entry, the LRU algorithm will move it to the top of the cache.

One way to implement an LRU cache in Python is to use a combination of a doubly linked list and a hash map. The `head` element of the doubly linked list would point to the most recently used entry, and the `tail` would point to the least recently used entry.

Using the hash map, you can ensure access to every item in the cache by mapping each entry to the specific location in the doubly linked list.

This strategy is very fast. Accessing the least recently used item and updating the cache are operations with a runtime of O(1).

## Using @lru_cache to Implement an LRU Cache in Python

Just like the caching solution you implemented earlier, `@lru_cache` uses a dictionary behind the scenes. It caches the function’s result under a key that consists of the call to the function, including the supplied arguments. This is important because it means that these arguments have to be **hashable** for the decorator to work.

Run following program will se huge performance difference between with `@lru_cache` and without `@lru_cache`.

```python
from timeit import repeat
from functools import lru_cache

@lru_cache
def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times.
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, then one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 2. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )

setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")
```

## Unpacking the Functionality of @lru_cache

With the `@lru_cache` decorator in place, you store every call and answer in memory to access later if requested again. But how many calls can you save before running out of memory?

Python’s `@lru_cache` decorator offers a `maxsize` attribute that defines the maximum number of entries before the cache starts evicting old items. By default, `maxsize` is set to 128. If you set `maxsize` to None, then the cache will grow indefinitely, and no entries will be ever evicted. 

In this case, you’re limiting the cache to a maximum of 16 entries. When a new call comes in, the decorator’s implementation will evict the least recently used of the existing 16 entries to make a place for the new item.

To see what happens with this new addition to the code, you can use `cache_info()`, provided by the `@lru_cache` decorator, to inspect the number of hits and misses and the current size of the cache. 

```python
print(steps_to(30))
print(steps_to.cache_info())
```
```
53798080
CacheInfo(hits=52, misses=30, maxsize=16, currsize=16)
```

# What is monkey patching in Python?

The process to dynamically change a class or module at run-time is known as Monkey Patching.

# Data Structure

- Dictionary
- List
- Dequeue
- Tree
- Graph

## Array Data Structures

Arrays consist of fixed-size data records that allow each element to be efficiently located based on its index.
Because arrays store information in adjoining blocks of memory, they’re considered contiguous data structures (as opposed to linked datas structure like linked lists, for example.)

Python includes several array-like data structures in its standard li- brary that each have slightly different characteristics. 

### Array

Python’s array module provides space-efficient storage of basic C- style data types like bytes, 32-bit integers, floating point numbers, and so on.

Arrays created with the array.array class are mutable and behave similarly to lists, except for one important difference—they are “typed arrays” constrained to a single data type.

Because of this constraint, array.array objects with many elements are more space-efficient than lists and tuples. 

Also, arrays support many of the same methods as regular lists, and you might be able to use them as a “drop-in replacement” without requiring other changes to your application code.

```python
from array import *
arrayName = array(typecode, [Initializers])
```
Typecode    |	Value
---         |   ---
b   |	Represents signed integer of size 1 byte
B	|   Represents unsigned integer of size 1 byte
c   |	Represents character of size 1 byte
i   |	Represents signed integer of size 2 bytes
I   |	Represents unsigned integer of size 2 bytes
f   |	Represents floating point of size 4 bytes
d   |	Represents floating point of size 8 bytes

```python
from array import *
array1 = array('i', [10,20,30,40,50])
for x in array1:
    print(x)
```

#### Accessing Array Element

We can access each element of an array using the index of the element. The below code shows how
```python
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])
array1.insert(1,60)
array1.remove(40)
print (array1.index(40))
array1[2] = 80
```

### str – Immutable Arrays of Unicode Characters

Oddly enough, it’s also a re- cursive data structure—each character in a string is a str object of length 1 itself.

String objects are space-efficient because they’re tightly packed and they specialize in a single data type. If you’re storing Unicode text, you should use them. 

### bytes – Immutable Arrays of Single Bytes

Bytes objects are immutable sequences of single bytes (integers in the rangeof0<=x<=255). Conceptually,they’resimilartostrobjects, and you can also think of them as immutable arrays of bytes.

unlike strings, there’s a dedicated “mutable byte array” data type called bytearray that they can be unpacked into. You’ll hear more about that in the next section.

```python
>>> arr = bytes((0, 1, 2, 3)) 
>>> arr[1]
1
```

### bytearray – Mutable Arrays of Single Bytes

The bytearray type is a mutable sequence of integers in the range 0 <= x <= 255.
```python
>>> arr = bytearray((0, 1, 2, 3)) 
>>> arr[1]
1

# Bytearrays can be converted back into bytes objects: # (This will copy the data)
>>> bytes(arr)
b'x00x02x03*'
```


### list – Mutable Dynamic Arrays

Despite their name, Python’s lists are implemented as dynamic arrays behind the scenes. This means a list allows elements to be added or removed, and the list will automatically adjust the backing store that holds these elements by allocating or releasing memory.

**Delete List Elements**

To remove a list element, you can use either the del statement if you know exactly which element(s) you are 
deleting or the remove() method if you do not know. For example −
```python
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)
```

### linked lists



#### Reverse Linked List


![Reverse Linked List](../Images/Reverse_linked_list.gif)


### tuple – Immutable Containers

The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
To write a tuple containing a single value you have to include a comma, even though there is only one value. Otherwise, it will be evaluated as a single value.

tup1 = (50,);

### collections.namedtuple – Convenient Data Objects

Namedtuples are immutable, just like regular tuples. T

Namedtuple objects are implemented as regular Python classes inter- nally. Namedtuples make the data that’s being passed around “self-documenting”, at least to a degree.
```python
from collections import namedtuple 
p1 = namedtuple('Point', 'x y z')(1, 2, 3) 
print(p1)
# Or
P = namedtuple('Point', 'x y z')
p2 = P(1, 2, 3)
print(p2)
# Point(x=1, y=2, z=3)
```

### typing.NamedTuple – Improved Namedtuples

It is very simi- lar to namedtuple, the main difference being an updated syntax for defining new record types and added support for type hints.
```python
from typing import NamedTuple
class Car(NamedTuple): 
    color: str 
    mileage: float
    automatic: bool
car1 = Car('red', 3812.4, True)
# Instances have a nice repr:
print(car1)
# Car(color='red', mileage=3812.4, automatic=True)
```

## struct.Struct – Serialized C Structs

The struct.Struct class converts between Python values and C structs serialized into Python bytes objects. For example, it can be used to handle binary data stored in files or coming in from network connections.

## types.SimpleNamespace – Fancy Attribute Access

This means you can use obj.key “dotted” attribute access instead of the obj['key'].

## Dictionaries, Maps, and Hashtables

Dictionaries are also often called maps, hashmaps, lookup tables, or associative arrays. They allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

Properties of Dictionary Keys:

- (a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. 
- (b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. 

O(1) time complexity for lookup, insert, update, and delete operations in the average case.

### collections.OrderedDict – Remember the Insertion Order of Keys

```python
>>> import collections
>>> d = collections.OrderedDict(one=1, two=2, three=3)
>>> d
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
>>> d['four'] = 4
>>> d
OrderedDict([('one', 1), ('two', 2),('three', 3), ('four', 4)]) 
>>> d.keys()
odict_keys(['one', 'two', 'three', 'four'])
```

### collections.defaultdict – Return Default Values for Missing Keys

```python
>>> from collections import defaultdict 
>>> dd = defaultdict(list)
```

### collections.ChainMap – Search Multiple Dictionaries as a Single Mapping

```python
>>> from collections import ChainMap 
>>> dict1 = {'one': 1, 'two': 2}
>>> dict2 = {'three': 3, 'four': 4} 
>>> chain = ChainMap(dict1, dict2)
>>> chain
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails): 
>>> chain['three']
3
>>> chain['one']
1
>>> chain['missing']
KeyError: 'missing'
```

### types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries

```python
>>> from types import MappingProxyType
>>> writable = {'one': 1, 'two': 2}
>>> read_only = MappingProxyType(writable)
# The proxy is read-only:
>>> read_only['one']
1
>>> read_only['one'] = 23
TypeError:
"'mappingproxy' object does not support item assignment"
# Updates to the original are reflected in the proxy:
>>> writable['one'] = 42
>>> read_only
mappingproxy({'one': 42, 'two': 2})
```

## set

Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical definition with below additional conditions.
- The elements in the set cannot be duplicates.
- The set type is mutable and allows for the dynamic insertion and deletion of ele- ments.
- There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.
- Be careful: To create an empty set you’ll need to call the set() constructor. 
### Accessing Values in a Set

We cannot access individual values in a set. We can only access all the elements together as shown above. But we can also get a list of individual elements by looping through the set.
```python 
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
for d in Days:
	print(d)

Days.add("Sun")
Days.discard("Sun")
```

### Union of Sets

The union operation on two sets produces a new set containing all the distinct elements from both the sets. 
In the below example the element “Wed” is present in both the sets.
```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

#{'Sun', 'Fri', 'Mon', 'Wed', 'Sat', 'Tue', 'Thu'}

# Intersection of Sets
AllDays = DaysA & DaysB
print(AllDays)

# {'Wed'}

# Difference of Sets
AllDays = DaysA - DaysB

```
### Compare Sets

We can check if a given set is a subset or superset of another set. The result is True or False depending on the elements present in the sets.

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
```
When the above code is executed, it produces the following result.

True
True

### frozenset – Immutable Sets

Because frozensets are static and hashable, they can be used as dictionary keys or as elements of another set, something that isn’t possible with regular (mutable) set objects.

### collections.Counter – Multisets

Implements a multiset (or bag) type that allows elements in the set to have more than one occurrence.
```python
>>> from collections import Counter >>> inventory = Counter()
>>> loot = {'sword': 1, 'bread': 3} >>> inventory.update(loot)
>>> inventory
Counter({'bread': 3, 'sword': 1})
>>> more_loot = {'sword': 1, 'apple': 1}
>>> inventory.update(more_loot)
>>> inventory
Counter({'bread': 3, 'sword': 2, 'apple': 1})

>>> len(inventory)
3 # Unique elements
>>> sum(inventory.values()) 
6 # Total no. of elements
```

## Stacks (LIFOs)


Performance-wise, a proper stack implementation is expected to take O(1) time for insert and delete operations.

several stack implementations:

### list – Simple, Built-In Stacks

Push and pop operations are in amortized O(1) time.
Their performance are less consistent than the stable O(1) inserts and deletes provided by a linked list based implementation (like collections.deque)
To get the amortized O(1) performance for inserts and deletes, new items must be added to the end of the list with the `append()` method and removed again from the end using `pop()`. 

### collections.deque – Fast & Robust Stacks

The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized). Thus, they can serve both as queues and as stacks.

### queue.LifoQueue – Locking Semantics for Parallel Computing

This stack implementation in the Python standard library is synchro- nized and provides locking semantics to support multiple concurrent producers and consumers.

## Queues (FIFOs)

Performance-wise, a proper queue implementation is expected to take O(1) time for insert and delete operations.

Queues have a wide range of applications in algorithms and often help solve scheduling and parallel programming problems. A short and beautiful algorithm using a queue is breadth-first search (BFS) on a tree or graph data structure.

### collections.deque – Fast & Robust Queues
The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non- amortized). 
Python’sdequeobjectsareimplementedasdoubly-linkedlists.

### queue.Queue – Locking Semantics for Parallel Computing
This queue implementation in the Python standard library is synchro- nized and provides locking semantics to support multiple concurrent producers and consumers.

### multiprocessing.Queue – Shared Job Queues
This is a shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers. Process-based parallelization is popular in CPython due to the global interpreter lock (GIL) that prevents some forms of parallel execution on a single interpreter process.
As a specialized queue implementation meant for sharing data between processes, `multiprocessing.Queue` makes it easy to distribute work across multiple processes in order to work around the GIL limitations. This type of queue can store and transfer any pickleable object across process boundaries.

## Priority Queues

A priority queue is a container data structure that manages a set of records with totally-ordered keys (for example, a numeric weight value) to provide quick access to the record with the smallest or largest key in the set.

You can think of a priority queue as a modified queue: instead of re- trieving the next element by insertion time, it retrieves the highest- priority element.

Implement Priority Queues in Python

### list – Maintaining a Manually Sorted Queue

You can use a sorted list to quickly identify and delete the smallest
or largest element. The downside is that inserting new elements into a list is a slow O(n) operation.

### heapq – List-Based Binary Heaps

This is a binary heap implementation usually backed by a plain list, and it supports insertion and extraction of the smallest element in O(log n) time.
```python
import heapq 
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
while q:
    next_item = heapq.heappop(q) 
    print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
```

### queue.PriorityQueue – Beautiful Priority Queues

PriorityQueue is synchronized and provides locking semantics to support multiple concurrent producers and con- sumers.

In any case, you might prefer the class-based interface provided by PriorityQueue over using the function-based interface provided by heapq.



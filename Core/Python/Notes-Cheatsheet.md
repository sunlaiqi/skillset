
- [Comments](#comments)
- [Code Blocks](#code-blocks)
- [Line breaks](#line-breaks)
- [Naming conventions](#naming-conventions)
- [Basic object types (not a complete list)](#basic-object-types-not-a-complete-list)
- [Operators](#operators)
- [Modules](#modules)
- [Often used modules](#often-used-modules)
- [Flow control](#flow-control)
  - [If - flow control](#if---flow-control)
  - [For - flow control](#for---flow-control)
  - [While - flow control](#while---flow-control)
  - [Ternary statement](#ternary-statement)
  - [Some useful adjuncts](#some-useful-adjuncts)
  - [Exceptions - flow control](#exceptions---flow-control)
- [Objects and variables (AKA identifiers)](#objects-and-variables-aka-identifiers)
- [Boolean and truthiness](#boolean-and-truthiness)
- [Comparisons](#comparisons)
- [Tuples](#tuples)
- [String (imutable, ordered, charaters)](#string-imutable-ordered-charaters)
  - [Old school string formatting (using % oper)](#old-school-string-formatting-using--oper)
  - [str.format()](#strformat)
  - [f-String](#f-string)
- [List（mutable， indexed, ordered container)](#listmutable-indexed-ordered-container)
- [Set (unique unordered container)](#set-unique-unordered-container)
- [Dictionary (indexed, unordered map - container)](#dictionary-indexed-unordered-map---container)
- [Key Functions (not a complete list)](#key-functions-not-a-complete-list)
- [Using functions](#using-functions)
- [An iterable object](#an-iterable-object)
  - [Iterators](#iterators)
- [Generators](#generators)
  - [Generator expressions](#generator-expressions)
- [Classes](#classes)
  - [Methods and attributes](#methods-and-attributes)
  - [The self](#the-self)
  - [Public and private methods and variables](#public-and-private-methods-and-variables)
  - [Inheritance and multiple inheritance](#inheritance-and-multiple-inheritance)
  - [The Diamond Problem](#the-diamond-problem)
  - [Mixins](#mixins)
- [Decorators](#decorators)
- [Getters and setters](#getters-and-setters)
- [Magic class methods](#magic-class-methods)


# Comments

```py
# from the hash symbol to the end of a line
```

# Code Blocks

Delineated by colons and indented code; and not by the curly brackets of C, C++ and Java.

```py
def is_fish_as_string(argument): # a function
    if argument:
        return 'fish'
    else:
        return 'not fish'
```
Note:
Four spaces per indentation level is the Python standard. Never use tabs: mixing tabs and spaces produces hard-tofind errors. Set your editor to convert tabs to spaces.

# Line breaks

Typically, a statement must be on one line. Bracketd cod - (), [] or {} - can be split across lines; or use a backslash \ at the end of a line can be used to continue a statement on to the next line.

# Naming conventions

Style       |   Use
------------|---------------------------
StudlyCase  |   Class names
joined_lower|   Identifiers, functions; and class methods, attributes
_joined_lower|  Internal class attributes
__joined_lower| Private class attributes # This use not recommended
joined_lower, ALL_CAPS| Constants

# Basic object types (not a complete list)

Type        |   Examples
------------|--------------------------
None        |None # singleton null object
Boolen      |True, False
integer     | -1, 0, 1, sys.maxint
long        | 1L, 9787L # arbitrary length ints
float       | 3.14159265, 
|   inf, float('inf') # infinity
|   -inf   # netative infinity
|   nan, float('nan') # not a number
complex     | 2+3j  # note use of j
string      | 'I am a string', "me too"
| '''multi-line string''', """+1"""
| r'raw string', b'ASCII string'
| u'unicode string'
tuple       | empty = ()    # empty tuple
| (1, True, 'dog')  # immutable list
| a_tuple = 1, True, 'dog'  # parentheses are not necessary
| (1,)  # one element tuple requires a comma
list        | empty = []    # empty list
| [1, True, 'dog']  # mutable list
set         | empty = set() # empty set
| set(1, True, 'dog')   # mutable
dict        | empty = {}    # empty dict
| {'a': 'dog', 7: 'seven', True: 1} # mutable object
file        | f = open('filename', 'rb')

Note:
Python has four numeric types (integer, float, long and complex) and several sequence type including strings, lists, tuples, bytearray, buffers, and xrange objects.
Collections?

# Operators

Operator        | Functionality
----------------|-------------------------------------
`+`  | Addition (also string, tuple, list concatenation)
`-`  | Subtraction (also set difference)
`*`  | Multiplication (also string, tuple, list replication)
/  | Division
%  | Modulus (also a string format function, but use deprecated)
// | Integer division rounded towards minus inifinity
** | Exponentiation
=, -=, +=       | Assignment operators
/=, *=          | 
%=, //=         | 
**=             | 
==, !=, <,      | Boolean comparisons
<=, >=, >       | 
and, or, not    | Boolean operators
in, not in      | Memberships test operators
is, is no       | Object identity operators
|, ^, &, ~      | Bitwise: or, xor, and, compliment
<<, >>          | Left and right bit shift
;               | Inline statement separator
| # inline statements discouraged

**Hint**: `float('inf')` always tests as larger than any number, including integers.

# Modules

Modules open up a world of Python extentions that can be imported and used. Access to the functions, variables, and classes of a module depend on how the module was imported.

Import method       | Access/Use syntax
--------------------|----------------------------
import math         | math.cos(math.pi/3)
import math as m # import using an alias    | m.cos(m.pi/3)
from math import cos, pi # only import specific   | cos(pi/3)
from math import * # BABish global import   | log(e)

Global imports make unreadable code!!!

# Often used modules

Module      |   Purpose
------------|-----------------------------------------
Datetime, time| Date and time functions
math        | Core math functions and the constants pi and e
pickle      | Serialise objects to a file
os, os.path | Operating system interfaces
re          | A library of Perl-like regular expression operations
string      | Useful constants and classes
sys         | Syste parameters and functions
numpy       | Numerical python library
pandas      | DataFrames for python
matplotlib  | Plotting/charting for Python

# Flow control

## If - flow control

```py
if condition:   # for example: if x < 5:
    statements
elif condition: # optional - can be mutiple
    statements
else:
    statements
```

## For - flow control

```py
for x in iterable:
    statements
else:           # optional completion code
    statements
```

## While - flow control

```py
while condition:
    statements
else:           # optional completion code
    statements
```

## Ternary statement
id = expression if condition else expression
```py
x = y if a > b else z - 5
```

## Some useful adjuncts

- `pass` - a statement that does nothing
- `continue` - moves to the next loop iteration
- `break` - to exit for and while loop

**Trap**: `break` skips the `else` completion code

## Exceptions - flow control

```py
try:
    statements
except (tuple_of_errors):   # can have multiple
    statements
else:                       # optional no exceptions
    statements
finally:                    # optional all circumstances
    statements
```

Common exceptions (not a complete list)

Exception   |   Why it happens
------------|--------------------------------------------
AsserionError | Assert statement failed
AttributeError | Class attribute assignment or reference failed
IOError     | Failed I/O operation
ImportError | Failed module import
IndexError  | Subscript out of range
KeyError    | Dictionary key not found
MemoryError | Ran out of memory
NameError   | Name not found
TypeError   | Value of the wrong type
ValueError  | Right type but wrong value

Raising errors

Errors are raised using the `raise` statement
```py
raise ValueError(value)
```

Creating new errors

```py
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
```

# Objects and variables (AKA identifiers)

- Everything is an object in Python (in the sense that it can be assigned to a variable or passed as an argument to a function)
- Most Python objects have methods and attributes. For example, all functions have the built-in attribute `__doc__`, which returns the doc string defined in the functions's source code.
- All variables are effectively "pointers", not "locations". They are fererences to objects; and often called identifiers.
- Objects are strongly typed, not identifiers
- Some objects are immutable (int, float, string, tuple, frozenset). But most are mutable (including: list, set, dictionary, MumPy arrays, etc.)
- You can create your own object types by defining a new class.

# Boolean and truthiness

Most Python objects have a notion of "truth".

False           | True
----------------|---------------------------------------------
None            | 
0               | Any number other than 0
int(False) #-->0| int(True) # --> 1
"" # the empty string | " ", 'fred', 'False' # all other strings
() [] {} set() # empty containers  | [None], (False,), {1,1} # non-empty containers

You can use bool() to discover the truth status of an object.
```py
a = bool(obj)   # the truth of obj
```

It is pythonic to use the truth of objects.
```py
if container:   # test not empty
    # do something
while items:    # common looping idiom
    item = items.pop()
    # process item
```
Specify the truth of the classes you write using the `__nonzero__()` magic method.

# Comparisons 

Python lets you compare ranges, for example

```py
if 1 < x < 100: # do something...
```
# Tuples

Tuples are immutable lists. They can be searched, indexed and iterated much like lists. List methods that do not change the list also work on tuples.

```py
a = ()                  # the empty tuple
a = (1,) # <--- note comma # one item tuple
a = (1, 2, 3)           # multi-item tuple
a = ((1, 2), (3, 4))    # nested tuple
a = tuple(['a', 'b'])   # conversion
```

**Note**:
The comma is the tuple constructor, not the parentheses. The parentheses add clarity.

The Python swap variable idiom

```py
a, b = b, a # no need for a temp variable
```
This syntax uses tuples to achieve its magic.

# String (imutable, ordered, charaters)

```py
s = 'string'.upper()        # STRING
s = 'fred' + 'was' + 'here' # concatenation
s = ' '.join(['fred', 'was', 'there']) # ditto
s = 'spam' * 3              # replication
s = str(x)                  # conversion
```

String iteration and sub-string searching

```py
for charater in 'str':      # iteration
    print(ord(character))   # 115 116 114
for index, character in enumerate('str'):
    print(index, character)
if 'red' in 'Fred':         # searching
    print('Fred is red')    # it print!
```

String methods (not a complete list)

capitalize, center, count, decode, encode, endswith, expandtabs, find, format, index, isalnum, isalpha, isdigit, islower, isspace, istitle, isupper, join, ljust, lower, lstrip, partition, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill

String constants (not a complete list)

```py
from string import *        # I'm bad...
print(digits, hexdigits, octdigits, ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, whitespace, printable)
```

## Old school string formatting (using % oper)

```py
print("It %s %d times" % ('occurred', 5))
# prints: 'It occurred 5 times'
```

Code        | Meaning
------------|---------------------------------
s           | String or string coversion
c           | Character
d           | Signed decimal integer
H or h      | Hex integer (upper or lower case)
f           | Floating point
E or e      | Exponent (upper or lower case E)
G or g      | The shorter of e and f (u/l case)
%           | Literal '%'

```py
'%s' % math.pi      # --> '3.141592653589793'
'%f' % math.pi      # --> '3.141593'
'%.2f' % math.pi    # --> '3.14'
'%.2e' % 3000       # --> '3.00e+03'
'%03d' % 5          # --> '005'
```

## str.format()

Uses: 'template-string'.format(arguments)

Examples
```py
'Hello {}'.format('World')  # 'Hello World'
'{}'.format(math.pi)        # '3.141592653589793'
'{0:.2f}'.format(5)         # '3.14'
'{0:+.2f}'.format(5)        # '+5.00'
'{:.2e}'.format(3000)       # '3.00e+03'
'{:0>2d}'.format(5)         # '05' (left pad)
'{:0<3d}'.format(5)         # '500' (rifht pad)
'{:,}'.format(1000000)      # '1,000,000'
'{:.1%}'.format(0.25)       # '25.0%'
'{0}{1}'.format('a', 'b')   # 'ab'
'{1}{0}'.format('a', 'b')   # 'ba'
'{num:}'.format(num=7)      # '7' (named args)
```

## f-String

```py
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'

# It would also be valid to use a capital letter F:

>>> F"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'

>>> f"{2 * 37}"
'74'

# you could also call functions

>>> def to_lowercase(input):
...     return input.lower()

>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.'

# You also have the option of calling a method directly:

>>> f"{name.lower()} is funny."
'eric idle is funny.'
```

# List（mutable， indexed, ordered container)

Indexed from zero to length-1

```py
a = []                      # the empty list
a = ['dog', 'cat', 'bird']  # simple list
a = [[1, 2], ['a', 'b']]    # nested lists
a = [1, 2, 3] + [4, 5, 6]   # concatenation
a = [1, 2, 3] * 456         # replication
a = list(x)                 # conversion
```

List comprehensions (can be nested)

Comprehensions: a tight way of creating lists

```py
t3 = [x*3 for x in [5, 6, 7]]   # [15, 18, 21]
z = [complex(x, y) for x in range(0, 4, 1) for y in range(4, 0, -1) if x > y]
# z --> [(2+1j), (3+2j), (3+1j)]
```

Interating lists

```py
L = ['dog', 'cat', 'turtle']
for item in L:
    print(item)
for index, item in enumrate(L):
    print(index, item)
```

Searching lists

```py
L = ['dog', 'cat', 'turtle']
value = 'cat'
if value in L:
    count = L.count(value)
    first_occurrence = L.index(value)
if value not in L:
    print('list is missing {}'.format(value))
```

List methods (not a complete list)

Method          | What it does
----------------|--------------------------------------
l.append(x)     | Append x to end of list
l.extend(other) | Append items from other
l.insert(pos,x) | Insert x at position
del l[pos]      | Delete item at pos
l.remove(x)     | Remove first occurrence of x; An error if no x
l.pop([pos])    | Remove last item from list(or item from pos); An error if empty list
l.index(x)      | Get index of first occurrence of x; An error if x not found
l.count(x)      | Count the number of times x is found in the list
l.sort()        | In place list sort
l.reverse()     | In place list reserval

List slicing

```py
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]     # play data
x[2]        # 3rd element - reference not slice
x[1:3]      # 2nd to 3rd element [1, 2]
x[:3]       # the first three elements [0, 1, 2]
x[-3:]      # last three elements
x[:-3]      # all but the last three elements
x[:]        # every element of x - copies x
x[1:-1]     # all but first and last element
x[::3]      # [0, 3, 6] 1st, then every 3rd
x[1:5:2]    # [1, 3] start 1, stop >= 5, every 2nd
```

**Note**:
All Python sequence types support the above index slicing (strings, lists, tuples, bytearrays, buffers, and xrange objects).

# Set (unique unordered container)

A Python set is an unordered, mutable collection of unique hashable objects.

```py
a = set()                   # empty set
a = {'red', 'white', 'blue'} # simple set
a = set(x)                  # convert list
```

**Trap**: {} creates empty dict, not an empty set.

Iterating a set

```py
for item in aset:
    print(item)
```

Searching a set

```py
if item in aset:
    print(item)

if item not in aset:
    print('{} is missing'.format(item))
```

set methods (not a complete list)

Method                  | What it does
------------------------|---------------------------------
len(s)                  | Number of items in set
s.add(item)             | Add item to set
s.remove(item)          | Remove item from set. Raise KeyError if item not found
s.discard(item)         | Remove item from set if present
s.pop()                 | Remove and return an arbitrary item. Raise KeyError on empty set.
s.clear()               | Remove all items from set
item in s               | True or False
item not in s           | True or False
iter(s)                 | An iterator over the items in the set (arbitrary order)
s.copy()                | Get shallow copy of set
s.isdisjoint(o)         | True if s has not items in common with other set o
s.issubset(o)           | Same as set <= other
s.issuperset(o)         | Same as set >= other
s.union(o[,...])        | Return new union set
s.intersection(o)       | Return new intersection
s.difference(o)         | Get net set of items in s but not others (same as `set - other`)

Frozenset

Similiar to a Python set above, but immutable (and therefore hashable)

```py
f = frozenset(s)        # convert set
f = frozenset(o)        # convert other
```

# Dictionary (indexed, unordered map - container)

A mutable hash map of unique key-value pairs

```py
a = {}                  # empty dict
a = {1: 1, 2: 4, 3: 9}  # simple dict
a = dict(x)             # convert dict
# next example - create from a list
l = ['alpha', 'beta', 'gamma', 'delta']
a = dict(zip(range(len(l)), l))
# Example using string & generator expression
s = 'a=apple,b=bird,c=cat,d=dog,e=egg'
a = dict(i.split("=") for in in s.split(","))
# {'a': 'apple', 'c': 'cat', 'b': 'bird', 'e': 'egg', 'd': 'dog'}
```

Dictionary comprehensions

Conceptually like list comprehensions; but it construts a dictionary rather than a list

```py
a = {n; n*n for n in range(7)}      
# a -> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
odd_sq = {n: n*n for n in range(7) if n%2}
# odd_sq = {1: 1, 3: 9, 5: 25}
# next example -> swaps the key:value pairs
a = { val: key for key, val in a.items()}
# next example -> count list occurrences
l = [1,2,9,2,7,3,7,1,22,1,7,7,22,22,9,0,9,0]
c = { key: l.count(key) for key in set(l)}
# c -> {0:2, 1:3, 2:2, 3:1, 7:4, 9:3, 22:3}
```

Iterating a dictionary

```py
for key in dictionary:
    print(key)
for key, value in dictionary.items():
    print(key, value)
```

Searching a dictionary

```py
if key in dictionary:
    print(key)
```

Dictionary methods (not a complete list)

Method              | What it does
--------------------|------------------------------------
len(d)              | Number of items in d
d[key]              | Get value for key or raise the KeyError exception
d[key] = value      | Set key to value
del d[key]          | deletion
key in d            | True or False
key not in d        | True or False
iter(d)             | An iterator over the keys
d.clear()           | Remove all items from d
d.copy()            | Shallow copy of dictionary
d.get(key[, def])   | Get value else default
d.items()           | Dictionary's (k,v) pairs
d.keys()            | Dictionary's keys
d.pop(key[, def])   | Get value else default; remove key from dictionary
d.popitem()         | Remove and return an arbitrary (k,v) pair
d.setdefault(k[,def]) | If k in dict return its value otherwise set def
d.update(other_d)   | Update d with key:val pairs from other
d.values()          | The values from dict


# Key Functions (not a complete list)

Function                | What it does
------------------------|-----------------------------------
abs(num)                | Absolute value of num
all(iterable)           | True if all are True
any(iterable)           | True if any are True
bytearray(source)       | A mutable array of bytes
callable(obj)           | True if obj is callable
chr(int)                | Character for ASCII int
complex(re[, im])       | Create a complex number
divmod(a, b)            | Get (quotient, remainder)
enumerate(seq)          | Get an enumerate object, with next() method returns an (index, element) tuple
eval(string)            | Evaluate an expression
filter(fn, iter)        | Construct a list of elements from iter for which fn() returns True
float(x)                | Convert from int/string
getattr(obj, str)       | Like obj.str
hasattr(obj, str)       | True if obj has attribute
id(obj)                 | Retur unique (run-time) identifier for an object
hex(x)                  | From int to hex string
int(x)                  | Convert from float/string
isinstance(o, c)        | If o is an instance of c 
len(x)                  | Number of items in x; x is string, tuple, list, dict
list(iterable)          | Make a list
long(x)                 | Convert a string or number to a long integer
map(fn, iterable)       | Apply fn() to every item in iterable; return results in a list
max(a, b), max(iterable)    | Return the max value
min(a, b), min(iterable)    | Ditto
next(iterator)          | Get next item from an iter
open(name[, model])     | Open a file object
ord(c)                  | Opposite of chr(int)
pow(x, y)               | Same as x ** y
print(objects)          | Print
range(stop), range(start, stop), range(fr,to,step) | integer list; stops < stop; default start=0, default step=1
reduce(fn, iter)        | Applies the two argument fn(x, y) cumulatively to the items of iter.
repr(object)            | Printable representation of an object
reversed(seq)           | Get a reversed iterator
round(n[, digits])      | Round to number of digits after the decimal place.
setattr(obj, n, v)      | Like obj.n = v # name/value
sorted(iterable)        | Get new sorted list
str(object)             | Get a string for an object
sum(iterable)           | Sum list of numbers
type(object)            | Get the type of object
xrange()                | Like range() but better: returns an iterator.
zip(x, y[, z])          | Return a list of tuples

# Using functions

When called, functions can take positional and named arguments. For example:
```py
result = function(32, aVar, c='see', d={})
````

Arguments are passed by reference (ie. the objects are not copied, just the references)

Writing a simple function

```py
def funct(arg1, arg2=None, *args, **kwargs):
    """explain what this function does"""
    statements
    return x    # optional statement
```
**Note**:
functions are first class objects that get instantiated with attributes and they can be referenced by variables.

Avoid named default mutable argument

Avoid mutable objects as default arguments. Expressions in default arguments are evaluated when the function is defined, not when it's called. Changes to mutable default arguments survive between function calls.

```py
def nasty(value=[]):            # <-- mutable arg
    value.append('a')
    return value
    print(nasty()) # --> ['a']
    print(nasty()) # --> ['a', 'a']

def better(val=None):
    val = [] if val is None else val
    val.append('a')
    return val
```

Lambda (inline expression) functions:

```py
g = lambda x: x ** 2        # Note: no return
print(g(8))                 # prints 64
mul = lambda a, b: a * b    # two arguments
mul(4, 5) == 4 * 5          # --> True
```
Note:
Only for expressions, not statements. Lambdas are often used with the Python functions filter(), map() and reduce().
```py
# get only those numbers divisible by three
div3 = filter(lambda x: x%3==0, range(1,101))
```

Typically, you can put a lambda function anywhere you put a normal function call.

Closures

Closures are functions that have inner functions with data fixed in the inner functions by the lexical scope of the outer. They are useful for avoiding hard constants. Wikipedia has a derivative function for changeable value of dx, using a closure.
```py
def derivative(f, dx):
    """Return a function that approximates
       the derivative of f using an interval
       of dx, which should be appropriately small.
    """
    def _function(x):
        return (f(x + dx) - f(x)) / dx
    
    return _function # from derivative(f, dx)

f_dash_x = derivative(lambda x: x*x, 0.00001)
f_dash_x(5) # yields approx. 10 (ie. y' = 2x)
```

# An iterable object


The contents of an iterable object can be selected one at a time. Such objects include the Python sequence types and classes with magic method `__iter__()`, which returns an iterabtor. An iterable object will produce a fresh iterator with each call to `__iter__()`.

```py
iterator = iter(iterable_object)
```

Iterable is an object, which one can iterate over.
Iterator is an object, which is used to iterate over an iterable object using `__next__()` method. 

Note that every iterator is also an iterable, but not every iterable is an iterator. For example, a list is iterable but a list is not an iterator. An iterator can be created from an iterable by using the function `iter()`. To make this possible, the class of an object needs either a method `__iter__`, which returns an iterator, or a `__getitem__` method with sequential indexes starting with 0.

When a `for` loop is executed, `for` statement calls `iter()` on the object, which it is supposed to loop over. If this call is successful, the iter call will return an iterator object that defines the method `__next__()`, which accesses elements of the object one at a time. The `__next__()` method will raise a `StopIteration` exception, if there are no further elements available. The `for` loop will terminate as soon as it catches a `StopIteration` exception.

## Iterators

Objects with a `next()` (Python 2) or `__next__()` (Python 3) method, that:
- returns the next value in the iteration
- updates the internal note of the next value
- raises a StopIteration exception when done

Note: with the loop `for x in y:` if y is not an iterator; Python calls iter() to get one. With each loop, it calls `next()` on the iterator until a StopIteration exception.

```py
x = iter('XY')      # iterate a string by hand
print(next(x))      # --> X
print(next(x))      # --> Y
print(next(x))      # --> StopIteration
```

# Generators

Generator functions are resumable functions that work like iterators. They can be more space or time efficient than iterating over a list, (especially a very large list), as they only produce items as they are needed.

```py
def fib(max=None):
    """ generator for Fibonacci sequence"""
    a, b = 0, 1
    while max is None or b <= max:
        yield b      # <-- yield is like return
        a, b = b, a+b
[i for i in fib(10)]    # --> [1, 1, 2, 3, 5, 8]
```

Note: a `return` statement (or getting to the end of the function) ends the iteration. 
Trap: a `yield` statement is not allowed in the `try` clause of a `try/finally` construct.

Messaging the generator

```py
def resetableCounter(max=None):
    j = 0
    while max is None or j <= max:
        x = yield j     # <-- x gets the sent arg
        j = j+1 if x is None else x

x = resetableCounter(10)
print(x.send(None))     # --> 0
print(x.send(5))        # --> 5
print(x.send(None))     # --> 6
print(x.send(11))       # --> StopIteration
```

Trap: Must send `None` on first `send()` call.

## Generator expressions

generator expressions build generators, just like building a list from a comprehension. You can turn a list comprehension into a generator expression simply by replacing the square bracket `[]` into parentheses `()`.

```py
[i for i in xrange(10)]     # list comprehension
list(i for i in xrange(10))     # generated list
```

# Classes


Python is an object-oriented language with a mutiple inheritance class mechanism that encapsulates program code and data.

## Methods and attributes

Most objects hae associated functions or "methods" that are called using dot syntax:
```py
obj.method(arg)
```

Objects also often have attributes or values that are directly accessed without using getters and setters (most unlike Java or C++)

```py
instance = Example_Class()
print(instance.attribute)
```

Simple example

```py
import math
class Point:
    # static class variable, point count
    count = 0

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        Point.count += 1
    
    def __str__(self):
        return '(x={}, y={})'.format(self.x, self.y)

    def to_polar(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)
    
    # static method - trivial example ...
    def static_eg(n):
        print('{}'.format(n))

    static_eg = staticmethod(static_eg)

# Instantiate 9 points & get polar coords

for x in range(-1, 2):
    for y in range(-1, 2):
        p = Point(x, y)
        print(p)    # uses __str__() method
        print(p.to_polar())

print(Point.count)  # check static variable
Point.static_eg(9)  # check static method
```

## The self

Class methods have an extra argument over functions. Usually named 'self'; it is a reference to the instance. It is not used in the method call; and is provided by Python to the method. Self is like 'this' in C++ & Java.

## Public and private methods and variables

Python does not enforce the public v private data distinction. By convention, variables and methods that begin with an underscore should be treated as private (unless you really know what you are doing). Variables that begin with double underscore are mangled by the compiler (and hence more private).

## Inheritance and multiple inheritance

```py
class DerivedClass1(BaseClass):
    statements
class DerivedClass2(module_name.BaseClass):
    statements
```

Multiple inheritance
```py
class DerivedClass(Base1, Base2, Base3):
    statements
```

## The Diamond Problem

When the method is overridden in both parent classes.

```py
# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
		
class Class4(Class2, Class3):
	pass
	
obj = Class4()
obj.m()
```
Output:
```
In Class2
```
Note: When you call obj.m() (m on the instance of Class4) the output is `In Class2`. If Class4 is declared as Class4(Class3, Class2) then the output of obj.m() will be `In Class3`.

## Mixins

Mixins are an alternative class design pattern that avoids both single-inheritance class fragmentation and multiple-inheritance diamond dependencies. A mixin is a class that defines and implements a single, well-defined feature. Subclasses that inherit from the mixin inherit this feature—and nothing else.

# Decorators

Technically, decorators are just functions(or classes), that take a callable object as an argument, and return an analogous object with the decoration. We will skip how to write them and focus on using a couple or common built-in decorators.

Practically, decorators are syntactic sugar for more readable code. The @wrapper is used to transform the existing code. For example, the following two method definitions are semantically equivalent.

```py
def f(...):
    ...
f = staticmethod(f)

@staticmethod
def f(...):
    ...
```

# Getters and setters

Although class attributes can be directly accessed, the property function creates a property manager.

```py
class Example:
    def __init__(self):
        self._x = None
    
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "Doc txt")
```

Which can be rewritten with decorators as:

```py
class Example:
    def __init__(self):
        self._x = None
    
    @property
    def getx(self):
        return self._x
    
    @x.setter
    def setx(self, value):
        self._x = value
    
    @x.deleter
    def delx(self):
        del self._x
```

# Magic class methods

Magic methods (which begin and end with double underscore) add functionality to your classes consistent with the broader language.

Magic method                | What it does
----------------------------|------------------------------
`__init__(self,[...])`      | Constructor
`__del__(self)`             | Destructor pre-garbage collection
`__str__(self)`             | Human readable string for class contents. Called by str(self)
`__repr__(self)`            | Machine readable unambiguous Python string expression for class contents. Called by repr(self). Note: str(self) will call `__repr__` if `__str__` is not defined.
`__eq__(self, other)`       | Behaviour for ==
`__ne__(self, other)`       | Behaviour for !=
`__lt__(self, other)`       | Behaviour for <
`__gt__(self, other)`       | Behaviour for >
`__le__(self, other)`       | Behaviour for <=
`__ge__(self, other)`       | Behaviour for >=
`__add__(self, other)`      | Behaviour for +
`__sub__(self, other)`      | Behaviour for -
`__mul__(self, other)`      | Behaviour for *
`__div__(self, other)`      | Behaviour for /
`__mod__(self, other)`      | Behaviour for %
`__pow__(self, other)`      | Behaviour for **
`__pos__(self, other)`      | Behaviour for unary +
`__neg__(self, other)`      | Behaviour for unary -
`__hash__(self)`            | Returns an int when hash() called. Allows class instance to be put in a dictionary.
`__len__(self)`             | Length of container
`__contains__(self, i)`     | Behaviour for `in` and `not in` operators
`__missing__(self, i)`      | What to do when dict key i is missing
`__copy__(self)`            | Shallow copy constructor
`__deepcopy__(self, memodict={})` | Deep copy onstructor
`__iter__(self)`            | Provide an iterator
`__nonzero__(self)`         | Called by `bool(self)`
`__index__(self)`           | Called by `x[self]`
`__setattr__(self, name, val)`  | Called by `self.name = val`
`__getattribute__(self, name)`  | Called by `self.name`
`__getattr__(self, name)`   | Called when `self.name` does not exist
`__delattr__(self, name)`   | Called by `del self.name`
`__getitem__(self, key)`    | Called by `self[key]`
`__setitem__(self, key, val)`   | Called by `self[key] = val`
`__delitem__(self, key)`    | Called by `del self[key]`



















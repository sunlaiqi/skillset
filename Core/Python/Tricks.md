- [Tricks and Tips](#tricks-and-tips)
  - [List](#list)
    - [List Slicing Tricks and the Sushi Operator](#list-slicing-tricks-and-the-sushi-operator)
    - [Sort Complex Lists With sorted()](#sort-complex-lists-with-sorted)
    - [Iterate With enumerate() Instead of range()](#iterate-with-enumerate-instead-of-range)
  - [String](#string)
    - [Format strings With f-Strings](#format-strings-with-f-strings)
    - [Access Common String Groups With string Constants](#access-common-string-groups-withstringconstants)
  - [Generator](#generator)
    - [Save Memory With Generators](#save-memory-with-generators)
  - [itertools](#itertools)
    - [Generate Permutations and Combinations With itertools](#generate-permutations-and-combinations-withitertools)
  - [Dictionary](#dictionary)
    - [Dictionary Default Values](#dictionary-default-values)
    - [How to merge two dicts](#how-to-merge-two-dicts)
    - [Sort Dictionary](#sort-dictionary)
      - [lexicographical ordering](#lexicographical-ordering)
      - [key func in sorted](#key-func-in-sorted)
    - [How to sort a dict descending by its value and then ascending (A-Z) by its key (alphabetically).](#how-to-sort-a-dict-descending-by-its-value-and-then-ascending-a-z-by-its-key-alphabetically)
    - [Define Default Values in Dictionaries With .get() and .setdefault()](#define-default-values-in-dictionaries-with-get-and-setdefault)
    - [Handle Missing Dictionary Keys With collections.defaultdict()](#handle-missing-dictionary-keys-withcollectionsdefaultdict)
    - [Count Hashable Objects With collections.Counter](#count-hashable-objects-withcollectionscounter)
    - [Emulating Switch/Case Statements With Dicts](#emulating-switchcase-statements-with-dicts)
  - [Some dict tricks](#some-dict-tricks)
    - [Dictionary Pretty-Printing](#dictionary-pretty-printing)
  - [Functions](#functions)
    - [Function argument unpacking](#function-argument-unpacking)
    - [Measure the execution time of small bits of Python code with the "timeit" module](#measure-the-execution-time-of-small-bits-of-python-code-with-the-timeit-module)
  - [Debug](#debug)
    - [Debug With breakpoint() Instead of print()](#debug-with-breakpoint-instead-of-print)
  - [Pythonic Productivity Techniques](#pythonic-productivity-techniques)
    - [Isolating Project Dependencies With Virtualenv](#isolating-project-dependencies-with-virtualenv)
    - [Peeking Behind the Bytecode Curtain](#peeking-behind-the-bytecode-curtain)
  - [collections](#collections)
    - [collections.defaultdict](#collectionsdefaultdict)
    - [collections.Counter](#collectionscounter)

# Tricks and Tips

## List

### List Slicing Tricks and the Sushi Operator
```python
lst[start:end:step]
# reverse 
lst[::-1]
# full list
lst[::]
lst[:]
# delete all elements
del list[:] # = lst.clear()

# replaced all elements in lst but did not destroy and recreate the list itself. 

>>> original_lst = lst 
>>> lst[:] = [7, 8, 9] 
>>> lst
[7, 8, 9]
>>> original_lst
[7, 8, 9]
>>> original_lst is lst 
True

# the sushi operator is creating (shallow) copies of existing lists. 
# Creating a shallow copy means that only the structure of the elements is copied, not the elements themselves.
>>> copied_lst = lst[:] 
>>> copied_lst
[7, 8, 9]
>>> copied_lst is lst 
False

```
### Sort Complex Lists With sorted()

You’ve probably seen the most simple uses of sorting, such as sorting lists of numbers or strings in ascending or descending order:
```python
>>>
>>> sorted([6,5,3,7,2,4,1]) 
[1, 2, 3, 4, 5, 6, 7]
>>> sorted(['cat', 'dog', 'cheetah', 'rhino', 'bear'], reverse=True)
['rhino', 'dog', 'cheetah', 'cat', 'bear]
```

It’s worth knowing about the optional keyword argument `key` that lets you specify a function that will be called on every element prior to sorting.
Adding a function allows custom sorting rules, which are especially helpful if you want to sort more complex data types:
```python
>>>
>>> animals = [
... {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
... {'type': 'elephant', 'name': 'Devon', 'age': 3},
... {'type': 'puma', 'name': 'Moe', 'age': 5}, ... ]
>>> sorted(animals, key=lambda animal: animal['age']) 
[
{'type': 'elephant', 'name': 'Devon', 'age': 3}, {'type': 'puma', 'name': 'Moe', 'age': 5}, {'type': 'penguin', 'name': 'Stephanie, 'age': 8},
]
```
In this case, the dictionary is now sorted in ascending order by age.


### Iterate With enumerate() Instead of range()

Range allows you to access the elements of numbers by index and is a useful tool for some situations. But in this case, where you want to get each element’s index and value at the same time, a more elegant solution uses enumerate(). 
The enumerate() built-in helps you make those kinds of loops nice and Pythonic:

```python
numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers, start=52):
    print(i, num)
```
## String

### Format strings With f-Strings

From Python 3.6+, the suggested formatting approach is Python’s f-strings.
f-strings support use of the string formatting mini-language, as well as powerful string interpolation. These features allow you to add variables or even valid Python expressions and have them evaluated at runtime before being added to the string:
```python
def get_name_and_decades(name, age):
    return f"My name is {name} and I'm {age / 10:.5f} decades old."

get_name_and_decades("Maria", 31)

# My name is Maria and I'm 3.10000 decades old.
```

The one risk to be aware of is that if you’re outputting user-generated values, then that can introduce security risks, in which case **Template Strings** may be a safer option.

### Access Common String Groups With string Constants

It’s much easier to use the constants defined as part of the string module.
You can see one in use in is_upper(), which returns whether all characters in a string are uppercase letters:
```python
>>>
>>> import string
>>> def is_upper(word):
...     for letter in word:
...         if letter not in string.ascii_uppercase:
...             return False
...     return True
...
>>> is_upper('Thanks Geir')
False
>>> is_upper('LOL')
True
```
The value of `string.ascii_uppercase` is set to the literal 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
All string constants are just strings of frequently referenced string values. They include the following:
```python
string.ascii_letters
string.ascii_uppercase
string.ascii_lowercase
string.digits
string.hexdigits
string.octdigits
string.punctuation
string.printable
string.whitespace
```
These are easier to use and, even more importantly, easier to read.


## Generator

### Save Memory With Generators

List comprehensions are convenient tools but can sometimes lead to unnecessary memory usage.

Thankfully, there’s a quick way to solve the memory problem. You just replace the brackets with parentheses:
```python
>>>
>>> sum((i * i for i in range(1, 1001)))
333833500
```
Swapping out the **brackets** changes your list comprehension into a generator expression. Generator expressions are perfect for when you know you want to retrieve data from a sequence, but you don’t need to access all of it at the same time.

Instead of creating a list, the generator expression returns a generator object. That object knows where it is in the current state (for example, i = 49) and only calculates the next value when it’s asked for.
The design allows generators to be used on massive sequences of data, because only one element exists in memory at a time.

## itertools

### Generate Permutations and Combinations With itertools

`itertools` has multiple tools for generating iterable sequences of input data, but right now we’ll just focus on two common functions: `itertools.permutations()` and `itertools.combinations()`.

`itertools.permutations()`
The r keyword argument lets us specify how many values go in each grouping:
```python
>>>
>>> import itertools
>>> friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
>>> list(itertools.permutations(friends, r=2))
[('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
('Ashish', 'Monique'), ('Ashish', 'Devon'), ('Ashish', 'Bernie'),
('Devon', 'Monique'), ('Devon', 'Ashish'), ('Devon', 'Bernie'),
('Bernie', 'Monique'), ('Bernie', 'Ashish'), ('Bernie', 'Devon')]
```
With permutations, the order of the elements matters, so ('sam', 'devon')represents a different pairing than ('devon', 'sam'), meaning that they would both be included in the list.

1itertools.combinations()` builds combinations. But now the order of the values doesn’t matter. Because ('sam', 'devon') and ('devon', 'sam')represent the same pair, only one of them would be included in the output list:
```python
>>>
>>> list(itertools.combinations(friends, r=2))
[('Monique', 'Ashish'), ('Monique', 'Devon'), ('Monique', 'Bernie'),
('Ashish', 'Devon'), ('Ashish', 'Bernie'), ('Devon', 'Bernie')]
```

## Dictionary

### Dictionary Default Values

Syntax
```python
dictionary.get(keyname, value)
```

When `get()` is called, it checks if the given key exists in the dictionary. If it does, the value for the key is returned. If it does not exist, then the value of the default parameter is returned instead.

### How to merge two dicts

```python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

>>> z
{'a': 1, 'b': 3, 'c': 4}
>>> z = {**x, 'foo': 1, 'bar': 2, **y}
>>> z
{'a': 1, 'b': 3, 'foo': 1, 'bar': 2, 'c': 4}

c = x.copy()
c.update(y)
>>> c
{'a': 1, 'b': 3, 'c': 4}

>>> z = dict(x, **y)
>>> z
{'a': 1, 'b': 3, 'c': 4}

import itertools
z = dict(itertools.chain(x.items(), y.items()))

z = dict(list(x.items()) + list(y.items()))

```

### Sort Dictionary

#### lexicographical ordering

The key/value tuples are ordered using Python’s standard lexico- graphical ordering for comparing sequences.

To compare two tuples, Python compares the items stored at index zero first. If they differ, this defines the outcome of the comparison. If they’re equal, the next two items at index one are compared, and so on.

```python
>>> xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
>>> sorted(xs.items())
[('a', 4), ('b', 3), ('c', 2), ('d', 1)]
>>> dict(sorted(xs.items()))
{'a': 4, 'b': 3, 'c': 2, 'd': 1}
```

####  key func in sorted

Syntax
```python
sorted(iterable, key=key, reverse=reverse)
```
Examples:

```python
 >>> sorted(xs.items(), key=lambda x: x[1]) 
 [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
 ```
 Use operator module
 ```python
 >>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1)) 
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

Apparently, lambda has more controls than operater.itemgetter.

### How to sort a dict descending by its value and then ascending (A-Z) by its key (alphabetically).
```python
dict = {'apple': 2, 'banana': 3, 'almond':2 , 'beetroot': 3, 'peach': 4}

>>> [item[0] for item in sorted(dict.items(), key=lambda x: (-x[1], x[0]) )]

['peach', 'banana', 'beetroot', 'almond', 'apple']

# The following solution might be working in python 2.7:??
>>> [v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))]
['peach', 'banana', 'beetroot', 'almond', 'apple']


# Python 3 removed tuple parameter unpacking, so the line above should now be written as [v[0] for v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))]. See PEP 3113 python.org/dev/peps/pep-3113
```

### Define Default Values in Dictionaries With .get() and .setdefault()

Imagine you have a dictionary named `cowboy`, and you want to get that cowboy’s name. One approach is to explicitly check for the key with a conditional:
```python
>>>
>>> cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'} 
>>> if 'name' in cowboy:
...     name = cowboy['name']
... else:
...     name = 'The Man with No Name'
...
>>> name
'The Man with No Name'
```
It can easily be replaced with one line if you use `get()`:
```python
>>>
>>> name = cowboy.get('name', 'The Man with No Name')
```

But what if you want to update the dictionary with a default value while still accessing the name key? Python offers a more elegant method with .`setdefault()`:
```python
>>>
>>> name = cowboy.setdefault('name', 'The Man with No Name') 
```
`setdefault()` checks if name exists in cowboy, and if so it returns that value. Otherwise, it sets cowboy['name'] to `The Man with No Name` and returns the new value.

### Handle Missing Dictionary Keys With collections.defaultdict()

`get()` and `setdefault()` work well when you’re setting a default for a single key, but it’s common to want a default value for all possible unset keys.
Pretend you have a group of students, and you need to keep track of their grades on homework assignments. The input value is a list of tuples with the format (student_name, grade), but you want to easily look up all the grades for a single student without iterating over the list.
One way to store the grade data uses a dictionary that maps student names to lists of grades:
```python
>>>
>>> student_grades = {}
>>> grades = [
...     ('elliot', 91),
...     ('neelam', 98),
...     ('bianca', 81),
...     ('elliot', 88),
... ]
>>> for name, grade in grades:
...     if name not in student_grades:
...         student_grades[name] = []
...     student_grades[name].append(grade)
...
>>> student_grades
{'elliot': [91, 88], 'neelam': [98], 'bianca': [81]}
```

But there’s an even cleaner approach that uses a `defaultdict`, which allows you to set a default value that will be operated upon if the key doesn’t exist:
```python
>>>
>>> from collections import defaultdict
>>> student_grades = defaultdict(list)
>>> for name, grade in grades:
...     student_grades[name].append(grade)
```
In this case, you’re creating a defaultdict that uses the `list()` constructor with no arguments as a default factory method. list() with no arguments returns an empty list, so defaultdict calls list() if the name doesn’t exist and then allows the grade to be appended. If you want to get fancy, you could also use a `lambda` function as your factory value to return an arbitrary constant.

### Count Hashable Objects With collections.Counter

You have a long string of words with no punctuation or capital letters and you want to count how many times each word appears.
You could use a dictionary or defaultdict and increment the counts, but `collections.Counter` provides a cleaner and more convenient way to do exactly that. Counter is a subclass of `dict` that uses 0 as the default value for any missing element and makes it easier to count occurrences of objects:
```python
>>>
>>> from collections import Counter
>>> words = "if there was there was but if \
... there was not there was not".split()
>>> counts = Counter(words)
>>> counts
Counter({'if': 2, 'there': 4, 'was': 4, 'not': 2, 'but': 1})
```

Are you curious what the two most common words were? Just use `most_common()`:
```python
>>>
>>> counts.most_common(2)
[('there', 4), ('was', 4)]
```

### Emulating Switch/Case Statements With Dicts

The idea here is to leverage the fact that Python has first-class func- tions. This means they can be passed as arguments to other functions, returned as values from other functions, and assigned to variables and stored in data structures.

The core idea here is to define a dictionary that maps lookup keys for the input conditions to functions that will carry out the intended operations:

To support a default case, use `get()` of dictionary

```python
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y, 
        'sub': lambda: x - y, 
        'mul': lambda: x * y, 
        'div': lambda: x / y,
        }.get(operator, lambda: None)()
print(dispatch_dict('mul', 2, 8))
print(dispatch_dict('unknown', 2, 8))
# 16
# None
```

## Some dict tricks

How Python process dict for 
`{True: 'yes', 1: 'no', 1.0: 'maybe'}`
```
>>> xs = dict()
>>> xs[True] = 'yes' 
>>> xs[1] = 'no'
>>> xs[1.0] = 'maybe'

#
>>> True == 1 == 1.0 
True
 >>> ['no', 'yes'][True] 
 'yes'
```
The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respec- tively, in almost all contexts, the exception being that when converted to a string, the strings ‘False’ or ‘True’ are returned, respectively.

Python’s dictionaries don’t update the key object itself when a new value is associated with it.

The {True: 'yes', 1: 'no', 1.0: 'maybe'} dictionary expres- sion evaluates to {True: 'maybe'} because the keys True, 1, and 1.0 all compare as equal, and they all have the same hash value:

```
>>> True == 1 == 1.0
True
>>> (hash(True), hash(1), hash(1.0)) 
(1, 1, 1)
```

### Dictionary Pretty-Printing

use json.dumps() (it's like jq in bash)

```python 
>>> mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee} 
>>> str(mapping)
{'b': 42, 'c': 12648430, 'a': 23}

>>> import json
>>> json.dumps(mapping, indent=4, sort_keys=True)
{
    "a": 23,
    "b": 42,
    "c": 12648430 
}
```

json module only works with dicts that contain primitive types.
Another downside of using json.dumps() is that it can’t stringify complex data types.

## Functions




### Function argument unpacking
```python

# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
```

### Measure the execution time of small bits of Python code with the "timeit" module 
```python
# The "timeit" module lets you measure the execution
# time of small bits of Python code

>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)

0.3412662749997253

>>> timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)

0.2996307989997149

>>> timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)

0.24581470699922647
```

## Debug

### Debug With breakpoint() Instead of print()


For non-trivial bugs, it’s almost always faster than using print(), and given that debugging is a big part of writing software, it shows that you know how to use tools that will let you develop quickly on the job.
If you’re using Python 3.7, you don’t need to import anything and can just call `breakpoint()` at the location in your code where you’d like to drop into the debugger:
```python
# Some complicated code with bugs
breakpoint()
```
Calling `breakpoint()` will put you into `pdb`, which is the default Python debugger. On Python 3.6 and older, you can do the same by
importing pdb explicitly:
```python
import pdb; pdb.set_trace()
```
Or you can use pdb at command line:
```
$python -m pdb myscript.py
```
Like `breakpoint()`, `pdb.set_trace()` will put you into the `pdb` debugger. It’s just not quite as clean and is a tad more to remember.
There are other debuggers available that you may want to try, but `pdb` is part of the standard library, so it’s always available. 

## Pythonic Productivity Techniques

dir() and help()

### Isolating Project Dependencies With Virtualenv

Here, we put Python virtual environment into a separate folder named `./venv` under current directory.

```bash
$ python3 -m venv ./venv
$ ls venv/
bin        include    lib        pyvenv.cfg
$ source ./venv/bin/activate 
(venv) $
# Stop virtual env
(venv) $ deactivate
```

### Peeking Behind the Bytecode Curtain

When the CPython interpreter executes your program, it first trans- lates it into a sequence of bytecode instructions. Bytecode is an in- termediate language for the Python virtual machine that’s used as a performance optimization.

Each function has a __code__ attribute (in Python 3) that we can use to get at the virtual machine instructions, constants, and variables used by our greet function:
```python
def greet(name):
    return 'Hello, ' + name + '!'
>>> greet.__code__.co_code 
b'dx01|x00x17x00dx02x17x00Sx00' 
>>> greet.__code__.co_consts 
(None, 'Hello, ', '!')
>>> greet.__code__.co_varnames 
('name',)
```

Use disassembler to make inspecting the bytecode easier.
```python
>>> import dis
>>> dis.dis(greet)
  2           0 LOAD_CONST               1 ('Hello, ')
              2 LOAD_FAST                0 (name)
              4 BINARY_ADD
              6 LOAD_CONST               2 ('!')
              8 BINARY_ADD
             10 RETURN_VALUE
>>> 
```

## collections

### collections.defaultdict

Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class.

**The definition of defaultdict:**
```python
class collections.defaultdict([default_factory[, ...]])
```
The first argument provides the initial value for the `default_factory` attribute; it defaults to `None`.
`default_factory`could be int, list, etc.


In a dict, accessing value associated with a key that is not present leads to a KeyError exception. However, a collections.defaultdict retums the default value of the type that was specified when the collection was instantiated, e.g.,if 
```python
import collections
a = {"a": [1,2,3], "b": [1,2]}
d = collections.defaultdict(list)
d["a"] = [1,2,3]
d["b"] = [1]
e = d["c"]
print(f"The nonexist key in defaultdict: {e}")
f = a["c"]
```
The result would be:

```
The nonexist key in defaultdict: []
Traceback (most recent call last):
  File "/Users/michael/Documents/mywriting/python.py", line 9, in <module>
    f = a["c"]
KeyError: 'c'
```

Setting the `default_factory` to `list`
This technique is simpler and faster than an equivalent technique using `dict.setdefault()`

```python
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
  d[k].append(v)
print("Using collections.defaultdict(): ", d.items())
# Using collections.defaultdict():  dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
```

```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = {}
for k, v in s:
  d.setdefault(k, []).append(v) 
print("Using dict.setdefault(): ", d.items())
# Using dict.setdefault():  dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
```

Setting the `default_factory` to `int` makes the defaultdict useful for counting (like a bag or multiset in other languages):
```python
import collections
s = 'mississippi'
d = collections.defaultdict(int) 
for k in s:
    d[k] += 1
print("default_factory = int: ", d.items())
# default_factory = int:  dict_items([('m', 1), ('i', 4), ('s', 4), ('p', 2)])
```

Setting the `default_factory` to `set` makes the defaultdict useful for building a dictionary of sets:
```python
import collections
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)
print("default_factory = set: ", d.items())
# default_factory = set:  dict_items([('red', {1, 3}), ('blue', {2, 4})])
```

### collections.Counter

**Definition**
```python
class collections.Counter([iterable-or-mapping])
```

A `Counter` is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The `Counter` class is similar to `bags` or `multisets` in other languages.



Elements are counted from an iterable or initialized from another mapping (or counter):
```python
>>> c = Counter() # a new, empty counter
>>> c = Counter('gallahad')
>>> c = Counter({'red': 4, 'blue': 2})
>>> c = Counter(cats=4, dogs=8)
```

Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:
```python
>>> c = Counter(['eggs', 'ham'])
>>> c['bacon'] # count of a missing element is zero
0
```

Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:
```python
>>> c['sausage'] = 0 # counter entry with a zero count
>>> del c['sausage'] # del actually removes the entry
```


A `collections.Counter` is used for counting the number of occurrences of keys, with a number of set like operations, as illustrated below.
```python
c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
# add two counters together: c[x] + d[x], collections.Counter({‘a’: 4, ‘b’: 3}) 
c + d
# subtract (keeping only positive counts), collections.Counter({‘a’: 2})
c - d
# intersection: min(c[x], d[x]), collections.Counter({‘a’: 1, ‘b’: 1}) 
# union: max(c[x], d[x]), collections.Counter({‘a’: 3, ‘b’: 2})
c | d
```

Counter objects support three methods beyond those available for all dictionaries:

**elements()**

Return an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order. If an element’s count is less than one, elements() will ignore it.
```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']
```

**most_common([n])**

Return a list of the `n` most common elements and their counts from the most common to the least. If `n` is omitted or `None`, `most_common()` returns all elements in the counter. Elements with equal counts are ordered arbitrarily:
```python
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
```

**subtract([iterable-or-mapping])**

Elements are subtracted from an iterable or from another mapping (or counter). Like `dict.update()` but subtracts counts instead of replacing them. Both inputs and outputs may be zero or negative.
```python
>>> c = Counter(a=4, b=2, c=0, d=-2) 
>>> d = Counter(a=1, b=2, c=3, d=4) 
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```

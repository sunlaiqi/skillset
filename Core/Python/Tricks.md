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
  - [How to merge two dicts](#how-to-merge-two-dicts)
  - [How to sort a dict descending by its value and then ascending (A-Z) by its key (alphabetically).](#how-to-sort-a-dict-descending-by-its-value-and-then-ascending-a-z-by-its-key-alphabetically)
  - [Define Default Values in Dictionaries With .get() and .setdefault()](#define-default-values-in-dictionaries-with-get-and-setdefault)
  - [Handle Missing Dictionary Keys With collections.defaultdict()](#handle-missing-dictionary-keys-withcollectionsdefaultdict)
  - [Count Hashable Objects With collections.Counter](#count-hashable-objects-withcollectionscounter)
- [Functions](#functions)
  - [Function argument unpacking](#function-argument-unpacking)
  - [Measure the execution time of small bits of Python code with the "timeit" module](#measure-the-execution-time-of-small-bits-of-python-code-with-the-timeit-module)
- [Debug](#debug)
  - [Debug With breakpoint() Instead of print()](#debug-with-breakpoint-instead-of-print)


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

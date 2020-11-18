
- [Dict](#dict)
  - [Calculating with Dictionaries](#calculating-with-dictionaries)
  - [Finding Commonalities in Two Dictionaries](#finding-commonalities-in-two-dictionaries)
  - [Removing Duplicates from a Sequence while Maintaining Order](#removing-duplicates-from-a-sequence-while-maintaining-order)
  - [Determining the Most Frequently Occurring Items in a Sequence](#determining-the-most-frequently-occurring-items-in-a-sequence)
  - [Sorting a List of Dictionaries by a Common Key](#sorting-a-list-of-dictionaries-by-a-common-key)
  - [How to merge two dicts](#how-to-merge-two-dicts)
  - [Function argument unpacking](#function-argument-unpacking)
  - [Measure the execution time with "timeit" module](#measure-the-execution-time-with-timeit-module)
  - [Sort dict by key and item](#sort-dict-by-key-and-item)
- [Assert](#assert)
- [Context Managers and the with Statement](#context-managers-and-the-with-statement)
  - [Single Underscore: “_”](#single-underscore-_)
- [Cell in python](#cell-in-python)

## Dict 

### Calculating with Dictionaries

Problem 
You want to perform various calculations (e.g., minimum value, maximum value, sort‐ ing, etc.) on a dictionary of data. 

Solution 
Consider a dictionary that maps stock names to prices: 
```python
prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 } 
```
In order to perform useful calculations on the dictionary contents, it is often useful to invert the keys and values of the dictionary using zip(). For example, here is how to find the minimum and maximum price and stock name: 
```python
min_price = min(zip(prices.values(), prices.keys())) # min_price is (10.75, 'FB') 
max_price = max(zip(prices.values(), prices.keys())) # max_price is (612.78, 'AAPL') 
```
Similarly, to rank the data, use zip() with sorted(), as in the following: 
```python
prices_sorted = sorted(zip(prices.values(), prices.keys())) 
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'), 
#  (45.23, 'ACME'), (205.55, 'IBM'), 
#  (612.78, 'AAPL')]
```
When doing these calculations, be aware that zip() creates an iterator that can only be consumed once. For example, the following code is an error: 
```python
prices_and_names = zip(prices.values(), prices.keys()) 
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence 
```

The solution involving zip() solves the problem by “inverting” the dictionary into a sequence of `(value, key)` pairs. When performing comparisons on such tuples, the value element is compared first, followed by the key. This gives you exactly the behavior that you want and allows reductions and sorting to be easily performed on the dictionary contents using a single statement. 

### Finding Commonalities in Two Dictionaries 

Problem 

You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.). 

Solution 
Consider two dictionaries: 
```python
a={ 
    'x':1, 
    'y':2, 
    'z':3 
} 

b={
    'w' : 10, 
    'x' : 11, 
    'y' : 2 
} 

# Find keys in common
a.keys() & b.keys() # { 'x', 'y' } 
# Find keys in a that are not in b 
a.keys() - b.keys() # { 'z' } 
# Find (key,value) pairs in common 
a.items() & b.items() # { ('y', 2) } 
```
These kinds of operations can also be used to alter or filter dictionary contents. For example, suppose you want to make a new dictionary with selected keys removed. Here is some sample code using a dictionary comprehension: 
```python
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}} 
# c is {'x': 1, 'y': 2} 
```
Notes:
the values() method of a dictionary does not support the set operations described in this recipe 

### Removing Duplicates from a Sequence while Maintaining Order 

If the values in the sequence are hashable, the problem can be easily solved using a set and a generator. For example: 
```python
def dedupe(items): 
    seen = set() 
    for item in items:
        if item not in seen:
            yield item
            seen.add(item) 
```
Here is an example of how to use your function: 
```python
>>>a=[1,5,2,1,9,1,5,10] 
>>> list(dedupe(a))
[1, 5, 2, 9, 10]
>>> 
```

This only works if the items in the sequence are hashable. If you are trying to eliminate duplicates in a sequence of unhashable types (such as dicts), you can make a slight change to this recipe, as follows: 
```python
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val) 
```
Here, the purpose of the key argument is to specify a function that converts sequence items into a hashable type for the purposes of duplicate detection. Here’s how it works: 
```python
>>> a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}] 
>>> list(dedupe(a, key=lambda d: (d['x'],d['y'])))
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe(a, key=lambda d: d['x'])) 
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
>>>
```
The specification of a key function mimics similar functionality in built-in functions such as sorted(), min(), and max(). 

### Determining the Most Frequently Occurring Items in a Sequence 

The collections.Counter class is designed for just such a problem. It even comes with a handy `most_common()` method that will give you the answer. 
To illustrate, let’s say you have a list of words and you want to find out which words occur most often. Here’s how you would do it: 
```python
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
] 
from collections import Counter 
word_counts = Counter(words) 
top_three = word_counts.most_common(3) 
print(top_three) 
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
```

### Sorting a List of Dictionaries by a Common Key 

Sorting this type of structure is easy using the `operator` module’s `itemgetter` function. Let’s say you’ve queried a database table to get a listing of the members on your website, and you receive the following data structure in return: 
```python
rows=[
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} 
]
```
It’s fairly easy to output these rows ordered by any of the fields common to all of the dictionaries. For example: 
```python
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname')) 
rows_by_uid = sorted(rows, key=itemgetter('uid')) 
```
The `itemgetter()` function can also accept multiple keys. For example, this code
```python
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) 
```
The functionality of `itemgetter()` is sometimes replaced by lambda expressions. For example: 
```python
rows_by_fname = sorted(rows, key=lambda r: r['fname']) 
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname'])) 
```
This solution often works just fine. However, the solution involving `itemgetter()` typically runs a bit faster. Thus, you might prefer it if performance is a concern. 
Last, but not least, don’t forget that the technique shown in this recipe can be applied to functions such as min() and max(). For example: 
```python
>>> min(rows, key=itemgetter('uid'))
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001} 
>>> max(rows, key=itemgetter('uid'))
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004} 
>>> 
```



### How to merge two dicts

```python
# Use ** unpacking

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
>>> z
{'a': 1, 'b': 3, 'c': 4}
>>> z = {**x, 'foo': 1, 'bar': 2, **y}
>>> z
{'a': 1, 'b': 3, 'foo': 1, 'bar': 2, 'c': 4}
# ==========================================
>>> z = dict(x, **y)
>>> z
{'a': 1, 'b': 3, 'c': 4}

# Use copy and update functions
c = x.copy()
c.update(y)
>>> c
{'a': 1, 'b': 3, 'c': 4}

# Use itertools.chain
import itertools
z = dict(itertools.chain(x.items(), y.items()))

# Use list
z = dict(list(x.items()) + list(y.items()))
```

###  Function argument unpacking

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


###  Measure the execution time with "timeit" module 

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


### Sort dict by key and item

sort a dict descending by its value and then ascending (A-Z) by its key (alphabetically).

```python
dict = {'apple': 2, 'banana': 3, 'almond':2 , 'beetroot': 3, 'peach': 4}

>>> [item[0] for item in sorted(dict.items(), key=lambda x: (-x[1], x[0]) )]

['peach', 'banana', 'beetroot', 'almond', 'apple']
```

The following solution might be working in python 2.7:??
```python
>>> [v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))]
['peach', 'banana', 'beetroot', 'almond', 'apple']
```

Python 3 removed tuple parameter unpacking, so the line above should now be written as 
```python
[v[0] for v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))]. 
```
See PEP 3113 python.org/dev/peps/pep-3113





## Assert

At its core, Python’s assert statement is a debugging aid that tests a condition. If the assert condition is true, nothing happens, and your program continues to execute as normal. But if the condition evaluates to `false`, an AssertionError exception is raised with an optional error message. 
```python
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price'], "Some error happened!!!"
    return price
```
```
Traceback (most recent call last):
  File "assert.py", line 9, in <module>
    print(apply_discount(product, discount))
  File "assert.py", line 3, in apply_discount
    assert 0 <= price <= product['price'], "Some error happened!!!"
AssertionError: Some error happened!!!
```

You can use following to raise an AssertionError. But remember, it will be gone when assertions are globally disabled.
```python
assert False, ("Error message here!!!")
```

- Caveat #1 – Don’t Use Asserts for Data Validation 
    Assertions can be globally disabled3 with the -O and -OO command line switches, as well as the PYTHONOPTIMIZE environment variable in CPython. 

- Caveat #2 – Asserts That Never Fail 
    When you pass a tuple as the first argument in an assert statement, the assertion always evaluates as true and therefore never fails. 
    `assert(1 == 2, 'This should fail') `
    This has to do with non-empty tuples always being truthy in Python. 

    But, this caveat seems corrected in the newer python version:
    assert.py:5: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    `assert(1 == 2, 'This should fail’)`

## Context Managers and the with Statement 

What’s a context manager? It’s a simple “protocol” (or interface) that your object needs to follow in order to support the `with` statement. Basically, all you need to do is add __enter__ and __exit__ methods to an object if you want it to function as a context manager. 
```python
class ManagedFile:
    def __init__(self, name): 
		self.name = name 
	def __enter__(self):
        self.file = open(self.name, 'w') 
		return self.file 
	def __exit__(self, exc_type, exc_val, exc_tb): 
		if self.file: 
			self.file.close() 

>>> with ManagedFile('hello.txt') as f: 
	...  f.write('hello, world!') 
	...  f.write('bye now') 

# You can use contextmanager decorator
from contextlib import contextmanager
@contextmanager
def managed_file(name): 
    try: 
	    f = open(name, 'w') 
	    yield f 
	finally: 
		f.close() 
```

### Single Underscore: “_”

Per convention, a single stand-alone underscore is sometimes used as 
a name to indicate that a variable is temporary or insignificant.

“_” is a special variable in most Python REPLs that represents the result of the last expression evaluated by the interpreter. 

## Cell in python

In Python, cell objects are used to store the free variables of a closure.
Let's say you want a function that always returns a particular fraction of its argument. You can use a closure to achieve this:
```python
def multiplier(n, d):
    """Return a function that multiplies its argument by n/d."""
    def multiply(x):
        """Multiply x by n/d."""
        return x * n / d
    return multiply
```
And here's how you can use it:
```pytohn
>>> two_thirds = multiplier(2, 3)
>>> two_thirds(7)
4.666666666666667
```

What happens is that when multiplier is compiled, the interpreter notices that multiply is going to want to use its local variables later, so it keeps a note of them:
```python
>>> multiplier.__code__.co_cellvars
('d', 'n')
```

Then when multiplier is called, the value of those outer local variables is stored in the returned function's __closure__ attribute, as a tuple of cell objects:
```python
>>> two_thirds.__closure__
(<cell at 0x7f7a81282678: int object at 0x88ef60>,
 <cell at 0x7f7a81282738: int object at 0x88ef40>)
 ```
... with their names in the `__code__` object as `co_freevars`:
```
python >>> two_thirds.__code__.co_freevars 
('d', 'n') 
```
You can get at the contents of the cells using their cell_contents attribute:
```
python >>> {v: c.cell_contents for v, c in zip( two_thirds.__code__.co_freevars, two_thirds.__closure__ )} 
{'d': 3, 'n': 2} 
```
You can read more about closures and their implementation in the Python Enhancement Proposal which introduced them: PEP 227 — Statically Nested Scopes.
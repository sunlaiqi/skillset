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




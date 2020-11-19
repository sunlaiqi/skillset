

## What is iterator

iterator protocol

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

Up until now, our iterator example consisted of two separate classes, Repeater and RepeaterIterator. They corresponded directly to the two phases used by Python’s iterator protocol:
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

## built-in functions

- len()
len() function internally works like `list.__len__()` or `tuple.__le__()`. Thus, note that len() works only on objects that has a `__len__()`

- reversed(seq)
It returns the reverse iterator. seq must be an object which has `__reversed__()` method or supports the sequence protocol (the `__len__()` method and the `__getitem__()` method).It is generally used in for loop.

- enumerate

The enumerate() method adds a counter to an iterable and returns the enumerate object.
The syntax of enumerate () is −
enumerate(iterable, start = 0)

- sorted

- hasattr, getattr, setattr and delattr,
which allows attributes of an object to be manipulated by their string names.
- all and any,
which accept an iterable object and return
True if all, or any, of the items evaluate to be true.
- nzip
which takes two or more sequences and returns a new sequence of tuples, where each tuple contains a single value from each sequence.


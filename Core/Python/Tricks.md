
## How to merge two dicts
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

## Function argument unpacking
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

## Measure the execution time of small bits of Python code with the "timeit" module 
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

## How to sort a dict descending by its value and then ascending (A-Z) by its key (alphabetically).
```python
dict = {'apple': 2, 'banana': 3, 'almond':2 , 'beetroot': 3, 'peach': 4}

>>> [item[0] for item in sorted(dict.items(), key=lambda x: (-x[1], x[0]) )]

['peach', 'banana', 'beetroot', 'almond', 'apple']

# The following solution might be working in python 2.7:??
>>> [v[0] for v in sorted(d.iteritems(), key=lambda(k, v): (-v, k))]
['peach', 'banana', 'beetroot', 'almond', 'apple']


# Python 3 removed tuple parameter unpacking, so the line above should now be written as [v[0] for v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))]. See PEP 3113 python.org/dev/peps/pep-3113
```





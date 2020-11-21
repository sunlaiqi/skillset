
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

when a return statement is invoked inside a function, it perma- nently passes control back to the caller of the function. When a yield is invoked, it also passes control back to the caller of the function—but it only does so temporarily.

Whereas a return statement disposes of a function’s local state, a yield statement suspends the function and retains its local state.

An example with `return` which is hidden in for-in loop

```python
def bounded_repeater(value, max_repeats): 
    for i in range(max_repeats):
        yield value
iterator = bounded_repeater('Hello', 3)
next(iterator)
```

## Generator Expressions

You see, class-based iterators and generator functions are two expres- sions of the same underlying design pattern.

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

## Iterator Chains

when chaining generators, the data processing happens one element at a time. There’s no buffering between the processing steps in the chain.

```python
def integers():
    for i in range(1, 9):
        yield i
def squared(seq): 
    for i in seq:
        yield i * i
def negated(seq): 
    for i in seq:
        yield -i
chain = negated(squared(integers()))
print(list(chain))

# Use generator expression
integers = range(8)
squared = (i * i for i in integers) 
negated = (-i for i in squared)
print(type(squared))
print(list(negated))
```
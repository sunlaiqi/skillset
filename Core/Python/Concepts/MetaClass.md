- [Metaclass](#metaclass)
  - [Defining a Class Dynamically](#defining-a-class-dynamically)
    - [Examples](#examples)
    - [Custom Metaclasses](#custom-metaclasses)
    - [Object Factory and Class Factory](#object-factory-and-class-factory)

# Metaclass

In general, the type of any new-style class is type.
The type of the built-in classes you are familiar with is also type:

type is a metaclass, of which classes are instances. Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3, is an instance of the type metaclass.

type is also an instance of the type metaclass, so it is an instance of itself.

## Defining a Class Dynamically

You can also call type() with three arguments — `type(<name>, <bases>, <dct>)`:
- `<name>` specifies the class name. This becomes the `__name__` attribute of the class.
- `<bases>` specifies a tuple of the base classes from which the class inherits. This becomes the `__bases__` attribute of the class.
- `<dct>` specifies a namespace dictionary containing definitions for the class body. This becomes the `__dict__` attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. In other words, it dynamically creates a new class.

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
None ???
```

### Custom Metaclasses
Consider again this well-worn example:
```
>>> class Foo: 
...     pass
...
>>> f = Foo()
```
When the interpreter encounters Foo(), the following occurs:
The `__call__()` method of Foo’s parent class is called. Since Foo is a standard new-style class, its parent class is the `type` metaclass,
so type’s `__call__()` method is invoked.
That `__call__()` method in turn invokes the following:
```python
__new__() 
__init__()
```
In the following, a custom method called new() is defined and assigned as the `__new__()` method for Foo:
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

Define a metaclass from `tyep`:
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
Since type is a metaclass, that makes Meta a metaclass as well.
Delegates via super() to the `__new__()` method of the parent metaclass (type) to actually create a new class
Assigns the custom attribute attr to the class, with a value of 100
Returns the newly created class

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


- [Descriptor](#descriptor)
  - [What Are Python Descriptors?](#what-are-python-descriptors)
  - [Python Descriptors in Properties](#python-descriptors-in-properties)
  - [Python Descriptors in Methods and Functions??](#python-descriptors-in-methods-and-functions)
  - [How Attributes Are Accessed With the Lookup Chain](#how-attributes-are-accessed-with-the-lookup-chain)
  - [Shared Descriptor Instance](#shared-descriptor-instance)
  - [Use Dictionary to Rescue - Strong Reference](#use-dictionary-to-rescue---strong-reference)
  - [Best Solution - Store In The Object](#best-solution---store-in-the-object)
  - [`__set_name__(self, owner, name)`](#__set_name__self-owner-name)
  - [Why Use Python Descriptors?](#why-use-python-descriptors)
    - [Lazy Properties](#lazy-properties)
    - [D.R.Y. Code](#dry-code)

## Descriptor

### What Are Python Descriptors?

Descriptors are Python objects that implement a method of the **descriptor protocol**, which gives you the ability to create objects that have special behavior when they’re accessed as attributes of other objects. Here you can see the correct definition of the descriptor protocol:
```
__get__(self, obj, type=None) -> object 
__set__(self, obj, value) -> None 
__delete__(self, obj) -> None 
__set_name__(self, owner, name)
```
If your descriptor implements just .`__get__()`, then it’s said to be a **non-data descriptor**. If it implements .`__set__() or .__delete__()`, then it’s said to be a **data descriptor**. 

Take a look at the following example, which defines a descriptor that logs something on the console when it’s accessed:
```python
# descriptors.py
class Verbose_attribute():
    def __get__(self, obj, type=None) -> object: 
        print("accessing the attribute to get the value") return 42
    def __set__(self, obj, value) -> None: 
        print("accessing the attribute to set the value") raise AttributeError("Cannot change the value")

class Foo():
    attribute1 = Verbose_attribute()

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
```
In the example above, `Verbose_attribute()` implements the descriptor protocol. Once it’s instantiated as an attribute of Foo, it can be considered a descriptor.

### Python Descriptors in Properties

 The following example uses a **property** that logs a message to the console when it’s accessed:
```python
# property_decorator.py 
class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value") 
        return 42
    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value") 
        raise AttributeError("Cannot change the value")

my_foo_object = Foo()
x = my_foo_object.attribute1 
print(x)
```

The example before, in fact, can be written as follows:

```python
# property_function.py 
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value") 
        return 42
    def setter(self, value) -> None:
        print("accessing the attribute to set the value") 
        raise AttributeError("Cannot change the value")
    
    attribute1 = property(getter, setter) 
my_foo_object = Foo()
x = my_foo_object.attribute1 
print(x)
```
The signature of this function is as follows:
```python
property(fget=None, fset=None, fdel=None, doc=None) -> object
```
`property()` returns a property object that implements the descriptor protocol. 

### Python Descriptors in Methods and Functions??

Note that, in Python, a class method is just a static method that takes the class reference as the first argument of the argument list.

### How Attributes Are Accessed With the Lookup Chain

In Python, every object has a built-in `__dict__` attribute. This is a dictionary that contains all the attributes defined in the object itself. 

So, what’s going on under the hood when you access an attribute in Python? Consider this code:

```python
# lookup.py
class Vehicle(object):
    can_fly = False 
    number_of_weels = 0
class Car(Vehicle): 
    number_of_weels = 4
    def __init__(self, color): 
        self.color = color
my_car = Car("red")
print(my_car.color) 
print(my_car.number_of_weels) 
print(my_car.can_fly)
```
Result:
```
$ python lookup.py 
red
4
False
```
Here, when you access the attribute `color` of the instance `my_car`, you’re actually accessing a single value of the `__dict__` attribute of the
object `my_car`, `my_car.__dict__['color']`. 

So, what happens when you access the attribute of an object with dot notation? How does the interpreter know what you really need? Well, here’s where a concept called the lookup chain comes in:
- First, you’ll get the result returned from the `__get__` method of the data descriptor named after the attribute you’re looking for.
- If that fails, then you’ll get the value of your object’s `__dict__` for the key named after the attribute you’re looking for.
- If that fails, then you’ll get the result returned from the `__get__` method of the non-data descriptor named after the attribute you’re looking for.
- If that fails, then you’ll get the value of your object type’s `__dict__` for the key named after the attribute you’re looking for.
- If that fails, then you’ll get the value of your object parent
type’s `__dict__` for the key named after the attribute you’re looking for.
- If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.
- If everything else has failed, then you’ll get an AttributeError exception.

If you want to use Python descriptors in your code, then you just need to implement the descriptor protocol. The most important methods of this protocol are `__get__()` and `__set__()`, which have the following signature:
- `__get__(self, obj, type=None) -> object` 
- `__set__(self, obj, value) -> None`
  
When you implement the protocol, keep these things in mind:
- `self` is the instance of the descriptor you’re writing.
- `obj` is the instance of the object your descriptor is attached to. 
- `type` is the type of the object the descriptor is attached to.
In `__set__()`, you don’t have the type variable, because you can only
call `__set__()` on the **object**. In contrast, you can call `__get__()` on both the object and the class.

### Shared Descriptor Instance

Another important thing to know is that Python descriptors are
instantiated just once per class. That means that every single instance of a class containing a descriptor shares that descriptor instance. This is something that you might not expect and can lead to a classic pitfall.

### Use Dictionary to Rescue - Strong Reference

Since .__get__() and .__set__() have the obj attribute, which is the instance of the object you’re attached to. You could use this value as a key for the dictionary.

Unfortunately, the downside here is that the descriptor is keeping a strong reference to the owner object. This means that if you destroy the object, then the memory is not released because the garbage collector keeps finding a reference to that object inside the descriptor!

### Best Solution - Store In The Object

You may think that the solution here could be the use of weak references. While that may, you’d have to deal with the fact that not everything can be referenced as weak and that, when your objects get collected, they disappear from your dictionary.
The best solution here is to simply not store values in the descriptor itself, but to store them in the object that the descriptor is attached to. Try this approach next:
```python
# descriptors4.py
class OneDigitNumericValue():
    def __init__(self, name): 
        self.name = name
    def __get__(self, obj, type=None) -> object: 
        return obj.__dict__.get(self.name) or 0
    def __set__(self, obj, value) -> None: 
        obj.__dict__[self.name] = value
class Foo():
    number = OneDigitNumericValue("number")
my_foo_object = Foo() 
my_second_foo_object = Foo()
my_foo_object.number = 3 
print(my_foo_object.number) 
print(my_second_foo_object.number)
my_third_foo_object = Foo() 
print(my_third_foo_object.number)
```

In this example, when you set a value to the number attribute of your object, the descriptor stores it in the `__dict__` attribute of the object it’s attached to using the same name of the descriptor itself.
The only problem here is that when you instantiate the descriptor you have to specify the `name` as a parameter:
```python
number = OneDigitNumericValue(“number")
```
Wouldn’t it be better to just write `number = OneDigitNumericValue()`? It might, but if you’re running a version of Python less than 3.6, then you’ll need a little bit of magic here with metaclasses and decorators. If you
use Python 3.6 or higher, however, then the descriptor protocol has a new method .`__set_name__()` that does all this magic for you, as proposed in PEP 487:

### `__set_name__(self, owner, name)`

With this new method, whenever you instantiate a descriptor this method is called and the name parameter automatically set.
Now, try to rewrite the former example for Python 3.6 and up:
```python
# descriptors5.py
class OneDigitNumericValue():
    def __set_name__(self, owner, name): 
        self.name = name
    def __get__(self, obj, type=None) -> object: 
        return obj.__dict__.get(self.name) or 0
    def __set__(self, obj, value) -> None: 
        obj.__dict__[self.name] = value
class Foo():
    number = OneDigitNumericValue()
my_foo_object = Foo() 
my_second_foo_object = Foo()
my_foo_object.number = 3 
print(my_foo_object.number) 
print(my_second_foo_object.number)
my_third_foo_object = Foo() 
print(my_third_foo_object.number)
```

### Why Use Python Descriptors?

#### Lazy Properties
The first and most straightforward example is lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time. Then, they load their initial value and keep that value cached for later reuse.
Consider the following example. You have a class DeepThought that contains a method meaning_of_life() that returns a value after a lot of time spent in heavy concentration:
```python
# slow_properties.py 
import random 
import time
class DeepThought:
    def meaning_of_life(self):
        time.sleep(3) 
        return 42
my_deep_thought_instance = DeepThought() 
print(my_deep_thought_instance.meaning_of_life()) 
print(my_deep_thought_instance.meaning_of_life()) 
print(my_deep_thought_instance.meaning_of_life())
```
If you run this code and try to access the method three times, then you get an answer every three seconds, which is the length of the sleep time inside the method.
Now, a lazy property can instead evaluate this method just once when it’s first executed. Then, it will cache the resulting value so that, if you need it again, you can get it in no time. You can achieve this with the use of Python descriptors:
```python
# lazy_properties.py 
import random 
import time
class LazyProperty:
    def __init__(self, function):
        self.function = function 
        self.name = function.__name__
    def __get__(self, obj, type=None) -> object: 
        obj.__dict__[self.name] = self.function(obj) 
        return obj.__dict__[self.name]

class DeepThought: 
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3) 
        return 42
my_deep_thought_instance = DeepThought() 
print(my_deep_thought_instance.meaning_of_life) 
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
```
Take your time to study this code and understand how it works. Can you see the power of Python descriptors here? In this example, when you use the @LazyProperty descriptor, you’re instantiating a descriptor and passing to it `meaning_of_life()`. This descriptor stores both the method and its name as instance variables.
Since it is a non-data descriptor, when you first access the value of
the `meaning_of_life` attribute, `__get__()` is automatically called and executes `meaning_of_life()` on the my_deep_thought_instance object. The resulting value is stored in the `__dict__` attribute of the object itself. When you access the meaning_of_life attribute again, Python will use the lookup chain to find a value for that attribute inside the `__dict__` attribute, and that value will be returned immediately.
Note that this works because, in this example, you’ve only used one method `__get__()` of the descriptor protocol. You’ve also implemented a non-data descriptor. If you had implemented a data descriptor, then the trick would not have worked. 

#### D.R.Y. Code

```python
# properties.py
class Values:
    def __init__(self): 
        self._value1 = 0 
        self._value2 = 0 
        self._value3 = 0 
        self._value4 = 0 
        self._value5 = 0

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value % 2 == 0 else 0
    @property
    def value2(self):
        return self._value2
    @value2.setter
    def value2(self, value):
        self._value2 = value if value % 2 == 0 else 0
    @property
    def value3(self):
        return self._value3
    @value3.setter
    def value3(self, value):
        self._value3 = value if value % 2 == 0 else 0
    @property
    def value4(self):
        return self._value4
    @value4.setter
    def value4(self, value):
        self._value4 = value if value % 2 == 0 else 0
    @property
    def value5(self):
        return self._value5
    @value5.setter
    def value5(self, value):
        self._value5 = value if value % 2 == 0 else 0

my_values = Values() 
my_values.value1 = 1
my_values.value2 = 4 
print(my_values.value1) 
print(my_values.value2)
```
As you can see, you have a lot of duplicated code here. It’s possible to use Python descriptors to share behavior among all the properties. You can create an EvenNumber descriptor and use it for all the properties like this:
```python
# properties2.py 
class EvenNumber:
    def __set_name__(self, owner, name): 
        self.name = name
    def __get__(self, obj, type=None) -> object: 
        return obj.__dict__.get(self.name) or 0
    def __set__(self, obj, value) -> None: 
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)

class Values:
    value1 = EvenNumber() 
    value2 = EvenNumber() 
    value3 = EvenNumber() 
    value4 = EvenNumber() 
    value5 = EvenNumber()

my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
```
This code looks a lot better now! The duplicates are gone and the logic is now implemented in a single place so that if you need to change it, you can do so easily.


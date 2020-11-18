
- [装饰器高阶篇](#装饰器高阶篇)
  - [高级主题](#高级主题)
    - [类作为装饰器](#类作为装饰器)
      - [类装饰类](#类装饰类)
      - [类装饰函数](#类装饰函数)
    - [内置类装饰器](#内置类装饰器)
    - [装饰整个类](#装饰整个类)
  - [高级应用](#高级应用)
    - [Registering Plugins](#registering-plugins)
    - [用户认证](#用户认证)
    - [Creating Singletons](#creating-singletons)
    - [Caching Return Values](#caching-return-values)
    - [Adding Information About Units](#adding-information-about-units)
    - [Validating JSON](#validating-json)

# 装饰器高阶篇

## 高级主题

### 类作为装饰器

#### 类装饰类

```python
>>> def decorator(cls):
...     class NewClass(cls): 
...         attr = 100
...     return NewClass 
...
>>> @decorator
... class X:
...     pass
...
>>> @decorator 
... class Y:
...     pass
...
>>> @decorator 
... class Z:
...     pass
...
>>> X.attr 
100
>>> Y.attr 
100
>>> Z.attr 
100
```

#### 类装饰函数
为了将类作为装饰器，我么需要使用类的`__call__`方法。
```python
# Python program showing 
# use of __call__() method 
  
class MyDecorator: 
    def __init__(self, function): 
        self.function = function 
      
    def __call__(self, *args, **kwargs): 
  
        # We can add some code  
        # before function call 
        print("Before decorating for {}".format(self.function.__name__))
        self.function(*args, **kwargs) 
        print("After decorating for {}".format(self.function.__name__))
        # We can also add some code 
        # after function call. 
  
# adding class decorator to the function 
@MyDecorator
def my_function(x): 
    print("Hello {}".format(x)) 
  
my_function("world !") 

# Before decorating for my_function
# Hello world !
# After decorating for my_function
```
### 内置类装饰器
@classmethod, @staticmethod, and @property decorators

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
```
**注解**：
- `cylinder_volume()`是一个常规函数。
- `radius`是一个可修改属性。
- `area`是一个不可修改属性。 
- `unit_circle()`是一个类方法。它不绑定于Circle的某个特定实例。类方法经常被用来作为工厂方法创建类的特殊实例。 
- `pi()`是一个静态方法。除了它是Circle类的命名空间的一部分，它实际上并不依赖Circle类。静态方法既可以通过实例调用，也可以通过类调用。通常用于构建一类工具的集合。

### 装饰整个类

下面的例子相当于：
MyClass = my_decorator(MyClass)
你会发现，装饰器并没有装饰类的方法，它只是装饰了类的实例化过程，也就是`__init__`方法。
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start decoration.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
class MyClass:
    def __init__(self, x="Hello!"):
        self.x = x
        print(self.x)
    def hello(self, y):
        print(y)
    

a = MyClass()
a.hello("This is fun!")
b = MyClass("Ni Hao!")
b.hello("Zhen Hao Wan!")
```

## 高级应用

### Registering Plugins

Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:
```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
```
The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict. Note that you do not have to write an inner function or use @functools.wraps in this example because you are returning the original function unmodified.

The randomly_greet() function randomly chooses one of the registered functions to use. Note that the PLUGINS dictionary already contains references to each function object that is registered as a plugin:
```python
>>> PLUGINS
{'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>}

>>> randomly_greet("Alice")
Using 'say_hello'
'Hello Alice'
```
The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins exist. That list is created when the plugins register themselves. This makes it trivial to add a new plugin: just define the function and decorate it with @register.

If you are familiar with globals() in Python, you might see some similarities to how the plugin architecture works. globals() gives access to all global variables in the current scope, including your plugins:
```python
>>> globals()
{..., # Lots of variables not shown here.
 'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>,
 'randomly_greet': <function randomly_greet at 0x7f768eae6840>}
```
Using the @register decorator, you can create your own curated list of interesting variables, effectively hand-picking some functions from globals().


### 用户认证

Is the User Logged In?
The final example before moving on to some fancier decorators is commonly used when working with a web framework. In this example, we are using Flask to set up a /secret web page that should only be visible to users that are logged in or otherwise authenticated:
```python
from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...
```
While this gives an idea about how to add authentication to your web framework, you should usually not write these types of decorators yourself. For Flask, you can use the Flask-Login extension instead, which adds more security and functionality.

### Creating Singletons

A singleton is a class with only one instance. There are several singletons in Python that you use frequently, including None, True, and False. It is the fact that None is a singleton that allows you to compare for None using the is keyword, like you saw in the Both Please section:
```python
if _func is None:
    return decorator_name
else:
    return decorator_name(_func)
```
Using is returns True only for objects that are the exact same instance. The following @singleton decorator turns a class into a singleton by storing the first instance of the class as an attribute. Later attempts at creating an instance simply return the stored instance:
```python
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass
```
As you see, this class decorator follows the same template as our function decorators. The only difference is that we are using cls instead of func as the parameter name to indicate that it is meant to be a class decorator.

Let’s see if it works:
```python
>>> first_one = TheOne()
>>> another_one = TheOne()

>>> id(first_one)
140094218762280

>>> id(another_one)
140094218762280

>>> first_one is another_one
True
```

It seems clear that first_one is indeed the exact same instance as another_one.

Note: Singleton classes are not really used as often in Python as in other languages. The effect of a singleton is usually better implemented as a global variable in a module.

### Caching Return Values

Decorators can provide a nice mechanism for caching and memoization. As an example, let’s look at a recursive definition of the Fibonacci sequence:
```python
from decorators import count_calls

@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
While the implementation is simple, its runtime performance is terrible:

>>> fibonacci(10)
<Lots of output from count_calls>
55

>>> fibonacci.num_calls
177
```
To calculate the tenth Fibonacci number, you should really only need to calculate the preceding Fibonacci numbers, but this implementation somehow needs a whopping 177 calculations. It gets worse quickly: 21891 calculations are needed for fibonacci(20) and almost 2.7 million calculations for the 30th number. This is because the code keeps recalculating Fibonacci numbers that are already known.

The usual solution is to implement Fibonacci numbers using a for loop and a lookup table. However, simple caching of the calculations will also do the trick:
```python
import functools
from decorators import count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
The cache works as a lookup table, so now fibonacci() only does the necessary calculations once:

>>> fibonacci(10)
Call 1 of 'fibonacci'
...
Call 11 of 'fibonacci'
55

>>> fibonacci(8)
21
```
Note that in the final call to fibonacci(8), no new calculations were needed, since the eighth Fibonacci number had already been calculated for fibonacci(10).

In the standard library, a Least Recently Used (LRU) cache is available as @functools.lru_cache.

This decorator has more features than the one you saw above. You should use @functools.lru_cache instead of writing your own cache decorator:
```python
import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
```
The maxsize parameter specifies how many recent calls are cached. The default value is 128, but you can specify maxsize=None to cache all function calls. However, be aware that this can cause memory problems if you are caching many large objects.

You can use the .cache_info() method to see how the cache performs, and you can tune it if needed. In our example, we used an artificially small maxsize to see the effect of elements being removed from the cache:
```python
>>> fibonacci(10)
Calculating fibonacci(10)
Calculating fibonacci(9)
Calculating fibonacci(8)
Calculating fibonacci(7)
Calculating fibonacci(6)
Calculating fibonacci(5)
Calculating fibonacci(4)
Calculating fibonacci(3)
Calculating fibonacci(2)
Calculating fibonacci(1)
Calculating fibonacci(0)
55

>>> fibonacci(8)
21

>>> fibonacci(5)
Calculating fibonacci(5)
Calculating fibonacci(4)
Calculating fibonacci(3)
Calculating fibonacci(2)
Calculating fibonacci(1)
Calculating fibonacci(0)
5

>>> fibonacci(8)
Calculating fibonacci(8)
Calculating fibonacci(7)
Calculating fibonacci(6)
21

>>> fibonacci(5)
5

>>> fibonacci.cache_info()
CacheInfo(hits=17, misses=20, maxsize=4, currsize=4)
```

### Adding Information About Units

The following example is somewhat similar to the Registering Plugins example from earlier, in that it does not really change the behavior of the decorated function. Instead, it simply adds unit as a function attribute:
```python
def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit
```
The following example calculates the volume of a cylinder based on its radius and height in centimeters:
```python
import math

@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height
```
This .unit function attribute can later be accessed when needed:
```python
>>> volume(3, 5)
141.3716694115407

>>> volume.unit
'cm^3'
```
Note that you could have achieved something similar using function annotations:
```python
import math

def volume(radius, height) -> "cm^3":
    return math.pi * radius**2 * height
```
However, since annotations are used for type hints, it would be hard to combine such units as annotations with static type checking.

Units become even more powerful and fun when connected with a library that can convert between units. One such library is pint. With pint installed (pip install Pint), you can for instance convert the volume to cubic inches or gallons:
```python
>>> import pint
>>> ureg = pint.UnitRegistry()
>>> vol = volume(3, 5) * ureg(volume.unit)

>>> vol
<Quantity(141.3716694115407, 'centimeter ** 3')>

>>> vol.to("cubic inches")
<Quantity(8.627028576414954, 'inch ** 3')>

>>> vol.to("gallons").m  # Magnitude
0.0373464440537444
```
You could also modify the decorator to return a pint Quantity directly. Such a Quantity is made by multiplying a value with the unit. In pint, units must be looked up in a UnitRegistry. The registry is stored as a function attribute to avoid cluttering the namespace:
```pytohn
def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()
    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration
With the @use_unit decorator, converting units is practically effortless:

>>> bolt = average_speed(100, 9.58)
>>> bolt
<Quantity(10.438413361169102, 'meter / second')>

>>> bolt.to("km per hour")
<Quantity(37.578288100208766, 'kilometer / hour')>

>>> bolt.to("mph").m  # Magnitude
23.350065679064745
```
### Validating JSON

Let’s look at one last use case. Take a quick look at the following Flask route handler:
```python
@app.route("/grade", methods=["POST"])
def update_grade():
    json_data = request.get_json()
    if "student_id" not in json_data:
        abort(400)
    # Update database
    return "success!"
```
Here we ensure that the key student_id is part of the request. Although this validation works, it really does not belong in the function itself. Plus, perhaps there are other routes that use the exact same validation. So, let’s keep it DRY and abstract out any unnecessary logic with a decorator. The following @validate_json decorator will do the job:
```python
from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
```
In the above code, the decorator takes a variable length list as an argument so that we can pass in as many string arguments as necessary, each representing a key used to validate the JSON data:

The list of keys that must be present in the JSON is given as arguments to the decorator.
The wrapper function validates that each expected key is present in the JSON data.
The route handler can then focus on its real job—updating grades—as it can safely assume that JSON data are valid:
```python
@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"
```

Conclusion
This has been quite a journey! You started this tutorial by looking a little closer at functions, particularly how they can be defined inside other functions and passed around just like any other Python object. Then you learned about decorators and how to write them such that:

They can be reused.
They can decorate functions with arguments and return values.
They can use @functools.wraps to look more like the decorated function.
In the second part of the tutorial, you saw more advanced decorators and learned how to:





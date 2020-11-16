- [描述符](#描述符)
  - [描述符设计模式](#描述符设计模式)
  - [调用描述符](#调用描述符)
    - [描述符调用纵览](#描述符调用纵览)
  - [自动命名通知](#自动命名通知)
  - [描述符的完善](#描述符的完善)
  - [为什么使用描述符](#为什么使用描述符)
    - [Lazy Properties](#lazy-properties)
    - [D.R.Y. Code](#dry-code)
  - [ORM的例子](#orm的例子)


# 描述符

## 描述符设计模式

A common use for descriptors is in an object-oriented database (or an object-relational mapping). In a database context, getting an attribute value may require fetching data objects from the file system; which may involve creating and executing a query in a database.

**Descriptor Design Pattern**. The Descriptor design pattern has two parts: the Owner and the attribute Descriptor . The Owner is usually a relatively complex object that uses one or more Descriptors for it's attributes. Each Descriptor class defines get, set and delete methods for a specific attribute of the Owner.

Note that Desciptors can easily be written as reusable, generic types of attributes. The Owner can have multiple instances of each Descriptor. Each use of a Desciptor class is a unique instance of a Descriptor object, bound to an attribute name when the Owner class is defined.

To be recognized as a Descriptor, a class must implement some combination of the following three methods.

- **`__get__ ( self , instance , owner )`**
The instance argument is the self variable of the owning class; the owner argument is the owning class object. This method of the descriptor must return this attribute's value. If this descriptor implements a class level variable, the instance parameter can be ignored.

- **`__set__ ( self , instance , value )`**
The instance argument is the self variable of the owning class. This method of the descriptor must set this attribute's value.

- **`__delete__ ( self , instance )`**
The instance argument is the self variable of the owning class. This method of the descriptor must delete this attribute's value.

Sometimes, a descriptor class will also need an `__init__` method function to initialize the descriptor's internal state. Less commonly, the descriptor may also need `__str__` or `__repr__` method functions to display the instance variable correctly.

You must also make a design decision when defining a descriptor. You must determine where the underlying instance variable is contained. You have two choices.

- The Descriptor object has the instance variable.

- The Owner object contains the instance variable. In this case, the descriptor class must use the instance parameter to reference values in the owning object.

Descriptor Example. Here's a simple example of an object with two attributes defined by descriptors. One descriptor (Celsius) contains it's own value. The other desriptor (Farenheit), depends on the Celsius value, showing how attributes can be "linked" so that a change to one directly changes the other.

Example 25.1. descriptor.py

class Celsius( object ):
    def __init__( self, value=0.0 ):
        self.value= float(value)
    def __get__( self, instance, owner ):
        return self.value
    def __set__( self, instance, value ):
        self.value= float(value)
        
class Farenheit( object ):
    def __get__( self, instance, owner ):
        return instance.celsius * 9 / 5 + 32
    def __set__( self, instance, value ):
        instance.celsius= (float(value)-32) * 5 / 9

class Temperature( object ):
    celsius= Celsius()
    farenheit= Farenheit()
1	
We've defined a Celsius descriptor. The Celsius descriptor has an __init__ method which defines the attribute's value. The Celsius descriptor implements the __get__ method to return the current value of the attribute, and a __set__ method to change the value of this attribute.

2	
The Farenheit descriptor implements a number of conversions based on the value of the celsius attribute. The __get__ method converts the internal value from Celsius to Farenheit. The __set__ method converts the supplied value (in Farenheit) to Celsius.

3	
The owner class, Temperature has two attributes, both of which are managed by descriptors. One attribute, celsius, uses an instance of the Celsius descriptor. The other attribute, farenheit, uses an instance of the Fareheit descriptor. When we use one of these attributes in an assignment statement, the descriptor's __set__ method is used. When we use one of these attributes in an expression, the descriptor's __get__ method is used. We didn't show a __delete__ method; this would be used when the attribute is used in a del statement.

Let's look at what happens when we set an attribute value, for example, using oven.farenheit= 450. In this case, the farenheit attribute is a Descriptor with a __set__ method. This __set__ method is evaluated with instance set to the object which is being modified (the oven variable) and owner set to the Temperature class. The __set__ method computes the celsius value, and provides that to the celsius attribute of the instance. The Celsius descriptor simply saves the value.

When we get an attribute value, for example, using oven.celsius, the following happens. Since celsius is a Descriptor with a __get__ method, this method is evaluated, and returns the celsius temperature.

## 调用描述符

The most common method of calling a descriptor is for the descriptor to be invoked automatically when you access an attribute. A typical example would be my_obj.attribute_name. This will cause your object to look up attribute_name in the my_obj object. If your attribute_name happens to define __get__(), then attribute_name.__get__(my_obj) will get called. This all depends on whether your instance is an object or a class.

The magic behind this lies in the magic method known as __getattribute__, which will turn my_obj.a into this: type(my_obj).__dict__[‘a’].__get__(a, type(a)). You can read all about the implementation in Python’s documentation here: https://docs.python.org/3/howto/descriptor.html.

According to said documentation, there are a few points to keep in mind in regards to calling a descriptor:

The descriptor is invoked via the default implementation of the __getattribute__ method
If you override __getattribute__, this will prevent the descriptor from getting automatically called
object.__getattribute__() and type.__getattribute__() don’t call __get__() the same way
A data descriptor will always, ALWAYS override instance dictionaries
The non-data descriptor can be overridden by instance dictionaries.
More information on how all this works can be found in Python’s data model, the Python source code and in Guido van Rossum’s document, “Unifying types and class in Python”.

### 描述符调用纵览

A descriptor can be called directly with desc.__get__(obj) or desc.__get__(None, cls).

But it is more common for a descriptor to be invoked automatically from attribute access.

The expression obj.x looks up the attribute x in the chain of namespaces for obj. If the search finds a descriptor, its __get__() method is invoked according to the precedence rules listed below.

The details of invocation depend on whether obj is an object, class, or instance of super.

Invocation from an instance
Instance lookup scans through a chain of namespaces giving data descriptors the highest priority, followed by instance variables, then non-data descriptors, then class variables, and lastly __getattr__() if it is provided.

If a descriptor is found for a.x, then it is invoked with: desc.__get__(a, type(a)).

The logic for a dotted lookup is in object.__getattribute__(). Here is a pure Python equivalent:

def object_getattribute(obj, name):
    "Emulate PyObject_GenericGetAttr() in Objects/object.c"
    null = object()
    objtype = type(obj)
    value = getattr(objtype, name, null)
    if value is not null and hasattr(value, '__get__'):
        if hasattr(value, '__set__') or hasattr(value, '__delete__'):
            return value.__get__(obj, objtype)  # data descriptor
    try:
        return vars(obj)[name]                  # instance variable
    except (KeyError, TypeError):
        pass
    if hasattr(value, '__get__'):
        return value.__get__(obj, objtype)      # non-data descriptor
    if value is not null:
        return value                            # class variable
    # Emulate slot_tp_getattr_hook() in Objects/typeobject.c
    if hasattr(objtype, '__getattr__'):
        return objtype.__getattr__(obj, name)   # __getattr__ hook
    raise AttributeError(name)
The TypeError exception handler is needed because the instance dictionary doesn’t exist when its class defines __slots__.

Invocation from a class
The logic for a dotted lookup such as A.x is in type.__getattribute__(). The steps are similar to those for object.__getattribute__() but the instance dictionary lookup is replaced by a search through the class’s method resolution order.

If a descriptor is found, it is invoked with desc.__get__(None, A).

The full C implementation can be found in type_getattro() and _PyType_Lookup() in Objects/typeobject.c.

Invocation from super
The logic for super’s dotted lookup is in the __getattribute__() method for object returned by super().

A dotted lookup such as super(A, obj).m searches obj.__class__.__mro__ for the base class B immediately following A and then returns B.__dict__['m'].__get__(obj, A). If not a descriptor, m is returned unchanged.

The full C implementation can be found in super_getattro() in Objects/typeobject.c. A pure Python equivalent can be found in Guido’s Tutorial.

Summary of invocation logic
The mechanism for descriptors is embedded in the __getattribute__() methods for object, type, and super().

The important points to remember are:

Descriptors are invoked by the __getattribute__() method.

Classes inherit this machinery from object, type, or super().

Overriding __getattribute__() prevents automatic descriptor calls because all the descriptor logic is in that method.

object.__getattribute__() and type.__getattribute__() make different calls to __get__(). The first includes the instance and may include the class. The second puts in None for the instance and always includes the class.

Data descriptors always override instance dictionaries.

Non-data descriptors may be overridden by instance dictionaries.

## 自动命名通知

Sometimes it is desirable for a descriptor to know what class variable name it was assigned to. When a new class is created, the type metaclass scans the dictionary of the new class. If any of the entries are descriptors and if they define __set_name__(), that method is called with two arguments. The owner is the class where the descriptor is used, and the name is the class variable the descriptor was assigned to.

The implementation details are in type_new() and set_names() in Objects/typeobject.c.

Since the update logic is in type.__new__(), notifications only take place at the time of class creation. If descriptors are added to the class afterwards, __set_name__() will need to be called manually.


## 描述符的完善

Another important thing to know is that Python descriptors are instantiated just once per class. That means that every single instance of a class containing a descriptor shares that descriptor instance. This is something that you might not expect and can lead to a classic pitfall, like this:
```python
# descriptors2.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

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
Here, you have a class Foo that defines an attribute number, which is a descriptor. This descriptor accepts a single-digit numeric value and stores it in a property of the descriptor itself. However, this approach won’t work, because each instance of Foo shares the same descriptor instance. What you’ve essentially created is just a new class-level attribute.

Try to run the code and examine the output:

$ python descriptors2.py
3
3
3
You can see that all the instances of Foo have the same value for the attribute number, even though the last one was created after the my_foo_object.number attribute was set.

So, how can you solve this problem? You might think that it’d be a good idea to use a dictionary to save all the values of the descriptor for all the objects it’s attached to. This seems to be a good solution since .__get__() and .__set__() have the obj attribute, which is the instance of the object you’re attached to. You could use this value as a key for the dictionary.

Unfortunately, this solution has a big downside, which you can see in the following example:
```python
# descriptors3.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value

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
In this example, you use a dictionary for storing the value of the number attribute for all your objects inside your descriptor. When you run this code, you’ll see that it runs fine and that the behavior is as expected:

$ python descriptors3.py
3
0
0
Unfortunately, the downside here is that the descriptor is keeping a strong reference to the owner object. This means that if you destroy the object, then the memory is not released because the garbage collector keeps finding a reference to that object inside the descriptor!

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
In this example, when you set a value to the number attribute of your object, the descriptor stores it in the __dict__ attribute of the object it’s attached to using the same name of the descriptor itself.

The only problem here is that when you instantiate the descriptor you have to specify the name as a parameter:

`number = OneDigitNumericValue("number")`
Wouldn’t it be better to just write number = OneDigitNumericValue()? It might, but if you’re running a version of Python less than 3.6, then you’ll need a little bit of magic here with metaclasses and decorators. If you use Python 3.6 or higher, however, then the descriptor protocol has a new method .`__set_name__()` that does all this magic for you, as proposed in PEP 487:

`__set_name__(self, owner, name)`
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
Now, .__init__() has been removed and .__set_name__() has been implemented. This makes it possible to create your descriptor without specifying the name of the internal attribute that you need to use for storing the value. Your code also looks nicer and cleaner now!

Run this example one more time to make sure everything works:

$ python descriptors5.py
3
0
0

## 为什么使用描述符

Now you know what Python descriptors are and how Python itself uses them to power some of its features, like methods and properties. You’ve also seen how to create a Python descriptor while avoiding some common pitfalls. Everything should be clear now, but you may still wonder why you should use them.

In my experience, I’ve known a lot of advanced Python developers that have never used this feature before and that have no need for it. That’s quite normal because there are not many use cases where Python descriptors are necessary. However, that doesn’t mean that Python descriptors are just an academic topic for advanced users. There are still some good use cases that can justify the price of learning how to use them.

### Lazy Properties

The first and most straightforward example is lazy properties. These are properties whose initial values are not loaded until they’re accessed for the first time. Then, they load their initial value and keep that value cached for later reuse.

Consider the following example. You have a class DeepThought that contains a method meaning_of_life() that returns a value after a lot of time spent in heavy concentration:
```python
# slow_properties.py
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
Take your time to study this code and understand how it works. Can you see the power of Python descriptors here? In this example, when you use the @LazyProperty descriptor, you’re instantiating a descriptor and passing to it .meaning_of_life(). This descriptor stores both the method and its name as instance variables.

Since it is a non-data descriptor, when you first access the value of the meaning_of_life attribute, .__get__() is automatically called and executes .meaning_of_life() on the my_deep_thought_instance object. The resulting value is stored in the __dict__ attribute of the object itself. When you access the meaning_of_life attribute again, Python will use the lookup chain to find a value for that attribute inside the __dict__ attribute, and that value will be returned immediately.

Note that this works because, in this example, you’ve only used one method .__get__() of the descriptor protocol. You’ve also implemented a non-data descriptor. If you had implemented a data descriptor, then the trick would not have worked. Following the lookup chain, it would have had precedence over the value stored in __dict__. To test this out, run the following code:
```python
# wrong_lazy_properties.py
import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        pass

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
In this example, you can see that just implementing .__set__(), even if it doesn’t do anything at all, creates a data descriptor. Now, the trick of the lazy property stops working.

### D.R.Y. Code

Another typical use case for descriptors is to write reusable code and make your code D.R.Y. Python descriptors give developers a great tool to write reusable code that can be shared among different properties or even different classes.

Consider an example where you have five different properties with the same behavior. Each property can be set to a specific value only if it’s an even number. Otherwise, it’s value is set to 0:
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

## ORM的例子

The following code is simplified skeleton showing how data descriptors could be used to implement an object relational mapping.

The essential idea is that the data is stored in an external database. The Python instances only hold keys to the database’s tables. Descriptors take care of lookups or updates:

class Field:

    def __set_name__(self, owner, name):
        self.fetch = f'SELECT {name} FROM {owner.table} WHERE {owner.key}=?;'
        self.store = f'UPDATE {owner.table} SET {name}=? WHERE {owner.key}=?;'

    def __get__(self, obj, objtype=None):
        return conn.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        conn.execute(self.store, [value, obj.key])
        conn.commit()
We can use the Field class to define “models” that describe the schema for each table in a database:

class Movie:
    table = 'Movies'                    # Table name
    key = 'title'                       # Primary key
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key

class Song:
    table = 'Music'
    key = 'title'
    artist = Field()
    year = Field()
    genre = Field()

    def __init__(self, key):
        self.key = key
An interactive session shows how data is retrieved from the database and how it can be updated:

>>>
>>> import sqlite3
>>> conn = sqlite3.connect('entertainment.db')

>>> Movie('Star Wars').director
'George Lucas'
>>> jaws = Movie('Jaws')
>>> f'Released in {jaws.year} by {jaws.director}'
'Released in 1975 by Steven Spielberg'

>>> Song('Country Roads').artist
'John Denver'

>>> Movie('Star Wars').director = 'J.J. Abrams'
>>> Movie('Star Wars').director
'J.J. Abrams'
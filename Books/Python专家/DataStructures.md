- [数据结构为什么这么重要？](#数据结构为什么这么重要)
- [抽象数据类型(ADT)](#抽象数据类型adt)
- [抽象基类(ABC)](#抽象基类abc)
- [Dicts](#dicts)
- [Lists](#lists)
- [Tuples](#tuples)
- [Sets](#sets)
- [空对象(Empty Objects)](#空对象empty-objects)

Abstract Data Types
Abstract Base Class
Dictionary
Array - List
Linked List
Queue

## 数据结构为什么这么重要？

计算机程序基本上由两个部分组成：数据和处理。而且，数据是基础。
大多数著名的应用，比如邮件服务器，web服务器，数据库等，基本上是在创建和处理复杂的数据结构。
根据我自己的经验，程序一旦复杂起来，数据结构超级重要。大部分时间，我们是在规划，创建和处理复杂的数据结构。或者说，一个程序的根基就是你是否选择或者定一个了一个好的数据结构。


## 抽象数据类型(ADT)
抽象数据类型的基本想法是把数据定义为抽象的对象集合，只为它们定义可用的合法操作，并不暴露其内部实现的具体细节，不论是其数据的表示细节还是操作的实现细节。
其实，编程语言的一个内置类型就可以看作是一个抽象数据类型。Python的字符串类型str是一个典型实例：字符串对象有一种内部表示形式（无须对外宣布），人们用Python编程序时并不依赖于实际表示（甚至不知道其具体表示方式）；str提供了一组操作供编程使用，每个操作都有明确的抽象意义，不依赖于内部的具体实现技术。

## 抽象基类(ABC)

Why use Abstract Base Classes :
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 

By default, Python does not provide abstract classes. Python comes with a module which provides the base for defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.
```python
# Python program showing 
# abstract base class work 
  
from abc import ABC, abstractmethod 
  
class Polygon(ABC): 
  
    # abstract method 
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 
  
# Driver code 
R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides() 
```

Output:
```
I have 3 sides
I have 4 sides
I have 5 sides
I have 6 sides
```

This module provides the metaclass ABCMeta for defining ABCs and a helper class ABC to alternatively define ABCs through inheritance:

class abc.ABC
A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply deriving from ABC avoiding sometimes confusing metaclass usage, for example:
```python
from abc import ABC

class MyABC(ABC):
    pass
```
Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions regarding metaclass usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the metaclass keyword and using ABCMeta directly, for example:
```python
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
```
New in version 3.4.

## Dicts

字典是超级有用的数据结构，尤其是在做算法题，要求速度性能的场景下。Dict具有典型的hash表的特征，O(1)的访问速度。在研究算法相关的场景时，首先要想想能不能利用Dict。花括号curly braces{}键-值对组成。

## Lists

Python中最常用也是最多样性的内部数据结构。List类似于C语言的数组，比如连续的内从空间，Index从0开始，O(1)的访问速度，数据元素可改写。但是List明显比C中我们认识的数组要灵活的多。

## Tuples

Tuples就是不能改写的Lists。所以可以作为字典（dict）的key，而Lists不可以。tuples定义用的是括号parentheses()，而List用的是中括号square bracket[]。
注意()定义一个空的tuple对象，但是(1)定义的是int 1，("string")定义的是‘str’ “string”。对于这种只有一个元素的情况，别忘了在元素后面加","，例如(1,)， ("string",)。

## Sets

Sets存的无序的非重复数据。常用来去重。花括号curly braces{}定义。记得{}定义的是空的dict，而不是set，空set请用set()来定义。


## 空对象(Empty Objects)

一般用来将一些属性或者方法组织在一起，进行统一管理。
但是直接实例化空对象object却不可以，如下：
```
>>> obj = object()
>>> obj.x = 9
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'object' object has no attribute 'x'
```
你必须先定义类再实例化，如下：
```
>>> class EmpObject:
...     pass
... 
>>> obj = EmpObject()
>>> obj.x = 9
>>> obj.x
9
```
但是这种方法不太推荐，只有在非常有必要而又没有其他选择的情况下，才使用。毕竟，Python要为任何类的实例分配一定的内从空间，为可能的任意属性做准备。

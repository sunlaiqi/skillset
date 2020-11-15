

Abstract Data Types
Abstract Base Class
Dictionary
Array - List
Linked List
Queue

### 空对象(Empty Objects)
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

### Lists

Python中最常用也是最多样性的内部数据结构。List类似于C语言的数组，比如连续的内从空间，Index从0开始，O(1)的访问速度，数据元素可改写。但是List明显比C中我们认识的数组要灵活的多。

### Tuples

Tuples就是不能改写的Lists。所以可以作为字典（dict）的key，而Lists不可以。tuples定义用的是括号parentheses()，而List用的是中括号square bracket[]。
注意()定义一个空的tuple对象，但是(1)定义的是int 1，("string")定义的是‘str’ “string”。对于这种只有一个元素的情况，别忘了在元素后面加","，例如(1,)， ("string",)。

### Dicts

字典是超级有用的数据结构，尤其是在做算法题，要求速度性能的场景下。Dict具有典型的hash表的特征，O(1)的访问速度。在研究算法相关的场景时，首先要想想能不能利用Dict。花括号curly braces{}键-值对组成。

### Sets

Sets存的无序的非重复数据。常用来去重。花括号curly braces{}定义。记得{}定义的是空的dict，而不是set，空set请用set()来定义。
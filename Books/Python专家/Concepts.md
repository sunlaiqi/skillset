# 关键概念认识

- [关键概念认识](#关键概念认识)
  - [Python语言的本质](#python语言的本质)
    - [Python是解释型语言](#python是解释型语言)
    - [Python是脚本语言](#python是脚本语言)
    - [Python是动态类型的语言](#python是动态类型的语言)
    - [Python是面向对象的语言](#python是面向对象的语言)
    - [Python是面向过程的语言](#python是面向过程的语言)
    - [Python是服务器语言](#python是服务器语言)
    - [与其他语言集成](#与其他语言集成)
  - [Python的类，实例和对象](#python的类实例和对象)
    - [Python类的机制](#python类的机制)
    - [类的定义](#类的定义)
      - [通过关键词`class`定义](#通过关键词class定义)
      - [动态定义类](#动态定义类)
    - [类的实例化过程](#类的实例化过程)
    - [类属性和实例属性](#类属性和实例属性)
    - [自定义metaclass](#自定义metaclass)
    - [类装饰器](#类装饰器)
    - [方法重载(overloading)](#方法重载overloading)
    - [Magic method](#magic-method)
    - [覆盖(overriding)](#覆盖overriding)
    - [类的各种方法类型](#类的各种方法类型)
  - [Python的函数和方法](#python的函数和方法)
    - [函数也是对象](#函数也是对象)
    - [可调用对象](#可调用对象)
    - [函数和方法](#函数和方法)
    - [高阶函数](#高阶函数)
    - [闭包(Closure)](#闭包closure)
  - [property对象](#property对象)
    - [为什么用property对象？](#为什么用property对象)
    - [property()函数](#property函数)
    - [@property装饰器](#property装饰器)
  - [装饰器](#装饰器)
    - [为什么使用装饰器？](#为什么使用装饰器)
    - [究竟什么是装饰器？](#究竟什么是装饰器)
    - [常用装饰器写法](#常用装饰器写法)
    - [多层装饰器应用顺序](#多层装饰器应用顺序)
    - [装饰带输入参数的函数](#装饰带输入参数的函数)
    - [functools.wraps](#functoolswraps)
  - [生成器](#生成器)
  - [描述符](#描述符)
  - [The Zen of Python](#the-zen-of-python)
    - [如何理解The Zen of Python](#如何理解the-zen-of-python)
  - [什么是Pythonic?](#什么是pythonic)

在学习任何语言之前，先从概念上理解它，能够起到事半功倍的效果。尤其是理解语言创建者的设计理念，设计初衷甚至使用的设计技术，都会对真正深入的了解这门语言有帮助。这也是成为专家级开发者必备的基础。
我们不讲历史，已经有很多人讲过了，你也很容易能从网上查到。我们只讲Python语言的本质。

## Python语言的本质 

谈到Python，大家几乎第一反应就是它是一个脚本语言，主要用来自动化一些工作，就像Bash，Perl一样。没错，但是不仅如此。Python已经不是简单的脚本语言，它可以做很多事情，理论上说，几乎无所不能。说Python的本质有点托大，下面简单而深刻地列出Python的特性，这样我们对此种语言有一个清晰深刻的理解。至少清楚了这些点之后，在你跟别人聊天的时候，真的听起来像个专家一样头头是道，让人对你刮目相看。
先来看看Python的官方定义：
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

### Python是解释型语言

意味着你需要一个解释器，当然这样你可以交互运行你的Python脚本。
同时意味着，Python程序是可以跨平台的，因为只要针对每个平台开发Python解释器就可以了。

### Python是脚本语言 

没错，这一点每个人都知道。但是你更应该深刻地认识到，它是一种高级脚本语言：） 。可以想想它跟Bash，Perl，PHP有啥区别？是不是觉得Python用起来更自然，更爽？

### Python是动态类型的语言

意味着变量的类型是在运行时确定的，而不是定义时决定的。因此，我们不需要指定变量的类型，非常的灵活。

### Python是面向对象的语言

Python支持几乎所有的面向对象特性。支持类，实例，对象。在Python中，任何东西都是对象，包括函数，包括类，类型。Python支持一下核心的面向对象特性：
Inheritance - 继承
Polymorphism - 多态
Encapsulation - 封装
Abstraction - 抽象

但是Python不是100%面向对象，如java那样。比如，Python中没有私有的访问限制，但是会通过其特有的表示法来进行规范。

我们会有专门的章节讲述Python的类和对象。

### Python是面向过程的语言

最重要的是，Python是面向过程的编程语言，这也是Python刚被创建时的特性。你可以不用写一句面向对象的语句也同样能完成你的工作。

### Python是服务器语言

基于Python的后端服务器不计其数，其中著名的有Django，Flask，Fastai。当然也有用Python做前端的，比如kivy，但是目前还不成熟。

### 与其他语言集成

Python由C语言写成，自然支持C。同时，Python还支持Java，C++，C#等。

## Python的类，实例和对象

### Python类的机制

Python类结合了C++和Modula-3的类机制。Python提供了面向对象编程的所有标准特性。最重要的是，Python类充分利用了Python的动态特性，类在运行时创建，而且可以动态修改。
所谓类就是用户定义的蓝图或者模型，并由此创建对象。通过类，将数据和函数打包在一起。创建一个新的类，也就是创建了一个新的对象类型，类型的实例就是对象。每个类的实例拥有属性用来维护其状态，当然也可以通过实例的方法来更新其状态。
与C++和Modula-3不同，Python的内置类型也可以由用户扩展。同时，大多数的内置操作符（比如加法，减法等）也可重新定义。
因此类是用户自定义的数据结构，拥有自身的数据成员和成员函数，并通过创建类的实例进行访问。

Python 3中，类和类型是统一的，因此，一个类实例的类型也就是其类，如type(obj)与obj.__class__是一回事。
记住，在Python中，任何事物都是对象。类也是对象。因此，类也有类型（type）。那么类的类型是什么呢？任何类的类型就是type。内置类的类型也是type。因此，类型的类型也是type：
```python
>>> type(type) 
<class ‘type'>
```
type是一种metaclass。就像一个普通对象是一个类的实例一样，任何类是type metaclass的实例。

### 类的定义
两种方式：
#### 通过关键词`class`定义

为人熟知，这里略过。
```python
>>> class Foo:
...     pass
... 
>>> x = Foo()
>>> type(x)
<class '__main__.Foo'>
>>> type(Foo)
<class 'type'>
```

#### 动态定义类

通过给内置`type()`函数传入参数就可以返回一个对象的类型，也就是类。也就是 `type(<name>, <bases>, <dct>)`，其中：

- `<name>` 指定类的名字，也就是类的`__name__`属性。
- `<bases>` 指定一个基类组成的tuple，也就是类的`__bases__` 属性。
- `<dct>` 指定一个namespace字典，包含了类的实体定义，也就是`__dict__` 属性。

通过这种方法调用`type()`就可以创建一个以type为metaclass的新的类。
```python
>>> Foo = type('Foo', (), {})
>>> x = Foo()
>>> type(x)
<class '__main__.Foo'>
>>> type(Foo)
<class 'type'>
>>> 
>>> Bar = type('Bar', (Foo,), dict(attr=100))

>>> Foo = type(
...     'Foo',
...     (),
...     {
...         'attr': 100,
...         'attr_val': lambda x : x.attr
...     }
... )

>>> x = Foo()
>>> x.attr
100
>>> x.attr_val()
100

```

### 类的实例化过程

所谓实例化的过程就像工厂里通过磨具生产某个产品，磨具就相当于类的定义，事先将未来生产的产品的样子通过磨具设计固定下来，再通过生产过程（runtime）生产出一个个实际的产品（也就是对象）。

```python
>>>
>>> class Foo: 
...     pass
...
>>> f = Foo()
```
`Foo()`创建了类Foo的一个新实例。当解释器遇到`Foo()`时，会发生以下过程：

- Foo的父类方法`__call__()`会被调用。而Foo的父类是type metaclass。
- 因此，type的`__call__()`方法就会被调用。 
- `__call__()`方法反过来就会调用下列方法： 
    - `__new__()` 
    - `__init__()`

如果Foo没有定义`__new__()`和`__init__()`, 就会从祖先类继承。但是如果Foo的确定义了这些方法，它们就会覆盖祖先的方法。
下面的例子中，首先定制一个方法叫·new()·，然后再将它分配给Foo的`__new__()`方法。
```python
>>>
>>> def new(cls):
...     x = object.__new__(cls)
...     x.attr = 100
...     return x 
...
>>> Foo.__new__ = new
>>> f = Foo() 
>>> f.attr 
100
>>> g = Foo() 
>>> g.attr 
100
```
这里改变了类`Foo`的实例化行为。每次创建`Foo`的实例，属性`attr`被初始化为`100`（通常这样的代码会放在`__init__()`里，这里为了演示放在了`__new__()`。)

记住，`type`的`__new__()`的方法是不能重新分配的，Python不允许这么做。

### 类属性和实例属性

类中定义的属性就是类属性，实例中定义的属性就是实例属性。
类属性可以通过类自身进行访问( className.attributeName)以及类的实例进行访问(inst.attributeName)。因此实例可以同时访问实例属性以及类属性。

```python
>>> class myclass:  #类
...     classy = "class value"
... 
>>> dd = myclass()  #类实例
>>> print(dd.classy)    #类属性
class value
>>> dd.classy = "Instance value"    #实例属性
>>> print(dd.classy)
Instance value
>>> print(myclass.classy)
class value
>>> del dd.classy
>>> print(dd.classy)
class value
>>> 
```

### 自定义metaclass

所谓metaclass就是类的模版，类是metaclass的实例，就像对象是类的实例一样。你可以将metaclass称作类的工厂，而类就是对象的工厂。

`type`是Python内置的metaclass。但是你可以定义自己的metaclass，当然要基于`type`。
- 第一步，基于`type`定义一个metaclass：

```python
>>> class Meta(type):
...     def __new__(cls, name, bases, dct):
...         x = super().__new__(cls, name, bases, dct)
...         x.attr = 100
...         return x
...
```
`Meta(type)`: 表示Meta来自type。由于type是一个metaclass，从而使`Meta`也成为一个metaclass。

- 注意这里还为`Meta`定制了一个`__new__()`方法。 但是请记住，不可以对`type` metaclass这么做。这里的`__new__()`方法实现一下功能：
  - 通过`super()`来调用父metaclass(`type`)的`__new__()`创建一个新的类x。
  - 将attr属性分配给类，并赋值100。
  - 返回新创建的类。

- 下面就可以利用新的metaclass来定义一个新类Foo：
  
```python
>>> class Foo(metaclass=Meta): 
    ... pass
    ...
>>> Foo.attr 
100
```

### 类装饰器

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

### 方法重载(overloading)

在典型的面向对象编程中，方法重载指的是多个方法使用相同的名字但是接收不同的参量，从而同一个函数根据输入实现不同的功能。
但是Python并不直接支持方法重载。当然，在Python中，你可以定义很多名字相同的方法，但是真正有效的是最后定义的那个方法，其他方法被覆盖掉了。

### Magic method

可以定义自己的magic方法。
`__add__` => `+`
`__sub__` => `-`
`__mul__` => `*`
`__truediv__` => `/`
`__floordiv__` => `//`


### 覆盖(overriding)

在Python中，当一个子类的方法覆盖了父类的方法时，如果你想调用父类的方法，可以调用
`Super(Subclass, self).method` 而不是`self.method`.

### 类的各种方法类型

- 实例方法
```python
def func(self,):
    pass
```

- 类方法

如果需要操作类的属性，需要用到类方法。类方法绑定的是类而不是类的对象。因此，类方法不能修改对象实例的属性。

```python
@classmethod 
def cfunc(cls,):
    pass
```

- 静态方法

静态方法既不接受类（cls）也不接受对象（self）作为第一个参数。通常使用静态方法创建工具函数。

```python
@staticmethod 
def tool():
    pass
```

## Python的函数和方法

### 函数也是对象

什么是可调用对象？就是可以接收参量而且可能会返回一个对象的对象。
而在Python中，函数其实就是一个最简单的可调用对象。
Python中的每一个函数都是一个对象。对象可以包含方法或者函数，但是对象不一定是函数。

### 可调用对象

就像函数是对象可以通过对其设置属性一样，我们也可以创建一个对象并假装它是一个函数。
在Python中，任何拥有`__call__()` 方法的对象都可以使用函数的调用语法进行调用。

### 函数和方法

方法和函数类似，不同就在于方法与类或者对象相关联，一般在类内部定义。

### 高阶函数

一个函数被称为高阶函数是因为它把另一个函数作为输入参数或者它返回的是一个函数，也就是说，操作对象是函数的函数。

functools模块中定义了很多高阶函数，比如partial, reduce, wraps等。

### 闭包(Closure)

Python允许函数内定义另外一个函数。这个时候就可能发生闭包。
Python函数内定义一个函数，不仅能将这个内部函数作为返回输出，同时这个内部函数还能够获取并保持住父函数的状态值，这个时候就发生了闭包。这个内部函数就是闭包，也叫词法闭包(lexical closure)
一个闭包能够记住来自包含它的词法作用域(lexical scope)的值，也就是包含它的代码，即便程序的执行流程已经离开了那个包含它的词法作用域。
实践中，意味着，函数不仅能够返回某些行为（另外的函数），而且它还能预先设置这些行为。

```python
def make_adder(n): 
    def add(x):
        return x + n 
    return add

plus_2 = make_adder(2)
plus_4 = make_adder(4)

print(plus_2(5))
# 7
print(plus_4(5))
# 9
```
这里，`make_adder`实际上成了一个生产和设置`add`函数的工厂。请注意这里，`add`函数仍然能够访问`make_adder`函数(包含作用域)的参数`n`的值。


## property对象

```python
>>> property
<class 'property'>
>>> a = property()
>>> a
<property object at 0x7f8808a2e810>
>>> type(a)
<class 'property'>
```

可见property是一个可调用的对象。一个property就是一个属性对象包含了一个getter和一个setter方法。我们常用的是它的函数形式property()。

### 为什么用property对象？

property可以被认为是一种更加"Pythonic"的方式来处理类或者实例的属性，因为：
- 语法更加简洁和易读
- 你可以像通常那样访问实例的属性(instanceName.attribute)，同时你可以使用中间“magic”方法(getters和setters)来对新的值进行验证，从而避免直接访问或者修改数据。
- 通过使用@property，你可以“重用”某个property的名字，从而避免每次都要针对getters, setters和deleters创建新的名字。

### property()函数

property()函数可以创建和返回一个property对象。property()函数有四个参量：
```python
property(fget, fset, fdel, doc)
# fget is a function for retrieving an attribute value. 
# fset is a function for setting an attribute value. 
# fdel is a function for deleting an attribute value. 
# doc creates a docstring for attribute.
```
一个property对象有三个方法，getter(), setter()和delete()，分别用来指定fget, fset, 和fdel。 

```python
class Prop: 
    def __init__(self): 
        self._age = 0
    
    # function to get value of _age 
    def get_age(self): 
        print("getter method called") 
        return self._age 
    
    # function to set value of _age 
    def set_age(self, a): 
        print("setter method called") 
        self._age = a 

    # function to delete _age attribute 
    def del_age(self): 
        del self._age 
        
    age = property(get_age, set_age, del_age)  

mark = Prop()
mark.age = 10
print(mark.age) 
```

### @property装饰器

装饰器的主要目的就是为了改变类的方法或者属性，这样开发人员不用修改他们的代码就可以使用装饰器的功能。
下面的例子可以看到使用@property装饰器可以增加验证功能。

```python
class Prop: 
    def __init__(self): 
        self._age = 0
    
    # using property decorator 
    # a getter function 
    @property
    def age(self): 
        print("getter method called") 
        return self._age 
    
    # a setter function 
    @age.setter 
    def age(self, a): 
        if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
        print("setter method called") 
        self._age = a 

mark = Prop() 
mark.age = 19
print(mark.age) 
```
## 装饰器

### 为什么使用装饰器？

装饰器最大的好处是可以让你改变代码的功能，而不用重写代码。比如你相对已有的代码添加日志功能，就可以使用装饰器，而不用改写现有的代码。

一般装饰器用在一下方面：
- 日志，程序的log
- 实施访问控制和安全认证
- 功能限制
- caching

### 究竟什么是装饰器？

所谓装饰器就是一个函数或者类，“装饰”或者“包裹”另一个函数或者类，这样在被“装饰”的函数或类之前和之后执行你的代码。看起来就像被装饰的函数或者类行为发生了改变。

**最简单的装饰器**

```python
def null_decorator(func): 
    return func

def greet():
    return 'Hello!'

greet = null_decorator(greet)

>>> greet() 'Hello!'
```
**使用@语法**

```python
@null_decorator
def greet():
    return 'Hello!'

>>> greet() 
'Hello!'
```
注意，使用@语法在函数的定义时刻开始装饰，意思就是说原来的函数行为在定义的时候被改变了。程序中使用的函数是被装饰过的，没有机会再调用装饰前的函数。

### 常用装饰器写法

问题：为什么要定一个一个wrapper内嵌函数，而不是直接像上面那样直接返回func？


```python
def uppercase(func): 
    def wrapper():
        # 可以在之前添加代码
        original_result = func()
        modified_result = original_result.upper() 
        return modified_result

    return wrapper

@uppercase
def greet():
    return 'Hello!'

>>> greet() 'HELLO!'
```

**注意**：
wrapper中一定要用return返回装饰后的函数。否则，如果被装饰函数有返回值的话，就会被丢弃。

### 多层装饰器应用顺序

由底向上

### 装饰带输入参数的函数

```python
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) 
    return wrapper
```

### functools.wraps

functools.wraps会将被装饰函数的名称，docstring，参数列表等元数据拷贝到装饰后的函数，否则这些元数据在修饰后会被隐藏。而这会给调试带来麻烦。作为最佳实践，推荐为每个装饰器使用functools.wraps。

```python
import functools
def uppercase(func): 
    @functools.wraps(func) 
    def wrapper():
        return func().upper() 
    return wrapper
```

## 生成器

## 描述符

## The Zen of Python

我也不脱俗，在这里列出著名的The Zen of Python。输入下列命令：

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
### 如何理解The Zen of Python

## 什么是Pythonic?


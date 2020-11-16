- [设计模式](#设计模式)
  - [Singleton Pattern（单例模式）](#singleton-pattern单例模式)
    - [常见的单例模式：](#常见的单例模式)
    - [需要使用单例模式的情景](#需要使用单例模式的情景)
    - [单例模式的python实现](#单例模式的python实现)

# 设计模式

我这里不会详细的讲解各种设计模式如何实现。我是希望能够将各个常用的设计模式的应用场景列出来。在你需要的时候，能知道选用什么样的设计模式。具体到某个设计模式，你可以到时候仔细研究它的实现。

## Singleton Pattern（单例模式）
该模式的主要目的是确保某一个类只有一个实例存在

### 常见的单例模式：

（1）比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

（2）当有同步需要的时候，可以通过一个实例来进行同步控制，比如对某个共享文件（如日志文件）的控制，对计数器的同步控制等，这种情况下由于只有一个实例，所以不用担心同步问题。

（3）Python的logger就是一个单例模式，用以日志记录；Windows的资源管理器是一个单例模式；线程池，数据库连接池等资源池一般也用单例模式；网站计数器等等，这些都是单例模式。

### 需要使用单例模式的情景

当每个实例都会占用资源，而且实例初始化会影响性能，这个时候就可以考虑使用单例模式，它给我们带来的好处是只有一个实例占用资源，并且只需初始化一次；归纳为以下几条：

1、要求生产唯一序列号。

2、WEB 中的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。

3、创建的一个对象需要消耗的资源过多，比如 I/O 与数据库的连接等。

优缺点：

优点： 1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。 2、避免对资源的多重占用（比如写文件操作）。

缺点：没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。

### 单例模式的python实现

- 使用“装饰器”来实现单例模式
```python
def Singleton(cls):
    ...

@Singleton
class MyClass(object):
    ...
```

- 通过__new__函数去实现
下面的例子中，Logger就是单例模式。
```python
class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls).__new__(cls, *args， **kwargs) 
        return cls._logger
```

- 使用一个单独的模块作为单例模式

因为，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。


The Singleton pattern is used for,
- When logging needs to be implemented. The logger instance is shared by all the components of the system.
- The configuration files is using this because cache of information needs to be maintained and shared by all the various components in
the system.
- Managing a connection to a database.

